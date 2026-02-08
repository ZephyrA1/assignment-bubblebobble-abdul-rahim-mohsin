# DESIGN — Tasks A, B, C

## Task A — Screens architecture (State pattern)

The refactor replaces global branching on state in `update()`/`draw()` with Screen objects managed by an `App`.

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

### Screens (Task A)
- **MenuScreen**
  - Shows title + “Press SPACE” animation.
  - Uses a background `Game(player=None)` to animate behind the menu.
  - On `SPACE` pressed-this-frame → transitions to `PlayScreen`.

- **PlayScreen**
  - Creates the real `Game(Player())` instance.
  - Updates the game each frame using the `input_state`.
  - If `player.lives < 0` → transitions to `GameOverScreen`.

- **GameOverScreen**
  - Draws final scene + HUD + “Game Over” overlay.
  - On `SPACE` pressed-this-frame → transitions back to `MenuScreen`.

### Why this meets Task A requirements
- Global `update()` and `draw()` are thin delegates:
  - `update()` → `app.update()`
  - `draw()` → `app.draw(screen)`
- No global state branching inside global `update()`.
- `Game()` creation occurs during screen transitions (Menu → Play).
- Screen changes go through one method: `app.change_screen(...)`.

---

## Task B — Input snapshot + edge detection (Command pattern)

Task B removes:
- global `space_down`
- global `space_pressed()`
- direct access to `keyboard.*` inside `Player.update()`

### InputState
Input is represented by an immutable snapshot built once per frame:

Required fields:
- `left: bool`
- `right: bool`
- `jump_pressed: bool` (edge)
- `fire_pressed: bool` (edge; start game + create orb)
- `fire_held: bool` (level; blow orb further)
- `pause_pressed: bool` (edge; used in Task C)

### Centralized input capture (InputManager)
- `InputManager.capture()` reads keyboard state once per frame and produces `InputState`.
- Edge detection is implemented using previous-frame values:
  - `fire_pressed = space_now and not space_prev`
  - `jump_pressed = up_now and not up_prev`
  - `pause_pressed = p_now and not p_prev`

### Input flow
1. `App.update()` builds `InputState` once per frame.
2. The current screen receives it via `screen.update(input_state)`.
3. In Play, `Game.update(input_state)` passes the same object to `Player.update(input_state)`.

### Task B acceptance points
- `Player.update(input_state)` does not read `keyboard.*`.
- Edge detection works for:
  - starting from Menu (`fire_pressed`)
  - firing an orb (`fire_pressed`)
- Holding SPACE uses `fire_held` to blow further.

---

## Task C — Pause design

Pause is implemented as a separate screen: **PauseScreen**.

### How Pause is triggered (recommended behavior)
- Only `PlayScreen` reacts to pause input:
  - if `input_state.pause_pressed` → switch to `PauseScreen`
- Menu/GameOver do not check pause input, so pause cannot be triggered there.

### While paused (simulation frozen)
- `PauseScreen.update()` does **not** call `game.update()` (no movement/spawns/timers).
- `PauseScreen.draw()` still renders:
  1. the current play scene (by drawing the existing `PlayScreen`)
  2. a pause overlay text (e.g., “PAUSED”, “PRESS P”)

### Resume behavior
- Pressing `P` again returns to the **same PlayScreen instance**.
- This guarantees a clean resume with the exact same game objects and state.
