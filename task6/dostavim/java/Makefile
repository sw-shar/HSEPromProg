IMAGE = 4-maven-java

build:
	docker build . -t $(IMAGE)
	
run:
	docker run --rm --name=$(IMAGE) -it $(IMAGE) bash
