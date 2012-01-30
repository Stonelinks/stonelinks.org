.PHONY: clean site

clean:
	@rm -rf build/*

compile: clean
	@rsync -avz static/ build/static/
	@rsync -avz content/ build/
	@python compile.py

deploy:
	#@rsync -avz build/ /var/www/build/
	@rsync -avz build/ /home/ld/Dropbox/Public/sl/
	@chmod 777 -R /home/ld/Dropbox/Public/sl/

	@rsync -axhvve ssh build/ root@stonelinks.org:/media/sdb1
	#@ssh root@stonelinks.org 'service apache2 restart && \
	#                          chmod 755 -R /ABS/static && \
	#                          chown ld -R /ABS/static && \
	#                          cd /ABS && \
	#                          pip install -r requirements.txt && \
	#                          python manage.py syncdb && python manage.py migrate '
	@echo "\n"
	@echo "==============================="
	@echo "=   Deployed to stonelinks!   ="
	@echo "==============================="
	@echo "\n\n"




site: compile deploy
