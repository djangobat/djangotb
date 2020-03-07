# djangotb

Khởi tạo dự án Django nhanh chóng, hiệu quả.

## Blog

For detail: 

## DEMO

![Demo Video](https://github.com/djangobat/djangotb/blob/master/demo.gif)

## Features

* Tùy chỉnh người dùng;
* Dùng Email/password cho đăng ký và đăng nhập;
* Cập nhật Profile;
* Lưu trữ cấu hình ở file settings.py tăng tính bảo mật

## Third-Party Packages

* [x] [django-allauth](https://github.com/pennersr/django-allauth) for social authentication
* [x] [Bootstrap](https://github.com/twbs/bootstrap) for styling
* [x] [Jquery](https://github.com/jquery/jquery)
* [x] [Font-awesome](https://github.com/FortAwesome/Font-Awesome) for icon fonts
* [x] [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar) for debugging
* [x] [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms) for DRY forms
* [x] [sorl-thumbnail](https://github.com/jazzband/sorl-thumbnail) for thumbnail images
* [x] [python-decouple](https://github.com/henriquebastos/python-decouple/) Storing application settings
* [x] [dj-database-url](https://github.com/jacobian/dj-database-url) Storing application settings

## Quickstart

1. Đảm bảo bạn đã cài Virtualenv hoặc Pipenv
2. Clone repostory về:

```bash
$ git clone https://github.com/djangobat/djangotb.git
$ cd djangotb
```

3. Cài đặt virtual environment:

* Dùng windows

```bash
$ virtualenv env
$ env\Scripts\activate
(env) $
(env) $ pip install -r requirements.txt
```

* Dùng Linux

```bash
$ virtualenv env
$ source env/bin/activate
(env) $
(env) $ pip install -r requirements.txt
```

* Dùng Mac

```bash
$ virtualenv env -p python3
$ source env/bin/activate
(env) $
(env) $ pip install -r requirements.txt
```

Hoặc cài virtual environment với Pipenv:

```bash
$ pipenv --python 3
$ pipenv install
$ pipenv shell
```

4. Khởi tạo migration của custom user

```bash
(env) $ python manage.py makemigrations users
(env) $ python manage.py migrate
```

5. Create a superuser:

```bash
(env) $ python manage.py createsuperuser
```

6. Run server

```bash
(env) $ python manage.py runserver
```

## Tech Specs

* Python 3.6
* Django 3.0.3
* dj-database-url 0.5.0
* django-allauth 0.41.0
* django-crispy-forms 1.9.0
* Bootstrap 4.3.1
* jQuery 3.4.1
* Font Awesome 5.11.2
* python-decouple 3.3
* Pillow 7.0.0
* sorl-thumbnail 12.6.3
* django-debug-toolbar 2.2
