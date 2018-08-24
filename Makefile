test: clean-pyc
	pytest

coverage: clean-pyc
	coverage run --source sheetfu -m pytest
	coverage report

cov: coverage

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +