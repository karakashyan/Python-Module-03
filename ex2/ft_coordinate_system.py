import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        text = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = text.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        values = []
        for i in parts:
            try:
                values.append(float(i))
            except ValueError as e:
                print(f"Error on parameter '{i}': {e}")
                break
        else:
            return (values[0], values[1], values[2])


print("=== Game Coordinate System ===")
print()
print("Get a first set of coordinates")
p1 = get_player_pos()
print(f"Got a first tuple: {p1}")
print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")
distance = math.sqrt((p1[0])**2 + (p1[1])**2 + (p1[2])**2)
print(f"Distance to center: {round(distance, 4)}")
print()
print("Get a second set of coordinates")
p2 = get_player_pos()
distance = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)
print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")
