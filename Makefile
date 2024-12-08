VENV = venv

.PHONY: setup activate clean compile install solution

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

solution:
	@if [ -z "$(word 2,$(MAKECMDGOALS))" ]; then \
		echo "Usage: make run-solution <day_number>"; \
	else \
		python main.py $(word 2,$(MAKECMDGOALS)); \
	fi

clean:
	rm -rf $(VENV)

# Ignore positional arguments as Makefile targets
%:
	@:
