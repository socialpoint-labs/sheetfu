# Sheetfu API usage



## List of methods for **SpreadsheetApp**.


| **Methods for SpreadsheetApp object**                 | **return type**     |
|-------------------------------------------------------|---------------------|
| [create()](#SpreadsheetApp.create)                    |  Spreadsheet        |
| [add_permission()](#SpreadsheetApp.add_permission)    |                     |
| [open_by_id()](#SpreadsheetApp.open_by_id)            |  Spreadsheet        |
| [open_by_url()](#SpreadsheetApp.open_by_url)          |  Spreadsheet        |


For authentication, please refer to the [authentication tutorial](authentication.rst).



## List of methods for **Spreadsheet** object


| **Methods for Spreadsheet object**                    | **return type**     |
|-------------------------------------------------------|---------------------|
| [get_sheets()](#Spreadsheet.get_sheets)               |                     |
| [get_sheet_by_name()](#Spreadsheet.get_sheet_by_name) |  Sheet              |
| [get_sheet_by_id()](#Spreadsheet.get_sheet_by_id)     |  Sheet              |
| [create_sheets()](#Spreadsheet.create_sheets)         |  List[Sheet]        |
| [duplicate_sheet()](#Spreadsheet.duplicate_sheet)     |  Sheet              |
| [commit()](#Spreadsheet.commit)                       |                     |



## List of methods for **Sheet** object

| **Methods for Sheet object**                          | **return type**     |
|-------------------------------------------------------|---------------------|
| [get_range()](#Sheet.get_range)                       |  Range              |
| [get_range_from_a1()](#Sheet.get_range_from_a1)       |  Range              |
| [get_data_range()](#Sheet.get_data_range)             |  Range              |
| [get_max_rows()](#Sheet.get_max_rows)                 |  Integer            |
| [get_max_columns()](#Sheet.get_max_columns)           |  Integer            |



## List of methods for **Range** object

| **Methods for Range object**                  | **return type**     |
|-----------------------------------------------|---------------------|
| [get_values()](#Range.get_values)             |  List[List]         |
| [get_notes()](#Range.get_notes)               |  List[List]         |
| [get_backgrounds()](#Range.get_backgrounds)   |  List[List]         |
| [get_font_colors()](#Range.get_font_colors)   |  List[List]         |
| [set_values()](#Range.set_values)             |                     |
| [set_notes()](#Range.set_notes)               |                     |
| [set_backgrounds()](#Range.set_backgrounds)   |                     |
| [set_font_colors()](#Range.set_font_colors)   |                     |
| [set_value()](#Range.set_value)               |                     |
| [set_note()](#Range.set_note)                 |                     |
| [set_background()](#Range.set_background)     |                     |
| [set_font_color()](#Range.set_font_color)     |                     |
| [commit()](#Range.commit)                     |                     |
| [get_row()](#Range.get_row)                   |  Integer            |
| [get_column()](#Range.get_column)             |  Integer            |
| [get_max_row()](#Range.get_max_row)           |  Integer            |
| [get_max_column()](#Range.get_max_column)     |  Integer            |
| [get_cell()](#Range.get_cell)                 |  Range              |
| [add_dropdown()](#Range.add_dropdown)         |  Integer            |



## SpreadsheetApp Methods


### <a name="SpreadsheetApp.create" >create()</a>


```python
from sheetfu import SpreadsheetApp

sa = SpreadsheetApp('path/to/secret.json')
spreadsheet = sa.create(name='my spreadsheet', editor='youremail@gmail.com')
```

It is highly recommended to add your email as an editor. This will make your
email the owner of the newly created spreadsheet instead of the service account
user from your secret.json. As a result, you will be able to find the created
spreadsheets in your Google Drive.


### <a name="SpreadsheetApp.add_permission" >add_permission()</a>

This method will give ownership to any user for any spreadsheets created by
the service account. Useful, if you have not indicated an editor in the create()
method.

```python

from sheetfu import SpreadsheetApp

sa = SpreadsheetApp('path/to/secret.json')
sa.add_permission(file_id='<spreadsheet_id>', default_owner='youremail@gmail.com')
```


### <a name="SpreadsheetApp.open_by_id" >open_by_id()</a>


```python

from sheetfu import SpreadsheetApp

sa = SpreadsheetApp('path/to/secret.json')
spreadsheet = sa.open_by_id(spreadsheet_id='<spreadsheet id>')
```

Returns a Spreadsheet object.


### <a name="SpreadsheetApp.open_by_url" >open_by_url()</a>

```python

from sheetfu import SpreadsheetApp

sa = SpreadsheetApp('path/to/secret.json')
spreadsheet = sa.open_by_url(url='http://<spreadsheet url>')
```
Returns a Spreadsheet object.


## Spreadsheet Methods



### <a name="Spreadsheet.get_sheets" >get_sheets()</a>



```python

from sheetfu import SpreadsheetApp

sa = SpreadsheetApp('path/to/secret.json')
spreadsheet = sa.open_by_id(spreadsheet_id='<spreadsheet id>')
sheets = spreadsheet.get_sheets()
```


### <a name="Spreadsheet.get_sheet_by_name" >get_sheet_by_name()</a>



```python

from sheetfu import SpreadsheetApp

sa = SpreadsheetApp('path/to/secret.json')
spreadsheet = sa.open_by_id(spreadsheet_id='<spreadsheet id>')
sheet1 = spreadsheet.get_sheet_by_name('Sheet1')
```


### <a name="Spreadsheet.get_sheet_by_id" >get_sheet_by_id()</a>


```python

from sheetfu import SpreadsheetApp

sa = SpreadsheetApp('path/to/secret.json')
spreadsheet = sa.open_by_id(spreadsheet_id='<spreadsheet id>')
sheet1 = spreadsheet.get_sheet_by_id('<sheet_id>')
```


### <a name="Spreadsheet.create_sheets" >create_sheets()</a>



```python

from sheetfu import SpreadsheetApp

sa = SpreadsheetApp('path/to/secret.json')
spreadsheet = sa.open_by_id(spreadsheet_id='<spreadsheet id>')
new_sheets = spreadsheet.create_sheets(['my_first_sheet', 'my_second_sheet'])
```


It returns a list of Sheet objects in the same order of the new sheet names
list given as parameter.


### <a name="Spreadsheet.duplicate_sheet" >duplicate_sheet()</a>


```python

from sheetfu import SpreadsheetApp

sa = SpreadsheetApp('path/to/secret.json')
spreadsheet = sa.open_by_id(spreadsheet_id='<spreadsheet id>')
cloned_sheet = spreadsheet.duplicate_sheet(
    new_sheet_name='cloned name',
    sheet_name='original sheet'
)
```

`cloned_sheet` in that case will return the Sheet object of the new cloned
sheet.


## Sheet Methods


### <a name="Sheet.get_range" >get_range()</a>


```python

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
    number_of_row=2,
    number_of_column=2
)

```

### <a name="Sheet.get_range_from_a1" >get_range_from_a1()</a>


```python

from sheetfu import SpreadsheetApp

sa = SpreadsheetApp('path/to/secret.json')
spreadsheet = sa.open_by_id(spreadsheet_id='<spreadsheet id>')
sheet1 = spreadsheet.get_sheet_by_name('Sheet1')

# to get cell A1
A1_cell = sheet1.get_range_from_a1(a1_notification='A1')

# to get cell A3:B5
A3_B5_range = sheet1.get_range_from_a1(a1_notification='A3:B5')
```


### <a name="Sheet.get_data_range" >get_data_range()</a>


```python

from sheetfu import SpreadsheetApp

sa = SpreadsheetApp('path/to/secret.json')
spreadsheet = sa.open_by_id(spreadsheet_id='<spreadsheet id>')
sheet = spreadsheet.get_sheet_by_name('Sheet1')
data_range = sheet.get_data_range()
```

This method is particularly useful when you're not quite sure how many rows you
have in your sheet. Under the hood, this method actually makes a request to the
sheet and figure out the A1 notification of the range containing data.


### <a name="Sheet.get_max_row" >get_max_row()</a>


Method to return the last row in sheet. this does not necessarily means a row
with data. An empty new sheet, typically, has 1000 rows. The method in that
case will return 1000.

```python

from sheetfu import SpreadsheetApp

sa = SpreadsheetApp('path/to/secret.json')
spreadsheet = sa.open_by_id(spreadsheet_id='<spreadsheet id>')
sheet = spreadsheet.get_sheet_by_name('Sheet1')
max_row = sheet.get_max_row()
```

### <a name="Sheet.get_max_column" >get_max_column()</a>


Method to return the last column in sheet. this does not necessarily means a
column with data. An empty new sheet, typically, has 26 columns (letter Z). The
method in that case will return 26 even if the sheet has no data.

```python

from sheetfu import SpreadsheetApp

sa = SpreadsheetApp('path/to/secret.json')
spreadsheet = sa.open_by_id(spreadsheet_id='<spreadsheet id>')
sheet = spreadsheet.get_sheet_by_name('Sheet1')
max_row = sheet.get_max_column()
```

### Range Methods


The Range object is where the magic happens. This is from this object that you
will be able to get or set values, notes, colors, etc.
This object implies working with two-dimensional lists (list of list) where an
inside list represents a row.


### <a name="Range.get_values" >get_values()</a>

```python

from sheetfu import SpreadsheetApp

ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
data_range = ss.get_sheet_by_name('Sheet1').get_data_range()
values = data_range.get_values()

# values = [
#    ['name', 'surname', 'age'],
#    ['john', 'doe', 28],
#    ['jane', 'doe', 27]
# ]
```
The values are returned in the form of a 2D arrays. Empty cells will return
empty strings.

### <a name="Range.get_notes" >get_notes()</a>

```python

from sheetfu import SpreadsheetApp

ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
data_range = ss.get_sheet_by_name('Sheet1').get_data_range()
notes = data_range.get_notes()
```

Similar to get_values(), this will return a 2D list of the notes. When a cell
does not contain a note, it returns an empty string.


### <a name="Range.get_backgrounds" >get_backgrounds()</a>


```python

from sheetfu import SpreadsheetApp

ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
data_range = ss.get_sheet_by_name('Sheet1').get_data_range()

backgrounds = data_range.get_backgrounds()

# [
#    ['#ffffff', '#123456', '#000000'],
#    ['#ffffff', '#123456', '#000000'],
#    ['#ffffff', '#123456', '#000000']
#]
```
The backgrounds colors are returned in the hexadecimal forms. An empty cell
returns a white background (#ffffff).

### <a name="Range.get_font_colors" >get_font_colors()</a>

```python

from sheetfu import SpreadsheetApp

ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
data_range = ss.get_sheet_by_name('Sheet1').get_data_range()

font_colors = data_range.get_font_colors()

# [
#    ['#000000', '#000000', '#000000'],
#    ['#000000', '#000000', '#000000'],
#    ['#000000', '#000000', '#000000'],
#]
```
The font colors are returned in the hexadecimal forms. An empty cell
returns a black font (#000000).

### <a name="Range.set_values" >set_values()</a>

```python

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
```
This will simply fill the values into the range A1:B3. A 2D list must be
submitted, matching the range size. If it does not match, an error will be
raised.
Committing must be done or none of the changes will be sent to the spreadsheets.

### <a name="Range.set_notes" >set_notes()</a>

```python

from sheetfu import SpreadsheetApp

ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
data_range = ss.get_sheet_by_name('Sheet1').get_range_from_a1('A1:B3')

notes = [
    ['this is a note', 'this is a note'],
    ['', ''],
    ['', '']
]
data_range.set_notes(notes)
data_range.commit()
```
This would set notes on the top 2 cells of the range. Empty strings means no
notes to be submitted.

### <a name="Range.set_backgrounds" >set_backgrounds()</a>

```python

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
```

### <a name="Range.set_font_colors" >set_font_colors()</a>


```python

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
```

### <a name="Range.set_value" >set_value()</a>


```python

from sheetfu import SpreadsheetApp

ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
data_range = ss.get_sheet_by_name('Sheet1').get_range_from_a1('A1:B3')
data_range.set_value('foo')
data_range.commit()
```
This would set cells value to 'foo' in the whole range.

### <a name="Range.set_note" >set_note()</a>


```python

from sheetfu import SpreadsheetApp

ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
data_range = ss.get_sheet_by_name('Sheet1').get_range_from_a1('A1:B3')
data_range.set_note('this is a note')
data_range.commit()
```
This would put the note 'this is a note' on every cells within the range.

### <a name="Range.set_background" >set_background()</a>

```python

from sheetfu import SpreadsheetApp

ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
data_range = ss.get_sheet_by_name('Sheet1').get_range_from_a1('A1:B3')
data_range.set_background('#0000FF')
data_range.commit()
```
This would set the background of the whole range in blue.

### <a name="Range.set_font_color" >set_font_color()</a>


```python

from sheetfu import SpreadsheetApp

ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
data_range = ss.get_sheet_by_name('Sheet1').get_range_from_a1('A1:B3')
data_range.set_font_color('#0000FF')
data_range.commit()
```
This would set the font colors of the whole range in blue.


### <a name="Range.get_row" >get_row()</a>


```python

from sheetfu import SpreadsheetApp

ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
data_range = ss.get_sheet_by_name('Sheet1').get_range_from_a1('A1:B3')
data_range.get_row() # 1
```



### <a name="Range.get_column" >get_column()</a>


```python

from sheetfu import SpreadsheetApp

ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
data_range = ss.get_sheet_by_name('Sheet1').get_range_from_a1('A1:B3')
data_range.get_column() # 1
```

### <a name="Range.get_max_row" >get_max_row()</a>


```python

from sheetfu import SpreadsheetApp

ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
data_range = ss.get_sheet_by_name('Sheet1').get_range_from_a1('A1:B3')
data_range.get_max_row() # 3
```

### <a name="Range.get_max_column" >get_max_column()</a>

```python

from sheetfu import SpreadsheetApp

ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
data_range = ss.get_sheet_by_name('Sheet1').get_range_from_a1('A1:B3')
data_range.get_max_column() # 2
```


### <a name="Range.get_cell" >get_cell()</a>


Get the range of a specific cell by giving its coordinates within the parent
range. First row and first column starts at 1 (to keep it consistent with
google sheet api).

```python

from sheetfu import SpreadsheetApp

ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
data_range = ss.get_sheet_by_name('Sheet1').get_range_from_a1('A1:B3')
cell_range = data_range.get_cell(row=1, column=1)
```


### <a name="Range.add_dropdown" >add_dropdown()</a>


Adds a dropdown with the given options on every cells within the range.

```python

from sheetfu import SpreadsheetApp

ss = SpreadsheetApp('path/to/secret.json').open_by_id(spreadsheet_id='<spreadsheet id>')
data_range = ss.get_sheet_by_name('Sheet1').get_range_from_a1('A1:B3')
choices = [
    'option1'
    'option2'
]
data_range.add_dropdown(choices)
```