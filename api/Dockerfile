FROM python:3.7-alpine
RUN apk add --no-cache gcc musl-dev linux-headers
WORKDIR /api
ADD . /api
COPY anothertest.py /api
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["anothertest.py"]
EXPOSE 5050
