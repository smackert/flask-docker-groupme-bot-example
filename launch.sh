#!/bin/sh

if [ "$IS_PRODUCTION" = "true" ]; then
    echo "Launching in PRODUCTION mode."
    waitress-serve --host 0.0.0.0 --port 5000 main:app
else
    echo "Launching in DEV mode."
    flask run
fi