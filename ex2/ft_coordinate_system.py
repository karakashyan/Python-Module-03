import math

def get_player_pos() -> tuple:
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