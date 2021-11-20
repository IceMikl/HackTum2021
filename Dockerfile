FROM python:3.8-slim-buster

WORKDIR /src

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

ADD src /src
ADD resources/Zeiss/ZEISS_hacakatum_challenge_dataset.csv ../resources/Zeiss/

EXPOSE 8050

CMD ["python3", "interactive_dash.py"]