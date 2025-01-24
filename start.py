from math import gcd
from functools import reduce


def lcm(a, b):
    return (a * b) // gcd(a, b)


def lcm_multiple(numbers):
    return reduce(lcm, numbers)


def find_cycle_length(start_room, rooms, door_sequence, target_rooms):
    visited = {}
    target_visited = {}
    room = start_room
    step = 0
    iterations = 0
    sequence_length = len(door_sequence)

    print(f"\nStarting simulation for room {start_room}...")

    while (room, step % sequence_length) not in visited:
        visited[(room, step % sequence_length)] = step
        door = door_sequence[step % sequence_length]
        room = rooms.get(room, {}).get(door, room)

        if (step % sequence_length) == 0:
            iterations += 1

        step += 1

        for target in target_rooms:
            if room == target:
                print(
                    f"Child {start_room} reached target {target} at step {step} (iteration {iterations})"
                )
                target_visited[(room, step % sequence_length)] = iterations

    first_target = min(target_visited.values())
    cycle_length = step - visited[(room, step % sequence_length)]

    print(
        f"Cycles length = {cycle_length} Iterations = {iterations} First target steps = {first_target}"
    )
    print(f"Targets visited: {target_visited}")
    print("\n")

    return cycle_length, first_target


def main(input_file):

    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")

    with open(input_file, "r") as f:
        lines = f.readlines()

    num_rooms = int(lines[0].strip())
    num_children = int(lines[1].strip())
    initial_rooms = list(map(int, lines[2].strip().split()))
    target_rooms = list(map(int, lines[3].strip().split()))
    door_sequence = lines[4].strip()

    rooms = {}
    for i in range(num_rooms):
        doors = list(map(int, lines[5 + i].strip().split()))
        rooms[i + 1] = {
            "A": doors[0],
            "B": doors[1],
            "C": doors[2],
            "D": doors[3],
        }

    results = [
        find_cycle_length(room, rooms, door_sequence, target_rooms)
        for room in initial_rooms
    ]

    cycle_lengths, first_targets = zip(*results)

    print(f"First target room steps: {first_targets}")

    finish_steps = lcm_multiple(cycle_lengths)
    fmt_nmbr = f"{finish_steps:,}".replace(",", " ")
    print("Steps to finish:", fmt_nmbr)

    return finish_steps


if __name__ == "__main__":
    input_file = "12.in"
    main(input_file)
