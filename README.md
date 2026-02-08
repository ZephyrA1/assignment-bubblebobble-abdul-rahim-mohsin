# Bubble Bobble (Cavern) Refactor — Tasks A + B

This project refactors the original PyGame Zero `main.py` code while keeping gameplay equivalent (controls, scoring, enemy behavior, and level progression).

- **Task A:** Screen objects (State pattern) — replaces global state branching with Screen classes managed by an `App`.
- **Task B:** Input snapshot + edge detection (Command pattern) — removes global `space_down/space_pressed()` and stops reading `keyboard.*` directly inside `Player.update()`.

---

## How to run the game (Task A + Task B)

From the repo root:

```powershell
cd .\assignment_repo\
python -m pgzero main.py
