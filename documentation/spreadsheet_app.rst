Spreadsheet API usage
=====================



List of methods for **SpreadsheetApp**.

+-------------------------------------------------------+---------------------+
| Method                                                | return type         |
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
| Method for Spreadsheet                                | return type         |
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



