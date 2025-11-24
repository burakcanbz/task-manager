#!/bin/bash

# Redis container var mı kontrol et
if docker ps -a --format '{{.Names}}' | grep -q '^redis_local$'; then
    # Container var mı ayakta mı kontrol et
    if ! docker ps --format '{{.Names}}' | grep -q '^redis_local$'; then
        # Var ama kapalı, başlat
        docker start redis_local
        echo "Redis container started"
    else
        echo "Redis container already running"
    fi
else
    # Container yok, oluştur
    docker run -d --name redis_local -p 6379:6379 redis:latest
    echo "Redis container created"
fi

cd ./api || exit

if [ -f "./venv/bin/activate" ]; then
    source ./venv/bin/activate
    echo "Virtual environment activated"
else
    echo "No venv found, please create one first"
fi

python -m uvicorn app:app --reload