FROM python:3.7-alpine
RUN apk add --no-cache gcc musl-dev linux-headers
WORKDIR /code
ADD . /code
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["gmain4.py"]
EXPOSE 5000
