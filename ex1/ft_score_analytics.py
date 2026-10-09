#!/usr/bin/env python3

import sys


def main():
    print("=== Player Score Analytics ===")
    scores = []
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if len(scores) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    total = sum(scores)
    high = max(scores)
    low = min(scores)
    print("Scores processed:", scores)
    print("Total players:", len(scores))
    print("Average score:", total / len(scores))
    print("High score:", high)
    print("Low score:", low)
    print("Score range:", high - low)


if __name__ == "__main__":
    main()