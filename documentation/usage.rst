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



Spreadsheet Methods
===================


**get_sheets()**
----------------


.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')




**get_sheet_by_name()**
-----------------------


.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')



**get_sheet_by_id()**
---------------------


.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')



**create_sheets()**
-------------------


.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')



**duplicate_sheet()**
---------------------


.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')


**commit() - Spreadsheet**
--------------------------


.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')



Sheet Methods
=============


**get_range()**
---------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')



**get_range_from_a1()**
-----------------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')



**get_data_range()**
--------------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')



**get_max_rows()**
------------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')



**get_max_columns()**
---------------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')






Range Methods
=============


**get_values()**
----------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')


**get_notes()**
---------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')


**get_backgrounds()**
---------------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')


**get_font_colors()**
---------------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')


**set_values()**
----------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')



**set_notes()**
---------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')


**set_backgrounds()**
---------------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')



**set_font_colors()**
---------------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')



**set_value()**
---------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')



**set_note()**
--------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')


**set_background()**
--------------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')


**set_font_color()**
--------------------

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')

