Authentication
==============


To be able to connect Sheetfu to spreadsheets you need to create a google cloud project at
https://console.cloud.google.com, with the Spreadsheet and the Drive APIs enabled.

Once your project is created, create a service account within that project:
 - to get your service account secret JSON, needed for instantiating your Sheetfu SpreadsheetApp object.
 - to get your service email account (email you need to give permission on any spreadsheet you want to interact with).


This is how a secret JSON should look like when the file is opened.

.. code-block:: json

    {
      "type": "service_account",
      "project_id": "spreadsheet-api-whatever",
      "private_key_id": "alotofdigits",
      "private_key": "-----BEGIN PRIVATE KEY-----\nA VERY LONG STRING\n-----END PRIVATE KEY-----",
      "client_email": "yourserviceclientemail@whatever.iam.gserviceaccount.com",
      "client_id": "someclientid",
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://accounts.google.com/o/oauth2/token",
      "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
      "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/whatever"
    }

Your service email account is the "client_email" attribute from the secret JSON.

Once you have your secret.json file, you can initialize the SpreadsheetApp adding the path to the secret
JSON file or creating env variables.

Here you have an example using the downloaded JSON file:

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp('path/to/secret.json')

    # to read a spreadsheet, you need your service account
    # to have permission to read it.
    spreadsheet = sa.open_by_id('1VZ8tXVWRn_h0nkvXkjfhdnffj5w68olM8Gz2oE4DAP-BY')


If you want to initialize it from ENV vars, you will need to create them and set their value with
the corresponding one from the json file.
Here you have the mapping between ENV vars and JSON fields:

.. code-block:: json

    SHEETFU_CONFIG_TYPE=type
    SHEETFU_CONFIG_PROJECT_ID=project_id
    SHEETFU_CONFIG_PRIVATE_KEY_ID=private_key_id
    SHEETFU_CONFIG_PRIVATE_KEY=private_key
    SHEETFU_CONFIG_CLIENT_EMAIL=client_email
    SHEETFU_CONFIG_CLIENT_ID=client_id
    SHEETFU_CONFIG_AUTH_URI=auth_uri
    SHEETFU_CONFIG_TOKEN_URI=token_uri
    SHEETFU_CONFIG_AUTH_PROVIDER_URL=auth_provider_x509_cert_url
    SHEETFU_CONFIG_CLIENT_CERT_URL=client_x509_cert_url

Once those ENV variables are set, you should be able to initialize it just adding
the parameter `from_env=True`, which will automatically grab the config from your ENV:

.. code-block:: python

    from sheetfu import SpreadsheetApp

    sa = SpreadsheetApp(from_env=True)

    # to read a spreadsheet, you need your service account
    # to have permission to read it.
    spreadsheet = sa.open_by_id('1VZ8tXVWRn_h0nkvXkjfhdnffj5w68olM8Gz2oE4DAP-BY')


For a more detailed explanation on how to get this secret JSON, you can follow the guidelines below.


Create a project
----------------

Go to console and find the option to create a new project. You will then be prompted for a project name.

.. image:: images/auth_create_project.png



Enable APIs
-----------

After creating your new project, go to the project dashboard, open the menu, and click on the option "APIs and Services",
as shown in screenshot.

You should now reach a new interface that covers the APIs the project can access, and also a credentials section
(to create accounts).

First click on the button "Enable APIs and Services". You will reach a new interface from where you should search for
the Spreadsheet and the Drive APIs to finally enable them.

.. image:: images/auth_enable_apis.png



Create a service account
------------------------

You now need to create a service account. Click on "Credentials" from the APIs & Services dashboard menu. You should be
prompted with the kind of account you want to create. You must select "Service account key".

.. image:: images/auth_choose_service_key.png





After choosing this option, then you can create the service account as shown below.


.. image:: images/auth_new_service_account.png




After completing this step, your browser should download a secret json file, which is the file that needs to be put in
your project for Sheetfu to work properly.



