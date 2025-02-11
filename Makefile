.PHONY: dev, down, prod

prod:
	docker-compose up --build -d

down:
	docker-compose down

dev:
	docker-compose -f docker-compose.dev.yml up --build -d && npm --prefix ovalie/paparugby-vite run dev
