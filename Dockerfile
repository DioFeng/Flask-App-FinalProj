From python:3.7-alpine
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip3 install pyowm
EXPOSE 5000
COPY . /app
CMD ["python", "app.py"]