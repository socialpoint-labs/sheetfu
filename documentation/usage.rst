Sheetfu API usage
=================



List of methods for **SpreadsheetApp**.

+-------------------------------------------------------+---------------------+
| **Methods for SpreadsheetApp object**                 | **return type**     |
+-------------------------------------------------------+---------------------+
| `create() <usage.rst#create>`__                       |  Spreadsheet        |
+-------------------------------------------------------+---------------------+
| `add_permission() <usage.rst#add_permission>`__       |                     |
+-------------------------------------------------------+---------------------+
| `open_by_id() <usage.rst#open_by_id>`__               |  Spreadsheet        |
+-------------------------------------------------------+---------------------+
| `open_by_url() <usage.rst#open_by_url>`__             |  Spreadsheet        |
+-------------------------------------------------------+---------------------+

For authentication, please refer to
`the authentication tutorial`_.

.. _the authentication tutorial: https://github.com/socialpoint-labs/sheetfu/blob/master/documentation/authentication.rst



List of methods for **Spreadsheet** object

+-------------------------------------------------------+---------------------+
| **Methods for Spreadsheet object**                    | **return type**     |
+-------------------------------------------------------+---------------------+
| `get_sheets() <usage.rst#get_sheets>`__               |  List[Sheet]        |
+-------------------------------------------------------+---------------------+
| `get_sheet_by_name() <usage.rst#get_sheet_by_name>`__ |  Sheet              |
+-------------------------------------------------------+---------------------+
| `get_sheet_by_id() <usage.rst#get_sheet_by_id>`__     |  Sheet              |
+-------------------------------------------------------+---------------------+
| `create_sheets() <usage.rst#create_sheets>`__         |  List[Sheet]        |
+-------------------------------------------------------+---------------------+
| `duplicate_sheet() <usage.rst#duplicate_sheet>`__     |  Sheet              |
+-------------------------------------------------------+---------------------+
| `commit() <usage.rst#commit - Spreadsheet>`__         |                     |
+-------------------------------------------------------+---------------------+



List of methods for **Sheet** object

+-------------------------------------------------------+---------------------+
| **Methods for Sheet object**                          | **return type**     |
+-------------------------------------------------------+---------------------+
| `get_range() <usage.rst#get_range>`__                 |  Range              |
+-------------------------------------------------------+---------------------+
| `get_range_from_a1() <usage.rst#get_range_from_a1>`__ |  Range              |
+-------------------------------------------------------+---------------------+
| `get_data_range() <usage.rst#get_data_range>`__       |  Range              |
+-------------------------------------------------------+---------------------+
| `get_max_rows() <usage.rst#get_max_rows>`__           |  Integer            |
+-------------------------------------------------------+---------------------+
| `get_max_columns() <usage.rst#get_max_columns>`__     |  Integer            |
+-------------------------------------------------------+---------------------+



List of methods for **Range** object

+-------------------------------------------------------+---------------------+
| **Methods for Range object**                          | **return type**     |
+-------------------------------------------------------+---------------------+
| `get_values() <usage.rst#get_values>`__               |  List[List]         |
+-------------------------------------------------------+---------------------+
| `get_notes() <usage.rst#get_notes>`__                 |  List[List]         |
+-------------------------------------------------------+---------------------+
| `get_backgrounds() <usage.rst#get_backgrounds>`__     |  List[List]         |
+-------------------------------------------------------+---------------------+
| `get_font_colors() <usage.rst#get_font_colors>`__     |  List[List]         |
+-------------------------------------------------------+---------------------+
| `set_values() <usage.rst#set_values>`__               |                     |
+-------------------------------------------------------+---------------------+
| `set_notes() <usage.rst#set_notes>`__                 |                     |
+-------------------------------------------------------+---------------------+
| `set_backgrounds() <usage.rst#set_backgrounds>`__     |                     |
+-------------------------------------------------------+---------------------+
| `set_font_colors() <usage.rst#set_font_colors>`__     |                     |
+-------------------------------------------------------+---------------------+
| `set_value() <usage.rst#set_value>`__                 |                     |
+-------------------------------------------------------+---------------------+
| `set_note() <usage.rst#set_note>`__                   |                     |
+-------------------------------------------------------+---------------------+
| `set_background() <usage.rst#set_background>`__       |                     |
+-------------------------------------------------------+---------------------+
| `set_font_color() <usage.rst#set_font_color>`__       |                     |
+-------------------------------------------------------+---------------------+
| `commit() <usage.rst#commit - Range>`__               |                     |
+-------------------------------------------------------+---------------------+


SpreadsheetApp Methods
======================


**create()**
------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')
    spreadsheet = sa.create(name='my spreadsheet', editor='youremail@gmail.com')

It is highly recommended to add your email as an editor. This will make your
email the owner of the newly created spreadsheet instead of the service account
user from your secret.json. As a result, you will be able to find the created
spreadsheets in your Google Drive.


**add_permission()**
--------------------

This method will give ownership to any user for any spreadsheets created by
the service account. Useful, if you have not indicated an editor in the create()
method.

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')
    sa.add_permission(file_id='<spreadsheet_id>', default_owner='youremail@gmail.com')



**open_by_id()**
----------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')
    spreadsheet = sa.open_by_id(spreadsheet_id='<spreadsheet id>')

Returns a Spreadsheet object.


**open_by_url()**
-----------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')
    spreadsheet = sa.open_by_url(url='http://<spreadsheet url>')

Returns a Spreadsheet object.


Spreadsheet Methods
===================


**get_sheets()**
----------------


.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')
    spreadsheet = sa.open_by_id(spreadsheet_id='<spreadsheet id>')
    sheets = spreadsheet.get_sheets()


**get_sheet_by_name()**
-----------------------


.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')
    spreadsheet = sa.open_by_id(spreadsheet_id='<spreadsheet id>')
    sheet1 = spreadsheet.get_sheet_by_name('Sheet1')



**get_sheet_by_id()**
---------------------


.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')
    spreadsheet = sa.open_by_id(spreadsheet_id='<spreadsheet id>')
    sheet1 = spreadsheet.get_sheet_by_id('<sheet_id>')



**create_sheets()**
-------------------


.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')
    spreadsheet = sa.open_by_id(spreadsheet_id='<spreadsheet id>')
    new_sheets = spreadsheet.create_sheets(['my_first_sheet', 'my_second_sheet'])

It returns a list of Sheet objects in the same order of the new sheet names
list given as parameter.

**duplicate_sheet()**
---------------------


.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')
    spreadsheet = sa.open_by_id(spreadsheet_id='<spreadsheet id>')
    cloned_sheet = spreadsheet.duplicate_sheet(
        new_sheet_name='cloned name',
        sheet_name='original sheet'
    )
`cloned_sheet` in that case will return the Sheet object of the new cloned
sheet.


**commit() - Spreadsheet**
--------------------------


.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')

    # todo: figure out if needed


Sheet Methods
=============


**get_range()**
---------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')
    spreadsheet = sa.open_by_id(spreadsheet_id='<spreadsheet id>')
    sheet1 = spreadsheet.get_sheet_by_name('Sheet1')

    # to get cell A1
    A1_cell = sheet1.get_range(row=1, column=1)

    # to get cell C5
    C5_cell = sheet1.get_range(row=5, column=3)

    # to get range A1:A2
    A1A2_range = sheet1.get_range(
        row=1,
        column=1,
        number_of_column=2
    )

    # to get range A1:B2
    A1B2_range = sheet1.get_range(
        row=1,
        column=1,
        number_of_row=2
        number_of_column=2
    )

    # to get range C5:F10"
    A1B2_range = sheet1.get_range(
        row=5,
        column=3,
        number_of_row=6
        number_of_column=4
    )


**get_range_from_a1()**
-----------------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')
    spreadsheet = sa.open_by_id(spreadsheet_id='<spreadsheet id>')
    sheet1 = spreadsheet.get_sheet_by_name('Sheet1')

    # to get cell A1
    A1_cell = sheet1.get_range_from_a1(a1_notification='A1')

    # to get cell A3:B5
    A3_B5_range = sheet1.get_range_from_a1(a1_notification='A3:B5')



**get_data_range()**
--------------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')
    spreadsheet = sa.open_by_id(spreadsheet_id='<spreadsheet id>')
    sheet = spreadsheet.get_sheet_by_name('Sheet1')
    data_range = sheet.get_data_range()

This method is particularly useful when you're not quite sure how many rows you
have in your sheet. Under the hood, this method actually makes a request to the
sheet and figure out the A1 notification of the range containing data.



Range Methods
=============

The Range object is where the magic happens. This is from this object that you
will be able to get or set values, notes, colors, etc.
This object implies working with two-dimensional lists (list of list) where an
inside list represents a row.


**get_values()**
----------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
    data_range = ss.get_sheet_by_name('Sheet1').get_data_range()
    values = data_range.get_values()

    # values = [
    #    ['name', 'surname', 'age'],
    #    ['john', 'doe', 28],
    #    ['jane', 'doe', 27]
    # ]

The values are returned in the form of a 2D arrays. Empty cells will return
empty strings.

**get_notes()**
---------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
    data_range = ss.get_sheet_by_name('Sheet1').get_data_range()
    notes = data_range.get_notes()

Similar to get_values(), this will return a 2D list of the notes. When a cell
does not contain a note, it returns an empty string.


**get_backgrounds()**
---------------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
    data_range = ss.get_sheet_by_name('Sheet1').get_data_range()

    backgrounds = data_range.get_backgrounds()

    # [
    #    ['#ffffff', '#123456', '#000000'],
    #    ['#ffffff', '#123456', '#000000'],
    #    ['#ffffff', '#123456', '#000000']
    #]

The backgrounds colors are returned in the hexadecimal forms. An empty cell
returns a white background (#ffffff).

**get_font_colors()**
---------------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
    data_range = ss.get_sheet_by_name('Sheet1').get_data_range()

    font_colors = data_range.get_font_colors()

    # [
    #    ['#000000', '#000000', '#000000'],
    #    ['#000000', '#000000', '#000000'],
    #    ['#000000', '#000000', '#000000'],
    #]

The font colors are returned in the hexadecimal forms. An empty cell
returns a black font (#000000).

**set_values()**
----------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
    data_range = ss.get_sheet_by_name('Sheet1').get_range_from_a1('A1:B3')

    values = [
        ['name', 'surname'],
        ['john', 'doe'],
        ['jane', 'doe'],
    ]
    data_range.set_values(values)
    data_range.commit()

This will simply fill the values into the range A1:B3. A 2D list must be
submitted, matching the range size. If it does not match, an error will be
raised.
Committing must be done or none of the changes will be sent to the spreadsheets.

**set_notes()**
---------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
    data_range = ss.get_sheet_by_name('Sheet1').get_range_from_a1('A1:B3')

    notes = [
        ['this is a note', 'this is a note'],
        ['', ''],
        ['', '']
    ]
    data_range.set_backgrounds(backgrounds)
    data_range.commit()

This would set notes on the top 2 cells of the range. Empty strings means no
notes to be submitted.

**set_backgrounds()**
---------------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
    data_range = ss.get_sheet_by_name('Sheet1').get_range_from_a1('A1:B3')

    backgrounds = [
        ['#0000FF', '#0000FF'],
        ['#0000FF', '#0000FF'],
        ['#0000FF', '#0000FF']
    ]
    data_range.set_backgrounds(backgrounds)
    data_range.commit()



**set_font_colors()**
---------------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
    data_range = ss.get_sheet_by_name('Sheet1').get_range_from_a1('A1:B3')

    font_colors = [
        ['#0000FF', '#0000FF'],
        ['#0000FF', '#0000FF'],
        ['#0000FF', '#0000FF']
    ]
    data_range.set_font_colors(font_colors)
    data_range.commit()



**set_value()**
---------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
    data_range = ss.get_sheet_by_name('Sheet1').get_range_from_a1('A1:B3')
    data_range.set_value('foo')
    data_range.commit()

This would set cells value to 'foo' in the whole range.

**set_note()**
--------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
    data_range = ss.get_sheet_by_name('Sheet1').get_range_from_a1('A1:B3')
    data_range.set_note('this is a note')
    data_range.commit()

 This would put the note 'this is a note' on every cells within the range.

**set_background()**
--------------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
    data_range = ss.get_sheet_by_name('Sheet1').get_range_from_a1('A1:B3')
    data_range.set_background('#0000FF')
    data_range.commit()

This would set the background of the whole range in blue.

**set_font_color()**
--------------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
    data_range = ss.get_sheet_by_name('Sheet1').get_range_from_a1('A1:B3')
    data_range.set_font_color('#0000FF')
    data_range.commit()

This would set the font colors of the whole range in blue.

**commit()**
--------------------

This method is a key part of the API. It permits us to send all the changes we set
at the same time, using the batch API of the google sheets v4 API.

.. code-block:: python

    from sheetfu import SpreadsheetApp

    ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
    data_range = ss.get_sheet_by_name('Sheet1').get_range_from_a1('A1:B3')
    data_range.set_background('#000000')   # black background
    data_range.set_font_color('#0000FF')   # blue font

    values = [
        ['name', 'surname'],
        ['john', 'doe'],
        ['jane', 'doe'],
    ]
    data_range.set_values(values)

    # now pushing the changes
    data_range.commit()

When you set a change, nothing is actually sent to the spreadsheet. All the
change setters instead are batched at the range level. The commit method sends
every batched requests at once. This means being able to make as many change as
you want while sending only one request to the google sheet api, giving a
significant performance boost.