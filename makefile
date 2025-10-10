PWD=$(shell pwd)
IMAGE=wyracocha/publisherbot:v1.0.2
build:
	docker build -t ${IMAGE} .
run:
	mkdir -p files/uploaded files/pendent
	docker run --rm \
		-e TZ=America/Lima \
		-v ${PWD}/src:/app -w /app \
		-v ${PWD}/files:/files \
	${IMAGE} python -u /app/main.py
ad:
	./scripts/run.sh