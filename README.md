# Bucketlist API

A simple RestFull API made with Flask

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need Python 3 and Postgres. You will need to create a postgres db with the name flask_api

### Installing

1. Clone the repo:

```
git clone https://github.com/JPetsis/Bucket_list.git
```

2. Navigate to the folder:

```
cd Bucket_list
```

3. Create a virtual environment and install the requirements:

```
pip install -r requirements.txt
```

4. Create a .env file and add the following:

```
APP_SETTINGS=development
SECRET=<your SECRET-KEY-here-some-very-long-string-of-random-characters-CHANGE-TO-YOUR-LIKING>
DATABASE_URL=<your Postgres url>
```

4. Do the migrations:

```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

5. And type:

```
flask run
```

## API Endpoints

| Resource URL | Methods | Description | Requires Token |
| -------- | ------------- | --------- |--------------- |
| `/api/v1/auth/register/` | POST  | User registration | FALSE |
|  `/api/v1/auth/login/` | POST | User login | FALSE |
| `/api/v1/bucketlists/` | GET, POST | A user's bucket lists | TRUE |
| `/api/v1/bucketlists/<id>/` | GET, PUT, DELETE | A single bucket list | TRUE |
| `/api/v1/bucketlists/<id>/items/` | GET, POST | Items in a bucket list | TRUE |
| `/api/v1/bucketlists/<id>/items/<item_id>/` | GET, PUT, DELETE| A single bucket list item | TRUE |

## Running the tests

To run the tests just type

```
python manage.py test
```

