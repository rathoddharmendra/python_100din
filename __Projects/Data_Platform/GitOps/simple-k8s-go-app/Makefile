
build-go:
	docker build -t meetup-operator -f Dockerfile go/.

build:
	docker build -t flask-app .
push:
	docker tag flask-app:latest rathoddharmendra/flask-app:latest && docker push rathoddharmendra/flask-app:latest 

apply:
	kubectl apply -f k8s/ --recursive

restart:
	kubectl delete deployment flask-app && make apply
	# kubectl delete -f k8s/ --recursive