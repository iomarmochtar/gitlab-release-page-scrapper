.PHONY: setup dev unit-test lint tests

VIRTENVDIR = virtenv
BINDIR = $(VIRTENVDIR)/bin

setup:
	if [ ! -d $(VIRTENVDIR) ]; then python3 -m venv $(VIRTENVDIR) ;fi
	$(BINDIR)/pip install -r requirements/common.txt

dev: setup
	$(BINDIR)/pip install -r requirements/dev.txt

unit-test:
	$(BINDIR)/python -m unittest discover -s . -p 'test_*'

lint:
	$(BINDIR)/pylint shared.py scrap_*
	$(BINDIR)/mypy --ignore-missing-imports shared.py scrap_*

tests: unit-test lint