FROM python:3.10-slim-bullseye
ADD main.py .
ADD requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "./main.py"]