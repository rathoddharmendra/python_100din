# FROM golang:1.22-alpine as builder
# WORKDIR /app
# COPY go/. ./
# RUN go mod download
# COPY . .
# RUN go build -o bin/operator .

# # RUN
# FROM alpine:latest
# RUN apk add --no-cache curl
# WORKDIR /app
# COPY --from=builder ["/app/bin/operator", "/app/"]
# ENTRYPOINT ["/app/operator"]


FROM python:3.11-slim
RUN apt-get update && apt-get install -y curl
WORKDIR /app
COPY flask/ .
# RUN ['python', '-m', 'pip', 'install', '--no-cache-dir', '-r', 'requirements.txt']
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000
ENTRYPOINT ["python", "main.py"]