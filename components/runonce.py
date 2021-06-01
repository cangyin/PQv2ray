from threading import Thread
from time import sleep

# thread for simple async tasks  
class RunOnce(Thread):

    def __init__(self, tasks=[]) -> None:
        super().__init__()
        self._stop = False
        self.tasks = tasks
        self.start()

    def kick_all(self, func_name):
        new_list = [task_func for task_func in self.tasks if 'function ' +
                    func_name not in repr(task_func)]
        self.tasks = new_list

    def enqueue(self, task_or_tasks):
        if(isinstance(task_or_tasks, list)):
            self.tasks.extend(task_or_tasks)
        else:
            self.tasks.append(task_or_tasks)

    def stop(self):
        self._stop = True

    def run(self) -> None:
        while not self._stop:
            task = None
            if len(self.tasks):
                task = self.tasks.pop(0)
            if task:
                task()
            else:
                sleep(0.1)
