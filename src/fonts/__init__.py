from pygame.font import Font

from ..consts import FONT_SIZE

_font = None
_score_font = None


def get_font() -> Font:
    global _font
    if not _font:
        _font = Font("./src/fonts/roboto.ttf", FONT_SIZE)

    return _font


def get_score_font() -> Font:
    global _score_font
    if not _score_font:
        _score_font = Font("./src/fonts/roboto.ttf", 48)

    return _score_font
