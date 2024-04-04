### Word Counter

A simple app built with FastAPI to count words.

## Setup the environment

1. Install [Python 3](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. Create a virtual environment:
```bash
  python -m venv venv
```

3. Activate your virtual environment:
```bash
  source venv/bin/activate
```

4. Install the libraries with pip:
```bash
  pip install -r requirements/base.txt
  pip install -r requirements/dev.txt
```

## Run the app

1. Run the app
```bash
  uvicorn main:app --reload
```

2. Access the app on http://127.0.0.1:8000 and enjoy!

## Run automated tests

```bash
  pytest
```
