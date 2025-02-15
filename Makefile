VENV = venv

.PHONY: setup activate clean compile install format check-format check-types lint test new-day

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
	@if [ -z "$(day)" ]; then \
		echo "Usage: make solution day=<day_number> [part=<part_number>]"; \
		exit 1; \
	elif [ -z "$(part)" ]; then \
		python main.py $(day); \
	else \
		python main.py $(day) $(part); \
	fi

format:
	$(VENV)/bin/black .

check-format:
	$(VENV)/bin/black --check .

check-types:
	$(VENV)/bin/pyright .

lint: check-format check-types
	@echo "Linting passed!"

test:
	$(VENV)/bin/pytest solutions/

new-day:
	@read -p "Enter day number (e.g., 3 or 03): " day && \
	day_formatted=$$(printf "%02d" $$day) && \
	cookiecutter $(PWD)/templates/day_template --no-input day_name=day_$$day_formatted --output-dir solutions

clean:
	rm -rf $(VENV)

