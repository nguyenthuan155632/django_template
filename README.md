Django Template
===============

Dependences
-----------

```bash
$pip3 install mysqlclient
```

### `Implement SCSS`
```bash
$pip3 install libsass django-compressor django-sass-processor
```
[https://github.com/jrief/django-sass-processor](https://github.com/jrief/django-sass-processor)

### `Bootstrap 3`
```bash
$pip3 install django-bootstrap3
```

### `Typescript`
```bash
$pip3 install django-pipeline-typescript
```

### `CKEditor`
```
$pip3 install django-ckeditor
```

### `Pillow`
```
$pip3 install pillow
```

### `South`
```
$pip3 install south
```

Setup
-----

### `Create manually database`
```bash
$mysql -u <user> -p<password>
mysql> create database <database_name>
```

### `Migration`
```bash
$python3 manage.py migrate
```

### `Run server`
```bash
$python3 manage.py runserver
```

### `Create super user`
```bash
$python3 manage.py createsuperuser
```