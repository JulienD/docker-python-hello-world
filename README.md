# Simple Python Flask Dockerized Application#

Build the image using the following command

```bash
$ docker build -t friendlyhello .
```

Run the Docker container using the command shown below.

```bash
$ docker run -d -p 4000:80 friendlyhello
```

Use -e to override the NAME environment variable.

```bash
$ docker -e NAME=foobar run -d -p 4000:80 friendlyhello
```

The application will be accessible at http://localhost:4000

```bash
$ curl http://localhost:4000
```