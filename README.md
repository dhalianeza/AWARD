# Project-Awards
 an application that will allow a user to post a project he/she has created and get it reviewed by his/her peers

## Author
* names : Munezero Tesire Gisele
* github: amtesire
* Email: tesiregisele@gmail.com

>[amtesire](https://github.com/amtesire) 

## Description of user 
As a user of the application I should be able to:
* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects 
* View projects overall score
* View my profile page

##  Live Link  
 Click [View Site](https://tesiawards.herokuapp.com/)  to visit the site

## Screenshots 
###### Home page
 
<img src="https://raw.githubusercontent.com/amtesire/Project-Awards/master/media/images/homepage.png">

###### Home page
 
<img src="https://raw.githubusercontent.com/amtesire/Project-Awards/master/media/images/homepage2.png">
 
 ###### Rating of a post
 <img src="https://raw.githubusercontent.com/amtesire/Project-Awards/master/media/images/Rating a vote.png"> 

 ###### Profile Page
 <img src="https://raw.githubusercontent.com/amtesire/Project-Awards/master/media/images/profile page.png">


## Prerequisites && Installations
* Create and Activate a virtual environment.
* Download Django using pip install django==1.11
* Create a requirements.txt file with all the dependencies
* Create a new Django project using django-admin startproject name-of-project .
* Create a new Django app using django-admin startapp name-of-the-app .
* Run the development server confirm the project works.

## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/amtesire/Project-Awards.git 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd project-awwards pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations instagram
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  

## Technologies Used
* [Python3.6](https://www.python.org/)  
* [Django 1.11](https://docs.djangoproject.com/en/2.2/)
* [Heroku](https://heroku.com)  
* PostgreSQL
* HTML
* CSS

## Acknowledgments
* Canvas
* w3schools
* Stack overflow

## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [tesiregisele@gmail.com]  
  
## License 
MIT License

Licensed under MIT License
  
* Copyright (c) 2020 **Tesire Gisele**