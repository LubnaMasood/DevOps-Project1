# Fundamental Project 

## Contents

* [Objective](#objective)
* [CRUD Functionality Within the App](#CRUD-functionality-within-the-app)
* [Trello Board](#Trello-Board)
* [ERD](#Entity-Relation-Diagram)
* [CI PIPELINE](#CI-PIPELINE)
* [Risk Assessment](#Risk-Assessment)
* [Front End](#Front-End)
* [Testing & Automation](#Testing-&-Automation)
* [Future Improvements](#Future-Improvements)





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

<img width="861" alt="ERD-" src="https://user-images.githubusercontent.com/101265654/162644756-a5cd68be-6ad6-4ffa-9112-00d7126f0467.png">


As the project progressed, the design also changed during the development process. The first modification occurred when I realised that the attribute 'product_id' was unnecessary to the diagram- consequently, it was removed. Additional attributes (username and password) were also included in the model. However, the most noticeable change to the final model occurred when the date_placed attribute in the customer's orders table was changed from Integer to DateTime.


<img width="924" alt="ERD Complete" src="https://user-images.githubusercontent.com/101265654/162644948-ac9c4634-b312-4978-813c-4fedb1d5610c.png">


## CI PIPELINE



## Risk Assessment 

Below you can find my detailed risk assessment, which provides a comprehensive evaluation of the perceived risks associated with the success and failure of this project. 


_Note: The dark blue rows indicate risks discovered and subsequently added as the project developed._ 

## Front End

The entry point for this app is the homepage, navigated to with the '/' url suffix. When a user enters the website, they are greeted with the following homepage: 


The homepage displays the current Customers and Orders on the website,  


## Testing & Automation


## Future Improvements

With more time the imporovements that I would implement include: 

* To make the front-end more appealing and functional because the design of an application is essential for the app's functionality. Users are more likely to utilise an application if they find the layout easy to understand and appealing to the eye. I would add a functioning Navbar with the help of Bootstrap to enhance the overall design. 

* Including customisation into the app makes the website more personal for a user. Adding profile pictures and creating a login feature would help again with the usability aspect. Also, for safety purposes- only users could sign in and out and access their personal details and order history. 
