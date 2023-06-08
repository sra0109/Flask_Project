From python:3.8
# specifying working directory
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt
# the docker file same directory. so '.' it copies all directories and subdirectories from current one
COPY  . /app
# entrypoint
CMD ["python", "/app/main.py"]