import pytest
from sheetfu.helpers import convert_column_to_letter, convert_letter_to_column, convert_a1_to_coordinates, \
    convert_coordinates_to_a1, RangeCoordinates, append_sheet_name


class TestCoordinateColumnToA1Column:

    def test_convert_column_to_one_letter(self):
        assert convert_column_to_letter(1) == "A"
        assert convert_column_to_letter(2) == "B"
        assert convert_column_to_letter(6) == "F"
        assert convert_column_to_letter(25) == "Y"
        assert convert_column_to_letter(26) == "Z"

    def test_convert_column_to_multiple_letters_starting_a(self):
        assert convert_column_to_letter(27) == "AA"
        assert convert_column_to_letter(28) == "AB"
        assert convert_column_to_letter(32) == "AF"
        assert convert_column_to_letter(51) == "AY"
        assert convert_column_to_letter(52) == "AZ"

    def test_convert_column_to_multiple_letters_starting_b(self):
        assert convert_column_to_letter(53) == "BA"
        assert convert_column_to_letter(54) == "BB"
        assert convert_column_to_letter(58) == "BF"
        assert convert_column_to_letter(77) == "BY"
        assert convert_column_to_letter(78) == "BZ"


class TestA1ColumnToCoordinateColumn:

    def test_convert_letter_to_column(self):
        assert convert_letter_to_column("a") == 1
        assert convert_letter_to_column("b") == 2
        assert convert_letter_to_column("z") == 26
        assert convert_letter_to_column("A") == 1
        assert convert_letter_to_column("B") == 2
        assert convert_letter_to_column("Z") == 26

    def test_convert_letter_to_multiple_letters(self):
        assert convert_letter_to_column("aa") == 27
        assert convert_letter_to_column("ab") == 28
        assert convert_letter_to_column("az") == 52
        assert convert_letter_to_column("aA") == 27
        assert convert_letter_to_column("AB") == 28
        assert convert_letter_to_column("aZ") == 52

    def test_convert_letter_to_multiple_high_letters(self):
        assert convert_letter_to_column("ca") == 79
        assert convert_letter_to_column("db") == 106
        assert convert_letter_to_column("dz") == 130
        assert convert_letter_to_column("zA") == 677
        assert convert_letter_to_column("zB") == 678
        assert convert_letter_to_column("zZ") == 702

    def test_convert_letter_to_multiple_very_high_letters(self):
        # just for fun. you should not have that many columns in a sheet.
        assert convert_letter_to_column("aaa") == 703
        assert convert_letter_to_column("aab") == 704
        assert convert_letter_to_column("aba") == 729
        assert convert_letter_to_column("zZz") == 18278


class TestAppendSheetNameToA1:

    def test_append_sheet_name_to_a1(self):
        assert append_sheet_name("A1:B2", "random_sheet") == "random_sheet!A1:B2"
        assert append_sheet_name("random_sheet!A1:B2", "random_sheet") == "random_sheet!A1:B2"

    def test_invalid_append_sheet_name(self):
        with pytest.raises(ValueError):
            append_sheet_name("A1:B2", None)

    def test_mismatching_sheet_names(self):
        with pytest.raises(ValueError):
            append_sheet_name("another_sheet!A1:B2", "random_sheet")


class TestCoordinatesToA1:

    def test_coordinates_one_cell(self):
        assert convert_coordinates_to_a1(row=1, column=1) == "A1"
        assert convert_coordinates_to_a1(row=1, column=2) == "B1"
        assert convert_coordinates_to_a1(row=1, column=27) == "AA1"
        assert convert_coordinates_to_a1(row=1, column=53) == "BA1"
        assert convert_coordinates_to_a1(row=1, column=78) == "BZ1"

    def test_coordinates_one_cell_with_sheet_name(self):
        assert convert_coordinates_to_a1(row=1, column=1, sheet_name="Sheet1") == "Sheet1!A1"
        assert convert_coordinates_to_a1(row=1, column=2, sheet_name="Sheet1") == "Sheet1!B1"
        assert convert_coordinates_to_a1(row=1, column=27, sheet_name="Sheet1") == "Sheet1!AA1"
        assert convert_coordinates_to_a1(row=1, column=53, sheet_name="Sheet1") == "Sheet1!BA1"
        assert convert_coordinates_to_a1(row=1, column=78, sheet_name="Sheet1") == "Sheet1!BZ1"

    def test_coordinates_multiple_cells(self):
        assert convert_coordinates_to_a1(row=1, column=1, number_of_column=3) == "A1:C1"
        assert convert_coordinates_to_a1(row=25, column=3, number_of_column=3) == "C25:E25"
        assert convert_coordinates_to_a1(row=1, column=1, number_of_row=3, number_of_column=3) == "A1:C3"
        assert convert_coordinates_to_a1(row=25, column=3, number_of_column=3, sheet_name="Sheet1") == "Sheet1!C25:E25"

    def test_square_range(self):
        notation = convert_coordinates_to_a1(
            row=5,
            column=3,
            number_of_row=10,
            number_of_column=10,
            sheet_name='Sheet1'
        )
        assert notation == "Sheet1!C5:L14"


class TestA1ToCoordinates:

    def test_a1_one_cell(self):
        coordinates = convert_a1_to_coordinates("A1")
        assert coordinates == RangeCoordinates(
            row=1,
            column=1,
            number_of_rows=1,
            number_of_columns=1,
            sheet_name=None
        )

    def test_z5_one_cell(self):
        coordinates = convert_a1_to_coordinates("Z5")
        assert coordinates == RangeCoordinates(
            row=5,
            column=26,
            number_of_rows=1,
            number_of_columns=1,
            sheet_name=None
        )

    def test_small_matrix_range(self):
        coordinates = convert_a1_to_coordinates("A1:B3")
        assert coordinates == RangeCoordinates(
            row=1,
            column=1,
            number_of_rows=3,
            number_of_columns=2,
            sheet_name=None
        )

    def test_large_matrix_range(self):
        coordinates = convert_a1_to_coordinates("C1:H15")
        assert coordinates == RangeCoordinates(
            row=1,
            column=3,
            number_of_rows=15,
            number_of_columns=6,
            sheet_name=None
        )

    def test_large_matrix_range_with_sheetname(self):
        coordinates = convert_a1_to_coordinates("Sheet1!C1:H15")
        assert coordinates == RangeCoordinates(
            row=1,
            column=3,
            number_of_rows=15,
            number_of_columns=6,
            sheet_name='Sheet1'
        )
