#!/bin/bash
waitress-serve --listen=*:8000 wsgi:app
