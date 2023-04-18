# Kubernetes tutorial project

This is a small test-project I've written in order to learn more about Kubernetes, following a <a href="https://www.youtube.com/watch?v=d1ZMnV4yM1U&ab_channel=ThatDevOpsGuy">Youtube-tutorial by That DevOps Guy</a>. The project requires you to install Docker and the kubectl command line tool.

## Docker setup

First, you will have to change the docker user associated with the image ```audunsh/python:1.0.0``` in docker-composer.yaml (as well as update your login credentials for dockerhub).

In order to run it, you'll have to build the docker image from the project folder:

```console
docker-compose build python
```

You can then run a container with the image using:

```console
docker-compose up python
```

If it works, you will be able to login to ```localhost:6001``` from your browser.

Finally, before starting up Kubernetes, push the image to dockerhub:
```
docker-compose push python
```

## Kubernetes (kubectl)







