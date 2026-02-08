from dataclasses import dataclass
from pgzero.builtins import keyboard

@dataclass(frozen=True)
class InputState:
    left: bool
    right: bool

    # Jump is "held" to match original behavior (holding up can jump as you land)
    jump: bool
    jump_pressed: bool  # available if you want edge-jump later

    # Fire (space) needs pressed-this-frame for orb creation
    fire_pressed: bool
    fire_held: bool

    # Pause toggle
    pause_pressed: bool

    @property
    def start_pressed(self) -> bool:
        # Menu uses SPACE press to start (same as fire_pressed)
        return self.fire_pressed

class InputManager:
    """
    Captures keyboard state once per frame and does edge detection.
    """
    def __init__(self):
        self._prev_space = False
        self._prev_up = False
        self._prev_p = False

    def capture(self) -> InputState:
        left = bool(keyboard.left)
        right = bool(keyboard.right)

        up = bool(keyboard.up)
        space = bool(keyboard.space)
        p = bool(keyboard.p)

        jump_pressed = up and (not self._prev_up)
        fire_pressed = space and (not self._prev_space)
        pause_pressed = p and (not self._prev_p)

        state = InputState(
            left=left,
            right=right,
            jump=up,
            jump_pressed=jump_pressed,
            fire_pressed=fire_pressed,
            fire_held=space,
            pause_pressed=pause_pressed
        )

        self._prev_space = space
        self._prev_up = up
        self._prev_p = p
        return state
