#!/usr/bin/env python3

import random


def main(): 
    print("=== Game Data Alchemist ===")
    players = ['Alice', 'bob', 'Charlie', 'dylan', 
               'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print("Initial list of players:", players)

    all_capitalized = [name.capitalize() for name in players]
    print("New list with all names capitalized:", all_capitalized)

    only_capitalized = [name for name in players if name[0].isupper()]
    print("New list of capitalized names only:", only_capitalized)

    scores = {name: random.randint(0, 1000) for name in all_capitalized}
    print("Score dict:", scores)

    averege = round(sum(scores.values()) / len(scores), 2)
    print("Score average is", averege)

    high_scores = {name: score for name, score in scores.items()
                   if score > averege}
    print("High scores:", high_scores)


if __name__ == "__main__":
    main()