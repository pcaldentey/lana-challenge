# Lana challenge

[Problem description](https://gist.github.com/samlown/17abc235580fb291dd153b9c45e441d0)

Pablo Caldentey
pablo@caldentey.org

This code is done in python 3.6

# General approach

We need to build a server to communicate with over the network. And a client. We will build a REST API with all the four endpoints we need, and a class and a script that handles it as client.

In order to build REST API server I will use FastAPi framework and the docker image that fastAPI give us to play with as base to build our image.

# Tools & libraries
Python 3.6

[FastAPI](https://fastapi.tiangolo.com/)

[FastAPI Docker image repository](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker)

[requests](https://requests.readthedocs.io/en/master/)


# Build and run server
There is a makefile with main commands in it, to make it easier and speed up development.

    make build
    make run

Once finished you will have a container, called lanaserver, exposing the api on port 80, in [0.0.0.0](http://0.0.0.0), and swagger docs [here](http://0.0.0.0/docs)

# Run client
Client console utility uses requests python library, but is included inside docker container so you don't have to install anything. In order to access client:

    host$ docker exec -ti lanaserver bash
    container$ cd /client
    container$ python client.py -h

# Run tests
As the client script e2e tests use request python library so there is a make call that runs tests inside container

    make tests

Runs both, unit and e2e tests

# Code structure and implementation

## Folder structure

In the root of the repo we have *app* folder where all the code of the api server is stored, *client* folder keeps all code for the client.

## Client
Really simple piece of code.

**lana_client.py**

Class that talks to api server endpoints through requests python library. It has one method for each endpoint.

**client.py**

Command line utilitythat uses LanaClientclass to communicate with server.

**exercise.py**

Small script that uses LanaClient to replicate all four cases written in problem description.

## Server
So inside *app* folder we see 3 folders. *tests* keeps unit and e2e tests, *basketdb* this is a placeholder for storing files with basket information (without interest) and *src* where we have the code.

**main.py**

This file is the fastapi entry point, where all endpoints are defined, and all api boilerplate is kept (not much), rest of code is simple python. In each endpoint we call the service object
(app/src/services folder) and inject in it dependencies needed by each one, that will take care of executing the action required by endpoints.


For the sake of clarity and simplicity I took decisions that are not rigth:

* We stored interfaces and their implementations not only in the same folder but in same file
* Folder structure is defined to avoid folder/file explotion
* Other decision taken with this on mind was the way we defined services. All the output construction/normalization are done inside services and shouldn't, another entity (api_action) should take care of that, cause in this way we are coupling services with api requirements and needs.


###src folder and considerations

Product and Discount information: We stored product and discount information inside a dictionary as no editions were required to be done (*db/db.py*)

Basket information: this information is stored in files (*basketdb folder*) to keep the state of the basket between calls.

In order to access both sources of information we use reading and writing repositories (repository pattern). They are in *app/src/model/repository*. So to add a databae in the future we just have to
write new repositories but they should implement the interfaces actual ones are using, and inject them into each of one of the services.


**model/discount.py**

Discount object. It has been designed following *Strategy pattern*. So we have separated classes for each discount type or discount strategy.

The main Discount object will receive in the instatiation moment the discount strategy (TwoPerOneDiscountStrategy, BulkDiscountStrategy).

    Discount(TwoPerOneDiscountStrategy())

