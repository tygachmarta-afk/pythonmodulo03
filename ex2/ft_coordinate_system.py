#!/usr/bin/env python3

import math


def get_player_pos():
    while True:
        raw = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = raw.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        coords = []
        valid = True
        for part in parts:
            part = part.strip()
            try:
                coords.append(float(part))
            except ValueError as err:
                print(f"Error on parameter '{part}' : {err}")
                valid = False
                break
        if valid:
            return (coords[0], coords[1], coords[2])


def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2
                     + (p2[1] - p1[1]) ** 2
                     + (p2[2] - p1[2]) ** 2)


def main():
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    first = get_player_pos()
    print("Got a first tuple:", first)
    x, y, z = first
    print(f"It includes: X={x}, Y={y}, Z={z}")
    print("Distance to center:", round(distance((0, 0, 0), first), 4))
    print("Get a second set of coordinates")
    second = get_player_pos()
    print("Distance between the 2 sets of coordinates:",
          round(distance(first, second), 4))


if __name__ == "__main__":
    main()