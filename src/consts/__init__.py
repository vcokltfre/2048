from os import getenv
from typing import Final

BOARD_CELLS: Final[int] = int(getenv("CELLS", 4))
CELL_WIDTH: Final[int] = int(getenv("CELL_WIDTH", 128))
CELL_PADDING: Final[int] = 2
CELL_OFFSET: Final[int] = CELL_WIDTH + (CELL_PADDING * 2)
BOARD_WIDTH: Final[int] = BOARD_CELLS * CELL_OFFSET

WINDOW_WIDTH: Final[int] = BOARD_WIDTH
WINDOW_HEIGHT: Final[int] = BOARD_WIDTH + 64

FONT_SIZE: Final[int] = 4 * (CELL_WIDTH // 12)
