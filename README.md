# Flask_Microservice_POC

This project can be built by creating a virtualenv for python 3 and then installing the required packages listed in
requirements.txt as follows:
```
% virtualenv --python=python3 env
% env/bin/pip install -r requirements.txt
```

A local development server can then be run as follows:
```
% env/bin/python app.py
```
The file config.py contains the default configuration parameters for this project. Deployment specific configuration
parameters may be specified in a .env file.

The api documentation will appear at '/api'.