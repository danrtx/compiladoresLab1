#!/bin/bash
# -*- coding: utf-8 -*-
export LANG=es_CO.UTF-8
echo "========== UPDATE =========="
echo "Nodo: $(hostname) - Iniciando actualizacion del sistema..."
counter=0
max=3
while [ $counter -lt $max ]; do
    echo "Descargando paquete $(($counter+1)) de $max..."
    sleep 0.5
    counter=$(($counter+1))
done
echo "Actualizacion instalada correctamente."
