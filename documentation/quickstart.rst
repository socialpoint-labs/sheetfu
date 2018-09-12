

This is how it works.

    client = SpreadsheetApp('path/to/secret/json')
    spreadsheet = client.open_by_id('1VZ8tXVWRn_h0nkvXkjfhdnffj5w68olM8Gz2oE4DAP-BY')
    sheet = spreadsheet.get_sheet_by_name('people')
    people_range = sheet.get_data_range()

    # get the values
    values = people_range.get_values()