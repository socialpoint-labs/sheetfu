from sheetfu.helpers import rgb_to_hex, hex_to_rgb


class CellParsers:

    @staticmethod
    def get_value(cell):
        return

    @staticmethod
    def set_value(cell):
        return

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
        if cell:
            cell_background = hex_to_rgb(cell)
        else:
            cell_background = hex_to_rgb('#ffffff')
        return {"userEnteredFormat": {'backgroundColor': cell_background}}

    @staticmethod
    def get_note(cell):
        note = cell["note"]
        if not note:
            return ''
        return note

    @staticmethod
    def set_note(cell):
        if cell:
            note = cell
        else:
            note = ''
        return {'note': note}

    @staticmethod
    def get_font_color(cell):
        font_color = cell["effectiveFormat"]['textFormat']["foregroundColor"]
        if font_color or font_color == {}:
            font_color = rgb_to_hex(**font_color)

            # we prefer empty string instead of repeating black hex color
            if font_color == '#000000':
                font_color = ''

        return font_color

    @staticmethod
    def set_font_color(cell):
        if cell:
            font_color = hex_to_rgb(cell)
        else:
            font_color = hex_to_rgb('#000000')
        return {"userEnteredFormat": {'textFormat': {'foregroundColor': font_color}}}

    @staticmethod
    def get_formula(cell):
        formula = cell["formula"]
        if not formula:
            return ''
        return formula

    @staticmethod
    def set_formula(cell):
        if cell:
            formula = cell
        else:
            formula = ''
        return {'formula': formula}


