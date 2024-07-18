A small utility to download smart meter LV feeder data from SSEN

### Usage

`python download.py -s 2024-03-12 -e 2024-03-15 -r True`

- Date should be in YYYY-MM-DD format.
- Flag `-r` is optional. It defaults to False. It only accepts boolean.

For help:

`python download.py -h`

### Todo
- Catch `urllib3.exceptions.IncompleteRead` exception.