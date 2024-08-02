A small utility to download smart meter LV feeder data from SSEN

## Usage

### Docker
- Pull docker image `docker pull herald24/ssen_download:latest`
- run docker container `docker run herald24/ssen_download -s 2024-03-12 -e 2024-03-15 -r True`


### Local Environment
`python download.py -s 2024-03-12 -e 2024-03-15 -r True`

- Date should be in YYYY-MM-DD format.
- Flag `-r` is optional. It defaults to False. It only accepts boolean.

For help:

`python download.py -h`

### Todo
- Catch `urllib3.exceptions.IncompleteRead` exception.