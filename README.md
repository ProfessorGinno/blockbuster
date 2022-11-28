ENG
# Instructions to run this project locally

- Open Git Bash for `Windows` or a terminal for `Linux/Unix`.
- Create working directory for course project.
```bash
cd
mkdir -p folder_name/folder_name_projects
cd folder_name/folder_name_projects
```
- Clone the project.
```bash
git clone https://github.com/ProfessorGinno/blockbuster.git

cd blockbuster
```
- Create and activate virtual environment.
(Windows)
```bash
python -m venv venv
.\venv\Scripts\activate
```

(Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```
- Install the project dependencies.
```bash
pip install -r requirements.txt
```

- Create database from migrations.
```bash
python manage.py makemigrations
python manage.py migrate
```

- Create super-user.
```bash
python manage.py createsuperuser
```
Input `Username`, `Email address`(optional) y `Password`

- Create static.
```bash
python manage.py collectstatic
```
- Run project, django server exposes service by localhost on port 8000 by default `http://127.0.0.1:8000/`
```bash
python manage.py runserver
```

# Useful commands for Django

## Create project
```bash
django-admin startproject <name_project> .
```
## Create an application in a project
```bash
python manage.py startapp <name_app>
```

## Update the project database with changes in our models
The migrations are created in two steps, one per application, and then the tables are created in the database.
```bash
python manage.py makemigrations
python manage.py migrate
```

# Basic commands for Git

## Git clone
Git clone is a command to download existing source code from a remote repository (like Github, for example). Download the latest version of your project to a repository and save it to your computer.
```bash
git clone <https://link-of-repository>

```
## Git branch
- Creating a new branch.
```bash
git branch <name_branch>
```

- Display of branches.
```bash
git branch
git branch --list
```

- Delete a branch.
```bash
git branch -d <branch-name>
```

## Git checkout
- To switch to an existing branch.
```bash
git checkout <branch-name>
```

- To create and switch to that branch at the same time.
```bash
git checkout -b <branch-name>

```

## Git status
The git status command gives us all the necessary information about the current branch:
- Whether the current branch is up to date-
- If there is something to confirm, send or receive (pull).
- If there are files in preparation (staged), without preparation (unstaged) or that are not being tracked (untracked).
- If there are files created, modified or deleted status.
```bash
git status
```

## git add
- Add a single file.
```bash
git add <file_name>
```

- Add everything at once.
```bash
git add -A
git add .
git add *
```
***Important: The ``git add`` command stores file changes in the ``stage``, however they are not yet checked in to the repository until the ``git commit`` commit command is used to log a checkpoint of changes.***

## Git commit
Git commit establishes a checkpoint that you can return to later if necessary.
It is highly recommended to write a short message to explain what we have developed or modified in the source code.

```bash
git commit -m "commit message"
```

## Git push
After you have committed your changes, the next step you want to take is to push your changes to the remote server. Git push pushes your commits to the remote repository.
```bash
git push <remote-name> <branch-name>
git push origin <branch-name>
```
***Important: Git push only uploads changes that have been committed with a ``git commit``.***

## Git pull
The git pull command is used to receive updates from the remote repository.
```bash
git pull <remote-name> <branch-name>
git pull origin main
```

## Git remote
It is used to change the url address of the repository that we have by origin.
```bash
git remote set-url origin <url_of_repository_on_GitHub>
```




ES
# Instrucciones para ejecutar este proyecto en local

- Abrir Git Bash para `Windows` o una terminal para `Linux/Unix`.

- Crear directorio de trabajo para el proyecto de curso.
```bash
cd
mkdir -p nombre_folder/nombre_proyectos
cd nombre_folder/nombre_folder_proyectos
```

- Clonar el proyecto.
```bash
git clone https://github.com/ProfessorGinno/blockbuster.git
cd blockbuster
```

- Crear y activar entorno virtual.
(Windows)
```bash
python -m venv venv
.\venv\Scripts\activate
```

(Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```

- Instalar las dependencias del proyecto.
```bash
pip install -r requirements.txt
```

- Crear base de datos a partir de las migraciones.
```bash
python manage.py makemigrations
python manage.py migrate
```

- Crear super-usuario.
```bash
python manage.py createsuperuser
```
Ingrese `Username`, `Email address` (opcional) y `Password`


- Crear estáticos.
```bash
python manage.py collectstatic
```

- Ejecutar proyecto, el servidor de Django expone el servicio por el localhost en el puerto 8000 por defecto `http://127.0.0.1:8000/`
```bash
python manage.py runserver
```

# Comandos útiles para Django

## Crear proyecto
```bash
django-admin startproject <nombre_proyecto> .
```
## Crear una aplicación en un proyecto
```bash
python manage.py startapp <nombre_app>
```
## Actualizar la base de datos del proyecto con cambios en nuestros modelos
Se realiza en dos pasos la creación de las migraciones, una por aplicación, y luego se realiza la creación de las tablas en la base de datos.
```bash
python manage.py makemigrations
python manage.py migrate
```
# Comandos básicos para Git

## Git clone
Git clone es un comando para descargarte el código fuente existente desde un repositorio remoto (como Github, por ejemplo). Descarga la última versión de tu proyecto en un repositorio y la guarda en tu ordenador.
```bash
git clone <https://link-del-repositorio>
```

## Git branch
- Creando una nueva rama:
```bash
git branch <nombre-rama>
```
- Visualización de ramas:
```bash
git branch
git branch --list
```
- Borrar una rama:
```bash
git branch -d <nombre-rama>
```

## Git checkout
- Para cambiarte a una rama existente
```bash
git checkout <nombre-rama>
```
- Para crear y cambiarte a esa rama al mismo tiempo
```bash
git checkout -b <nombre-rama>

```

## Git status
El comando de git status nos da toda la información necesaria sobre la rama actual:
- Si la rama actual está actualizada.
- Si hay algo para confirmar, enviar o recibir (pull).
- Si hay archivos en preparación (staged), sin preparación(unstaged) o que no están recibiendo seguimiento (untracked).
- Si hay archivos creados, modificados o eliminados status.
```bash
git status
```

## Git add
- Añadir un único archivo:
```bash
git add <nombre_archivo>
```

- Añadir todo de una vez:
```bash
git add -A
git add .
git add *
```
***Importante: El comando ``git add`` almacena en el ``stage`` los cambios de los archivos sin embargo aún no quedan registrados en el repositorio hasta que se utilice el comando de confirmación ``git commit`` para registrar un punto de control de los cambios.***

## Git commit
Git commit establece un punto de control al cual puedes volver más tarde si es necesario.
Resulta muy aconsejable escribir un mensaje corto para explicar qué hemos desarrollado o modificado en el código fuente.

```bash
git commit -m "mensaje de confirmación"
```

## Git push
Después de haber confirmado tus cambios, el siguiente paso que quieres dar es enviar tus cambios al servidor remoto. Git push envía tus commits al repositorio remoto.
```bash
git push <nombre-remoto> <nombre-rama>
git push origin <nombre-rama>
```
***Importante: Git push solamente carga los cambios que han sido confirmados con un ``git commit``.***

## Git pull
El comando git pull se utiliza para recibir actualizaciones del repositorio remoto.
```bash
git pull <nombre-remoto> <nombre-rama>
git pull origin main
```
## Git remote
Sirve para cambiar la dirección url del repositorio que tenemos por origin.
```bash
git remote set-url origin <url_del_repositorio_en_GitHub>
```