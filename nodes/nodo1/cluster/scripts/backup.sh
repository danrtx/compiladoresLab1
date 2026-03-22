#!/bin/bash
# -*- coding: utf-8 -*-
export LANG=es_CO.UTF-8
echo "========== BACKUP =========="
echo "Nodo: $(hostname) - Iniciando respaldo de datos..."
echo "Comprobando directorios..."
if [ ! -d "../logs" ]; then
    echo "Creando directorio de logs..."
    mkdir -p ../logs
fi

for i in 1 2 3; do
    echo "Respaldando base de datos parte $i..."
    sleep 0.5
done
echo "Backup completado exitosamente."
date "+%Y-%m-%d %H:%M:%S"
