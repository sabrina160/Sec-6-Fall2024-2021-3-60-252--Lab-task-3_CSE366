# Class Scheduling Optimization using Genetic Algorithms
This project focuses on creating an optimal class schedule for students using genetic algorithms. The goal is to minimize scheduling conflicts, align schedules with student preferences, and balance time slot usage efficiently. The process includes real-time visualization of schedules and fitness evaluation using Pygame.
# Key Features
- Conflict-Free Scheduling: Minimizes time slot clashes and respects student availability.
- Preference Alignment: Balances class schedules with student time slot preferences.
- Genetic Algorithm Optimization: Uses selection, crossover, and mutation to generate optimal schedules over generations.
- Interactive Visualization: Displays the scheduling process in real-time, highlighting conflicts and priorities.
- Customizable Settings: Allows flexibility in the number of classes, students, and genetic algorithm parameters.
# Problem Setup
The scheduling problem involves:
- Classes:
  - Duration: 1-2 hours.
  - Priority: Scale of 1-5.
Students:
Availability: Specific time slots they are available.
Preferences: Priority for certain time slots.
Time Slots:
Total number of available slots to assign classes.
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
