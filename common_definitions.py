import tensorflow as tf
import numpy as np


# general parameters
RL_TASK = 'BipedalWalker-v3'
# RL_TASK = 'LunarLanderContinuous-v2'
# RL_TASK = 'Pendulum-v0'
RENDER_ENV = False
LEARN = True
USE_NOISE = True
CHECKPOINTS_PATH = "./checkpoints/DDPG_"
TF_LOG_DIR = './logs/DDPG/'
EPS_GREEDY = 0.95

# brain parameters
GAMMA = 0.99  # for the temporal difference
RHO = 0.001  # to update the target networks
KERNEL_INITIALIZER = tf.keras.initializers.glorot_normal()
# KERNEL_INITIALIZER = tf.random_uniform_initializer(-1.5e-3, 1.5e-3)

# buffer params
UNBALANCE_P = 0.3  # newer entries are prioritized
BUFFER_UNBALANCE_GAP = 0.5

# training parameters
STD_DEV = 0.2
BATCH_SIZE = 200
BUFFER_SIZE = 1e6
TOTAL_EPISODES = 10000
CRITIC_LR = 1e-3
ACTOR_LR = 1e-4
WARM_UP = 3  # num of warm up epochs
SAVE_WEIGHTS = True