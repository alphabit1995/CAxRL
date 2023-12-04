import gym
from gym import Env
from gym.core import ObservationWrapper
from gym.spaces import Box
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
import random
import re

from subprocess import check_output
import math

class Abaqus_Env(gym.Env):

    def __init__(self):

        self.action_space = spaces.Discrete(6)
        print("Action Space: " + str(self.action_space))

        self.observation_space = Box(
            low=np.array([0]),
            high=np.array([100]),
            dtype=np.float32)

        self.upper_stress_limit = 1000000
        
        self.length_upper_limit = 20
        self.length_lower_limit = 10
        self.length = random.randint(1, 30)
        self.length_step = 1

        self.breadth_upper_limit = 5
        self.breadth_lower_limit = 2
        self.breadth = random.randint(1, 6)
        self.breadth_step = 1

        self.step_counter = 0

    def step(self, action, steps):

        print("Step Counter: " + str(self.step_counter))
        self.stress_reward = 0
        self.length_reward = 0
        self.total_step_reward = 0
        previous_state = [self.length, self.breadth]
        ###########################################################################################
        # Parameter configuration
        ###########################################################################################
        # Increase length
        if action == 0:
            print("In action 0: Increasing length")
            if self.length == 60:
                self.length = 60
            else:
                self.length += self.length_step

        # Decrease length
        elif action == 1:
            print("In action 1: Decreasing length")
            if self.length == 1:
                self.length = 1
            else:
                self.length -= self.length_step
        
        # length bleib gleich
        elif action == 2:
            print("In action 2: Length remaining the same")
            self.length = self.length
        ###########################################################################################
        # Increase breadth
        if action == 3:
            print("In action 0: Increasing breadth")
            if self.breadth == 6:
                self.breadth = 6
            else:
                self.breadth += self.breadth_step

        # Decrease breadth
        elif action == 4:
            print("In action 1: Decreasing breadth")
            if self.breadth == 1:
                self.breadth = 1
            else:
                self.breadth -= self.breadth_step
        
        # breadth bleib gleich
        elif action == 5:
            print("In action 2: Breadth remaining the same")
            self.breadth = self.breadth
        ###########################################################################################

        # Calculate stress using Abaqus
        print(f"Value passed: Length -- {self.length} Breadth -- {self.breadth}")
        x = check_output(f"abaqus cae -noGUI Cantilever_Beam_Von_Mises.py -- {self.length} -- {self.breadth}", shell=True)
        pattern = r"b\'From Abaqus: [0-9]+\\r\\n([0-9]+.[0-9]+)\\r\\n\'"
        result = re.match(pattern, str(x))
        current_stress = float(result.group(1))
        self.current_stress = current_stress

        ###########################################################################################
        # Reward calculation
        ###########################################################################################
        # Stress Rewards

        if self.current_stress > self.upper_stress_limit:
            
            self.stress_reward = -1

        else:

            self.stress_reward = 1
        ###########################################################################################
        # Length Rewards

        if self.length > self.length_upper_limit or self.length < self.length_lower_limit:
            
            self.length_reward = -1

        else:

            self.length_reward = 1
        ###########################################################################################
        # Breadth Rewards

        if self.breadth > self.breadth_upper_limit or self.breadth < self.breadth_lower_limit:
            
            self.breadth_reward = -1

        else:

            self.breadth_reward = 1
        ###########################################################################################

        self.total_step_reward = self.stress_reward + self.length_reward + self.breadth_reward

        if self.step_counter == steps:
            done = True
        else:
            done = False

        print("Previous State: " + str(previous_state) + " Step Reward: " + str(self.total_step_reward) + ": Next Length State: " + str(self.length) + ": Next Breadth State: " + str(self.breadth) + ": Done: " + str(done))
        print("Current length: " + str(self.length) + ": Lower Length Limit: " + str(self.length_lower_limit) + ": Higher Length Limit: " + str(self.length_upper_limit) + " Length Reward: " + str(self.length_reward) + "\n" + \
              "Current breadth: " + str(self.breadth) + ": Lower breadth Limit: " + str(self.breadth_lower_limit) + ": Higher breadth Limit: " + str(self.breadth_upper_limit) + " Breadth Reward: " + str(self.breadth_reward) + "\n" + \
              "Current Stress: " + str(self.current_stress) + ": Stress Limit: " + str(self.upper_stress_limit) + " Stress Reward: " + str(self.stress_reward))

        info = {}
        
        self.step_counter += 1

        return self.length, self.total_step_reward, done, info

    def render(self):
        pass

    def reset(self):
  
        self.length = random.randint(1, 30)
        self.length = random.randint(1, 10)
        self.state = self.length
        self.step_counter = 1

        return self.state
