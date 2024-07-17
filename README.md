A small utility to download smart meter LV feeder data from SSEN

### Usage

`python download.py -s 2024-03-12 -e 2024-03-15`

Date should be in YYYY-MM-DD format.

For help:

`python download.py -h`

### Todo
- Catch `urllib3.exceptions.IncompleteRead` exception.