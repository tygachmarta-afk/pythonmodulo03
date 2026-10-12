#!/usr/bin/env python3

import random

ALL_ACHIEVEMENTS = [
    'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
    'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
    'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
    'Boss Slayer', 'Hidden Path Finder'
]


def gen_player_achievements():
    count = random.randint(1, len(ALL_ACHIEVEMENTS))
    return set(random.sample(ALL_ACHIEVEMENTS, count))


def main():
    print("=== Achievement Tracker System ===")
    print("")
    players = [
        ("Alice", gen_player_achievements()),
        ("Bob", gen_player_achievements()),
        ("Charlie", gen_player_achievements()),
        ("Dylan", gen_player_achievements())
    ]
    all_sets = []
    for name, achievements in players:
        print(f"Player {name}:", achievements)
        all_sets.append(achievements)

    all_distinct = set().union(*all_sets)
    common = set.intersection(*all_sets)
    print("\nAll distinct achievements:", all_distinct)
    print("\nCommon achievements:", common)
    print("")
    for name, achievements in players:
        others = []
        for other_name, other_achievements in players:
            if other_name != name:
                others.append(other_achievements)
        only_mine = set.difference(achievements, set().union(*others))
        print(f"Only {name} has:", only_mine)
    print("")
    full = set(ALL_ACHIEVEMENTS)
    for name, achievements in players:
        print(f"{name} is missing:", set.difference(full, achievements))


if __name__ == "__main__":
    main()