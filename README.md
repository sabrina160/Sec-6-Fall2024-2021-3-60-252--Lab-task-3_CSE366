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
- Students:
  - Availability: Specific time slots they are available.
  - Preferences: Priority for certain time slots.
- Time Slots:
  - Total number of available slots to assign classes.
# Project Structure
Here's a breakdown of the main files:
- agent.py: Implements the Student class to represent:
  - Attributes: id, availability, preference, and schedule.
  - Methods: Assign classes and clear schedules for new generations.
- environment.py: Defines the scheduling environment and visualizes schedules.
  - Generates random initial schedules.
  - Displays schedules using Pygame, showing preferences, assignments, and conflicts.
- run.py: Runs the genetic algorithm to optimize schedules.
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
# Genetic Algorithm Details
1. Fitness Function:
   - Conflict Minimization: Penalizes schedules where classes are assigned to unavailable students.
     - Formula: Conflict Penalty = Number of unavailable time slots used
   - Preference Alignment: Rewards schedules that match student time slot preferences.
     - Formula: Preference Penalty = 1 / Student’s Preference (if time slot is not preferred)
   - Total Fitness: Combines conflict and preference penalties.
     - Formula: Fitness = Conflict Penalty + Preference Penalty
2. Crossover:
- Combines genes (class assignments) from two parent schedules.
   - Single-Point Crossover:
     - Example:
       - Parent 1: [1, 2, 3, 4, 5]
       - Parent 2: [5, 4, 3, 2, 1]
       - Crossover Point: 3
       - Child: [1, 2, 3, 2, 1]
3. Mutation:
 - Introduces random changes to maintain genetic diversity.
   - Random Assignment Mutation:
     - Example:
       - Original Gene: [1, 2, 3, 4, 5]
       - Mutated Gene: [1, 2, 4, 4, 5]
# Visualization Highlights
- Schedule Grid:
   - Displays student preferences and assigned time slots.
   - Highlights conflicts and priorities.
- Progress Updates:
   - Shows current generation and best fitness score.
# Customizing the Simulation
- num_classes: Number of classes to schedule.
- num_students: Number of students in the system.
- population_size: Number of solutions per generation.
- mutation_rate: Probability of mutation for each gene.
- n_generations: Total number of generations to run.
- generation_delay: Delay (in milliseconds) between generations.
