import itertools


def freed_prisoners(prison):
    groups = [(k, list(v)) for k, v in itertools.groupby(prison)]
    print(f"Groups: {groups}")
    freed = [k for k, _ in groups]
    persons = len(freed) if freed[0] == 1 else 0
    print(f"Freed list: {freed}; freed {persons} persons")
    return persons


freed_prisoners([1, 1, 0, 0, 0, 1, 0])  # ➞ 4
freed_prisoners([1, 0, 1, 0])  # ➞ 4
freed_prisoners([1, 1, 1])  # ➞ 1
freed_prisoners([0, 0, 0])  # ➞ 0
freed_prisoners([0, 1, 1, 1])  # ➞ 0
