FROM python:3.10-slim

WORKDIR /code

COPY ./requirements.txt /code/

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ /code/

RUN chmod +x ./start.sh

CMD ["./start.sh"]
