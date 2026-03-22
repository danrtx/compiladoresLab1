#!/bin/bash
# -*- coding: utf-8 -*-
export LANG=es_CO.UTF-8
echo "========== DEPLOY =========="
echo "Nodo: $(hostname) - Iniciando despliegue de la aplicacion..."
env_var=${1:-production}

if [ "$env_var" == "production" ]; then
    echo "Desplegando en entorno de PRODUCCION."
    sleep 0.5
else
    echo "Desplegando en entorno de PRUEBAS."
    sleep 0.5
fi
echo "Servicio reiniciado."
echo "Deploy finalizado."
