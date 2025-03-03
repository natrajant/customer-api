FROM python:3.12.7
WORKDIR /api
COPY ./requirements.txt /api/requirements.txt
RUN pip install -r /api/requirements.txt
COPY ./src /api/src
EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
