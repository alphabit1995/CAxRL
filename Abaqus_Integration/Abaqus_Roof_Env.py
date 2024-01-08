import gym
from gym import Env
from gym.core import ObservationWrapper
from gym.spaces import Box
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
import random
import re
import os
import subprocess

from subprocess import check_output
import math

class Abaqus_Roof_Env(gym.Env):

    def __init__(self):

        self.action_space = spaces.Discrete(27)
        
        print("Action Space: " + str(self.action_space))

        self.observation_space = Box(low=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), high=np.array([5000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), shape=(14,), dtype=np.float32)

        self.upper_stress_limit = 5000
        self.support_reward = 0
        self.breadth_upper_limit = 75
        self.breadth_lower_limit = 35
        self.breadth_step = 5
        self.breadth = random.randrange(self.breadth_lower_limit, self.breadth_upper_limit+1, self.breadth_step)

        self.number_of_supports_min = 1
        self.number_of_supports_max = 13
        self.number_of_supports_upper_limit = 7
        self.number_of_supports_lower_limit = 3

        self.current_stress = 5000
        self.set_limit = 4

        self.step_counter = 0
        self.position_list = [0 for i in range(self.number_of_supports_max)]


    def add_or_remove_support(self, support_number, action):

        status = None
        if action == 0:
            print("In support action 0: Adding support")
            if support_number not in self.position_list:
                print(f"Support absent at position {support_number}, adding support")
                self.position_list.append(support_number)
                status = True
            else:
                print(f"Support already present at position {support_number}")
                status = False

        elif action == 1:
            print("In support action 1: Removing support")
            if support_number in self.position_list:
                print(f"Support present at position {support_number}, removing support")
                self.position_list.remove(support_number)
                status = True
            else:
                print(f"Support already absent at position {support_number}")
                status = False
        else:
            print(f"In support action 2: Support status remaining the same at position {support_number}")
            status = True
        
        return status


    def retrieve_support_number_and_action(self, action):
        pattern = r"([0-9]+)_([0-9]+)"
        result = re.match(pattern, str(action))
        support_number = int(result.group(1))
        support_parameter_change = int(result.group(2))
        return support_number, support_parameter_change

    def step(self, action, steps):

        print("Step Counter: " + str(self.step_counter))
        self.stress_reward = 0
        self.support_reward = 0
        #previous_state = [self.breadth] + self.position_list
        #print("Previous State:", previous_state)
        print("Action: " + str(action))
        
        breadth_parameter_change = action[0]

        support_number, support_parameter_change = self.retrieve_support_number_and_action(action[1])
        ###########################################################################################
        # Breadth Parameter configuration
        ###########################################################################################

        # Increase breadth
        if breadth_parameter_change == 0:
            print("In breadth action 0: Increasing breadth")
            if self.breadth == self.breadth_upper_limit:
                self.breadth = self.breadth_upper_limit
            else:
                self.breadth += self.breadth_step

        # Decrease breadth
        elif breadth_parameter_change == 1:
            print("In breadth 1: Decreasing breadth")
            if self.breadth == self.breadth_lower_limit:
                self.breadth = self.breadth_lower_limit
            else:
                self.breadth -= self.breadth_step
        
        # breadth bleib gleich
        elif breadth_parameter_change == 2:
            print("In breadth 2: Breadth remaining the same")
            self.breadth = self.breadth
        
        ###########################################################################################
        # Support Parameter configuration
        ###########################################################################################
        status = self.add_or_remove_support(support_number, support_parameter_change)
        if status == False:
            print("Trying another action...")
            return None, None, None, None
        ###########################################################################################
        # Print current state
        string_position_list = str(self.position_list)
        string_position_list = string_position_list.replace(" ", "")

        ###########################################################################################
        # Calculate average stress on the roof
        ###########################################################################################
        print(f"Value passed: Positions -- {string_position_list} Breadth -- {self.breadth}")
        x = check_output(f"abaqus cae -noGUI  Roof_catia_run.py -- {self.breadth} -- {string_position_list}", shell=True)
        pattern = r"b\'([0-9]+.[0-9]+)\\r\\n\'"
        result = re.match(pattern, str(x))
        current_stress = float(result.group(1))
        self.current_stress = current_stress
        print("Current Average Stress: " + str(self.current_stress))
        ###########################################################################################

        ###########################################################################################
        # Reward calculation
        ###########################################################################################
        # Support Rewards

        if len(self.position_list) > self.set_limit:

            self.support_reward += -1

        else:

            self.support_reward += 1

        ###########################################################################################
        """# Breadth Rewards

        if self.breadth > self.breadth_upper_limit or self.breadth < self.breadth_lower_limit:
            
            self.breadth_reward = -1

        else:

            self.breadth_reward = 1"""
        ###########################################################################################
        # Stress Rewards

        if self.current_stress > self.upper_stress_limit:
                
            self.stress_reward = -1
        
        else:
            
            self.stress_reward = 1
        ###########################################################################################

        self.total_step_reward = self.stress_reward + self.support_reward

        if self.step_counter == steps:
            done = True
            #check_output(f"abaqus cae script=Roof_ab_run.py -- {self.breadth} -- {string_position_list}", shell=True)
        else:
            done = False

        info = {}

        self.step_counter += 1

        list_of_supports_enabled = [0 for i in range(self.number_of_supports_max)]
        for i in self.position_list:
            list_of_supports_enabled[i-1] = 1

        total_state_space = [self.current_stress] + list_of_supports_enabled

        print("Total State Space: " + str(total_state_space))
        print("Current_State ~ Stress: " + str(self.current_stress) + " Breadth: " + str(self.breadth) + " Position List: " + str(self.position_list))
        print("Stress Reward: " + str(self.stress_reward) + " Support Reward: " + str(self.support_reward))
        print("Total Step Reward: " + str(self.total_step_reward))

        return total_state_space, self.total_step_reward, done, info

    def render(self):
        pass

    def reset(self):
        self.breadth = random.randint(self.breadth_lower_limit, self.breadth_upper_limit)
        self.position_list = []
        
        # Randomly select number of supports
        number_of_supports = random.randint(self.number_of_supports_min, self.number_of_supports_max)
        print("**********Number of Supports: " + str(number_of_supports))
        support_counter = 0
        while True:
            random_support = random.randint(self.number_of_supports_min, self.number_of_supports_max)
            if random_support not in self.position_list:
                if support_counter == number_of_supports:
                    print("Maximum number of random supports reached")
                    break
                print("**********Random Support not in position list")
                print("Random Support: " + str(random_support) + " Position List: " + str(self.position_list))
                self.position_list.append(random_support)
                if len(self.position_list) == self.number_of_supports_max:
                    print("Maximum number of global supports reached")
                    break

                support_counter += 1
            else:
                continue
        print("**********Position List: " + str(self.position_list))

        list_of_supports_enabled = [0 for i in range(self.number_of_supports_max)]
        for i in self.position_list:
            list_of_supports_enabled[i-1] = 1

        self.state = [self.current_stress] + list_of_supports_enabled

        self.step_counter = 1
        return self.state
