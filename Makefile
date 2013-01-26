SHELL := /bin/bash

help:
	@echo "usage:"
	@echo "    make deploy -- deploy to <hosting>"

deploy:
	git push heroku master
