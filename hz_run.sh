#~/bin/bash

programs=(hz hz hz hz-mc)

for ((i=0; i<${#programs[@]}; i++)); do
    program=${programs[i]}
    name="$program-$i"
    if ! $(screen -list | grep $name > /dev/null); then
        echo "Starting $name..."
        screen -S $name -d -m $program start
    fi
done


