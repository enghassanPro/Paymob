**Promo** **System**
==============


Requirements
------------

Python 3.9 supported.

Django 3.1.6 supported.

----

Setup
-----

Install from **pipenv**:

    pipenv install

----

Run server
-----

    python manage.py runserver

About
-----

**Promo System** 

Is the system that use to generate a promo code for each client user

**About the models**:

we have two main tables:
* `user`
* `promo`

**User Model**:


we have two types of users The user admin and The client user (normal user)
we can differ between them using field `type_acount` which store either `1` which means user admin
and `2` which means client user.

**The user admin has fully controls for all the system**

* can add other users
* can add promo
* can delete promo
* can specify promo for a user
* can update promo

**The clien admin has special access**
* can get all or specific valid promo that the user admin specified for him
* can take a promo code from list promo

Urls:
-------------

* ``auth/login``
~~~~~~~~~~~~~~~~~~~~~~~~
- request: post
- data: {
    "email": str,
    "password": str,
}

- return: {
    "token": str
}

~~~~~~~~~~~~~~~~~~~~~~~~
**NOTE:**

_To use this token for any request please add it in the headers 
with Key Authorization and value is `Token 'returned value'`_


* ``auth/logout``

~~~~~~~~~~~~~~~~~~~~~~~~
- request: get
- return: str

~~~~~~~~~~~~~~~~~~~~~~~~

**User Admin Urls**
----

* ``admin/user/create``

~~~~~~~~~~~~~~~~~~~~~~~~

- request: post
- data: {
    "username": str,
    "first_name": str,
    "last_name": str,
    "phone": str,
    "address": str,
    "promo_type": str,
    "start_time": accept this format "2021-02-01T15:51:32.339118Z",
    "end_time": accept this format "2021-02-01T15:51:32.339118Z",
    "promo_amount": float,
    "description": str,
    "email": str,
    "password": str
}

or

{
    "username": str,
    "first_name": str,
    "last_name": str,
    "phone": str,
    "address": str,
    "email": str,
    "password": str
}

- return: str

~~~~~~~~~~~~~~~~~~~~~~~~


* ``admin/user/retrieve``
~~~~~~~~~~~~~~~~~~~~~~~~

- request: get

- return: Array

~~~~~~~~~~~~~~~~~~~~~~~~

* ``admin/promo/create``
~~~~~~~~~~~~~~~~~~~~~~~~

- request: post
- data: {
    "user": int,
    "promo_type": str,
    "start_time": accept this format "2021-02-01T15:51:32.339118Z",
    "end_time": accept this format "2021-02-01T15:51:32.339118Z",
    "promo_amount": float,
    "description": str,
}
- return: str

~~~~~~~~~~~~~~~~~~~~~~~~

* ``admin/promo/update?id=number``
~~~~~~~~~~~~~~~~~~~~~~~~

- request: put
- data: {
    "user": int,
    "promo_type": str,
    "start_time": accept this format "2021-02-01T15:51:32.339118Z",
    "end_time": accept this format "2021-02-01T15:51:32.339118Z",
    "promo_amount": float,
    "description": str,
}
- return: str

~~~~~~~~~~~~~~~~~~~~~~~~

* ``admin/promo/delete?id=number``
~~~~~~~~~~~~~~~~~~~~~~~~

- request: delete
- return: str

~~~~~~~~~~~~~~~~~~~~~~~~

* ``admin/promo/retrieve``
~~~~~~~~~~~~~~~~~~~~~~~~

- request: get
- return: Array

~~~~~~~~~~~~~~~~~~~~~~~~


**Client User Urls**
----

* ``user/retrieve | user/retrieve?id=number``
~~~~~~~~~~~~~~~~~~~~~~~~

- request: get
- return: Array

~~~~~~~~~~~~~~~~~~~~~~~~

* ``user/submit?id=number``
~~~~~~~~~~~~~~~~~~~~~~~~

- request: put
- return: str

~~~~~~~~~~~~~~~~~~~~~~~~
