FROM python:3.8.2
COPY . /app
WORKDIR /app
CMD ["python", "catetan.py"]