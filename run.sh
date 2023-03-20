#~/bin/bash

services=(facade logging messages)
start_port=8000
for ((i=0; i<${#services[@]}; i++)); do
    name=${services[i]}
    port=$((i+start_port))
    if ! $(screen -list | grep $name > /dev/null); then
        echo "Starting $name..."
        screen -S $name -d -m python3 -m uvicorn $name-service.controller:app --reload --port $port
    fi
done
