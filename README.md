# rabbitmq-lab
Management Plugin for RabbitMQ docker container:

There is a second set of tags provided with the management plugin installed and enabled by default, which is available on the standard management port of 15672, with the default username and password of guest / guest:

$ docker run -d --hostname my-rabbit --name some-rabbit rabbitmq:3-management

You can access it by visiting http://container-ip:15672 in a browser or, if you need access outside the host, on port 8080:

$ docker run -d --hostname my-rabbit --name some-rabbit -p 8080:15672 rabbitmq:3-management

You can then go to http://localhost:8080 or http://host-ip:8080 in a browser.
