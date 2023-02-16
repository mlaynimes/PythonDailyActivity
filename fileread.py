

task_file = open("task.txt", "r")

for employee in task_file.readlines():
    print(employee)
task_file.close()