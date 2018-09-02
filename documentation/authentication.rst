Authentication
==============


To be able to connect Sheetfu to spreadsheets you need first to create a google cloud project at
https://console.cloud.google.com with the Spreadsheet and the Drive APIs enabled.
Then create a service account within that project:
 - to get your service account secret JSON, needed for instantiating your SpreadsheetApp object.
 - to get your service email account (email you need to give permission on any spreadsheet you want to interact with).


This is how a secret JSON should look like when the file is opened.

.. code-block:: json

    {
      "type": "service_account",
      "project_id": "spreadsheet-api-whatever",
      "private_key_id": "alotofdigits",
      "private_key": "-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQDcHd0eCmI8S+FbV4U3u/GyzB+g1Oh6tRa/uE5qpM7wurfLBsUR\nHEa+DuYslM7HPiTZnqbQwcvJmzaXDdHrKIALmgK3mHe/Bv0QouJqD3vlXPR9u8nm\nJb1ayw2aBbT1xc6MJeuf1bbxKO74xRpIO7rhP5/V/5smbitXRKH4qmOEIQIDAQAB\nAoGBALEJ1/m8ckx633OfDgfIw1qCcQHjnGRtWDG1ZGTDz6mxE/hYppHfg0qEIz9C\nJJn98peR0ivfYy/xBdQyil8wQOMVJJBGOWc56/EYexsa1arPhIIhgZr5a2ITUSpm\nHHutY8qlGJFm3H/Ma1b/ZxGax+ydixffjB1F5dB+WR7nJ/IdAkEA/mBBjwoUUC6L\nhuoZjQ27dqAaUSFjJcTalwiG5Y41rmfGsuqQ714lHeDT/gjjyCo8qzYJ2W4/WDFV\nFYOfCyUyNwJBAN2FnYNMZEB+FqqfvtHBZOhKScX5g4i0JUXwlLg71swGDO4mG3n6\n/fmaxDzqLLtH6Y1KOiFUGM20PFZI3ToOMGcCQQD3eo5Nq3C30ZDNYVQadxG7B2iT\nJfhf9nT0G8eh7gkr9KrLxonbV6yktOeKbvus8eq0Z46Ni0T1eIletP82yKlhAkBn\nMdF40uN478QbZCN+j3s0gzbu1RejXVhnxnVhhe7ASKlJX9M49eXOm3yDbAu+iveP\n7F48HHMZkLby8yqr2uRNAkEAwq5/TDWUqBNvtUgS876874g51ojQLts5+y4pUH+W\njhMn/2c5VuJnBgLtV3MIWxsQVDwibZLukc9OAdG2Jg0W9Q==\n-----END RSA PRIVATE KEY-----",
      "client_email": "whatever@whatever.iam.gserviceaccount.com",
      "client_id": "someclientid",
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://accounts.google.com/o/oauth2/token",
      "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
      "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/whatever"
    }

For a more detailed explanation, you can follow the guidelines below.


Create a project
----------------

Go to console and find the option to create a new project. You will then be prompted for a project name, as shown below.

INSERT SCREENSHOT HERE



Enable APIs
-----------

After creating your new project, go to the project dashboard, open the menu, and click on the option "APIs and Services",
as shown in screenshot.

You should now reach a new interface that covers the APIs the project can access, and also a credentials section
(to create accounts).

First click on the button "Enable APIs and Services". You will reach a new interface from where you should search for
the Spreadsheet and the Drive APIs to finally enable them.


Create a service account
------------------------

You now need to create a service account. Click on "Credentials" from the APIs & Services dashboard menu. You should be
prompted with the kind of account you want to create. You must select "Service account key". After choosing this option,
then you can create the service account as shown in screenshot below.



