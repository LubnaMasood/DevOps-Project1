# Fundamental Project 

## Contents

* [Objective](#objective)
* [CRUD Functionality Within the App](#CRUD-functionality-within-the-app)
* [Trello Board](#Trello-Board)
* [ERD](#Entity-Relation-Diagram)
* [Risk Assessment](#Risk-Assessment)
* [Front End](#Front-End)
* [Testing & Automation](#Testing-&-Automation)
* [Future Improvements](#Future-Improvements)
* [Acknowledgments](#Acknowledgments)




## Objective

This project aims to create a CRUD application with utilisation of supporting tools, methodologies and technologies that capture all core modules covered during the QA DevOps training.


## CRUD Functionaility Within the App

The CRUD functionality of this app will include: 

* CREATE\
  -Add Customers\
  -Add Orders
  
* READ\
  -View all Customers\
  -View all Customer Orders
  
 * UPDATE\
  -Update Customers\
  -Edit Customer Orders
  
  * DELETE\
  -Delete Customers\
  -Delete Customer Orders
 

## Trello Board



## Entity Relation Diagram 

A simple entity-relationship diagram (ERD) was constructed to showcase the relationship I expected these entities to have. The database consists of a one-to-many relationship; my initial design looked like this:


As the project progressed, the design also changed during the development process. The first modification occurred when I realised that the attribute 'product_id' was unnecessary to the diagram- consequently, it was removed. Additional attributes (username and password) were also included in the model. However, the most noticeable change to the final model occurred when the date_placed attribute in the customer's orders table was changed from Integer to DateTime.

## Risk Assessment 

Below you can find my detailed risk assessment, which provides a comprehensive evaluation of the perceived risks associated with the success and failure of this project. 


_Note: The dark blue rows indicate risks discovered and subsequently added as the project developed._ 

## Front End

The entry point for this app is the homepage, navigated to with the '/' url suffix. When a user enters the website, they are greeted with the following homepage: 


The homepage displays the current Customers and Orders on the website,  


## Testing & Automation


## Future Improvements


## Acknowledgments

