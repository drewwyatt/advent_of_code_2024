VENV = venv

.PHONY: setup activate clean compile install

setup:
	@echo "Creating virtual environment..."
	python3 -m venv $(VENV)
	$(VENV)/bin/python -m pip install --upgrade pip

activate:
	@echo "Run this to activate the virtual environment:"
	@echo "source $(VENV)/bin/activate"

compile:
	$(VENV)/bin/python -m pip install pip-tools
	$(VENV)/bin/pip-compile

install: setup compile
	$(VENV)/bin/pip install -r requirements.txt

clean:
	rm -rf $(VENV)
