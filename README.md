### Word Counter

A simple app built with FastAPI to count words.

## Setup the environment

1. Create the virtual environment:
```bash
  python -m venv venv
```

2. Activate the virtual environment:
```bash
  source venv/bin/activate
```

3. Install the libraries:
```bash
  pip install -r requirements/base.txt
  pip install -r requirements/dev.txt
```

## Run the app

1. Run app
```bash
  uvicorn main:app --reload
```

2. Access the app on http://127.0.0.1:8000 and enjoy!

## Run automated tests

```bash
  pytest
```
