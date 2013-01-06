.PHONY: clean compile deploy site

clean:
	@rm -rf build/*
	@rm -rf build/.* &

compile: clean
	@rsync -avz static/ build/static/
	@rsync -avz content/ build/
	@python compile.py

deploy:
	@rsync -axhvve ssh build/ www-data@stonelinks.org:/var/www

	@echo "\n"
	@echo "==============================="
	@echo "=   Deployed to stonelinks!   ="
	@echo "==============================="
	@echo "\n"

site: compile deploy
