.PHONY: clean site

clean:
	@rm -rf build/*

site: clean
	@rsync -avz static/ build/static/
	@python compile.py content build
