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
  - [Goal](#goal)
  - [Design](#design)
  - [User Stories](#user-stories)
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


### Goal
The goal of the website is to build a community of coffee lovers. The website is intended to be a place that coffee lovers come to post reviews of new coffee shops they find, discuss their views on exisiting coffee shops and discover coffee shops they haven't been to before.

It is inteded that once their is a community of coffee lovers additional functionality can be added so that business owners can promote their coffee shops on the site.

### Design
The website was designed with simplicity in mind. There is minimal clutter with the focus being on the coffee shop posts themselves. The font [Quicksand](https://fonts.google.com/specimen/Quicksand) was chosen as it adds to the minimalist feel of the site. The color palette was take from [Color Space](https://mycolor.space/) and was chosen as it is reflective of the colors of coffee itself. The darker colors which appear when hovering over buttons representing espresso, the header and footer being reminiscent of the coffe & milk mixture of cappucinos while the beige body similar to that of foamed milk that tops them.

### User Stories
Agile methodoligies were used to plan and design the website. User stories were created using issues on GitHub and were added  to two epics (milestones) the first for a minimal viable product and the second for additional functionality. The progress of these user stories were traked via the use of the GitHub kanban-board. 


#### Completed (Must Haves)
- As a **User** I can **add a coffee shop to the site** so that **other users can find it**.
- As a **User** I can **interact with coffee shop posts** so that **i can give my review**.
- As a **User** I can **edit my post or review** so that i can **give an updated opinion or correct a mistake**.
- As a **User** I can **delete posts or comments** so that **they are removed from the website**.
- As a **User** I can **search** so that **i can find coffee shops**.
- As a **User** I can **create an account** so that **i can login to use the site**.
- As a **User** I can **see confirmations** so that **i know actions taken have been successful**.
- As a **User** I can **rate a coffee shop out of stars** so that **others can easily see my opinion of a shop**.

#### Should Haves
- As a **User** I can **see an aggregate rating of all users on a post** so that **i can know the overall communities view of a coffee shop**.

#### Could Haves
- As a **User** I can **search by star rating** so that **I can discover the best coffee shops**.
- As a **User** I can **add my own photos to a  coffee shop post** so that **other users can view them**.
  
##### Wont Haves
- As a **User** I can **receive notifications** so that **I know when people have replied to my comments**.
- As a **User** I can **search by location on a map** so that **I can discover the best coffee shops in a certain area**.
- As a **User** I can **add my own photos to a  coffee shop post** so that **other users can view them**.


### Features
#### Homepage
The homepage displays the most recently added coffee shop posts paginated by three. On first arrival the navbar provides the options to register or login. The option to add a coffee shop is displayed but this is only actie for logged in users.
Each post dispalys an image, the shop name, location, a short description and who it was posted by. If users wish to they can click "read reviews" to read a full review and see comments.

There is a search function which allows users to search for coffee shops. Results matching the search parameters will be displayed and if there are no available results users are given the option of adding a coffee shop themselves.

#### Post Detail
Once a user clicks "read reviews" on a post they are taken to the post detail view. Here they can see a full review of the coffee shop as made by the original poster. Here they will also be able to read comments which have been added by other users. If the user has logged in they will be able to add additional comments themselves.

#### Add a Coffee Shop
If users are logged in they have the option to add a coffee shop by clicking "Add a Coffee Shop" in the navbar. Once clicked the user is taken to a form where they can fill out the details of the coffee shop, provide a review and upload an image to accompany their post.

#### Register / Login
Users have the ability to register or login. Once they have done so they have the ability to post reviews or add comments.

#### Confirmations
The site offers users confirmations and feedback throughout to ensure the user knows what they are doing. There are confirmations for logging in, logging out, adding or editing a post (notifying the user that their post will appear once it has been approved) and adding a comment (same as for a post). When a user chooses to delete a post a modal will appear asking them if they are sure they want to delete as this cannot be undone.



## Functionality
### CRUD
#### Create
Users can add a coffee shop to the site. This is done via the use of a crispy form. They also have the option to add comments to a post which also uses crispy forms. Once this is done the post requires approval from the administrator. This is to ensure the quality of the content that is posted to the site.

#### Read
Once a post is made it can be viewed on the homepage and if clicked into it can be seen in more detail. Here any comments that have been added can also be viewed.

#### Update
Users have the option of editing their own posts if they wish. Once a post is updated it requires approval once again. The reasoning for this is to prevent a user's post being approved and then them being able to edit it to say something which is not keeping inline with the sites ethos. 

#### Delete
Users have the option to delete their own posts. If they choose to do so a modal will appear asking them to confirm the deletion. This is to ensure a post is not deleted accidentally as deleting a post cannot be undone and all associated comments will also be deleted.

### Database & Models

<table>  
        <tr>
              <th>Coffee Shop Post</th>
            </tr>    
	<tr>
              <th>Name</th>
              <th>Type</th>
            </tr>
            <tr>
              <td>Shop</td>
              <td>CharField (unique)</td>
            </tr>
            <tr>
              <td>Description</td>
              <td>CharField</td>
            </tr>
            <tr>
              <td>Review</td>
              <td>CharField</td>
            </tr>
            <tr>
              <td>Author</td>
              <td>ForeignKey</td>
            </tr>
            <tr>
              <td>created_on</td>
              <td>DateTimeField</td>
            </tr>
            <tr>
              <td>featured_image</td>
              <td>CloudinaryField</td>
            </tr>
	<tr>
              <td>Approved</td>
              <td>BooleanField</td>
            </tr>
	<tr>
              <td>Location</td>
              <td>Charfield</td>
            </tr>
</table>

<table>  
        <tr>
              <th>Comment Model</th>
            </tr>  
	<tr>
              <th>Name</th>
              <th>Type</th>
            </tr>
	<tr>
              <td>Post</td>
              <td>ForeignKey</td>
            </tr>
            <tr>
              <td>Name</td>
              <td>CharField</td>
            </tr>
            <tr>
              <td>Email</td>
              <td>EmailField</td>
            </tr>
            <tr>
              <td>Body</td>
              <td>TextField</td>
            </tr>
            <tr>
              <td>created_on</td>
              <td>DateTimeField</td>
            </tr>
            <tr>
              <td>Approved</td>
              <td>BooleanField</td>
            </tr>
</table>

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
#### Homepage
<table>  
            <tr>
              <th>Action</th>
              <th>Expected Behaviour</th>
              <th>Pass / Fail </th>
            </tr>
            <tr>
              <td>View hompage</td>
              <td>last three posts are displayed in 3 columns all links work</td>
              <td></td>
            </tr>
            <tr>
              <td>View hompage</td>
              <td>All nav bar links work but "add coffee shop post" link is inactive when user is logged out</td>
              <td></td>
            </tr>
            <tr>
              <td>View hompage</td>
              <td>Footer sits at bottom of page and all icon links work</td>
              <td></td>
            </tr>
            <tr>
              <td>Use search bar</td>
              <td>Successful search returns result</td>
              <td>Unsuccessful search returns prompt to add coffee shop</td>
            </tr>
            <tr>
              <td>Click "Read reviews" button on post</td>
              <td>Brings user to post detail view</td>
              <td></td>
            </tr>
            <tr>
              <td>Click Login</td>
              <td>Brings user to login page</td>
              <td></td>
            </tr>
            <tr>
              <td>Click Register</td>
              <td>Brings user to register page</td>
              <td></td>
            </tr>
            <tr>
              <td>Click Add a Coffee Shop</td>
              <td>Brings user to new post page</td>
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
#### Register Page
<table>  
            <tr>
              <th>Action</th>
              <th>Expected Behaviour</th>
              <th>Pass / Fail </th>
            </tr>
            <tr>
              <td>Click Register in Nav Bar</td>
              <td>Sign Up form is displayed</td>
              <td></td>
            </tr>
            <tr>
              <td>Sign Up</td>
              <td>Message alert says registration was successful</td>
              <td></td>
            </tr>
</table>

#### Login Page
<table>  
            <tr>
              <th>Action</th>
              <th>Expected Behaviour</th>
              <th>Pass / Fail </th>
            </tr>
            <tr>
              <td>Click Login in Nav Bar</td>
              <td>Login form is displayed</td>
              <td></td>
            </tr>
            <tr>
              <td>Login</td>
              <td>Message alert says login was successful</td>
              <td></td>
            </tr>
</table>

#### Add a Coffee Shop Page
<table>  
            <tr>
              <th>Action</th>
              <th>Expected Behaviour</th>
              <th>Pass / Fail </th>
            </tr>
            <tr>
              <td>Click Add a Coffee Shop in Nav Bar</td>
              <td>Brings user to new post page</td>
              <td></td>
            </tr>
            <tr>
              <td>Create Post</td>
              <td>Message alert says post will appear once approved and user is returned to Homepage</td>
              <td></td>
            </tr>
</table>

#### Post Detail Page
<table>  
            <tr>
              <th>Action</th>
              <th>Expected Behaviour</th>
              <th>Pass / Fail </th>
            </tr>
            <tr>
              <td>Click Read Reviews on post on Homepage</td>
              <td>Brings User to Post Detail page</td>
              <td></td>
            </tr>
            <tr>
              <td>Edit / Delete</td>
              <td>If user is author of post there should be options to edit or delete post</td>
              <td></td>
            </tr>
            <td>Click Edit</td>
              <td>User is brought to Edit Post page</td>
              <td></td>
            </tr>
            <tr>
            <td>Edit Post</td>
              <td>User is returned to Homepage and message alert displays stating post is waiting approval</td>
              <td></td>
            </tr>
            <tr>
            <td>Delete Post</td>
              <td>Modal should appear asking user to confirm as deletion cannot be undone</td>
              <td></td>
            </tr>
            <tr>
            <td>Add Comment</td>
              <td>If user is not logged in text should display asking them to login or register in order to post a comment</td>
              <td></td>
            </tr>
            <tr>
            <td>Add Comment</td>
              <td>If user is  logged in comment form should display</td>
              <td></td>
            </tr>
            <tr>
            <td>Add Comment</td>
              <td>Once User adds comment, a message alert should display stating their comment is awaiting approval</td>
              <td></td>
            </tr>
</table>

#### Page Layout
<table>  
            <tr>
              <th>Action</th>
              <th>Expected Behaviour</th>
              <th>Pass / Fail </th>
            </tr>
            <tr>
              <td>Mobile - Home page</td>
              <td>Layout is displayed correctly</td>
              <td></td>
            </tr>
            tr>
              <td>Mobil - Post Detail page</td>
              <td>Layout is displayed correctly</td>
              <td></td>
            </tr>
            <tr>
              <td>Mobile - Register page</td>
              <td>Layout is displayed correctly</td>
              <td></td>
            </tr>
            <tr>
              <td>Mobile - Login page</td>
              <td>Layout is displayed correctly</td>
              <td></td>
            </tr>
            <tr>
              <td>Mobile - Logout page</td>
              <td>Layout is displayed correctly</td>
              <td></td>
            </tr>
            <tr>
              <td>Mobile - Add a Coffee Shop page</td>
              <td>Layout is displayed correctly</td>
              <td></td>
            </tr>
            <tr>
              <td>Mobile - Edit Post page</td>
              <td>Layout is displayed correctly</td>
              <td></td>
            </tr>
            <tr>
              <td>Mobile - Search page</td>
              <td>Layout is displayed correctly</td>
              <td></td>
            </tr>
</table>

<table>  
            <tr>
              <th>Action</th>
              <th>Expected Behaviour</th>
              <th>Pass / Fail </th>
            </tr>
            <tr>
              <td>Desktop - Home page</td>
              <td>Layout is displayed correctly</td>
              <td></td>
            </tr>
            tr>
              <td>Desktop - Post Detail page</td>
              <td>Layout is displayed correctly</td>
              <td></td>
            </tr>
            <tr>
              <td>Desktop - Register page</td>
              <td>Layout is displayed correctly</td>
              <td></td>
            </tr>
            <tr>
              <td>Desktop - Login page</td>
              <td>Layout is displayed correctly</td>
              <td></td>
            </tr>
            <tr>
              <td>Desktop - Logout page</td>
              <td>Layout is displayed correctly</td>
              <td></td>
            </tr>
            <tr>
              <td>Desktop - Add a Coffee Shop page</td>
              <td>Layout is displayed correctly</td>
              <td></td>
            </tr>
            <tr>
              <td>Desktop - Edit Post page</td>
              <td>Layout is displayed correctly</td>
              <td></td>
            </tr>
            <tr>
              <td>Desktop - Search page</td>
              <td>Layout is displayed correctly</td>
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

		




