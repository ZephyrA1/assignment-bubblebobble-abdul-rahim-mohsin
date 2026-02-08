# Assignment Bubble Bobble — Tasks A, B, C

This project refactors the original PyGame Zero `main.py` code while keeping gameplay equivalent (controls, scoring, enemy behavior, and level progression).

- **Task A:** Screen objects (State pattern) — replaces global state branching with Screen classes managed by an `App`.
- **Task B:** Input snapshot + edge detection (Command pattern) — removes global `space_down/space_pressed()` and stops reading `keyboard.*` directly inside `Player.update()`.
- **Task C:** Pause mode — adds a pause screen toggled by `P`, freezing simulation while still drawing the scene + overlay.

---

## How to run the game

From the repo root:

```powershell
cd .\assignment_repo\
python -m pgzero main.py
