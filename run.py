import pygame
import random
import numpy as np
from agent import Agent
from environment import Environment

pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Task Assignment Visualization")
font = pygame.font.Font(None, 24)

num_tasks = 8
num_robots = 5
environment = Environment(num_tasks, num_robots)
agents = [Agent(id=i, efficiency=environment.robot_efficiencies[i]) for i in range(num_robots)]

population_size = 50
mutation_rate = 0.1
n_generations = 100
generation_delay = 1000

population = environment.generate_assignments()

best_solution = None
best_fitness = float('inf')
max_fitness = float('inf')
generation_count = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    def fitness(individual):
        conflict_penalty = 0
        preference_penalty = 0

        for task, robot in enumerate(individual):
            # Conflict Minimization
            if not environment.robot_availability[robot, task]:#A solution is penalized if tasks are assigned to unavailable robots.
                conflict_penalty += 1

            # Preference Alignment
            preference_penalty += 1 / environment.robot_preferences[robot, task]#A solution is penalized if tasks are assigned to robots
            # in ways that don't match their preferences.

        # Combine penalties
        return conflict_penalty + preference_penalty

    def selection(population):
        return sorted(population, key=fitness)[:population_size // 2]##Selects the half of solutions based on fitness to create the next generation.


    def crossover(parent1, parent2):#Combines genes from two parent solutions to create a new child solution.
        point = random.randint(1, num_tasks - 1)#Selects a random crossover point.
        return np.concatenate([parent1[:point], parent2[point:]])#Combines genes from parent1 up to the point and parent2 after the point.

    def mutate(individual):#Applies mutation to a single individual (task assignment).A list or array representing a task assignment solution, where each element indicates which robot is assigned to a specific task.
        for i in range(len(individual)):
            if random.random() < mutation_rate:#Decides whether to mutate the current gene based on a random probability.random.random(): Generates a random float between 0 and 1.
                individual[i] = random.randint(0, num_robots - 1)#mutation occurs for the current gene and assign the current gene to a new random robot otherwise the task remains assigned to the robot without muted.
        return individual# return the muted individual

    selected = selection(population)
    next_generation = []
    while len(next_generation) < population_size:
        parent1, parent2 = random.sample(selected, 2)
        child = crossover(parent1, parent2)
        next_generation.append(mutate(child))

    population = next_generation#New population
    current_best = min(population, key=fitness)#lowest fitness score means better solution
    current_fitness = fitness(current_best)
    if current_fitness < best_fitness:
        best_fitness = current_fitness
        best_solution = current_best
    if best_fitness < max_fitness:
        max_fitness = best_fitness

    environment.draw_grid(screen, font, best_solution, generation_count + 1, best_fitness, max_fitness)
    pygame.display.flip()
    pygame.time.delay(generation_delay)
    generation_count += 1

    if generation_count >= n_generations:
        break

pygame.quit()
