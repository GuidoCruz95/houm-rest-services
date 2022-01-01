# houm-rest-services

This is a little service that provides you entrypoints for data related houmers and relationship with places and
visitors.

To start the API service, you should use an python execution environment and install the required third libraries, flask
to start the server, and pytest to execute the implemented unit tests.

Instruccions to create and go to an execution environment:

## MacOS/Linux

```sh
$ mkdir myproject
$ cd myproject
$ python3 -m venv venv
# Activate the environment
$ . venv/bin/activate
```

## Windows

```sh
> mkdir myproject
> cd myproject
> py -3 -m venv venv
# Activate the environment
> venv\Scripts\activate
```

Instruccions to install libraries:

```sh
pip install flask
pip install pytest
```

## Starting the service

```sh
# Execute the houmer_service.py file
.\houmer_service.py
```

You should be able to see in the console a message like this:

```sh
 * Serving Flask app 'houmer_service' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

maybe will be needed to specify python at the command beggining to start the server.

## Available entrypoints

| Entrypoint | Result |
| ------ | ------ |
| / | Welcome message |
| /houmers | Houmers registered in the system |
| /houmer/<int:houmer_id> | Houmer associated to the houmer_id |
| /houmer/<int:houmer_id>/coordinates | Houmer coordinate by houmer_id |
| /houmer/<int:houmer_id>/visited/<date> | Visited places by a houmer in a specific day |
| /visitors | Visitors registered in the system |
| /visitor/<int:visitor_id> | Visitor associated to the visitor_id |
| /places | Places registered in the system |
| /place/<int:place_id> | Place associated to the place_id |