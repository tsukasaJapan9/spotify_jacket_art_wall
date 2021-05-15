run:
	.venv/bin/python main.py

setup:
	rm -rf .venv
	python -m venv .venv
	.venv/bin/pip install -r requirements.txt

clean:
	rm -rf .venv

