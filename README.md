# 202305-8_Robot_Arm_Reinforcement_and_Imitation_Learning
## Project Description
Robot Arm Reinforcement and Imitation Learning explores training models to conduct tasks for the sawyer robot arm.  This repository contains the final iteration of the algorithms that were used in the project along with the simulator information.

## Required Packages
In order to use this repository, certain packages will need to be installed, some of which can't be installed simply with pip.  The main one being the mujoco-py engine or mujoco engine.  Information regarding the mujoco-py installation process can be found at https://github.com/openai/mujoco-py and information regarding the mujoco install can be found at https://github.com/deepmind/mujoco.  The engine that was used in this demo is the mujoco-py 200 but other versions can be used if training the arm on different datasets.  This is due to engine differences.

One other note for setting up the repository is that robosuite is the framework that was decided on, but the version of robosuite that is used is 0.3 even though a newer version exists.  This is due to issues with the installation process and with the physics engine differences.

## Notebooks
This directory contains the barebone notebooks that were used for both training and evaluating the models.  It also contains information regarding the reinforcement learning agents in how they were trained using the stable baselines package and how the imitation learning model was trained in tensorflow.

## Scripts
The scripts directory contains any sort of script that was used as helper functions for the data.  In order to use the data that is referenced in the scripts and notebooks, the RoboTurkPilot dataset will need to be downloaded which can be found at https://roboturk.stanford.edu/dataset_sim.html.

## Misc
The graphs, img, and videos directories all showcase the results of the project and can be used to see how the models and agents performed.  Since the environments were not seeded it is likely that exact reproduction of the results will be difficult, but it should still be possible.

## Sample Models
Two sample models were saved to be used with the notebooks in this repository, namely a mini baseline model and a proximal policy optimization agent that was trained.  The environments are setup so that should the packages all be installed correctly, the models will work with minimal additional effort.

## Processed Data
The processed data for any plotting can be found in the processed data directory.  This separates the rewards achieved based on the run number and shows the progress of the evaluation criteria.
