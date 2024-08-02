FROM python:3.11.0
WORKDIR /usr/local/app

COPY ./requirements.txt ./
RUN pip install --prefer-binary --no-cache-dir --upgrade -r requirements.txt

COPY ./*.py ./

ENTRYPOINT [ "python", "download.py" ]