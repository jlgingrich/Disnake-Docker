.PHONY: all push clean latest 3.11-alpine

TAG = jlgingrich/disnake

latest:
	@docker build . -t ${TAG}

push:
	@docker push ${TAG}

up:
	@docker compose up -d

down:
	@docker compose down

clean:
# Remove all docker images with the base tag
	@docker images -a | grep "${TAG}*" | awk '{print $$1 ":" $$2}' | xargs docker rmi