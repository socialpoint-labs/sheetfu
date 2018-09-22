Introduction
============


Sheetfu is a Python library that easily interacts with Google Sheets. Its API is simple, intuitive, and fast.
For Google apps scripts users, the API will be familiar as the primary goal of this code is to adapt the
original Javascript apps script API for spreadsheets to Python.

For example, this is how you would get the backgrounds data for a given sheet range.

.. code-block:: python

    spreadsheet = SpreadsheetApp('path/to/secret.json').open_by_id('a_spreadsheet_id')
    sheet = spreadsheet.get_sheet_by_name('Sheet1')
    data_range = sheet.get_data_range()
    backgrounds = data_range.get_backgrounds()

Replace the snake case to camel case, and you basically end up with the same naming convention of the Javascript
app scripts API.