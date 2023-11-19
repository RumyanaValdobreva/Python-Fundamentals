def tasks():
    daily_tasks = []

    while True:
        note = input()
        if note == 'End':
            break

        daily_tasks.append(note)

    sorted_tasks = sorted(daily_tasks, key=lambda x: int(x.split("-")[0]))
    final_sorted_tasks = [note.split("-")[1] for note in sorted_tasks]
    print(final_sorted_tasks)


tasks()