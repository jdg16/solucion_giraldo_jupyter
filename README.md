# Prueba Tecnica

Candidato: José Daniel Giraldo Gómez

## Descargar proyecto

Puedes pedirme que te envie por correo esta solucion o puedes decargar
por github este repositorio con el siguiente comando:

```bash
git clone git@github.com:jdg16/solucion_giraldo_jupyter.git
```

# Requisitos

- Se recomienda tener un manejador de versiones de python como pyenv
- Python 3.11.6 (o cualquier version 3.11)
- Instalar dependencias disponibles en `requiriments.txt` (ver instrucciones)
- Despues de descargar el proyecto colocar los archivos de data en el mismo 
  directorio del proyecto.

## Configuración de Python y virtual environment

Nota: este paso es opcional si ya se tiene python y/o si 
usted no desea aislar las dependencias, de ser asi salte
al paso de instalación de dependencias.

- En caso de tener instalado pyenv instalar python 

```bash
pyenv install 3.11.6
pyenv shell 3.11.6
```

- Creamos un virtual environment para aislar el proyecto

```bash
python -m venv .venv
```

- Activamos el virtual environment en el terminal 

```bash
 source .venv/bin/activate
```

- Si esta usando visual estudio code por favor acepte este environment
  como su entorno para instalar dependencias.

## Instacion de dependencias

Ejecutar

```bash
pip install -r requirements.txt
```

## Jupyter

Para ejecutar la prueba ejecute el archivo `prueba.ipynb` con su editor
de preferencia. (Yo use visual estudio code con las extensiones de Jupyter)

## Estructura del proyecto

```txt
.
├── 20211119_monitoreo.tif
├── 20230721_monitoreo.tif
├── README.md
├── acelero.txt
├── prueba.ipynb
└── requirements.txt

1 directory, 6 files
```

- README.md: Presente file para explicar como ejecutar el proyecto
- acelero.txt: Data cruda usada como input para el jupyter notebook
- prueba.ipynb: Archivo jupyter con solución propuesta
- requirements.txt: archivo de dependencias necesarias para ejecutar
  proyecto

Nota: como se observa en el árbol de archivos los archivos de entrada
deben estar posicionados (almacenados) en el mismo nivel del jupyter
script.