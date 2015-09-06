Exercise 2 (ex2)
==================

## Description

This repository contains a Django server for visualizing MODIS fire hostpost layers.

## Installation

As root (`sudo su -`), execute the following commands:

```
apt-get update
apt-get install -y curl vim git nginx
apt-get install -y python-dev python-pip
apt-get install -y supervisor
```

Then, as ubuntu, clone this repo with commands like the following.

```
cd ~
git clone https://github.com/pjdufour/ex2.git ex2.git
```

Then, as root, then install python packages with:
```
cd ex2.git
pip install -r requirements.txt
```

Then, update SITEURL (e.g., http://example.com/) in settings.py:

```
vim ex2.git/ex2/ex2/settings.py
```

Create directory for static files for NGINX and copy over static files.

```
sudo mkdir -p /var/www/static
sudo python manage.py collectstatic
```

## Usage

The application can be run through the Django built-in development server or Gnuicron ([http://gunicorn.org/](http://gunicorn.org/)).

There is a [supervisord.conf configuration file](https://github.com/pjdufour/ex2/blob/master/supervisord.conf) that should automate some of this process in a full production environment.  It is configured for vagrant, but can be easily configured for other users.

First, as root, clear the RabbitMQ cache of messages with:

Then, prepare the server.

```
cd ex2.git/ittc
python manage.py syncdb
```

If `syncdb` asks if you would like to create an admin user, do it. 

To run the application using the Django built-in development server, execute the following:

```
python manage.py runserver [::]:8000
```

To run the application using Gnuicorn, execute the following:

```
gunicorn --workers=4 --worker-class gevent -b 0.0.0.0:8000 ex2.wsgi
or
gunicorn --workers=4 --worker-class gevent -b unix:///tmp/gunicorn.sock --error-logfile error.log ittc.wsgi
```

You can learn more about gunicron configuration at [http://docs.gunicorn.org/en/develop/configure.html](http://docs.gunicorn.org/en/develop/configure.html).

## Contributing

We are not accepting pull requests for this repository.

## License

Copyright (c) 2015, Patrick Dufour
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of ex2 nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
