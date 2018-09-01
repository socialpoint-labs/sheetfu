Sheetfu: Python library for Google Sheets
=========================================


Sheetfu is a Python library that easily interacts with Google Sheets. Its API is simple, intuitive, and fast. For Google apps scripts users, the API will be familiar as the primary goal of this code is to adapt the app script API for spreadsheets to Python.
For example, this is how you would get the backgrounds data for a given sheet range.

.. code-block:: python
    :emphazize-lines: 4

    spreadsheet = SpreadsheetApp('path/to/secret.json').open_by_id('a_spreadsheet_id')
    sheet = spreadsheet.get_sheet_by_name('Sheet1')
    data_range = sheet.get_data_range()
    backgrounds = data_range.get_backgrounds()

Replace the snake case to camel case, and you basically end up with the same naming of the Javascript apps script API.

If you're looking for the Google Apps Script sheetfu library, follow this [link](https://github.com/socialpoint-labs/sheetfu-apps-script).



Differences with most common libraries.

Gspread
This is the most widely used spreadsheet library, and for good reasons. It has been there for a very long time now.
Up until recently, speed was a problem for Gspread as it was still running on version 3 of google sheet API. It looks like this has changed however, so speed may not be a problem anymore.
However, it is impossible to change/update backgrounds, font colors, or any other dimensions from a cell, although it is a major feature request.


Pygsheet
Pygsheet is a more recent library that gives the opportunity to update plenty other dimensions available at cells level. The library is complete.


Where Sheetfu makes a difference is on its model. Essentially, Sheetfu does not contain a cell class. Every set or get data methods is at the range level, where a range can be a line, a row, multiple cells, or just one cell. Pretty much every methods works with 2D matrix.
So you can submit backgrounds, for a whole range in just one method call. This model is identical to the one adopted by Google Apps Scripts, which mostly works with 2D matrix. This model is particularly effective from a performance perspective, as it reduces the number of requests made to Google Sheets Api.
More importantly, this model gave us the opportunity to build modules on top of it, like the Table module.

Regarding the latter, this is also a strong point for Sheetfu, it currently has the Table module which abstract the spreadsheet coordinates and create a DB like syntax based on headers and fields principles. This is a major plus for Sheetfu.