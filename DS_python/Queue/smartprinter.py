from collections import deque

class smartprinter:
    def __init__(self):
        self.urgentjob = deque()
        self.normaljob = deque()

    def add_ur_job(self, job):
        self.urgentjob.append(job)

    def add_nor_job(self, job):
        self.normaljob.append(job)

    def print_job(self):
        while self.urgentjob:
            print(f"Urgent jobs: {self.urgentjob.popleft()}")

        while self.normaljob:
            print(f"Normal jobs: {self.normaljob.popleft()}")

        if not self.urgentjob and not self.normaljob:
            print("No jobs left .")

a = smartprinter()

n = int(input("Enter the number of urgent jobs: "))
for i in range(n):
    a.add_ur_job(input("Enter the urgent job: "))

n = int(input("Enter the number of normal jobs: "))
for i in range(n):
    a.add_nor_job(input("Enter the normal job: "))

a.print_job()