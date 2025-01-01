# Class Scheduling Optimization using Genetic Algorithms
This project demonstrates a smart way to assign tasks to robots using genetic algorithms. It optimizes task distribution based on robot efficiency, availability, and task preferences, and visualizes the process in real-time with Pygame.
# Key Features
- Dynamic Task Assignment: Assigns tasks to robots based on efficiency and availability.
- Genetic Algorithm Optimization: Uses selection, crossover, and mutation to find the best task assignments.
- Interactive Visualization: Real-time grid display showing task assignments and optimization progress.
- Customizable Settings: Adjust the number of tasks, robots, and algorithm parameters to explore different scenarios.
# Project Structure
Here's a quick overview of the files:
- agent.py: It defines the Agent class to represent robots, their efficiencies, and assigned tasks.
- environment.py: It sets up tasks, robot preferences, and availability matrices.
- run.py: It is the main script that runs the simulation.
# Requirements
- Python 3.9.13 or higher version
- Libraries: pygame, numpy
# Installation
1. Install the required libraries:
   ```bash
      pip install pygame
      pip install numpy
# How to run:
1. Clone the repository:
   ```bash
     git clone https://github.com/sabrina160/Sec-6-Fall2024-2021-3-60-252--Lab-task-3_CSE366.git
     cd .\Sec-6-Fall2024-2021-3-60-252--Lab-task-3_CSE366\
2. Run the main simulation:
   ```bash
     py .\run.py
