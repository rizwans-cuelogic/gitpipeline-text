#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn injazati.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --daemon