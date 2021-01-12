help:
	# make help       -- print this help doc
	# make clean      -- cleanup
	# make new        -- rebuild everything
	# make test       -- run tests

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache

new:
	rm -rf .venv
	rm poetry.lock
	make test

.venv:
	poetry install

test: .venv
	poetry run pytest


