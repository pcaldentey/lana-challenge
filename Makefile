build-docker:
	docker build --no-cache -t lanaserverimg .

run:
	docker rm lanaserver
	docker run -d --name lanaserver -p 80:80 lanaserverimg

stop:
	docker stop lanaserver
