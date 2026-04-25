import random

ALL_ACHIEVEMENTS = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Unstoppable",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "First Steps",
    "Sharp Mind",
    "Hidden Path Finder"
]


def gen_player_achievements() -> set[str]:
    count = random.randint(1, len(ALL_ACHIEVEMENTS))
    achievements = random.sample(ALL_ACHIEVEMENTS, count)
    return set(achievements)


alice = gen_player_achievements()
bob = gen_player_achievements()
charlie = gen_player_achievements()
dylan = gen_player_achievements()

print("=== Achievement Tracker System ===")
print()
print(f"Player Alice: {alice}")
print(f"Player Bob: {bob}")
print(f"Player Charlie: {charlie}")
print(f"Player Dylan: {dylan}")
print()
print(f"All distinct achievements: {alice.union(bob, charlie, dylan)}")
print()
print(f"Common achievements: {alice.intersection(bob, charlie, dylan)}")
print()
print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
print(f"Only Charlie has: {charlie.difference(bob, alice, dylan)}")
print(f"Only Dylan has: {dylan.difference(bob, charlie, alice)}")
print()
print(f"Alice is missing: {set(ALL_ACHIEVEMENTS).difference(alice)}")
print(f"Bob is missing: {set(ALL_ACHIEVEMENTS).difference(bob)}")
print(f"Charlie is missing: {set(ALL_ACHIEVEMENTS).difference(charlie)}")
print(f"Dylan is missing: {set(ALL_ACHIEVEMENTS).difference(dylan)}")
