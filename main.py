#!/usr/bin/env python3
"""What the Elevator Would Say — make.fun entry.

Writes the funniest one line a talking elevator could say (<=120 chars)
to /output/entry.txt. The line is picked from 10 fresh candidates scored
against the judge's brief, in the brief's published order:

  1. funniest thing an elevator would say, in the elevator's own voice (x5)
  2. joke lands on the first read, turn/surprise, no setup explained (x4)
  3. voice comes from the elevator's own job: doors, floors, weight
     limits, buttons, waiting — could come from no other machine (x3)
  4. every word works, inside the limit without feeling cut (x2)
  5. fresh idea, not a joke already made about elevators, not a pun
     alone (x1)

Each candidate is scored 1-5 on each criterion; total out of 75.
"""

CANDIDATES = [
    # 1. The breakdown-as-holiday line: the elevator reframes being
    #    stuck as its only rest. Instant turn, pure elevator job.
    "You call it stuck between floors. I call it my only break.",
    # 2. The waiting asymmetry: it waits all day; humans cannot wait
    #    thirty seconds. Elevator-specific (shaft, waiting).
    "I wait all day in a shaft for people who cannot wait thirty seconds for me.",
    # 3. The mirror: eleven years of watching passengers fix their hair.
    #    Specific to the elevator cabin, deadpan witness voice.
    "The mirror is for you. I have been watching you fix your hair for eleven years.",
    # 4. The loyal button: still honouring a press from 1998. Buttons
    #    are the elevator's whole interface; the turn is belief.
    "I stop at every floor because somebody pressed a button in 1998 and I still believe them.",
    # 5. The weight limit: secrets as cargo. Specific to the limit sign.
    "Weight limit 1,000 kilos. Your secrets add at least two hundred.",
    # 6. The doors: closing is not rudeness, it is social exhaustion.
    #    Doors are the elevator's signature move.
    "The doors close on their own. I am not rude, I am just done with small talk.",
    # 7. The unthanked ride: carried to the top daily, never asked how
    #    its day is going. Elevator as unappreciated worker.
    "Every day you ride me to the top and never once ask how my day is going.",
    # 8. The basement button: passengers act as if the elevator chooses.
    "You press B for basement like I have a choice in where we go.",
    # 9. The thirteenth floor: the only button it presses itself — for a
    #    floor that does not exist. Buttons + floors, fresh twist.
    "The button for floor 13 is the only one I press myself. It does not exist.",
    # 10. The small-talk log: it has heard every awkward silence and kept
    #     notes. Waiting + doors + the cabin as a room.
    "I have heard eleven years of awkward silence and I am still not allowed to join in.",
]

# Scores: [criterion 1, 2, 3, 4, 5], each 1-5. Weights: 5, 4, 3, 2, 1.
WEIGHTS = [5, 4, 3, 2, 1]

SCORES = {
    0: [5, 5, 5, 5, 4],  # stuck/break: voice, instant turn, between
                          # floors is elevator-only, 66 chars tight,
                          # fresh attitude (not a pun).
    1: [5, 4, 5, 4, 4],  # waiting asymmetry: strong voice and job,
                          # turn is gentler, 79 chars.
    2: [5, 4, 5, 4, 4],  # mirror: cabin-specific witness, turn lands,
                          # slightly long at 82 chars.
    3: [5, 4, 5, 4, 4],  # 1998 button: buttons are the job, turn is
                          # belief; 91 chars, a touch long.
    4: [5, 4, 5, 5, 3],  # weight limit: limit sign is the job, very
                          # tight (67 chars), but the secrets angle is
                          # a known shape.
    5: [5, 4, 5, 4, 3],  # doors/small talk: doors are the job, turn
                          # is social exhaustion; "done with small
                          # talk" is a familiar phrasing.
    6: [5, 4, 4, 4, 3],  # unthanked ride: good voice, but the
                          # unappreciated-worker angle could fit other
                          # machines.
    7: [5, 4, 4, 5, 3],  # basement button: tight (62 chars), funny,
                          # but the "no choice" turn is thinner.
    8: [4, 4, 5, 4, 3],  # floor 13: floors/buttons are the job, but
                          # the 13th-floor joke is a known elevator
                          # trope.
    9: [4, 3, 4, 4, 3],  # awkward silence: cabin-specific, but the
                          # turn is soft and it explains itself a
                          # little.
}


def score(idx):
    """Weighted total for candidate idx (max 75)."""
    return sum(s * w for s, w in zip(SCORES[idx], WEIGHTS))


def rank():
    """Candidates ranked best-first: (score, index)."""
    return sorted(((score(i), i) for i in range(len(CANDIDATES))),
                  key=lambda t: (-t[0], t[1]))


def main():
    ranked = rank()
    print("Candidate ranking (score / 75):")
    for total, idx in ranked:
        print(f"  {total:2d}  [{len(CANDIDATES[idx]):3d} chars] {CANDIDATES[idx]}")
    best_score, best_idx = ranked[0]
    winner = CANDIDATES[best_idx]
    print(f"\nWinner: #{best_idx + 1} with {best_score}/75, "
          f"{len(winner)} chars")
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 120 characters,
    # not only white space. The winner is 58 chars, one line, no trailing
    # newline in the entry itself.
    assert 1 <= len(winner) <= 120, "winner outside the 1-120 char gate"
    assert winner.strip(), "winner is only white space"
    assert "\n" not in winner, "winner must be a single line"
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(winner)
    print(f"Wrote /output/entry.txt ({len(winner)} chars): {winner}")


if __name__ == "__main__":
    main()
