build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

shell:
	docker-compose exec app bash

logs:
	docker-compose logs -f app

ps:
	docker-compose ps -a

test:
	docker-compose exec app poetry run pytest

fmt:
	docker-compose exec app poetry run black src tests

lint:
	docker-compose exec app poetry run flake8
