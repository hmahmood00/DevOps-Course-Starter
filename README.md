# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.tempalate` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

# Docker build 
We have two different environments Development and Production. The image has all been set up and no need to run any other commands.
# Development 
To run development you will need to launch the power shell and run the following commands 
```bash
docker build --target development --tag todo_app . 

docker run -v "$(pwd)/todo_app:/app/todo_app" --env-file .env -p 5000:5000  todo_app 
```
Once these commands are successfully run you can access the application via: http://localhost:5000/ 
To exit in powershell press Ctr + c

# Production
To run production  you will need to launch the power shell and run the following commands 
```bash
docker build --target production --tag todo_app:prod .

docker run --env-file .env -p 8080:8080 todo_app:prod
```
Once these commands are successfully run you can access the application via: http://localhost:8080/ 
To exit in powershell press Ctr + c



# Module 2 trello apis

* You will need to create a  trello account if you do not have one already.
*  Make a new Todo board 
* You will need to go to https://trello.com/app-key to get your Trello app api key this goes in your .env under TRELLO_KEY
* In the same url if you follow steps to generate a token and add it to TRELLO_TOKEN in the .env
* You will then need to find the relevant id's for your To Do, Doing and Completed/Done lists
* I used postman to set up my requests to see what each api request brings back if you add the relevant keys to the request 
GET https://api.trello.com/1/boards/(BOARDID)/lists?key=(TRELLO_KEY)&token=(TRELLO_TOKEN) will show all the boards with their ids if you add them to the .env file

* TRELLO_TODO_IDLIST= this is the do card list id in trello
* TRELLO_DOING_IDLIST= this is the doing card list id in trello
* TRELLO_COMPLETE_IDLIST= this is the completed/done card list id in trello

To run if you do it for the first time do poetry install 
followed by poetry run flask run
