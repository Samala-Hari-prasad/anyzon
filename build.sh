#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations (Optional: Vercel SQLite is ephemeral, but this ensures schema exists)
python manage.py migrate
