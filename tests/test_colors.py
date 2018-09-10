from sheetfu.helpers import rgb_to_hex, hex_to_rgb


class TestColorConverters:

    def test_color_white(self):
        assert hex_to_rgb('#ffffff') == {'red': 1, 'green': 1, 'blue': 1}
        assert rgb_to_hex(**{'red': 1, 'green': 1, 'blue': 1}) == '#ffffff'

    def test_hex_to_rgb_to_hex(self):
        color = '#b4fbb8'
        rgb = hex_to_rgb(color)
        hex_color = rgb_to_hex(**rgb)
        assert color == hex_color

