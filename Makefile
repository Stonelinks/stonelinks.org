.PHONY: clean site

clean:
	@rm -rf build/*

compile: clean
	@rsync -avz static/ build/static/
	@python compile.py

deploy:
	#@rsync -avz build/ /var/www/build/
	@rsync -avz build/ /home/ld/Dropbox/Public/sl/
	@chmod 777 -R /home/ld/Dropbox/Public/sl/

site: compile deploy
