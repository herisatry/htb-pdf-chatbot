#!/bin/bash

if ! pgrep -f "ollama" > /dev/null
then
    echo "Starting Ollama..."
    nohup ollama serve > ollama.log 2>&1 &
else
    echo "Ollama is already running."
fi

docker-compose up --build
