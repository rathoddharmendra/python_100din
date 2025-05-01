APP_NAME = producer
VERSION = kafka-producer
IMAGE_NAME = $(USERNAME)/$(APP_NAME):$(VERSION)
USERNAME = rathoddharmendra

build:
	docker build -t $(IMAGE_NAME) .
	
push:
	docker push $(IMAGE_NAME)

apply:
	kubectl apply -f k8s/deployment.yaml

delete:
	kubectl delete -f k8s/deployment.yaml
	
logs:
	kubectl logs -l app=$(APP_NAME) --tail=100 -f
