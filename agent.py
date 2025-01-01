class Agent: 
    def __init__(self, id, efficiency):
        self.id = id
        self.efficiency = efficiency
        self.tasks = []

    def assign_task(self, task_duration, task_priority):
        effective_time = task_duration / self.efficiency * task_priority
        self.tasks.append(effective_time)

    def total_time(self):
        return sum(self.tasks)

    def reset_tasks(self):
        self.tasks = []
