![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

CREDITS

admin.py - https://stackoverflow.com/questions/28512710/how-to-add-custom-search-box-in-django-admin (i used following code:
    class PostAdmin(admin.ModelAdmin):
    search_fields = ['shop']
)

photo - https://images.pexels.com/photos/894695/pexels-photo-894695.jpeg?auto=compress&cs=tinysrgb&w=1600


to be addressed : slug field in model, debug=true, form resubmits on page refresh

class comments and class reply taken fromhttps://www.youtube.com/watch?v=ScABStHY8cc&t=5s


fix posts being added withouit approval


...............................................
# [Beansters](https://beansters-1fb9f50a5877.herokuapp.com/)

<image>

[Beansters](https://beansters-1fb9f50a5877.herokuapp.com/) is a website aimed at coffee lovers. User are able to search for coffee shops and read reviews. Users can then add their own review or comment. If a coffee shop is not listed on the site then a user can add a Coffee Shop Post and leave a review.

## Table of content

- [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
  - [Features](#features)


- [Functionality](#features)
  - [CRUD](#crud)
  - [Database & Models](#database-&-models)
    
- [Validation](#validation)
  
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [User Testing](#user-testing)
  - [Bugs](#bugs)
  - [Features to be Implemented](#features-to-be-implemented)
  
- [Libraries](#libraries)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Credits](#credits)
  


## User Experience
### User Stories
### Design
### Features


## Functionality
### CRUD
### Database & Models

### Validation

HTML - No errors were returned when code was checked with the official [W3C validator](https://validator.w3.org/).

<image>

CSS - No errors were returned when code was checked with the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/).

<image>

JAVASCRIPT - No errors were returned when code was checked with the official [JS Hint validator](https://jshint.com/).

<image>

PYTHON - No errors were shown when code was checked with the Code Institute Python Linter (https://pep8ci.herokuapp.com/).

<image>

Accessibility - I confirmed the code used is accessible by using lighthouse in devtools.

<image>

## TESTING

### Manual Testing
<table>  
            <tr>
              <th>Action</th>
              <th>Expected Behaviour</th>
              <th>Pass / Fail </th>
            </tr>
            <tr>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td></td>
              <td></td>
              <td></td>
            </tr>
</table>

### User Testing
The website link was provided to [ ] users all of whom were able to use the site easily and navigate the options without issue. A majority of the users said [ ]. 

### Bugs
#### Solved Bugs
[ ]

#### Remaining Bugs
- none

## Features to be Implemented

## LIBRARIES
The following libraries were used:
- [ ]

## DEPLOYMENT

In order to deploy the website he following steps were followed:
- From the Heroku dashboard, create a new app;
- Navigate to settings tab;
- Create confg var with key "CREDS" and for  value copy and paste the contents of creds.json file - click add;
- Create config var with key "PORT" and value "8000" - click add;
- Next add buildpacks to install dependencies;
- Click add buildpack and select python then save changes. Then select node.js and click save again;
- Buildpacks must be in this order with python first and node.js second;
- Next navigate to deploy tab;
- Select github as deployment method, confirm connect to github;
- Search for github repository and once found click connect; and
- Enable automatic deployment to deploy.



## CREDITS
Thanks to:
- Code Institute for providing the Gitpod template.

		




