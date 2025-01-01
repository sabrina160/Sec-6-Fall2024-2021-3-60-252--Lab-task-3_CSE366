import numpy as np
import pygame

class Environment:
    def __init__(self, num_tasks, num_robots):
        self.num_tasks = num_tasks
        self.num_robots = num_robots
        self.task_durations = np.random.randint(1, 3, size=num_tasks)
        self.task_priorities = np.random.randint(1, 6, size=num_tasks)
        self.robot_efficiencies = np.random.uniform(0.5, 1.5, size=num_robots)

        # Availability and preferences matrices
        self.robot_availability = np.random.randint(0, 2, size=(num_robots, num_tasks))  # Binary matrix: 1 if available, 0 if not
        self.robot_preferences = np.random.uniform(1, 5, size=(num_robots, num_tasks))  # Higher value = stronger preference

    def generate_assignments(self):
        return [np.random.randint(0, self.num_robots, size=self.num_tasks) for _ in range(50)]

    def draw_grid(self, screen, font, task_assignments, generation, best_fitness, max_fitness):
        screen.fill((255, 255, 255))

        color_map = [(0, 0, 255), (200, 200, 200)]
        cell_size = 60
        margin_left = 150
        margin_top = 100

        # Task slots (X-axis labels)
        for col in range(self.num_tasks):
            task_text = font.render(f"Slot {col + 1}", True, (0, 0, 0))
            screen.blit(task_text, (margin_left + col * cell_size + cell_size // 3, margin_top - 30))# x and y coordinates

        # Robot preferences (Y-axis labels)
        for row in range(self.num_robots):
            efficiency_text = font.render(f"Preference: {self.robot_efficiencies[row]:.2f}", True, (0, 0, 0))
            screen.blit(efficiency_text, (10, margin_top + row * cell_size + cell_size // 3))

            for col in range(self.num_tasks):
                assigned_robot = task_assignments[col]
                color = color_map[0] if assigned_robot == row else color_map[1]

                cell_rect = pygame.Rect(
                    margin_left + col * cell_size,
                    margin_top + row * cell_size,
                    cell_size,
                    cell_size
                )
                pygame.draw.rect(screen, color, cell_rect)
                pygame.draw.rect(screen, (0, 0, 0), cell_rect, 1)

                priority_text = font.render(f"P{self.task_priorities[col]}", True, (255, 255, 255) if assigned_robot == row else (0, 0, 0))
                duration_text = font.render(f"{self.task_durations[col]}h", True, (255, 255, 255) if assigned_robot == row else (0, 0, 0))
                screen.blit(priority_text, (cell_rect.x + 5, cell_rect.y + 5))
                screen.blit(duration_text, (cell_rect.x + 5, cell_rect.y + 25))

        # Right panel info
        generation_text = font.render(f"Generation: {generation}", True, (0, 0, 0))
        fitness_text = font.render(f"Best Fitness (Current): {best_fitness:.2f}", True, (0, 0, 0))
        max_fitness_text = font.render(f"Max Fitness Achieved: {max_fitness:.2f}", True, (0, 0, 0))
        screen.blit(generation_text, (750, 50))
        screen.blit(fitness_text, (750, 80))
        screen.blit(max_fitness_text, (750, 110))
