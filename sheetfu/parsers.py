from sheetfu.helpers import rgb_to_hex, hex_to_rgb


class CellParsers:

    @staticmethod
    def get_background(cell):
        background_value = cell["effectiveFormat"]["backgroundColor"]
        background_value = rgb_to_hex(**background_value)

        # we prefer empty string instead of white hex color
        if background_value == '#ffffff':
            background_value = ''
        return background_value

    @staticmethod
    def set_background(cell):
        pass

    @staticmethod
    def get_note(cell):
        pass

    @staticmethod
    def set_note(cell):
        pass

    @staticmethod
    def get_font_color(cell):
        pass

    @staticmethod
    def set_font_color(cell):
        pass

