#!/usr/bin/env python3

import random
import typing

PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "move", "grab", "use", "swim",
           "climb", "release", "eat", "sleep"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(
        events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        yield events.pop(index)


def main() -> None:
    print("=== Game Data Stream Processor ===")
    stream = gen_event()
    for i in range(1000):
        name, action = next(stream)
        print(f"Event {i}: Player {name} did action {action}")

    events = []
    for _ in range(10):
        events.append(next(stream))
    print("Built list of 10 events:", events)

    for event in consume_event(events):
        print("Got event from list:", event)
        print("Remains in list:", events)


if __name__ == "__main__":
    main()