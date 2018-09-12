Sheetfu
=======


Sheetfu was built to interacts with Google Sheets with a simple, intuitive, and fast API.
The primary goal of this library is to adapt the Google App Script API for spreadsheets,
to Python. With Sheetfu, you can easily get or set cell values, background colors, font
colors or any other format attributes.


Installing
----------

Install and update using `pip`_:

.. code-block:: text

    pip install -U Sheetfu


A Simple Example
----------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    spreadsheet = SpreadsheetApp('path/to/secret.json').open_by_id('HGjhg45HjHgjJgjHgJhgjhgmnJhkjhKjh')
    sheet = spreadsheet.get_sheet_by_name('Sheet1')
    data_range = sheet.get_data_range()           # returns the sheet range that contains data.
    backgrounds = data_range.get_backgrounds()    # returns a 2D matrix of background colors of the range.


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