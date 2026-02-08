# DESIGN — Task A (Screens / State Pattern)

## Screens architecture

The refactor replaces global “state branching” in `update()`/`draw()` with Screen objects managed by an `App`.

### App
- `App` owns:
  - the current screen (`self.screen`)
  - the input manager (`InputManager`)
- The only way to switch modes/screens is:
  - `app.change_screen(new_screen)`

### Screen interface
Each screen implements:
- `update(input_state)`
- `draw(screen)`

### Screens
- **MenuScreen**
  - Shows the title and “Press SPACE” animation.
  - Creates a background `Game(player=None)` so the background can animate like the original menu.
  - On `SPACE` (pressed-this-frame) → transitions to `PlayScreen`.

- **PlayScreen**
  - Creates the real `Game(Player())` instance (this is where gameplay begins).
  - Updates the game each frame using the current `input_state`.
  - When `player.lives < 0` → transitions to `GameOverScreen`.
  - On `P` (pressed-this-frame) → transitions to `PauseScreen` (optional screen).

- **GameOverScreen**
  - Draws the final scene + HUD + “Game Over” overlay.
  - On `SPACE` (pressed-this-frame) → transitions back to `MenuScreen`.

- **PauseScreen** (optional separate screen)
  - Wraps a reference to the existing `PlayScreen` instance.
  - Does not advance simulation; it only draws the frozen scene + a pause overlay.
  - On `P` (pressed-this-frame) → returns to the same `PlayScreen` instance.

### Why this meets Task A requirements
- Global `update()` and `draw()` are thin delegates:
  - `update()` → `app.update()`
  - `draw()` → `app.draw(screen)`
- No global state branching happens inside global `update()`.
- `Game()` creation happens inside screen transitions (Menu → Play), not in the global update.
- Screen transitions go through a single method: `app.change_screen(...)`.

---

## Input design

Input is captured once per frame by an `InputManager`, producing an `InputState` that is passed into `screen.update(input_state)`.

`InputState` includes:
- `left`, `right` (held)
- `jump` (held), plus optional `jump_pressed` (edge)
- `fire_held` (held) and `fire_pressed` (edge)
- `pause_pressed` (edge)

**Pressed-this-frame (edge detection)** is implemented by storing previous key states inside `InputManager` and comparing them to the current frame. This is used for:
- Starting the game on the menu (SPACE pressed)
- Firing a new orb (SPACE pressed)
- Toggling pause (P pressed)

---

## How Pause works

Pause is implemented as an optional separate screen (`PauseScreen`):

- In `PlayScreen.update`, when `pause_pressed` is true, the App switches to `PauseScreen`.
- While paused:
  - The game simulation is frozen (no updates to movement, timers, spawns, AI, collisions).
  - Drawing still occurs by calling the play screen’s draw logic.
  - A “PAUSED” overlay is drawn on top of the frozen frame.
- Pressing `P` again switches back to the same `PlayScreen` instance so gameplay resumes exactly where it stopped.
