make install
make run
make test
make lint
make format
make clean

.PHONY: infra-up infra-down infra-status

infra-up:
	docker-compose up -d

infra-down:
	docker-compose down

infra-status:
	docker-compose ps
