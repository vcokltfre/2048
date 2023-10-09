from typing import Final

from pygame import Surface
from pygame.draw import rect as draw_rect

from ..fonts import get_font

# (156 + 2 + 2) * 4 = 640
#  ^     ^   ^    ^
#  |     |   |    Number of cells
#  |     |   -----Right padding
#  |     ---------Left padding
#  ---------------Cell width
CELL_WIDTH: Final[int] = 156
CELL_PAD: Final[int] = 2
CELL_OFFSET: Final[int] = CELL_WIDTH + (CELL_PAD * 2)


_colours: Final[dict[int, tuple[int, int, int]]] = {
    2: (0xEE, 0xE4, 0xDA),
    4: (0xED, 0xE0, 0xC8),
    8: (0xF2, 0xB1, 0x79),
    16: (0xF5, 0x95, 0x63),
    32: (0xF6, 0x7C, 0x5F),
    64: (0xF6, 0x5E, 0x3B),
    128: (0xED, 0xCF, 0x72),
    256: (0xED, 0xCC, 0x61),
    512: (0xED, 0xC8, 0x50),
    1024: (0xED, 0xC5, 0x3F),
    2048: (0xED, 0xC2, 0x2E),
}


class Cell(int):
    @property
    def background(self) -> tuple[int, int, int]:
        return _colours[self]

    def draw(self, window: Surface, row: int, col: int) -> None:
        if not self:
            raise ValueError("Cannot draw an empty cell.")

        horizontal_offset = col * CELL_OFFSET
        vertical_offset = row * CELL_OFFSET

        draw_rect(
            surface=window,
            color=self.background,
            rect=(
                CELL_PAD + horizontal_offset,
                CELL_PAD + vertical_offset,
                CELL_WIDTH,
                CELL_WIDTH,
            ),
        )

        text = get_font().render(str(self), True, (0x77, 0x6E, 0x65))

        text_rect = text.get_rect(
            center=(
                CELL_WIDTH // 2 + horizontal_offset + CELL_PAD,
                CELL_WIDTH // 2 + vertical_offset + CELL_PAD,
            )
        )

        window.blit(text, text_rect)
