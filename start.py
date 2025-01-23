from math import gcd
from functools import reduce


def lcm(a, b):
    return (a * b) // gcd(a, b)


def gowno(a, b):
    return lcm(a, b)


def lcm_multiple(numbers):
    return reduce(lcm, numbers)


def find_cycle_length(start_room, room_graph, door_sequence, target_rooms):
    visited = {}
    target_visited = {}
    room = start_room
    step = 0
    iterations = 0
    sequence_length = len(door_sequence)

    while (room, step % sequence_length) not in visited:
        visited[(room, step % sequence_length)] = step
        door = door_sequence[step % sequence_length]
        room = room_graph.get(room, {}).get(door, room)  # Ensure valid room transition
        if (step % sequence_length) == 0:
            iterations += 1
            print(start_room, "iterations", iterations, "steps", step)

        for target in target_rooms:
            if room == target:
                print(start_room, "target", target, "room", room, "steps", step)
                target_visited[(room, step % sequence_length)] = step
        step += 1

    cycle_length = step - visited[(room, step % sequence_length)]
    print(target_visited)
    print(cycle_length)
    print("\n")
    return cycle_length


def main(input_file):

    with open(input_file, "r") as f:
        lines = f.readlines()

    num_rooms = int(lines[0].strip())
    num_children = int(lines[1].strip())
    initial_rooms = list(map(int, lines[2].strip().split()))
    target_rooms = list(map(int, lines[3].strip().split()))
    door_sequence = lines[4].strip()

    room_graph = {}
    for i in range(num_rooms):
        connections = list(map(int, lines[5 + i].strip().split()))
        room_graph[i + 1] = {
            "A": connections[0],
            "B": connections[1],
            "C": connections[2],
            "D": connections[3],
        }

    cycle_lengths = [
        find_cycle_length(room, room_graph, door_sequence, target_rooms)
        for room in initial_rooms
    ]
    synchronization_step = lcm_multiple(cycle_lengths)
    print("Steps to synchronize:", synchronization_step)


if __name__ == "__main__":
    input_file = "rooms_input2.txt"  # Replace with your actual file name
    main(input_file)
