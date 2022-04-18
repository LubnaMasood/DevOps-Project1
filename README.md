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

To ensure that an agile methodology has been followed, the progress of this project was recorded and tracked on Trello Board. 

The Trello Board for this project can be broken down into the following categories: 

<img width="1440" alt="Trello Board" src="https://user-images.githubusercontent.com/101265654/162663591-64545b9f-dc43-4963-a094-13d7d339d796.png">

* Project Resources: All things that are necessary for the project to be completed 
* User Stories: User stories are statements that exist to demonstrate the functionality of the application. Putting them into stories allows me to follow a step-by-step procedure in creating these functionalities.
* Backlog: Are outstanding tasks that need to be completed for the completion of the project.
* In Progress: Are tasks that are currently being worked on and developed.  
* Done: The tasks that have been completed and added to the project. 


## Entity Relation Diagram 

A simple entity-relationship diagram (ERD) was constructed to showcase the relationship I expected these entities to have. The database consists of a one-to-many relationship; my initial design looked like this:

<img width="861" alt="ERD-" src="https://user-images.githubusercontent.com/101265654/162644756-a5cd68be-6ad6-4ffa-9112-00d7126f0467.png">


As the project progressed, the design also changed during the development process. The first modification occurred when I realised that the attribute 'product_id' was unnecessary to the diagram- consequently, it was removed. Additional attributes (username and password) were also included in the model. However, the most noticeable change to the final model occurred when the date_placed attribute in the customer's orders table was changed from Integer to DateTime.


<img width="924" alt="ERD Complete" src="https://user-images.githubusercontent.com/101265654/162644948-ac9c4634-b312-4978-813c-4fedb1d5610c.png">


## CI PIPELINE

A CI pipeline or continuous integration pipeline diagram consists of associated frameworks, services and tools that have been used during the different development phases. This pipeline allows for rapid and simple development-to-deployment by automating the integration process

<img width="849" alt="CI Pipeline" src="https://user-images.githubusercontent.com/101265654/162669777-69489953-77b0-437a-a063-20ea6ed082b5.png">

Here the diagram shows the tools that were used for this particular project- (template from QA Community). The build stages are: 

* Pull Python and HTML Code from GitHub
* Build with Flask 
* Test with pytest- produce coverage reports
* Run by staring the app on the local VM (connected to MySQL)

## Risk Assessment 

Below you can find my detailed risk assessment, which provides a comprehensive evaluation of the perceived risks associated with the success and failure of this project. 

<img width="935" alt="Risk Assessment-project" src="https://user-images.githubusercontent.com/101265654/162667157-b1803ac7-3dc6-4072-8960-e57da99f6376.png">

_Note: The dark blue row indicates risks discovered and subsequently added as the project developed. Also, the likelihood of the risks were later updated._ 

## Front End

The entry point for this app is the homepage, navigated with the '/' url suffix. When a user enters the website, they are greeted with the following homepage: 

<img width="788" alt="Homepage" src="https://user-images.githubusercontent.com/101265654/162671031-d03affbc-1ba1-4db8-bae4-e74862a1e3e0.png">

The homepage displays the current Customers and Orders on the website. All customers inputted onto the app have their first name, last name, email, phone number, username and password displayed on the homepage. At the top of the page, a navigation bar is present, which can also be viewed on the other pages on the app, with links that contain the homepage, create a customer and add an order.

<img width="481" alt="View Customers" src="https://user-images.githubusercontent.com/101265654/162673446-cdc6e61b-744d-44f9-b0dd-4d3aa8daf9f3.png">

<img width="323" alt="View Orders" src="https://user-images.githubusercontent.com/101265654/162673357-c8a8ed57-2fde-4c7b-83bc-77b780dab0f2.png">


The next page is the Create a Customer Page: 

<img width="695" alt="Create Customer" src="https://user-images.githubusercontent.com/101265654/162672299-0e8e9fbd-b386-492e-9096-a180018f1e6d.png">

A user can create a new customer by filling in the relevant fields. Once the fields are filled out, the submit button is clicked. The user clicks back to the homepage to view the details that have just been created. Flask Form Validation is active on all fields so that no fields can be left empty or 'NULL'. 

Users can also create an order in the app: 

<img width="482" alt="Add Order" src="https://user-images.githubusercontent.com/101265654/162672449-c0348e91-2b53-45ed-82e8-5ceeb83e09b4.png">

The follwoing update pages are also avilable for the user to amend their personal details and order status: 

<img width="578" alt="Update Customer" src="https://user-images.githubusercontent.com/101265654/162672911-68ff1e11-7f1a-4c24-85fc-204f6eac69c5.png">

<img width="527" alt="Update Order" src="https://user-images.githubusercontent.com/101265654/162672920-09663d5f-3b11-43f7-b3f2-ac5e7f41be52.png">

Users can also delete their details and orders from the app: 

<img width="310" alt="Delete Customer" src="https://user-images.githubusercontent.com/101265654/162674105-3769a5d9-8ad2-4381-a246-524567a3de8d.png">

<img width="423" alt="Delete Order" src="https://user-images.githubusercontent.com/101265654/162674158-eb81837b-5186-4b64-bca2-b981af4e3916.png">

However, to delete a customer from the app, the corresponding order must be deleted first and vice versa. The rationale for this is because it is a relational database; therefore, you cannot remove just a customer for example- an error message like the one below is returned:

<img width="1438" alt="Error Message" src="https://user-images.githubusercontent.com/101265654/162674361-989c4d87-e290-4681-9241-f566a05a81ce.png">

Once the customer and order was delete from the app the order table had one less entry: 

<img width="287" alt="Delete orders" src="https://user-images.githubusercontent.com/101265654/162675565-4bb09bd5-3299-4538-9013-44e1c07713d4.png">



## Testing & Automation




## Future Improvements

With more time the imporovements that I would implement include: 

* To make the front-end more appealing and functional because the design of an application is essential for the app's functionality. Users are more likely to utilise an application if they find the layout easy to understand and appealing to the eye. I would add a functioning Navbar with the help of Bootstrap to enhance the overall design. 

* Including customisation into the app makes the website more personal for a user. Adding profile pictures and creating a login feature would help again with the usability aspect. Also, for safety purposes- only users could sign in and out and access their personal details and order history. 
