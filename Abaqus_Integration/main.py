import collections
import os
import random
from typing import Deque
import gym
import numpy as np
from gym import spaces

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import numpy as np

from DQN_Network import DQN
from Abaqus_Env import Abaqus_Env
from Abaqus_Roof_Env import Abaqus_Roof_Env
import datetime

PROJECT_PATH = os.path.abspath(r"C:\Users\basan\Documents\Thesis\Code\CAxRL\Abaqus_Integration")
FILE_NAME_PREFIX = "23_10_2023_10_Episodes_10_Steps_2L_16N_1"
MODELS_PATH = os.path.join(PROJECT_PATH, "Models")
MODEL_PATH = os.path.join(MODELS_PATH, FILE_NAME_PREFIX + "_dqn_cax.h5")
TARGET_MODEL_PATH = os.path.join(MODELS_PATH, FILE_NAME_PREFIX + "_target_dqn_cax.h5")

# Fixing random state for reproducibility
#np.random.seed(42)

class Agent:

    def __init__(self, env: gym.Env, replay_buffer_size, train_start, gamma, epsilon, epsilon_min, epsilon_decay, steps, learning_rate, batch_size):
        # DQN Env Variables
        self.env = env
        self.observations = self.env.observation_space.shape
        print("Observation Space: " + str(self.env.observation_space))
        print("Observation Space Shape: " + str(self.env.observation_space.shape))
        self.actions = 28

        self.breadth_actions = 3
        self.support_actions = 39
                
        # DQN Agent Variables
        self.replay_buffer_size = replay_buffer_size
        self.train_start = train_start
        self.memory: Deque = collections.deque(maxlen=self.replay_buffer_size)
        self.gamma = gamma
        self.epsilon = epsilon 
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay

        # DQN Network Variables
        self.state_shape = self.observations
        self.learning_rate = learning_rate

        self.dqn = DQN(self.state_shape,self.actions,self.learning_rate)
        self.target_dqn = DQN(self.state_shape,self.actions,self.learning_rate)
        self.target_dqn.update_model(self.dqn)

        self.dqn_breadth = DQN(self.state_shape, self.breadth_actions, self.learning_rate)
        self.target_dqn_breadth = DQN(self.state_shape, self.breadth_actions, self.learning_rate)
        self.target_dqn_breadth.update_model(self.dqn_breadth)

        self.dqn_support = DQN(self.state_shape,self.support_actions,self.learning_rate)
        self.target_dqn_support = DQN(self.state_shape,self.support_actions,self.learning_rate)
        self.target_dqn_support.update_model(self.dqn_support)

        self.batch_size = batch_size

        self.rnd_counter = 0
        self.model_counter = 0

        self.action_map = [None] * env.number_of_supports_max * 3
        for i in range(env.number_of_supports_max):
            for j in range(3):
                self.action_map[i*3 + j] = str(i+1) + "_" + str(j)


    def get_action_string(self, state):
        action_list = []
        if np.random.rand() <= self.epsilon:
            action_list.append(np.random.randint(3))
            action_string = str(np.random.randint(1, 13)) + "_" + str(np.random.randint(3))
            action_list.append(action_string)
            return action_list
        else:
            self.model_counter +=1
            action_list = [np.argmax(self.dqn_breadth(state)), self.action_map[np.argmax(self.dqn_support(state))]]
            print(f"Action List from epsilon condition: {str(action_list)}")
            return action_list


    def train(self, num_episodes, num_steps):      
        episode_reward_list=[]
    
        for episode in range (1, num_episodes + 1):
            
            print(f"------------------------------------------Running Episode in train{episode}----------------------------------------------")
            print("------------------------------------------------------------------------------------------------------------------")
            episode_reward = 0.0
            state = self.env.reset()
            state = np.reshape(state, newshape=(1, -1)).astype(np.float32)
            step_reward_list = []
            setting_list = []
            next_state_list = []

            while True:
                print("------------------------------------------------------------------------------------------------------------------")
                print(f"Running Episode {episode}")
                action_string = self.get_action_string(state)
                next_state, step_reward, done, setting  = self.env.step(action_string, num_steps)
                print(f"Action List: {str(action_string)}")
                if next_state is None:
                    continue
                episode_reward += step_reward
                print("Episode Reward: " + str(episode_reward))
                next_state_list.append(next_state)
                next_state = np.reshape(next_state, newshape=(1, -1)).astype(np.float32)

                self.remember(state, action_string, step_reward, next_state, done)
                self.replay()

                step_reward_list.append(step_reward)
                setting_list.append(setting)

                state = next_state

                if done:

                    episode_reward_list.append(episode_reward)
                    self.target_dqn.update_model(self.dqn)
                    self.target_dqn_breadth.update_model(self.dqn_breadth)
                    self.target_dqn_support.update_model(self.dqn_support)
                    
                    break
        
            print("Saving model...")
            self.dqn.save_model(MODEL_PATH)
            print("Saving target model...")
            self.target_dqn.save_model(TARGET_MODEL_PATH)
            print("------------------------------------------------------------------------------------------------------------------")
            print("------------------------------------------------------------------------------------------------------------------")
        
        print("Episode rewards: " + str(episode_reward_list))
        self.plotData(episode_reward_list, "Train_Rewards")


    def play(self, num_episodes, num_steps):
        self.dqn.load_model(MODEL_PATH)
        self.target_dqn.load_model(TARGET_MODEL_PATH)
        episode_reward_list=[]
        best_reward = -200
        
        for episode in range(1, num_episodes + 1):
            print(f"******************************************Running Episode in play{episode}**********************************************")
            print("******************************************************************************************************************")
            episode_reward = 0.0
            state = self.env.reset()
            state = np.reshape(state, newshape=(1, -1)).astype(np.float32)
            step_reward_list = []
            setting_list = []
            next_state_list = []
            self.epsilon = self.epsilon_min

            while True:
                print("------------------------------------------------------------------------------------------------------------------")
                print(f"Running Episode {episode}")
                action = self.get_action_string(state)
                next_state, step_reward, done, setting  = self.env.step(action, num_steps)
                if next_state is None:
                    continue
                episode_reward += step_reward
                print("Episode Reward: " + str(episode_reward))
                next_state_list.append(next_state)
                next_state = np.reshape(next_state, newshape=(1, -1)).astype(np.float32)

                step_reward_list.append(step_reward)
                setting_list.append(setting)
                
                state = next_state

                if done:
                    episode_reward_list.append(episode_reward)

                    if episode_reward_list[-1] > best_reward:
                        best_reward = episode_reward_list[-1]

                    episode_reward_list.append(episode_reward)
                    break

            print("Episode rewards: " + str(episode_reward_list))
            self.plotData(episode_reward_list, "Test_Rewards")

            print("Episode rewards: " + str(episode_reward_list))
            self.plotData(episode_reward_list, "Test_Rewards")


    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay


    def replay(self):
        if len(self.memory) < self.train_start:
            return

        minibatch = random.sample(self.memory, self.batch_size)
        states, actions, rewards, states_next, dones = zip(*minibatch)

        states = np.concatenate(states).astype(np.float32)
        states_next = np.concatenate(states_next).astype(np.float32)

        q_values = self.dqn(states) 
        q_values_next = self.target_dqn(states_next)
        #q_values_next = self.dqn(states_next)

        q_values_breadth = self.dqn_breadth(states)
        q_values_next_breadth = self.target_dqn_breadth(states_next)

        q_values_support = self.dqn_support(states)
        q_values_next_support = self.target_dqn_support(states_next)

        for i in range(self.batch_size):
            a = actions[i] 
            done = dones[i]
            if done:
                q_values[i][a] = rewards[i]
            else:
                q_values[i][a] = rewards[i] + self.gamma * np.max(q_values_next[i])
        
        for i in range(self.batch_size):
            a = actions[i][0]
            done = dones[i]
            if done:
                q_values_breadth[i][a] = rewards[i]
            else:
                q_values_breadth[i][a] = rewards[i] + self.gamma * np.max(q_values_next_breadth[i])
        
        for i in range(self.batch_size):
            a = actions[i][1]
            done = dones[i]
            if done:
                q_values_support[i][a] = rewards[i]
            else:
                q_values_support[i][a] = rewards[i] + self.gamma * np.max(q_values_next_support[i])

        print("Q Values: " + str(q_values))
        print("Q Values Breadth: " + str(q_values_breadth))
        print("Q Values Support: " + str(q_values_support))
        self.dqn.fit(states, q_values)
        self.dqn_breadth.fit(states, q_values_breadth)
        self.dqn_support.fit(states, q_values_support)


    def plotData(self, data, type_of_run):

        plt.clf()
        plt.cla()
        x = np.arange(0, len(data))
        window = 20
        ax = plt.gca()
        ax = ax.set_facecolor((0.5,0.5,0.5))

        if len(data) < window:
            print("window größer als data")
            plt.plot(x, data, 'orange', linewidth=0.5)
        
        else:
            print("window kleiner als data")
            plt.plot(x, data, 'orange', linewidth=0.5)

        plt.xlabel('Episodes')
        plt.ylabel('Rewards')
        plt.title('DQN Reward evaluation')
        MaxLegend = mpatches.Patch(color='orange', label=type_of_run)
        plt.legend(handles=[MaxLegend])
        plt.grid(True, linewidth=0.5)
    
        plt.savefig(f"{FILE_NAME_PREFIX}_DQN_Reward_Evaluation_{type_of_run}.png", dpi= 200)
    

def ProcessStart():

    episodes = 2
    steps = 10
    replay_buffer_size = 10000
    train_start = 700
    gamma = 0.95
    epsilon = 1
    epsilon_min = 0.01
    epsilon_decay = 0.996
    learning_rate = 0.001
    batch_size = 96

    env = Abaqus_Roof_Env()

    agent = Agent(env, replay_buffer_size, train_start, gamma, epsilon, epsilon_min, epsilon_decay, steps, learning_rate, batch_size)
    agent.dqn.internal_model.summary()

    agent.train(episodes, steps)

    agent.play(num_episodes= 2, num_steps= 10)

if __name__ == "__main__":

    start_time = datetime.datetime.now()

    ProcessStart()

    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    print("Elapsed time: ", elapsed_time)
