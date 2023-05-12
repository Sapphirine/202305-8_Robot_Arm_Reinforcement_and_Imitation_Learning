import os
os.environ['LD_LIBRARY_PATH'] = ':/root/.mujoco/mujoco200/bin'
os.environ['LD_PRELOAD'] = ':/root/.mujoco/mujoco200/bin/libglew.so'
import numpy as np
import robosuite as suite
from robosuite.utils.mjcf_utils import postprocess_model_xml
import os
import h5py
import argparse
import random

hdf5_path = "/home/ar4451/Data/RoboTurkPilot/bins-Cereal/demo.hdf5"
f = h5py.File(hdf5_path, "r")
env_name = f["data"].attrs["env"]

env = suite.make(
        env_name,
        has_renderer=True,
        ignore_done=True,
        use_camera_obs=False,
        gripper_visualization=True,
        reward_shaping=True,
        control_freq=100,
    )