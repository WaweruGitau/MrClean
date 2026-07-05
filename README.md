# Mr Clean — Order Tracker

A Django CRUD app for tracking cleaning-service orders — create, view, edit,
and delete client orders through a Bootstrap-styled interface.

## Features

- **List orders** — view all client orders at a glance
- **Order detail** — see the full detail of a single order
- **Create / edit** — a form for adding a new order or updating an existing
  one (client name, item, quantity, delivery date)
- **Delete** — remove an order

## Tech Stack

- **Django** (4.2)
- **SQLite** — default Django database backend
- **Bootstrap** — front-end styling for the templates

## Getting Started

### 1. Environment

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install django
```

### 3. Configure environment variables

The app reads its secret key and debug flag from the environment:

```bash
# Windows (PowerShell)
$env:DJANGO_SECRET_KEY = "<generate-your-own>"
$env:DJANGO_DEBUG = "True"
# Linux/Mac
export DJANGO_SECRET_KEY="<generate-your-own>"
export DJANGO_DEBUG=True
```

Generate a key with:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 4. Run migrations and start the server

```bash
python manage.py migrate
python manage.py runserver
```

The app is available at `http://localhost:8000`.

## Project Structure

```
.
├── clean/              # Django app: models, views, forms, URLs, settings
│   ├── models.py       # Order model
│   ├── views.py        # List/detail/create/edit/delete views
│   ├── forms.py        # OrderForm
│   └── urls.py
├── templates/          # Bootstrap-styled HTML templates
├── static/              # Bootstrap CSS/JS
└── manage.py
```
