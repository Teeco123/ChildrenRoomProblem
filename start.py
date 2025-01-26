def find_room(rooms, door_sequence, target_rooms):
    target_room = 681
    i = 0
    while i < 5:
        for room, doors in rooms.items():
            for (
                letter,
                next_room,
            ) in doors.items():
                if next_room == target_room:
                    print("U can get to: ", target_room, " from", room, " via", letter)
                    target_room = room
                    i += 1

    return 0


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

    find_room(rooms, door_sequence, target_rooms)

    return 0


if __name__ == "__main__":
    input_file = "test_04.in"
    main(input_file)
