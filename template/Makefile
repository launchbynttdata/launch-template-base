.PHONY: test
test:
	@uv run pytest

.PHONY: render
render:
	@uv run copier copy . temp/ --trust

.PHONY: render-defaults
render-defaults:
	@uv run copier copy . temp/ --trust --defaults

.PHONY: clean
clean:
	@find temp/ -mindepth 1 -maxdepth 1 -exec rm -rf {} \;
