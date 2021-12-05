# Django-Community-Forum-Website
A simple forum wesbite built with Django, an online discussion site where people can post questions, possts and interract with other users.

# EU CRIE ESSE FORK PARA ESTUDAR E APRIMORAR O PROJETO. MINHA INTENÇÃO É CRIAR UM FORUM PARA UMA ESCOLA TÉCNICA AONDE EU CURSEI O TÉCNICO EM INFORMÁTICA.
INSTALE E CONFIGURE O NGNIX PARA TESTAR ESSA APLICAÇÃO EM SUA MAQUINA

https://github.com/Felipe500/django-apache-nginx-uwsgi-vps-ubuntu

## Preparing the environmnet
```
sudo apt-get install python3-venv
```
* Create virtual env

```python3 -m venv venv```

* Clone repository

```git clone your-url.git```

* Install requirementst
``` pip install -r requirements.txt```

* Run the collectstatic command 
``` python manage.py collectstatic ```

* Create the database 
``` python manage.py migrate ```

* Create a superuser 
``` python manage.py createsuperuser ```

 ## Setup static and media files
 
 * Make sure your settings.py has the following configurations:
 ```
 STATIC_URL = '/static/'
 STATIC_ROOT = os.path.join(BASE_DIR, "static")
 
 MEDIA_URL = '/media/'
 MEDIA_ROOT = os.path.join(BASE_DIR, "media")
 ```
 
 * Run Django collectstatic
 ```python manage.py collectstatic```

 
 ## Install and setup 
 * Install uwsgi on your virtual environment
 
 ```
 sudo apt-get install python3.6-dev
 sudo apt-get install build-essential libssl-dev libffi-dev python-dev
 pip install wheel
 pip install uwsgi
```
* Install and start Nginx

```
sudo apt-get install nginx
sudo /etc/init.d/nginx start
```
## Configure Nginx

* Create the file uwsgi_params on your project path
```
vim uwsgi_params

---- file content -----

uwsgi_param  QUERY_STRING       $query_string;
uwsgi_param  REQUEST_METHOD     $request_method;
uwsgi_param  CONTENT_TYPE       $content_type;
uwsgi_param  CONTENT_LENGTH     $content_length;

uwsgi_param  REQUEST_URI        $request_uri;
uwsgi_param  PATH_INFO          $document_uri;
uwsgi_param  DOCUMENT_ROOT      $document_root;
uwsgi_param  SERVER_PROTOCOL    $server_protocol;
uwsgi_param  REQUEST_SCHEME     $scheme;
uwsgi_param  HTTPS              $https if_not_empty;

uwsgi_param  REMOTE_ADDR        $remote_addr;
uwsgi_param  REMOTE_PORT        $remote_port;
uwsgi_param  SERVER_PORT        $server_port;
uwsgi_param  SERVER_NAME        $server_name;
```

* Create NGINX config file at /etc/nginx/sites/available
```
upstream django {
    server unix:///home/ubuntu/django-apache-nginx-uwsgi-vps-ubuntu/mysite.sock; 
}

server {
    listen      8000;
    server_name example.com;
    charset     utf-8;

    client_max_body_size 75M; 

    location /media  {
        alias /home/ubuntu/django-apache-nginx-uwsgi-vps-ubuntu/media; 
    }

    location /static {
        alias /home/ubuntu/django-apache-nginx-uwsgi-vps-ubuntu/static;
    }

    location / {
        uwsgi_pass  django;
        include     /home/ubuntu/django-apache-nginx-uwsgi-vps-ubuntu/uwsgi_params; 
    }
}
```

* Create a symlink on sites-enabled
sudo ln -s ~/path/to/your/mysite/mysite_nginx.conf /etc/nginx/sites-enabled/

* Restart Nginx
```sudo /etc/init.d/nginx restart```

* Download an image to media folder and test

* Run and test using Unix sockets
```uwsgi --socket mysite.sock --module mysite.wsgi --chmod-socket=666```

* Create the ini file

```
[uwsgi]
chdir           = /home/ubuntu/django-apache-nginx-uwsgi-vps-ubuntu
module          = django_vps.wsgi
home            = /home/ubuntu/venv
master          = true
processes       = 10
socket          = /home/ubuntu/django-apache-nginx-uwsgi-vps-ubuntu/mysite.sock
vacuum          = true
chmod-socket    = 666
```

* Testing with .ini file
```uwsgi --ini mysite_uwsgi.ini```
