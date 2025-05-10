#!/bin/bash
# Update system and install Docker
apt-get update -y
apt-get install -y docker.io

# Enable Docker service
systemctl start docker
systemctl enable docker

# Run Flask app (local build)
cat <<EOF > /home/ubuntu/app.py
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello from EC2!"
EOF

cat <<EOF > /home/ubuntu/Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY app.py .
RUN pip install flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
EOF

cd /home/ubuntu
docker build -t ec2-flask-app .
docker run -d -p 80:80 ec2-flask-app
