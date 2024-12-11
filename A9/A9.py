def find_min_completion_time(tasks):
    # Sort task by processing time
    tasks.sort(reverse=False, key=lambda x: x[1])
    waiting_time = 0
    total_time = 0
    for i, (task, time) in enumerate(tasks):
        completion_time = time + waiting_time  # Calculating completion time
        waiting_time += time  # Adding time of previous job in waiting time
        total_time += completion_time  # Calculating total time
        # Updated task with completion time
        tasks[i] = (task, time, completion_time)

    avg_time = round(total_time / len(tasks), 2)
    return tasks, avg_time


if __name__ == "__main__":
    print("\n\n")
    tasks1 = [('a1', 5), ('a2', 3)]
    print(f"Input: {tasks1}")
    scheduled_tasks1, avg_completion_time1 = find_min_completion_time(tasks1)
    print("Output")
    print("Task id\t Processing Time  Completion Time")
    for task_id, processing_time, completion_time in scheduled_tasks1:
        print(f"{task_id}\t {processing_time}\t\t   {completion_time}")
    print(f"Average completion time: {avg_completion_time1}\n")

    # Test Case 2
    tasks2 = [('a1', 4), ('a2', 8), ('a3', 2)]
    print(f"Input: {tasks2}")
    scheduled_tasks2, avg_completion_time2 = find_min_completion_time(tasks2)
    print("Output")
    print("Task id\t Processing Time  Completion Time")
    for task_id, processing_time, completion_time in scheduled_tasks2:
        print(f"{task_id}\t {processing_time}\t\t   {completion_time}")
    print(f"Average completion time: {avg_completion_time2}\n")

    # Test Case 3
    tasks3 = [('a1', 10), ('a2', 3), ('a3', 7), ('a4', 1), ('a5', 2)]
    print(f"Input: {tasks3}")
    scheduled_tasks3, avg_completion_time3 = find_min_completion_time(tasks3)
    print("Output")
    print("Task id\t Processing Time  Completion Time")

    for task_id, processing_time, completion_time in scheduled_tasks3:
        print(f"{task_id}\t {processing_time}\t {completion_time}")
    print(f"Average completion time: {avg_completion_time3}")
