# DESIGN — Tasks A + B

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

### Screens
- **MenuScreen**
  - Shows the title and “Press SPACE” animation.
  - Creates a background `Game(player=None)` so the background can animate like the original menu.
  - On `SPACE` (pressed-this-frame) → transitions to `PlayScreen`.

- **PlayScreen**
  - Creates the real `Game(Player())` instance (this is where gameplay begins).
  - Updates the game each frame using the current `input_state`.
  - When `player.lives < 0` → transitions to `GameOverScreen`.

- **GameOverScreen**
  - Draws the final scene + HUD + “Game Over” overlay.
  - On `SPACE` (pressed-this-frame) → transitions back to `MenuScreen`.

### Why this meets Task A requirements
- Global `update()` and `draw()` are thin delegates:
  - `update()` → `app.update()`
  - `draw()` → `app.draw(screen)`
- No global state branching happens inside global `update()`.
- `Game()` creation happens inside screen transitions (Menu → Play), not in the global update.
- Screen transitions go through a single method: `app.change_screen(...)`.

---

## Task B — Input design (Input snapshot + edge detection / Command pattern)

Task B removes:
- global `space_down`
- global `space_pressed()`
- direct access to `keyboard.*` inside `Player.update()`

### InputState
Input is represented by an immutable snapshot object built once per frame:

Required fields:
- `left: bool`
- `right: bool`
- `jump_pressed: bool` (edge)
- `fire_pressed: bool` (edge; start game + create orb)
- `fire_held: bool` (level; blow orb further)

### Centralized input capture (InputManager)
- `InputManager.capture()` reads raw keyboard state once per frame and produces an `InputState`.
- Edge detection is implemented by storing previous frame values and comparing:
  - `fire_pressed = space_now and not space_prev`
  - `jump_pressed = up_now and not up_prev`

### How input flows through the program
1. `App.update()` calls `InputManager.capture()` once per frame.
2. The resulting `InputState` is passed into `screen.update(input_state)`.
3. In Play mode, `Game.update(input_state)` passes the same snapshot to `Player.update(input_state)`.

### Task B acceptance points
- `Player.update(input_state)` does not read `keyboard.*` directly.
- Edge detection works for:
  - starting the game from Menu (`fire_pressed` / SPACE press)
  - firing an orb (`fire_pressed` / SPACE press)
- Holding SPACE uses `fire_held` to control “blow further”.

---

## Pause (not required for Task B)

Pause is not part of Task B requirements. If implemented later (Task C), it should:
- freeze simulation updates when paused
- still draw the current frame plus a PAUSED overlay
- toggle using an edge-detected key press (e.g., `P`)
