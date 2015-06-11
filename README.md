Imagr Server
=============

This Docker image runs [Imagr Server](https://github.com/grahamgilbert/imagr_server). The container expects a linked PostgreSQL database container.

# Settings

Several options, such as the timezone and admin password are customizable using environment variables.

* ``ADMIN_PASS``: The default admin's password. This is only set if there are no other superusers, so if you choose your own admin username and password later on, this won't be created.
* ``DOCKER_IMAGR_TZ``: The desired [timezone](http://en.wikipedia.org/wiki/List_of_tz_database_time_zones). Defaults to ``Europe/London``.
* ``DOCKER_IMAGR_ADMINS``: The admin user's details. Defaults to ``Docker User, docker@localhost``.

If you require more advanced settings, you can override ``settings.py`` with your own. A good starting place can be found on this image's [Github repository](https://github.com/grahamgilbert/docker-imagr_server/blob/master/settings.py).

```
  -v /usr/local/docker/imagr/settings/settings.py:/home/docker/imagr/imagr_server/settings.py
  ```

#Postgres container

Out of the box, Imagr uses a SQLite database, however if you are running it in a production environment, it is recommended that you use a Postgres Database.
I have created a Postgres container that is set up ready to use with Imagr Server - just tell it where you want to store your data, and pass it some environment variables for the database name, username and password.

* ``DB_NAME``
* ``DB_USER``
* ``DB_PASS``

```bash
$ docker pull grahamgilbert/postgres
$ docker run -d --name="postgres-imagr" \
  -v /db:/var/lib/postgresql/data \
  -e DB_NAME=imagr \
  -e DB_USER=admin \
  -e DB_PASS=password \
  --restart="always" \
  grahamgilbert/postgres
```

#Running the Imagr Server Container

```bash
$ docker run -d --name="imagr" \
  -p 80:8000 \
  --link postgres-imagr:db \
  -e ADMIN_PASS=pass \
  -e DB_NAME=imagr \
  -e DB_USER=admin \
  -e DB_PASS=password \
  --restart="always" \
  grahamgilbert/imagr-server
```
