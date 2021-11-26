Sheetfu
=======

.. image:: https://travis-ci.org/socialpoint-labs/sheetfu.svg?branch=master
    :target: https://travis-ci.org/socialpoint-labs/sheetfu


Sheetfu was built to interacts with Google Sheets with a simple, intuitive, and fast API.
The primary goal of this library is to adapt the Google App Script API for spreadsheets,
to Python. With Sheetfu, you can easily get or set cell values, background colors, font
colors or any other cell attributes.


Installing
----------

Install and update using `pip`_:

.. code-block:: text

    pip install -U Sheetfu


A Simple Example
----------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')
    spreadsheet = sa.open_by_id('<insert spreadsheet id here>')
    sheet = spreadsheet.get_sheet_by_name('Sheet1')
    data_range = sheet.get_data_range()           # returns the sheet range that contains data values.

    # this is how you get things
    values = data_range.get_values()              # returns a 2D matrix of values.
    backgrounds = data_range.get_backgrounds()    # returns a 2D matrix of background colors in hex format.

    # this is how you set things
    data_range.set_background('#000000')          # set every cell backgrounds to black
    data_range.set_font_color('#ffffff')          # set every cell font colors to white


You can also create your SpreadsheetApp object with environment variables
instead of the `secrets.json` file. You can refer to `the authentication tutorial`_ for more info.

.. _the authentication tutorial: https://github.com/socialpoint-labs/sheetfu/blob/master/documentation/authentication.rst

Please read the `sheetfu API documentation`_ for a more detailed description.

.. _sheetfu API documentation: https://github.com/socialpoint-labs/sheetfu/blob/master/documentation/usage.rst


The Table module
----------------

Sheetfu also contains a table module that abstracts completely the coordinates
system for an ORM-like syntax. The example below is for a sheet with the 3
columns 'name', 'surname' and 'age'.

.. code-block:: python

    from sheetfu import Table

    spreadsheet = SpreadsheetApp('path/to/secret.json').open_by_id('<insert spreadsheet id here>')
    data_range = spreadsheet.get_sheet_by_name('people').get_data_range()

    table = Table(data_range, backgrounds=True)

    for item in table:
        if item.get_field_value('name') == 'foo':
            item.set_field_value('surname', 'bar')              # this set the surname field value
        age = item.get_field_value('age')
        item.set_field_value('age', age + 1)
        item.set_field_background('age', '#ff0000')             # this set the field 'age' to red color

    # Every set functions are batched for speed performance.
    # To send the batch update of every set requests you made,
    # you need to commit the table object as follow.
    table.commit()


You can refer to the `Table API documentation`_ for a more detailed description.

.. _Table API documentation: https://github.com/socialpoint-labs/sheetfu/blob/master/documentation/table.rst


Casting
-------

An effort has been made to guide Sheetu as a Google Sheet ORM, where any values
found in a spreadsheet are casted to a matching Python object. Since version
1.5.7, Sheetfu returns `DATE` and `DATE_TIME` as Python `datetime` object.
Similarly, setting a cell with a `datetime` object will make the necessary
parsing and casting to reflect those cells as `DATE_TIME` in the sheet.

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')
    spreadsheet = sa.open_by_id('<insert spreadsheet id here>')
    sheet = spreadsheet.get_sheet_by_name('Sheet1')

    # Assuming the cells are in DATE or DATE_TIME format.
    cells_with_dates = sheet.get_range_from_a1("A1:A2"))

    print(cells_with_dates.get_values())
    #   [
    #       [datetime.datetime(2021, 11, 26, 16, 58, 37, 737940)],
    #       [datetime.datetime(2021, 11, 26, 16, 58, 37, 737940)]
    #   ]

This means we can introduce python datetime operation in our code very
effectively.


.. code-block:: python

    from sheetfu import SpreadsheetApp
    from datetime import datetime

    sa = SpreadsheetApp('path/to/secret.json')
    spreadsheet = sa.open_by_id('<insert spreadsheet id here>')
    sheet = spreadsheet.get_sheet_by_name('Sheet1')

    a1 = sheet.get_range_from_a1("A1")

    # The following will set today's date in the
    #cell in the right google sheet format
    a1.set_value(datetime.today())


Contributing
------------

For guidance on how to make a contribution to Sheetfu, see the `contributing guidelines`_.

.. _contributing guidelines: https://github.com/socialpoint-labs/sheetfu/blob/master/CONTRIBUTING.rst


Links
-----

* License: `MIT <https://github.com/socialpoint-labs/sheetfu/blob/master/LICENSE>`_
* Releases: https://pypi.org/project/sheetfu/
* Code: https://github.com/socialpoint-labs/sheetfu
* Issue tracker: https://github.com/socialpoint-labs/sheetfu/issues


.. _pip: https://pip.pypa.io/en/stable/quickstart/


If you are looking for the original sheetfu google apps script library, it has been relocated to `this page`_.

.. _this page: https://github.com/socialpoint-labs/sheetfu-apps-script
