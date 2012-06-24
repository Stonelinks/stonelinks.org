.PHONY: clean compile deploy site

clean:
	@rm -rf build/*

compile: clean
	@rsync -avz static/ build/static/
	@rsync -avz content/ build/
	@python compile.py

deploy:
	#@rsync -avz build/ /home/ld/Dropbox/Public/sl/ &
	#@chmod 777 -R /home/ld/Dropbox/Public/sl/ &
	#@rsync -axhvve ssh build/ root@ec2-23-22-179-77.compute-1.amazonaws.com:/var/www
	@rsync -axhvve ssh build/ root@stonelinks.org:/var/www

	@echo "\n"
	@echo "==============================="
	@echo "=   Deployed to stonelinks!   ="
	@echo "==============================="
	@echo "\n\n"

site: compile deploy
