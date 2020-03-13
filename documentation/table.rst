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



Overview
========

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
        'surname': 'Durden',
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
    # this will create the request without executing it,
    # and add it to the list of pending requests at Table level.
    first_row_range.set_background('#0000FF', batch_to=table)

    # committing will make the row turn blue in your sheet.
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

    # recommended to manually add the requests to the table batch list, or
    # a request will be executed on each iteration.
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

