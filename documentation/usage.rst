Spreadsheet API usage
=====================



List of methods for SpreadsheetApp. For authentication, please refer to
`the authentication tutorial`_.

.. _the authentication tutorial: https://github.com/socialpoint-labs/sheetfu/blob/master/documentation/authentication.rst


+----------------------------------------------------+---------------------+
| Method                                             | return type         |
+----------------------------------------------------+---------------------+
| `create() <usage.rst#create()>`__                  |  Spreadsheet        |
+----------------------------------------------------+---------------------+
| `add_permission() <usage.rst#add_permission()>`__  |                     |
+----------------------------------------------------+---------------------+
| `open_by_id() <usage.rst#open_by_id()>`__          |  Spreadsheet        |
+----------------------------------------------------+---------------------+
| `open_by_url() <usage.rst#open_by_url()>`__        |  Spreadsheet        |
+----------------------------------------------------+---------------------+



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
