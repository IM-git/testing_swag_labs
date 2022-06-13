FROM python:3.10

RUN mkdir -p /testing_swag_labs/ &&  \
    mkdir /testing_swag_labs/allureress

WORKDIR /testing_swag_labs

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD pytest -s -v ./tests/ --alluredir=allureress
