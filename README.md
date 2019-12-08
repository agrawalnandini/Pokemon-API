# Pokemon-API

This is a web API that has been made as a part of the [CS-2375] - Database Management Systems course and has been developed using the Django REST framework.

## Setup

### Install Dependencies
1. Install [pip](https://pip.pypa.io) and [virtualenv](https://virtualenv.pypa.io/)

2. Create a virtualenv
> ```sh
> $ virtualenv --python python3 env
> ```
If you're on Windows, you may have to specify the full path to your python installation directory
> ```sh
> $ virtualenv --python "c:\python36\python.exe" env
> ```

3. Activate the virtual environment
> ```sh
> $ source env/bin/activate
> ```
If you're on Windows, then do the following instead
> ```sh
> $ .\env\Scripts\activate
> ```

3. Install the requirements for the API
> ```sh
> $ pip install -r requirements.txt
> ```

### Run
The API will have link to the entire database as well as options to GET, POST, UPDATE and DELETE from said database. The options for searching and ordering based on the different fields present in our Pokemon model is also available. To run the web API, just execute the following on the command line.
```sh
  $ python manage.py runserver
```
Then, open the following url on your web browser.
```sh
  $ localhost:8000
```
