from sheetfu.helpers import rgb_to_hex, hex_to_rgb, datetime_to_serial_number, serial_number_to_datetime
from datetime import datetime


class CellParsers:
    """
    Class to register every setters and getters from the Google Sheets API.

    Following documentation is essential for understanding what we're doing here.
    https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/cells

    """
    @staticmethod
    def get_value(cell):
        value_body = cell["effectiveValue"]
        format_type = (
            cell
            .get('effectiveFormat', {})
            .get("numberFormat", {})
            .get("type")
        )
        for value_type in [
            'stringValue',
            'numberValue',
            'boolValue',
            'formulaValue'
        ]:
            if value_body.get(value_type) is not None:
                if format_type in ["DATE", "DATE_TIME"]:
                    return serial_number_to_datetime(value_body[value_type])
                return value_body[value_type]

    @staticmethod
    def set_value(cell):
        if cell is not None:
            if isinstance(cell, str):
                if len(cell) > 0 and cell[0] == "=":
                    return {"userEnteredValue": {"formulaValue": cell}}
                return {"userEnteredValue": {"stringValue": cell}}
            elif isinstance(cell, bool):
                return {"userEnteredValue": {"boolValue": cell}}
            elif isinstance(cell, int) or isinstance(cell, float):
                return {"userEnteredValue": {"numberValue": cell}}
            elif isinstance(cell, datetime):
                return {
                    "userEnteredValue": {
                        "numberValue": datetime_to_serial_number(cell)
                    },
                    "userEnteredFormat": {
                        "numberFormat": {
                            "type": "DATE_TIME"
                        }
                    }
                }
        return {"userEnteredValue": {"stringValue": ''}}

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
        return {
            "userEnteredFormat": {
                "textFormat": {
                    "foregroundColor": font_color
                }
            }
        }

    @staticmethod
    def get_formula(cell):
        formula = cell["userEnteredValue"]["formulaValue"]
        if not formula:
            return ''
        return formula

    @staticmethod
    def set_formula(cell):
        if not cell:
            cell = ""
        formula = cell
        return {'userEnteredValue': {"formulaValue": formula}}
