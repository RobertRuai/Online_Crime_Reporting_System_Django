# Online Crime Reporting System
With the rapid urbanization and development of big cities and towns, the graph of crimes is rising rapidly. This phenomenal rise in offences and crime in cities is a matter of great concern. There are robberies, murders, smuggling, rapes and crimes which one can't think of.

Digitization of Records: Crime reporting solutions used today are trivial. Crime reports are still stored in paper records and evidences such as media files are stored in CD's or DVD's. When the case progresses, the paper records and evidences tend to increase and makes it difficult to manage. Also, if a previous case is reopened after a long time, there is a hard time finding all the records regarding the case.


The Online Crime Reporting System serves as a digital platform where individuals can efficiently report and document incidents, suspects, suspicious activities, or crimes they witness. Leveraging modern web technologies, the system facilitates a seamless and user-friendly interface accessible to a diverse range of users.


## Table of Contents
* [Tech Stack](#Tech Stack)
* [User Features of Online Crime Reporting System in Django](#User Features of Online Crime Reporting System in Django)
* [Authors](#authors)
* [Instructions for executing locally:](#Instructions for executing locally:)


## Tech Stack
Python
Django
Javascript/Jquery
SQLite
Bootstrap 4
Django Rest Framework


## User Features of Online Crime Reporting System in Django
1.Registration – For the registration, The user need to register first to create their own account.
2.Login – By default the user need to login first to enable to access the system.
3.Add, update, delete a record - a user can add and update their personal records on to the website database.
3.Add Complaint – For the complaint, The user can view and add complaint through this website.
4.Report Suspect - User can report a suspect they may have identified.


## Authors
* [Robert Ruai Mawich](https://github.com/RobertRuai)


## Instructions for executing locally:
cd Online_Crime_Reporting_System_Django/
pip3 install -r requirements.txt
cd crm/
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
