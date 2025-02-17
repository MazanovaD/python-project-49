install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-reinstall:
	uv tool install dist/*.whl --force-reinstall

brain-games:
	uv run brain-games

make lint:
	uv run ruff check brain_games
