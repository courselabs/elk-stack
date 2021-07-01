# https://github.com/elastic/examples/tree/master/Exploring%20Public%20Datasets/cdc_nutrition_exercise_patterns/scripts

FROM python:3.8-slim-buster

#RUN apt-get update && \
#    apt-get install -y build-essential

COPY requirements.txt .
RUN pip3 install -r requirements.txt

WORKDIR /src
COPY ./src/ .

CMD ["python3", "process_brfss_data.py"]
