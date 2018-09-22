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

    spreadsheet = SpreadsheetApp('path/to/secret.json').open_by_id('HGjhg45HjHgjJgjHgJhgjhgmnJhkjhKjh')
    sheet = spreadsheet.get_sheet_by_name('Sheet1')
    data_range = sheet.get_data_range()           # returns the sheet range that contains data values.

    # this is how you get things
    values = data_range.get_values()              # returns a 2D matrix of values.
    backgrounds = data_range.get_backgrounds()    # returns a 2D matrix of background colors in hex format.

    # this is how you set things
    data_range.set_background('#000000')          # set every cell backgrounds to black
    data_range.set_background('#ffffff')          # set every cell font colors to white


To obtain your secret json file, you can refer to `the authentication tutorial`_.

.. _the authentication tutorial: https://github.com/socialpoint-labs/sheetfu/blob/master/documentation/authentication.rst


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