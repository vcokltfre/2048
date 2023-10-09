from enum import Enum, auto
from random import choice, choices

from pygame import Surface
from pygame.display import set_caption as set_window_title

from ..consts import BOARD_CELLS, CELL_OFFSET
from ..fonts import get_score_font
from .cell import Cell


class GameOver(Exception):
    pass


class ShiftDirection(Enum):
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()


class Game:
    def __init__(self) -> None:
        self._cells: list[list[Cell]] = [[Cell() for _ in range(BOARD_CELLS)] for _ in range(BOARD_CELLS)]

        self._spawn_cell()
        self._spawn_cell()

        self._score = 0

    def draw(self, window: Surface) -> None:
        for row, cells in enumerate(self._cells):
            for col, cell in enumerate(cells):
                if not cell:
                    continue

                cell.draw(window, row, col)

        score_text = f"Score: {self._score:,}"

        text = get_score_font().render(score_text, True, (0x77, 0x6E, 0x65))
        window.blit(text, (16, CELL_OFFSET * BOARD_CELLS))

        set_window_title(f"2048 - {score_text}")

    def shift(self, direction: ShiftDirection) -> None:
        if direction in (ShiftDirection.LEFT, ShiftDirection.RIGHT):
            self._shift_horizontal(direction)
        else:
            self._shift_vertical(direction)

        self._spawn_cell()

    def _shift_horizontal(self, direction: ShiftDirection) -> None:
        new_cells: list[list[Cell]] = []

        for row in self._cells:
            if direction == ShiftDirection.LEFT:
                new_cells.append(self._compact_cells(row))
            else:
                new_cells.append(self._compact_cells(row[::-1])[::-1])

        self._cells = new_cells

    def _shift_vertical(self, direction: ShiftDirection) -> None:
        new_cells: list[list[Cell]] = []

        for col in range(BOARD_CELLS):
            column: list[Cell] = []

            for row in range(BOARD_CELLS):
                column.append(self._cells[row][col])

            if direction == ShiftDirection.UP:
                new_cells.append(self._compact_cells(column))
            else:
                new_cells.append(self._compact_cells(column[::-1])[::-1])

        self._cells = [[new_cells[row][col] for row in range(BOARD_CELLS)] for col in range(BOARD_CELLS)]

    def _compact_cells(self, cells: list[Cell]) -> list[Cell]:
        """Compact a list of cells, left-to-right, left-priority."""

        compacted_cells: list[Cell] = [cell for cell in cells if cell]

        while True:
            if len(compacted_cells) < 2:
                break

            modified = False

            for index in range(len(compacted_cells) - 1):
                if not compacted_cells[index]:
                    continue

                if compacted_cells[index] == compacted_cells[index + 1]:
                    new = Cell(compacted_cells[index] * 2)
                    compacted_cells[index] = new  # type: ignore
                    compacted_cells[index + 1] = Cell()

                    self._score += new

                    modified = True

            compacted_cells = [cell for cell in compacted_cells if cell]

            if not modified:
                break

        compacted_cells = [cell for cell in compacted_cells if cell]

        return [*compacted_cells, *([Cell()] * (BOARD_CELLS - len(compacted_cells)))]

    def _spawn_cell(self) -> None:
        empty_cells: list[tuple[int, int]] = []

        for row, cells in enumerate(self._cells):
            for col, cell in enumerate(cells):
                if not cell:
                    empty_cells.append((row, col))

        if not empty_cells:
            raise GameOver()

        row, col = choice(empty_cells)
        num = choices([2, 4], weights=[0.9, 0.1])[0]

        self._cells[row][col] = Cell(num)
