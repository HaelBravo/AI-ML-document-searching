#!/bin/bash

# Terminamos el proceso en caso de haber algún error:
set -e

# Mensajes para el log de inicio.
echo "***** Iniciando Contendor *****"
echo "*** Version de Python ***"
python3 --version
echo "*** Version de pip ***"
pip --version
source venv/bin/activate
pip install -r AI-ML-document-searching/requirements.txt
echo "*****   Contenedor iniciado correctamente   *****"
echo "Para iniciar el servidor de fastapi, ejecute: fastapi dev main.py --host 0.0.0.0 --port 8000"

# Mantenemos el contenedor activo.
tail -f /dev/null