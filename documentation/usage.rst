Sheetfu API usage examples
==========================


SpreadsheetApp
--------------


List of methods for SpreadsheetApp. For authentication, please refer to
`the authentication tutorial`_.

.. _the authentication tutorial: https://github.com/socialpoint-labs/sheetfu/blob/master/documentation/authentication.rst


+------------------------------------------+-------------------------------+
| Method                                   | return type                   |
+------------------------------------------+-------------------------------+
| create() create_                         |  Spreadsheet                  |
+------------------------------------------+-------------------------------+
| `add_permission() add-permission_`       |                               |
+------------------------------------------+-------------------------------+
| open_by_id():ref:`open-by-id`            |  Spreadsheet                  |
+------------------------------------------+-------------------------------+
| open_by_url() open-by-url_               |  Spreadsheet                  |
+------------------------------------------+-------------------------------+



.. _create:
**create()**

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')
    spreadsheet = sa.create(name='my spreadsheet', editor='youremail@gmail.com')

It is highly recommended to add your email as an editor. This will make your
email the owner of the newly created spreadsheet instead of the service account
user from your secret.json. As a result, you will be able to find the created
spreadsheets in your Google Drive.


.. _add-permission:
**add_permission()**

This method will give ownership to any user for any spreadsheets created by
the service account. Useful, if you have not indicated an editor in the create()
method.

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')
    sa.add_permission(file_id='<spreadsheet_id>', default_owner='youremail@gmail.com')



.. _open-by-id:
**open_by_id()**

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')
    spreadsheet = sa.open_by_id(spreadsheet_id='<spreadsheet id>')

Returns a Spreadsheet object.


.. _open-by-url:
**open_by_url()**

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')
    spreadsheet = sa.open_by_url(url='http://<spreadsheet url>')
