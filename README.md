# Test Case Monkey

Test case management tool written in Django

[![Build Status](https://travis-ci.org/Fanarim/test_case_monkey.svg?branch=master)](https://travis-ci.org/Fanarim/test_case_monkey)

Project structure was generated using using Django Cookiecutter ([docs](http://cookiecutter-django.readthedocs.io/en/latest/index.html))

## Development using Docker
###Running
The following commands has to be executed once only. After that, local changes in this directory will automatically take effect (thanks to using docker-compose's volume option).

* Build the docker images

`$ sudo docker-compose -f dev.yml build`

* Run the images in background

`$ sudo docker-compose -f dev.yml up -d`

After a few seconds, app should be up and running.

### Basic Commands
#### Docker related commands
* To connect to the running docker image, use

`$ sudo docker exec -i -t image_name /bin/bash`

* To see the output of django's webserver or postgres, use

`$ sudo docker log -f image_name`

#### Setting Up Your Users

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    `$ sudo docker exec -i django_image_name manage.py createsuperuser`

For testing purposes, you can e.g. login with normal user in Firefox and superuser in Chrome.

#### Test coverage
To run the tests using `coverage` and generate an HTML coverage report:
```
$ coverage run manage.py test
$ coverage html
$ open htmlcov/index.html
```

Running tests with py.test:

`$ pytest`

#### SASS -> CSS autogeneration using gulp
* At first, you need to install nodejs and it's package manager (you might need to add repository with newer versions of nodejs)

`sudo apt-get install nodejs`

* After that, install nodejs dependencies listed in package.json

`npm install`

* Multiple gulp tasks are available (see gulpfile.js). If you want to automatically regenerate CSS only, run

`gulp watch_styles`



## Deployment using Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

### Production features

#### Sentry - TODO

Sentry is an error logging aggregator service. You can sign up for a free account at  https://getsentry.com/signup/?code=cookiecutter  or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.
