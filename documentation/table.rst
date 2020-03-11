Sheetfu Table API
=================

One of the key feature of the Sheetfu library is the Table module, which
abstracts completely the coordinate system to a more table-like API.


List of methods for **Table**.

+--------------------------------------------------------------+---------------------+
| **Methods for Table object**                                 | **return type**     |
+--------------------------------------------------------------+---------------------+
| `get_table_from_sheet() <table.rst#get_table_from_sheet>`__  |  Table              |
+--------------------------------------------------------------+---------------------+
| `get_items_range() <table.rst#get_items_range>`__            |  Range              |
+--------------------------------------------------------------+---------------------+
| `add_one() <table.rst#add_one>`__                            |  Item               |
+--------------------------------------------------------------+---------------------+
| `delete() <table.rst#delete>`__                              |                     |
+--------------------------------------------------------------+---------------------+
| `delete_items() <table.rst#delete_items>`__                  |                     |
+--------------------------------------------------------------+---------------------+
| `delete_all() <table.rst#delete_all>`__                      |                     |
+--------------------------------------------------------------+---------------------+
| `sort() <table.rst#sort>`__                                  |                     |
+--------------------------------------------------------------+---------------------+
| `commit() <table.rst#commit>`__                              |                     |
+--------------------------------------------------------------+---------------------+
| `select() <table.rst#select>`__                              |  List[Item]         |
+--------------------------------------------------------------+---------------------+


List of methods for **Item**.

+--------------------------------------------------------------+---------------------+
| **Methods for Item object**                                  | **return type**     |
+--------------------------------------------------------------+---------------------+
| `get_index() <table.rst#get_index>`__                        |  Integer            |
+--------------------------------------------------------------+---------------------+
| `get_field_value() <table.rst#get_field_value>`__            |  Str/Int/Float      |
+--------------------------------------------------------------+---------------------+
| `get_field_note() <table.rst#get_field_note>`__              |  Str                |
+--------------------------------------------------------------+---------------------+
| `get_field_background() <table.rst#get_field_background>`__  |  Str                |
+--------------------------------------------------------------+---------------------+
| `get_field_font_color() <table.rst#get_field_font_color>`__  |  Str                |
+--------------------------------------------------------------+---------------------+
| `get_range() <table.rst#get_range>`__                        |  Range              |
+--------------------------------------------------------------+---------------------+
| `get_field_range() <table.rst#get_field_range>`__            |  Range              |
+--------------------------------------------------------------+---------------------+
| `set_field_value() <table.rst#set_field_value>`__            |                     |
+--------------------------------------------------------------+---------------------+
| `set_field_note() <table.rst#set_field_note>`__              |                     |
+--------------------------------------------------------------+---------------------+
| `set_field_background() <table.rst#set_field_background>`__  |                     |
+--------------------------------------------------------------+---------------------+
| `set_field_font_color() <table.rst#set_field_font_color>`__  |                     |
+--------------------------------------------------------------+---------------------+


All examples below will be based on the following data in a sheet called `people`.

+-----------------+-----------------+----------+
| **name**        | **surname**     | **age**  |
+-----------------+-----------------+----------+
| Philippe        | Oger            | 35       |
+-----------------+-----------------+----------+
| Guillem         | Orpinell        | 25       |
+-----------------+-----------------+----------+
| John            | Doe             | 33       |
+-----------------+-----------------+----------+
| Jane            | Doe             | 33       |
+-----------------+-----------------+----------+



Overview
========

This is how you would most commonly instantiate your Table object:

.. code-block:: python

    from sheetfu import Table

    spreadsheet = SpreadsheetApp('path/to/secret.json').open_by_id('<insert spreadsheet id here>')
    data_range = spreadsheet.get_sheet_by_name('people').get_data_range()

    table = Table(data_range)
    # alternatively, if you want to read notes, backgrounds and font_colors,
    # you can do as follow:
    #
    table = Table(data_range, notes=True, backgrounds=True, font_colors=True)

    # a Table object is made of Items objects (basically rows),
    # and you can easily iterate through them

    for item in table:
        print(item.get_field_value('name'))

    # Philippe
    # Guillem
    # John
    # Jane

Under the hood, the Table object download and keep in memory the whole table
data. This basically gives you the opportunity to executes multiple changes
on your sheet data by doing only two requests to the spreadsheet.

* One request to download the data
* One request (batch request) to push every changes in your data



Table Methods
=============


**commit()**
------------

This method will commit changes in your Table state and push it to the sheet.
Typically, you should apply `commit` at the end of your process, and only if
your data has changes.

.. code-block:: python

    data_range = spreadsheet.get_sheet_by_name('people').get_data_range()
    table = Table(data_range)

    for item in table:
        # the following action will not update the sheet.
        # it will only change the Table data.
        item.set_field_value('age', 30)

    # to persist your changes, you need to commit.
    table.commit()


**get_table_from_sheet()**
--------------------------

Static method to create a Table object based on a spreadsheet and a given sheet
name.

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')
    spreadsheet = sa.open_by_id(spreadsheet_id='<spreadsheet id>')

    table = Table.get_table_from_sheet(
        spreadsheet=spreadsheet,
        sheet_name='people'
    )


**select()**
------------

Conjunctive Normal Form search within items of a table.

.. code-block:: python

    data_range = spreadsheet.get_sheet_by_name('people').get_data_range()
    table = Table(data_range)

    criteria = [{'age': 33}]
    items_33_yo = table.select(criteria)

    # we can do more complex stuff
    # must be age 25 and names Philippe OR Guillem
    criterias = [
        {'age': 25},
        [{'name': 'Philippe'},{'name': 'Guillem'}]
    ]

    selected = table.select(criterias)

It returns a list of items matching the CNF criterias.


**add_one()**
-------------

Create a new item object and append to the other items within the Table object.

.. code-block:: python

    new_person = {
        'name': 'tyler',
        'surname': 'Durden,
        'age': 35
    }

    data_range = spreadsheet.get_sheet_by_name('people').get_data_range()
    table = Table(data_range)
    table.add_one(new_person)

    table.commit()


**delete()**
------------

You can delete Item from your sheet when you know its position in the table.

.. code-block:: python

    data_range = spreadsheet.get_sheet_by_name('people').get_data_range()
    table = Table(data_range)

    table.delete(indexes_to_delete=[0, 1])

    table.commit()

This will remove the first 2 items of the table. You can figure out the index
of an item with its parameter `row_index`.

.. code-block:: python

    data_range = spreadsheet.get_sheet_by_name('people').get_data_range()
    table = Table(data_range)

    for item in table:
        print(item.get_index())

    # 0
    # 1
    # 2
    # 3


**delete_items()**
------------------

You can also delete items by submitting a list of Item objects. Particularly
useful when used with the select method.

.. code-block:: python

    data_range = spreadsheet.get_sheet_by_name('people').get_data_range()
    table = Table(data_range)
    doe_people = table.select([{'surname': 'doe'}])

    table.delete_items(doe_people)

    table.commit()

**delete_all()**
----------------

.. code-block:: python

    data_range = spreadsheet.get_sheet_by_name('people').get_data_range()
    table = Table(data_range)

    table.delete_all()

Removes every rows from the table (preserve the header).

**sort()**
----------

Sort the items of the table by the given field.

.. code-block:: python

    data_range = spreadsheet.get_sheet_by_name('people').get_data_range()
    table = Table(data_range)
    table.sort('age')

    # for descending sort
    table.sort('age', reverse=True)


Item methods
============

**get_index()**
---------------

Get you the index of the Item object within the parent table. Index is 0 for
first index.

.. code-block:: python

    data_range = spreadsheet.get_sheet_by_name('people').get_data_range()
    table = Table(data_range)
    first_item = table[0]

    index = first_item.get_index()
    # 0


**get_field_value()**
---------------------

Returns the value found in the cell for the given field.

.. code-block:: python

    data_range = spreadsheet.get_sheet_by_name('people').get_data_range()
    table = Table(data_range)

    for item in table:
        print(item.get_field_value('name'))

    # Philippe
    # Guillem
    # John
    # Jane


**get_field_note()**
--------------------

Returns the note found in the cell for the given field.

.. code-block:: python

    data_range = spreadsheet.get_sheet_by_name('people').get_data_range()
    table = Table(data_range, notes=True)
    for item in table:
        print(item.get_field_note('name'))

    # if no note, it returns an empty string


**get_field_background()**
--------------------------

Returns the background color in hexadecimal format of the given field within
the item.

.. code-block:: python

    data_range = spreadsheet.get_sheet_by_name('people').get_data_range()
    table = Table(data_range, backgrounds=True)
    for item in table:
        print(item.get_field_background('name'))

    # Returns:
    # #ffffff
    # #ffffff
    # #ffffff
    # #ffffff


**get_field_font_color()**
--------------------------

Returns the font color in hexadecimal format of the given field within the item.

.. code-block:: python

    data_range = spreadsheet.get_sheet_by_name('people').get_data_range()
    table = Table(data_range, font_colors=True)
    for item in table:
        print(item.get_field_font_color('name'))

    # Returns:
    # #000000
    # #000000
    # #000000
    # #000000

**get_range()**
---------------

Returns the Range object of the table Item. Useful if you want to set some
properties that are only available at Range object level.

If setting some properties to the Range object, it is advised to manually batch
those requests into the table using the `batch_to` parameter. See below:

.. code-block:: python

    data_range = spreadsheet.get_sheet_by_name('people').get_data_range()
    table = Table(data_range)
    first_item = table[0]

    first_row_range = first_item.get_range()

    # setting in blue the background of the whole item in the table.
    # this would make a request right away to the API.
    first_row_range.set_background('#0000FF')

    # instead do the following for better performance.
    first_row_range.set_background('#0000FF', batch_to=table)

    table.commit()


**get_field_range()**
---------------------

Returns the Range object of a specific field in an Item. Useful if you want to
set some properties that are only available at Range object level on specific
cells.

If setting some properties to the Range object, it is advised to manually batch
those requests into the table using the `batch_to` parameter. See below:

.. code-block:: python

    data_range = spreadsheet.get_sheet_by_name('people').get_data_range()
    table = Table(data_range)

    for item in table:
        cell_range.add_dropdown(choices=range(0, 100), batch_to=table)

    table.commit()

This would create drop downs on every rows within the field 'age', with choices
between 0 and 99.


**set_field_value()**
---------------------

Set a value for indicated field. Must commit table data to be reflected in
sheet.

.. code-block:: python

    data_range = spreadsheet.get_sheet_by_name('people').get_data_range()
    table = Table(data_range)
    first_item = table[0]

    first_item.set_field_value('name', 'Felipe')

    table.commit()

**set_field_note()**
--------------------

Set a note for indicated field. Must commit table data to be reflected in sheet.

.. code-block:: python

    data_range = spreadsheet.get_sheet_by_name('people').get_data_range()
    table = Table(data_range)
    first_item = table[0]

    first_item.set_field_note('name', 'This is a note for my cell')

    table.commit()

**set_field_background()**
--------------------------

Set a background color for indicated field. Must commit table data to be
reflected in sheet.

.. code-block:: python

    data_range = spreadsheet.get_sheet_by_name('people').get_data_range()
    table = Table(data_range)
    first_item = table[0]

    first_item.set_field_background('name', '#0000FF')
    # this would turn in blue the background of the
    # field 'name' on the first row.

    table.commit()

**set_field_font_color()**
--------------------------

Set a font color for indicated field. Must commit table data to be reflected in
sheet.

.. code-block:: python

    data_range = spreadsheet.get_sheet_by_name('people').get_data_range()
    table = Table(data_range)
    first_item = table[0]

    first_item.set_field_value('name', '#0000FF')
    # this would turn in blue the font color of the
    # field 'name' on the first row.
    table.commit()













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


**get_max_row()**
--------------------

Method to return the last row in sheet. this does not necessarily means a row
with data. An empty new sheet, typically, has 1000 rows. The method in that
case will return 1000.

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')
    spreadsheet = sa.open_by_id(spreadsheet_id='<spreadsheet id>')
    sheet = spreadsheet.get_sheet_by_name('Sheet1')
    max_row = sheet.get_max_row()


**get_max_column()**
--------------------

Method to return the last column in sheet. this does not necessarily means a
column with data. An empty new sheet, typically, has 26 columns (letter Z). The
method in that case will return 26 even if the sheet has no data.

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')
    spreadsheet = sa.open_by_id(spreadsheet_id='<spreadsheet id>')
    sheet = spreadsheet.get_sheet_by_name('Sheet1')
    max_row = sheet.get_max_column()


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


**get_row()**
--------------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
    data_range = ss.get_sheet_by_name('Sheet1').get_range_from_a1('A1:B3')
    data_range.get_row() # 1




**get_column()**
--------------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
    data_range = ss.get_sheet_by_name('Sheet1').get_range_from_a1('A1:B3')
    data_range.get_column() # 1


**get_max_row() - Range**
-------------------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
    data_range = ss.get_sheet_by_name('Sheet1').get_range_from_a1('A1:B3')
    data_range.get_max_row() # 3


**get_max_column() Range**
-------------------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
    data_range = ss.get_sheet_by_name('Sheet1').get_range_from_a1('A1:B3')
    data_range.get_max_column() # 2