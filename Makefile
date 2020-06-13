build-docker:
	docker build --no-cache -t lanaserverimg .

run:
	docker run -d --name lanaserver -p 80:80 lanaserverimg

stop:
	docker stop lanaserver
	docker rm lanaserver

rundev:
	docker run -d --name lanaserver -p 80:80 -v /home/pcaldentey/dev/workSearch/lana-challenge/app:/app -v /home/pcaldentey/dev/workSearch/lana-challenge/client:/client lanaserverimg  /start-reload.sh
