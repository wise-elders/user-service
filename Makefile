USER_SERVICE_DEV_IMAGE ?= wise-elders-user-service:dev
USER_SERVICE_TEST_IMAGE ?= wise-elders-user-service:test


.default: run

.EXPORT_ALL_VARIABLES:

run: COMPOSE ?= docker-compose -f compose-base.yml
run: docker-build
	$(COMPOSE) up -d

docker-build:
	docker build -t $(USER_SERVICE_DEV_IMAGE) .
	docker build --target=test \
	-t $(USER_SERVICE_TEST_IMAGE) .

test: docker-build
test:
	docker run \
	-t $(USER_SERVICE_TEST_IMAGE) \
	pytest