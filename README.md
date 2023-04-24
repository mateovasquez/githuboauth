# Github OAuth Application
## Description
Github Oauth is an application developed in `Django 4.2` which enables authentication using `OAuth` provided by Github.
This application also includes a Homepage, an User settings page and a CRUD for the user's Profile.

In order to ensure its integrity, the application is backed with unit and integration tests made with `pytest` and Django's integrated `unittest` library.

## Installation steps
- Clone or download the repository
- Create a virtual environment in the repository's folder
- Activate the virtual environment
- Install the project requirements with `pip install -r requirements.txt`

## Run application
First you need to setup the database. You can do so with `python manage.py migrate` in your virtual environment.
Then you can run the application's server with `python manage.py runserver`, and access it through http://127.0.0.1:8000/

## Tests
To run the tests, execute `pytest` command in the console.
These are the tests made for the application:
- `./githuboauth/test_urls.py`: Tests the correct behavior of the routing depending if the user is authenticated or not.
- `./user_profile/test_forms.py`: Tests the validation of the forms.
- `./user_profile/test_views.py`: Tests the views requests.