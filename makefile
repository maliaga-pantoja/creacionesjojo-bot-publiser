PWD=$(shell pwd)
IMAGE=wyracocha/publisherbot:v1.0.1
build:
	docker build -t ${IMAGE} .
run:
	mkdir -p files/uploaded files/pendent
	docker run --rm -d \
		-e TZ=America/Lima \
		-v ${PWD}/src:/app -w /app \
		-v ${PWD}/files:/files \
	${IMAGE} python -u /app/main.py
ad:
	./scripts/run.sh