# Instawork Backend Assignment

This repo is made for the work to be done under assignment for Instawork. It contains all the details on how to setup the project and test different fucntionalityies.

### Requirements

* After going in to the directory of the repo, install the requirements with 

```
$ pip install -r requirements.txt
```

* Setup MySQL with this link [here](https://www.digitalocean.com/community/tutorials/how-to-use-mysql-or-mariadb-with-your-django-application-on-ubuntu-14-04)

### Deploying
```
$ python manage.py migrate
$ python manage.py runserver
```

### View and Add a User

Browse to 127.0.0.1:8000/users to view all the users currently in the database or submit a post request to the same API to add a user. 

Using curl to add user
```
$ curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/users/ -d '{"id": 1, "first_name": "David", "last_name": "Jones", "phone_number": "+15101234567", "email": "test@test.com", "role": 0}'
```

Similarly, browse to http://127.0.0.1:8000/users/1/delete/ to delete the data for user with id '1'.

### Partial Edit

To partial edit an entry, example edit first name of entry with id = '1'
```
curl -X PATCH -H "Content-Type:application/json" http://127.0.0.1:8000/users/1/edit/ -d '{"id": 1, "first_name": "David"}'
```

### Contact 
If any queries contact at parth.verma96@gmail.com.


