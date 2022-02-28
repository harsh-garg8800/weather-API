## `Weather Backend` setup Guide

## Clone Git repository:

 `git clone <git repo>`
 
>> git checkout <branch name>


## Install Python On Local System

`python version >= 3.6`


>https://phoenixnap.com/kb/how-to-install-python-3-ubuntu

  

## Setup Environment and Insatll Dependencies:

### Install virtual enviournment
>`pip install virtualenv`

>https://www.geeksforgeeks.org/python-virtual-environment/

#### Create virtual envoiurnment

python3 -m venv <env_name>

or
    
>/usr/bin/python -m venv env
>>Ex: python -m venv env
  
#### Activate virtual envoiurnment

source <env_name>/bin/activate
>Ex: source env/bin/activate

  

#### Install requirements / Dependencies


>`pip install --upgrade pip`
> 
>`pip install -r requirements.txt`

## Do changes in the Database variable under the settings.py file
```
change Name, User, Host and password values according to your DB credentials
```


### Create Database for City Dropdown

## we are getting US, CA, IN cities name using django-cities-light library

## To make migrations Run

> Python manage.py makemigrations

#### To migrate django-cities-light table into DB Run

> Python manage.py migrate

## Now to populate data into DB Run

> Python manage.py cities_light


## Run the server

> python manage.py runserver
