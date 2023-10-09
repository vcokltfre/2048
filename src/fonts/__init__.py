from pygame.font import Font

_font = None


def get_font() -> Font:
    global _font
    if not _font:
        _font = Font("./src/fonts/roboto.ttf", 48)

    return _font
