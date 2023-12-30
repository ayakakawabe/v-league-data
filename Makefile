.PHONY: setup start run stop

setup:
	docker-compose build
	docker-compose up -d

start:
	docker-compose start
	. ./messageShell/startMessage.sh
enter:
	docker-compose exec python bash

stop:
	docker-compose stop
	. ./messageShell/stopMessage.sh