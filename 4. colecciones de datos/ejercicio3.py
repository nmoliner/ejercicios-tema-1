tasks = [
    (3, "Task C"),
    (1, "Task A"),
    (2, "Task B"),
    (4, "Task D")
]

# Sort the tasks based on priority
tasks.sort(key=lambda x: x[0])

# Create a queue with tasks without priority numbers
queue = [task[1] for task in tasks]

print(queue)