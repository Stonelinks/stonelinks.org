.PHONY: clean compile deploy site

clean:
	@rm -rf build/*

compile: clean
	@rsync -avz static/ build/static/
	@rsync -avz content/ build/
	@python compile.py

deploy:
	@rsync -avz build/ /home/ld/Dropbox/Public/sl/ &
	@chmod 777 -R /home/ld/Dropbox/Public/sl/ &

	@rsync -axhvve ssh build/ root@stonelinks.org:/media/sdb1
	@echo "\n"
	@echo "==============================="
	@echo "=   Deployed to stonelinks!   ="
	@echo "==============================="
	@echo "\n\n"

site: compile deploy

THINGS = $(shell find content/* | grep ".html" | cut -d "." -f1)

convert-html:
	for thing in $(THINGS); do \
	  mv $$thing.md $$thing.html ;\
	  pandoc --no-wrap -f html -t markdown -o $$thing.md $$thing.html ; \
	  rm $$thing.html ; \
	done;
