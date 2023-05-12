# Online Banking System

This is an Online Banking Concept created using Django Web Framework.


## Features

* Create Bank Account.
* Deposit & Withdraw Money
* Bank Account Type Support (e.g. Current Account, Savings Account)
* Interest calculation depending on the Bank Account type
* See balance after every transaction in the Transaction Report


## Prerequisites

Be sure you have the following installed on your development machine:

+ Python >= 3.7
+ Git
+ pip

## Requirements

+ Django==3.2
+ python-dateutil==2.8.1

## Install Redis Server

[Redis Quick Start](https://redis.io/topics/quickstart)

Run Redis server
```bash
redis-server
```

## Project Installation
```
cd bank
```
Migrate Database,
```bash
python manage.py migrate
```

Run the web application locally,
```bash
python manage.py runserver # 127.0.0.1:8000
```

Create Superuser,
```bash
python manage.py createsuperuser
```

Admin Username,
```bash
Username: admin
Password: 12345
```
