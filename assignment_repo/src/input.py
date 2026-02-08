from dataclasses import dataclass
from pgzero.builtins import keyboard

@dataclass(frozen=True)
class InputState:
    left: bool
    right: bool
    jump_pressed: bool   # edge
    fire_pressed: bool   # edge (create orb / start game)
    fire_held: bool      # level (blow further)

class InputManager:
    """
    Builds InputState once per frame, with edge detection.
    """
    def __init__(self):
        self._prev_space = False
        self._prev_up = False

    def capture(self) -> InputState:
        left = bool(keyboard.left)
        right = bool(keyboard.right)

        up = bool(keyboard.up)
        space = bool(keyboard.space)

        # edge detection
        jump_pressed = up and (not self._prev_up)
        fire_pressed = space and (not self._prev_space)

        state = InputState(
            left=left,
            right=right,
            jump_pressed=jump_pressed,
            fire_pressed=fire_pressed,
            fire_held=space
        )

        self._prev_up = up
        self._prev_space = space
        return state
