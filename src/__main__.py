from typing import Final

from pygame import K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP
from pygame import KEYUP as KEYUP_EVENT
from pygame import QUIT as QUIT_EVENT
from pygame import Surface
from pygame import init as pygame_init
from pygame.display import flip as flip_display_buffer
from pygame.display import set_caption as set_window_title
from pygame.display import set_mode as set_display_mode
from pygame.event import get as get_events
from pygame.time import Clock

from .game import Game, ShiftDirection

INITIAL_RESOLUTION: Final[tuple[int, int]] = (640, 720)
BACKGROUND_COLOUR: Final[tuple[int, int, int]] = (0xFA, 0xF8, 0xEF)


def event_loop(window: Surface, game: Game) -> bool:
    """Run a cycle of the event loop.

    Returns:
        bool: True if the program should stop, False otherwise.
    """

    for event in get_events():
        if event.type == QUIT_EVENT:
            return True
        elif event.type == KEYUP_EVENT:
            if event.key == K_ESCAPE:
                return True
            elif event.key == K_LEFT:
                game.shift(ShiftDirection.LEFT)
            elif event.key == K_RIGHT:
                game.shift(ShiftDirection.RIGHT)
            elif event.key == K_UP:
                game.shift(ShiftDirection.UP)
            elif event.key == K_DOWN:
                game.shift(ShiftDirection.DOWN)

    window.fill(BACKGROUND_COLOUR)
    game.draw(window)

    flip_display_buffer()

    return False


def main() -> None:
    pygame_init()
    window = set_display_mode(INITIAL_RESOLUTION)
    set_window_title("2048")

    clock = Clock()
    game = Game()

    while True:
        stop = event_loop(window, game)
        clock.tick(60)

        if stop:
            break


if __name__ == "__main__":
    main()
