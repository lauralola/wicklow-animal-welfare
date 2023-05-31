# **Wicklow Animal Welfare**

![](/readme_docs/readme_imgs/am-i-responsive.png)

<br>

[💻Live Site](https://wicklow-animal-welfare.herokuapp.com/)


# **About**
<br>
This project had been designed to be a B2C e-commerce store to raise funds and supplies for a animla rescue charity. The products offered are for the consumer to donate food, toys or donations to the resuce through the site. It also has a section for dogs looking for homes, information on the charity and general useful information for those thinking of adopting or volunteering. This was added to further engage users in the product and as a site to visit to get information on the charity and what we do. These posts with dogs for adoption should be constantly updating and so inform the public through the marketing strategy.

This project was built as the final portfolio submission for the [Code Institute](https://codeinstitute.net/) Higher National Diploma in Full Stack Software Development. 

<br>

# **Contents**
* [**Business Model**](<#bussines-model>)
    *[**Marketing Strategy**](<#marketing-strategy>)
         *[SEO](<#seo>)
* [**Project**](<#project>)
    * [**Project Management**](<#project-management>)
        * [GitHub Project Board](<#github-project-board>)
        * [Database Schema](<#database-schema>)
* [**User Experience UX**](<#user-experience-ux>)
    * [**User Stories**](<#user-stories>)
        - [User](#users)
        - [User Unregister](#unregistered-user)
        - [User Register](#registered-user)
        - [User Staff](#staff-user)
    * [Site Structure](<#site-structure>)
    * [Colour Scheme](<#colour-scheme>)
    * [Typography](<#typography>)
    * [Flowcharts](#flowcharts)
        - [Flowchart Unregister User](#user-unregister-👇)
        - [Flowchart Registered User](#user-registered-👇)
        - [Flowchart Staff User](#user-staff-👇)
        - [Flowchart Others](#other-👇)
* [**Features**](<#features>)
        * [Sign-Up Page](<#sign-up-page>)
        * [Sign-In Page](<#sign-in-page>)
        * [Sign Out](<#sign-out>)
        * [Home Page](<#home-page>)
        * [Nav Bar](<#nav-bar>)
        * [Products Page](<#products-page>)
        * [Product Detail Page](<#fproduct-detail-page>)
        * [Edit Product Form](<#edit-product-form>)
        * [Delete Product](<#delete-product>)
        * [Product Management Form](<#product-management-form>)
        * [Shopping Bag Page](<#shopping-bag-page>) 
        * [Checkout Page](<#checkout-page>) 
        * [Checkout Success Page](<#checkout-success-page>) 
        * [Adoption Page](<#adoption-page>)
        * [Dog Detail Page](<#dog-detail-page>)        
        * [Edit Dog Form](<#edit-dog-form>)
        * [Delete Dog](<#delete-dog>)
        * [Dog Management Form](<#dog-management-form>)
        * [Profile Page](<#profile-page>)
        * [Dog Detail Page-Comments](<#dog-detail-page-comments>)  
        * [Edit Comments Page](<#edit-comments-page>)
        * [Search Results Page](<#search-results-page>)
        * [Footer](<#footer>)
    * [**Future Features**](<#future-features>)
* [**Testing**](<#testing>)
    * [**Validator Tests**](<#validator-tests>)
        * [W3C (HTML)](<#w3c-html>)
        * [W3C (CSS)](<#w3c-css>)
        * [ESLint (JavaScript)](<#eslint-javascript>)
    * [**Additional Tests**](<#additional-tests>)
        * [Manual Tests](<#manual-tests>)
        * [Input Validation Tests](<#input-validation-tests>)
        * [Automated Tests](<#automated-tests>)
        * [Responsive Tests](<#responsive-tests>)
        * [Browser Tests](<#browser-tests>)
        * [Lighthouse Tests](<#lighthouse-tests>)
    * [**Bugs**](<#bugs>)
        * [Resolved](<#resolved>)
        * [Unresolved](<#unresolved>)
* [**Technologies Used**](<#technologies-used>)
    * [Languages](<#languages>)
    * [Frameworks](<#frameworks>)
    * [Software](<#software>)
    * [Libraries](<#libraries>)
* [**Deployment**](<#deployment>)
    * [Project Deployment via Heroku](<#project-deployment-via-heroku>)
* [**Credits**](<#credits>)
    * [Content](<#content>)
    * [Media](<#media>)
    * [Code](<#code>)
*  [**Acknowledgements**](<#acknowledgements>)

# **Bussines Model**
<br>
The project had been based in Business to Consumer (B2C) style. It is an e-commerce where the consumer can find options to donate specific items to the charity.
<br>

## **Marketing Strategy**
<br>

### **SEO**
Several SEO techniques were undertaken in order to ensure the site ranks highly in search engine results. Also the files robots.txt and sitemap.xml had been included. The sitemap.xml file had been created using 

[xml-sitemap](https://www.xml-sitemaps.com/)

**Keywords:**
<br>
Starting with a brain storm of keywords that are relevant to the e-commerce itself. And reduced by making use of a word search so as to target the more relevant, the site I had used is 

[wordtracker](https://www.wordtracker.com/)

**Content marketing:**
<br>
The information and description of the products in the site had been kept the more relevant to the site purpose. Also the keywords had been taken into account when creating things like categories and such, so insure they are present without getting to be considere as spam. 
Each page has its own title, and finally meta tag description had been included in the base so that every page contains them.


**Social Media Marketing: Facebook**
<br>
The e-commerce has its own facebook, the one that will keep posting a minimun of three times a week, and releasing alerts of monthly offers and benefits, which are sent by e-mail to the subscribers. This is for to motivate the subscription to our newsletter and increase the clients database.
<br>

![](/readme_docs/readme_imgs/facebook-1.png)

<br>

![](/readme_docs/readme_imgs/facebook-3.png)

<br>

![](/readme_docs/readme_imgs/facebook-2.png)

<br>

**Email Marketing**
This will be based in our newsletter service and also to the users that had purchased with us previously. The starting strategy is to produce a monthly mail with new arrivals and deals, also will contain some news about the gaming world, etc.
Subscribed users will recieve a welcome mail informing benefits will that be coming in future mails. This refering to the monthly mail with deals, so the user does not feel overwhelmed or spammed. 
For now there is a basic mail, but in future a better design will be implemented. Also had been set for the staff to recieve a daily report from mailchimp so to keep track of the traffic on it.

Also when the user registers for an account in the app will recieve a welcome email with some information about benefits and promoting our newsletter on it.
<br>

Screenshot of subscribed temp mail inbox
<br>

![](/readme_docs/readme_imgs/temp-inbox-subscription.png)

<br>
Mail to the subscribers
<br>

![](/readme_docs/readme_imgs/welcome-mailchimp.png)

<br>
Mailchimp daily report

<br>

![](/readme_docs/readme_imgs/mailchimp-mail.png)

<br>
[Back to top](<#contents>)
[Back to top](<#contents>)
[Back to top](<#contents>)

# Project

## Project Management

An agile methodology was used to plan and develop the Wicklow Animal Welfare project. All the main features of the application were recorded and refined into user stories. These user stories were created and stored as GitHub issues and then mapped into iterations to help to plan and allocate the workload. 

[Back to top](<#contents>)

### GitHub Project Board

![Project Board](readme/images/project-board.png)

All the user stories were added to a GitHub project board to assist with tracking progress. All user stories started in the to-do section. On completion, each user story was moved into the done section and marked as closed. 

[Click here to view the Project Board](https:/)

[Back to top](<#contents>)

### Database Schema

![Database Schema](readme/images/database-schema.png)

[Back to top](<#contents>)

# User Experience UX

As target users, we are aiming for individuals interetsed in animal welfare, adopting a dog or donating to the charty. The section with information on how to help also links to our products for sale. 

# User Stories

## **Users**

<br>
   
As a **user** I can **view a navbar from every page** so that **navigate easily between pages**

### Acceptance Criteria:
* Acceptance Criteria 1: A site wide nav bar component should be visible to the user from all pages of the site.
* Acceptance Criteria 2: The navbar should be accessible, intuitive and user friendly.
* Acceptance Criteria 3: All the main pages of the site should be visible on the navbar.
* Acceptance Criteria 4: Some pages should be hidden on the nav bar based on user logged in status.

### Tasks:
&check; Create navbar component
<br>
&check; Assign icons to logged in and logged out variables
<br>
&check; Add links and urls 
<br>
<hr>

As a **user** I can **view an ordered list of all the products** so that **I can browse through them**

### Acceptance Criteria:
* Acceptance Criteria 1: A 'Donate' link should be visible to users on the site nav bar
* Acceptance Criteria 2: When clicked, the user should be directed to the products page displaying a list of products to purchase

### Tasks:
&check; Add donate link to site nav bar
<br>
&check; Add product app
<br>
&check; Test functionality
<hr>

As a **user** I can **view an ordered list of all the dogs** so that **I can browse through them**

### Acceptance Criteria:
* Acceptance Criteria 1: An 'Adopt' link should be visible to users on the site nav bar
* Acceptance Criteria 2: When clicked, the user should be directed to the dogs page displaying a list of dogs for adoption
### Tasks:
&check; Add adopt link to site nav bar
<br>
&check; Add dog app
<br>
&check; Test functionality
<hr>

As a **user** I can **view details of the dogs, comments and likes** so that **I can know more about them**

### Acceptance Criteria:
* Acceptance Criteria 1: A link which when clicked can bring a detailed page of the selected dog 
* Acceptance Criteria 2: Likes and comments are visible on detailed page of the selected dog 

### Tasks:
&check; Add link to the homing page to bring to dog detail page
<br>
&check; Add dog detail template, urls and views
<br>
&check; Test functionality
<hr>

As a **user** I can **view details of the products** so that **I can know more about them and add to my bag**

### Acceptance Criteria:
* Acceptance Criteria 1: A link which when clicked can bring a detailed page of the selected product
* Acceptance Criteria 2: A link which when clicked adds selected product to bag

### Tasks:
&check; Add link to the product page to bring to product detail page
<br>
&check; Add product detail template, urls and views
<br>
&check; Add bag app and link to add to bag
<br>
&check; Test functionality

As a **user** I can **add, edit and remove items from my bag** so that **I can adjust my bag**

### Acceptance Criteria:
* Acceptance Criteria 1: Separate links which when clicked can add, edit and delete items in bag
* Acceptance Criteria 2: Bag is updated and correct after adjustments

### Tasks:
&check; Add links to edit bag app
<br>
&check; Test functionality

As a **user** I can **checkout** so that **I can purchase items in my bag**

### Acceptance Criteria:
* Acceptance Criteria 1: Checkout link brings to checkout page
* Acceptance Criteria 2: Successful checkout sends confirmation email, order detail page, database order
* Acceptance Criteria 3: Interrupted checkout sends webhook to stripe

### Tasks:
&check; Set up checkout app, forms, templates etc
<br>
&check; Set up and connect stripe for checkout
<br>
&check; Set up and connect webhooks through stripe
<br>
&check; Test functionality

As a **logged in user** I can **add, edit and delete my own comments and likes to the dog posts** so that **I can interact with the site**

### Acceptance Criteria:
* Acceptance Criteria 1: When logged in I have access to comment and like a dog post
* Acceptance Criteria 2: When logged in, my own posts have edit and delete links that work

### Tasks:
&check; Add like and comment functionality to homing app
<br>
&check; Test functionality

## **Unregistered User**
<br>

As an **unregistered user** I can **clearly identify purpose of the page** so that **I can interact with the site**

### Acceptance Criteria:
* Acceptance Criteria 1: Clear landing page with links to further details

### Tasks:
&check; Add home app and links
<br>
&check; Test functionality

As an **unregistered user** I can **register for an account** so that **I can interact further with the site**

### Acceptance Criteria:
* Acceptance Criteria 1: A sign up button link should be visible to non logged in users on the site nav bar
* Acceptance Criteria 2: Clicking the sign up button should direct the user to the sign up form page
* Acceptance Criteria 3: Successful sign up form submission should direct the user to the sign in page 

### Tasks:
&check; Add sign up button link to the nav bar
<br>
&check; Add conditional to button to only display if the user is logged out
<br>
&check; Add URL link to button to navigate to the dj rest auth sign up url
<br>
&check; Add sign up form component with on change and on submit methods
<br>
&check; Add redirect to sign in page on successful submission
<br>
&check; Test functionality
<br>
<br>

## **Registered User**
<br>

As Registered User I want to be able to sign in and out of my account
## Acceptance Criteria:
* Acceptance Criteria 1: A log in and log out page link should be visible on the nav bar depending on status
* Acceptance Criteria 2: Clicking the link should direct the user to the log in or logout form page depending on status
* Acceptance Criteria 3: Filling in the form correctly should direct the user to the homepage and display their profile link in the navbar as well as the other pages only available to logged in users or redirect them to the homepage with a success message on log out

## Tasks:
&check; Add log in and log out page component
<br>
&check; Add conditional to only display to logged out users
<br>
&check; Add on change and on submit methods for log in and log out form
<br>
&check; Add route for log in and log out page component to app.js
<br>
&check; Add redirect to homepage on success
<br>
&check; Test functionality
<br>
<hr>

## **Staff User**
<br>
As Staff/Admin User I want to access to a staff panel where I can manage the store's database from
   - Staff Panel page

As Staff/Admin User I want to be able to manage the DB from the front-end
   - Staff Panel page:
      - Add, update or delete Product Form
      - Add, update or delete a dog profile

[Back to top](<#contents>)


7. As a **logged in user** I can **edit my profile and see past orders** so that **I can change and update my profile and see past orders**

### Acceptance Criteria:
* Acceptance Criteria 1: A dropdown menu with a my profile link should be visible to the user
* Acceptance Criteria 2: The dropdown menu should only be visible if the user is logged in
* Acceptance Criteria 3: Clicking the profile button should direct the user to profile form page
* Acceptance Criteria 4: The form fields should be pre-populated with the data from the specific user if completed before
* Acceptance Criteria 5: Upon successful submission, the user should be redirected back to the updated profile page
* Acceptance Criteria 6: Past orders should be visible and update accordingly

### Tasks:
&check; Add dropdown menu component with profile button 
<br>
&check; Add URL to direct the user to profile
<br>
&check; Add conditional to only show dropdown menu if the user is logged in
<br>
&check; Add profile edit form component with on change and on submit methods
<br>
&check; Add user redirect to profile page on successful submit
<br>
&check; Add error handling and validation
<br>
&check; Test functionality
<hr>

10. As an **admin user** I can **add, edit and delete products** so that **I can keep the site up to date**

### Acceptance Criteria:
* Acceptance Criteria 1: An edit or delete icon button should be visible to a admin user in the product detail page and from the product management in my account drop down 
* Acceptance Criteria 2: This should only be visible if the user is admin 
* Acceptance Criteria 3: Clicking the edit or delete button should edit or delete the product and redirect the user back to the home page

### Tasks:
&check; Add edit and delete button link to the product detail page and product management drop down to my account area
<br>
&check; Add handle add, edit, delete methods
<br>
&check; Add user redirect to home page on successful task
<br>
&check; Add conditional to dropdown menu 
<br>
&check; Test functionality
<hr>

10. As an **admin user** I can **add, edit and delete dogs** so that **I can keep the site up to date**

### Acceptance Criteria:
* Acceptance Criteria 1: An edit or delete icon button should be visible to a admin user in the dog detail page and from the dog management in my account drop down 
* Acceptance Criteria 2: This should only be visible if the user is admin 
* Acceptance Criteria 3: Clicking the edit or delete button should edit or delete the product and redirect the user back to the home page

### Tasks:
&check; Add edit and delete button link to the dog detail page and dog management drop down to my account area
<br>
&check; Add handle add, edit, delete methods
<br>
&check; Add user redirect to home page on successful task
<br>
&check; Add conditional to dropdown menu 
<br>
&check; Test functionality
<hr>

10. As an **admin user** I can **delete users comments** so that **I can keep the site up to date**

### Acceptance Criteria:
* Acceptance Criteria 1: A delete icon button should be visible to a admin user in the comments section
* Acceptance Criteria 2: This should only be visible if the user is admin 
* Acceptance Criteria 3: Clicking delete button should delete the comment

### Tasks:
&check; Add delete button link to the comment section for admin user
<br>
&check; Add handle delete method
<br>
&check; Add user redirect on successful task
<br>
&check; Test functionality
<hr>

11. As a **user** I can **use a search bar to search the products list** so that **I can find a specific product quickly and easily**

### Acceptance Criteria:
* Acceptance Criteria 1: A search bar with a text input field should be visible to users on all pages
* Acceptance Criteria 2: When a user adds text to the search field the products list should be queried and products not matching the query should be filtered out and removed from view

### Tasks:
&check; Add search bar component with query method
<br>
&check; Import and add search bar component into header
<br>
&check; Add search method query into products list 
<br>
&check; Test functionality
<hr>


3. As a **user** I can **delete my account** so that **I can remove my profile and all its content from the platform instantly**

### Acceptance Criteria:
* Acceptance Criteria 1: A delete button should be visible within a users profile dropdown menu
* Acceptance Criteria 2: Clicking the delete button should display a pop up window prompting the user to confirm their request to delete their profile
* Acceptance Criteria 3: If a user clicks the delete button on the pop up their profile should be deleted along with all their content and they should be logged out and redirected back to the home page

### Tasks:
x Add delete button icon to profile page dropdown menu
<br>
x Add delete user/profile method
<br>
x Add pop up delete confirmation to confirm user deletion
<br>
x Add redirect to method on successful completion
<br>
x Test functionality
<hr>

## Site Structure

The site structure for Wicklow Animal Welfare was kept simple and user-friendly to avoid confusion. The main site nav bar and is present on every page of the site to allow for easy access to site navigation. Non-authenticated users have limited access to pages within the site, and this is reflected in the changing state of the nav menus. Non logged in users only have access to certain areas and log-in / sign-up auth pages are clearly labelled. Authenticated users can access commenting, liking and their profile page with admin users able to change the database on the front end. 

[Back to top](<#contents>)

## Colour Scheme

The colour scheme was kept simple with black and white mostly used and pops of colour from the images through the site. 

[Back to top](<#contents>)

## Typography

Wicklow Animal Welfare uses [Google Fonts](https://fonts.google.com/) for its typography. The font utilised is 

[Back to top](<#contents>)

# Features

### Sign-Up Page

![Sign Up Page](readme/images/sign-up-page.png)

The sign-up page was created to allow users to register their details and sign-up for an account. On successful form submission the user is redirected to the sign in page to sign into their new account.

[Back to top](<#contents>)

### Sign-In Page

![Sign In Page](readme/images/sign-in-page.png)

The sign-in page was created to allow users to sign into their account to access features. On successful form submission, the user is redirected to the homepage.

[Back to top](<#contents>)

### Sign Out

![Sign Out](readme/images/sign-out.png)

The sign-out functionality doesn't have its own page. The user simply clicks the sign out button in one of the nav menus and they are signed out of their account and redirected back to the home page.

[Back to top](<#contents>)

### Home Page

![Home Page 1](readme/images/homepage-1.png)

![Home Page 2](readme/images//homepage-2.png)

The homepage features the a striking image and links to access our donation page, also some basic information about the rescue and links about donating, adopting and volunteering with some information. Links in the nav bar link directly to these sections within the home page.

[Back to top](<#contents>)

### Nav Bar

![Nav Bar 1](readme/images/navbar-1.png)

![Nav Bar 2](readme/images/navbar-2.png)

The nav bar handles the main site menu. It is available on all pages and contains all links to pages across the site. 

[Back to top](<#contents>)

### Products Page

![Products Page](readme/images/products-page.png)

The products page is available to view for both authenticated and non-authenticated users. The page features a list of all the products currently on the site with their prices and image. The list  csn be ordered by price, category and rating. Clicking on the image of a product will open the detail on that product. 

[Back to top](<#contents>)

### Product Detail Page
![Product Detail Page](readme/images/products-detail-page.png)

The product detail page is available to view for both authenticated and non-authenticated users. Clicking on the image of a productin the main page will open the detail on that product. This displays more information and an area to add the product to the bag. A success message confirming this is given if added or updated here. 

[Back to top](<#contents>)

### Edit Product Form

![Edit Product Form](readme/images/edit-product-form.png)

The edit product form is only accessible to admin users who are authenticated. Clicking the edit icon next to the product directs the user to the form to edit the details for this product prefilled with the text already present. An alert is also displayed to the user that they are editing this product. Changing the fields and submitting the form directs the user back to the product page for this product with the details changed and a success message. Clicking the cancel button returns the user to the product page with no changes made. Issues with submitting an incorrectly filled form will raise an alert box to tell the user the form was not submitted or saved.  

[Back to top](<#contents>)

### Delete Product

![Delete Product](readme/images/delete-product.png)

The delete product is available to authenticated admin users. There is no page for deletion. The user simply clicks the delete icon and it is removed. A success message is given to let the user know the item has been deleted. 

[Back to top](<#contents>)

### Product Management Form

![Product Management Form](readme/images/product-management-form.png)

The product management form is only available to authenticated users via their account tab. If non-authenticated users try to access this page they are redirected to the home page. The page features the the blank product form. On successful submission, the user is redirected to the product page with the new product visible as a card. If the user clicks the cancel button they are returned to the previous page they were on. 

[Back to top](<#contents>)

### Shopping Bag Page

![Shopping Bag Page](readme/images/shopping-bag-page.png)

The shopping bag page opens when the bag icon on the top right of the screen is clicked. This will also inform user of the total cost of the shopping bag. If the bag is empty the user is infomed and directed back to the shopping area. Any items added to the bag will be displayed with the details of their cost, quantity and total with buttons to edit or delete the items. Tax back is available for donations over $250 and the user is informed of this. From the bag the user is able to go to the checkout area. 

[Back to top](<#contents>)

### Checkout Page

![Checkout Page](readme/images/checkout-page.png)

The user is asked to complete a form with their details and an order summary is displayed. They can save the details completed to their profile by leaving the box for this checked. The user is asked for their card details. A warning that their card will be charged the amount displayed is given before the complete order button. If user information has not been correctly completed in the correct format the user is redirected back to this section of the page to rectify. If submitted successfully the user is directed to the checkout success page. 

[Back to top](<#contents>)

### Checkout Success Page

![Checkout Success Page](readme/images/checkout-success-page.png)

This page displays an order summery and order number for the user. Email confirmation is also provided. 

[Back to top](<#contents>)

### Adoption Page

![Adoption Page](readme/images/adoption-page.png)

The adoption page is available to view for both authenticated and non-authenticated users. The page features a list of all the dogs currently on the site for adoption with their image, sex, name and date created. Clicking on the image of a dog will open more detail on the dog. 

[Back to top](<#contents>)

### Dog Detail Page
![Dog Detail Page](readme/images/dog-detail-page.png)

The dog detail page is available to view for both authenticated and non-authenticated users. Clicking on the image of a dog in the main page will open the detail on that dog. The page features more information on the dog with comments and likes visible. Only logged in users have access to comment or like. Users must be logged in to comment or like and are alerted to this if not. Once logged in users can like and unlike, comment and edit or delete their own comments. 

[Back to top](<#contents>)

### Edit Dog Form

![Edit Dog Form](readme/images/edit-dog-form.png)

The edit dog form is only accessible to admin users who are authenticated. Clicking the edit icon next to the dog directs the user to the form to edit the details for this dog prefilled with the text already present. An alert is also displayed to the user that they are editing this. Changing the fields and submitting the form directs the user back to the dog page with the details changed and a success message. Clicking the cancel button returns the user to the dog page with no changes made. Issues with submitting an incorrectly filled form will raise an alert box to tell the user the form was not submitted or saved.  

[Back to top](<#contents>)

### Delete Dog

![Delete Dog](readme/images/delete-dog.png)

The delete dog is available to authenticated admin users. There is no page for deletion. The user simply clicks the delete icon and it is removed. A success message is given to let the user know it has been deleted. 

[Back to top](<#contents>)

### Dog Management Form

![Dog Management Form](readme/images/dog-management-form.png)

The dog management form is only available to authenticated users via their account tab. If non-authenticated users try to access this page they are redirected to the home page. The page features the the blank dog form. On successful submission, the user is redirected to the homing page with the new dog visible as a card. If the user clicks the cancel button they are returned to the previous page they were on. 

[Back to top](<#contents>)

### Profile Page

![Profile Page](readme/images/profile-page.png)

The user profile page is only visible to authenticated users. Here any saved information is displayed and can be edited and details of previous orders are visible. Details can be edited and updated by completing and selecting the update tab. A success message will appear is correct. Orders can also be opened from here by selecting the order number to see more details on the order. 

[Back to top](<#contents>)

### Dog Detail Page - Comments

![Dog Detail Page - Comments](./assets/readme_images/comment.png) 

* At the bottom of detailed page, users can read the comments posted by other users. If the user is logged in or is a superuser they have access to the buttons for deleting or updating comments. If the comment field is left blank and submit clicked the user is prompted to fill in the field. 

[Back to top](<#contents>)

### Edit Comments Page

![Edit Comments Page](./assets/readme_images/logged_in_comment.png)

* If a user is logged in they can click a link beside their own comments and they are allowed to add, edit or delete their own comments. The website superuser can delete or update any comments without having to access the admin panel.

[Back to top](<#contents>)

### Search Results Page

![Search Page](./assets/readme_images/search.png)

* A user can user the search bar tool to find relevant products. They are displayed below a message informing the user that if not results found please try another. If the user clicks the search button on an empty enquiry they will be informed that they forgot to search. This currently just searches products but a future feature could be to search all apps. 

[Back to top](<#contents>)

### Footer

![Footer](./assets/readme_images/footer.png)
* The footer contains links to all social media for the page. 

[Back to top](<#contents>)

### 404 Page

![404 Page](readme/images/404-page.png)

The 404 page is triggered when a user navigates to a site URL which doesn't exist. This could be because of a number of reasons, including a faulty link or an expired URL. Most users will not see this page, but it is there as a backup for users who encounter these rare errors. The purpose of the 404 page is to notify the user that there has been an error, and the page that they have tried to access cannot be found.

[Back to top](<#contents>)

## Future Features

1. Further functionality to search the site. 

2. A user could have the functionality to completely delete their account along with any related content. 

3. An events section could be added so users can fundraising events.

4. Rating section could be implemented.

[Back to top](<#contents>)

# Testing

## Validator Tests

### W3C HTML

All the pages of the site have been passed through the [W3C HTML Markup Validation Service](https://validator.w3.org/), with minor errors rectified. No errors or warnings are now showing.

![HTML Validator Feed Page](readme/images/html-validator-page.png)

[Back to top](<#contents>)

### W3C CSS

![CSS Validator](readme/images/css-validator.png)

This file was passed through the [Jigsaw W3C CSS Validation Service](https://validator.w3.org/).

[Back to top](<#contents>)

### ESLint Javascript

All JavaScript files in the project have been run through the [JavaScript ESLinter](https://eslint.org/). 

2. Do not pass children as props - this is based off of code provided by Code Institute

All other errors were corrected.

[Back to top](<#contents>)

### Manual Tests

# **Responsiveness**
<bt>

The site had been test for the following devices:

Mobile: 360 * 640 / 390 * 844 / 414 * 896

Tablet: 768 * 1024 / 820 * 1180 / 1366 * 768

Monitor: 1280 * 1024 / 1600 * 900 / 1950 & UP

The site had been test in Chrome seeming all according to the design. In Firefox. In Internet Explorer all seems to work as the design.
<br>

## **Navbar**
<br>
The features will be displayed according to the logged user, as marked in features page

<br>

**Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Logo     | Directs to the landing/index page | Click |✅|
| User Menu Icon     | Dropdown allauth options menu | Click |✅|
| Sign Up     | Directs to Sign Up Form | Click |✅|
| Sign In     | Directs to Sign In Form | Click |✅|
| Sign Out     | Directs to Sign Out Form | Click |✅|
| User name beside User Icon | Display 'guest' for unregister users  | Click |✅|
| Shopping Cart Icon | Directs to the shopping cart page | Click |✅|
| Shopping Cart Amount | Display the total of the shopping cart | Click |✅|
| Toggle Menu Icon - Small devices     | Dropdown menu options | Click |✅|
| Store | Directs to the store page, wares list | Click |✅|
| News | Directs to the news page, news list | Click |✅|
| Search | Render wares according to user's input | Click |✅|
<br>

**Register User**
<br>

| Feature       | Expected           | Action| Result|
| ------------- |:------------- | :-----|-----:|	 	
| User name beside User Icon | Display user's name when logged in | Click |✅|
| My Profile     | Directs to the request user profile page | Click |✅|
| Sign Out     | Directs to Sign Out Form | Click |✅|
<br>

**Staff User**
<br>

| Feature       | Expected           | Action| Result|
| ------------- |:------------- | :-----|-----:|	 	
| User name beside User Icon | Display user's name when logged in | Click |✅|
| Staff Panel     | Directs to the Staff Panel page | Click |✅|
| Sign Out     | Directs to Sign Out Form | Click |✅|
<br>


## **Messages**
<br>
The features will be displayed for all the users, as marked in features page

<br>

**Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:------------- | :-----|-----:|
| Message in top right of screen     | Floating message according to the user action | Triggered by user action |✅|
<br>

## **Top Button**
<br>
The features will be displayed for all the users, as marked in features page
<br>

**Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Top Button     | Display when user scroll screen down | Triggered by user action |✅|
| Top Button     | Takes screen to top | Click |✅|
<br>


## **Footer**
<br>
The features will be displayed according to the user actions, as marked in features page

<br>

**Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Subscribe Newsleeter Form | Verify if mail is register already and gives feedback to user | On Submit button |✅|
| Subscribe Newsleeter - Success | If user subscribtion went successful | Response to form action |✅|
| Subscribe Newsleeter - Fail | If user subscribtion failed | Response to form action |✅|
| Facebook | Directs to e-commerce's facebook in new tab | Click |✅|
| Q&A | Directs to the questions and answers page - underconstruction | Click |✅|
| Terms & Conditions | Directs to the terms and conditions page - underconstruction | Click |✅|
| Contact Us | Directs to Contact Us Form page | Click |✅|
| Contact Us - Success | Directs to Contact Us Success page | Click |✅|
<br>

**From here the features are present just in the page they are mentioned.**

## **Landing Page**

**Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Accordion of Images     | Allows interaction and display animation | Click on |✅|
| Animated Text    | Visual slogan with word game | - |✅|
<br>

## **Store Page**

**Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Animated Deliver Banner      | Display the delivery conditions | - |✅|
| Categories Filters Bar       | Display the Categories filters | - |✅|
| Categories Filters Bar    | Dropdown the menu with the subcategories according to the one clicked on | Click |✅|
| Pagination    | Display according to the page the user is in, it would show prev or next plus
||  a set of pages | Click |✅|
| Pagination | Directs to the clicked page | Click |✅|
| Wares Cards | Up to 4 by pagination | - |✅|
| Wares Cards - QBuy button | Add the product to the shopping cart | Click |✅|
| Wares Cards - Link | Directs to the selected ware details page | Click |✅|
<br>

## **Ware Details Page**

**Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Back to Store Button       | Directs to Store page  | Click |✅|
| Display images accordion       | Accordion with ware images - interaction with user  | Click |✅|
| Add To Cart Button       | Add the ware to the shopping cart  | Click |✅|
| Reviews       | Render ware reviews and staff replies to  | - |✅|
| Images Toggle Button       | Display all the images in bigger size than accordion   | Click |✅|
<br>

**Unregister User**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Invitation to sign up or sign in to be able to leave a review | Directs to Sign Up or Sign In as clicked on  | Click |✅|
<br>

**Register User**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Bookmark Button       | Button that display the state of the ware,
||if bookmarked or not and save the action  | Click |✅|
| Link to Leave a Review       | Opens a Pop Up form for it  | Click |✅|
<br>

**Staff User**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Edit Ware Button       | Open the form fill with the ware to be edit  | Click |✅|
| Delete Ware Button       | Open a pop up form to confirm the ware to be delete  | Click |✅|
| Reply Review Toggle Button       | Display a form to reply the user review   | Click |✅|
| Delete Images Button       | Open a pop up form to confirm the image to be delete  | Click |✅|
<br>

## **News Page**

**Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Pagination    | Display according to the page the user is in, it would show prev or next plus
||  a set of pages | Click |✅|
| Pagination | Directs to the clicked page | Click |✅|
| News Cards | Up to 4 by pagination | - |✅|
<br>

## **News Details Page**

**Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Back to News Button       | Directs to News page  | Click |✅|
| Source Link       | Directs the user to the source of the new - new tab  | Click |✅|
<br>

**Staff User**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Edit New Button       | Open the form fill with the new to be edit  | Click |✅|
| Delete New Button       | Open a pop up form to confirm the new to be delete  | Click |✅|
<br>

## **Staff Page**

**Staff Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Add Ware Button   | Directs to a form page for it  | Click |✅|
| Add Image Button   | Directs to a form page for it  | Click |✅|
| News Entry Button   | Directs to a form page for it  | Click |✅|
| Orders   | Directs to a page where the orders are render  | Click |✅|
| Contacted Us   | Directs to a page where the inquiries are render  | Click |✅|
| Search Wares  | Display the ware or wares, according to staff input  | Click |✅|
<br>

### **Staff Forms**
<br>

| Feature       | Expected           | Action | Result |
| ------------- |:-------------| :-----|-----:|
| Add Ware Form   | Save and trigger message  | Click |✅|
| Edit Ware Form   | Save and trigger message  | Click |✅|
| Delete Ware Form   | Delete and trigger message  | Click |✅|
| Add Image Form   | Save and trigger message  | Click |✅|
| Delete Image Form   | Delete and trigger message  | Click |✅|
<br>

## **Shopping Cart**

**Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Remove  | Remove the item from the shopping cart | Click |✅|
| Update Qty | Modify the quantity of the item as user's input | Click |✅|
| Keep Shopping Link | Returns the user to the store | Click |✅|
| Secure Checkout Link | Directs to the Checkout Form page | Click |✅|
<br>

## **CheckOut Page**

**Unregister Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Form to fill  | Form with required fields, validate | - |✅|
| Payment fields  | Form with required fields, validate | - |✅|
| Adjust Cart Link | Returns the user to the shopping cart | Click |✅|
| Complete Order Link | Directs to the Checkout Success page if successful | Click |✅|
<br>

**Register Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Form to review, prefill  | Form filled with profile user's data, validate required fields | - |✅|


Here you will find a comprehensive list of all the manual tests that were carried out on the Gear Addict front-end interface.

| Status | **Home Page**
|:-------:|:--------|
| &check; | Page has correct URL
| &check; | Hottest rigs displays four rigs
| &check; | Hottest rigs displays rigs ordered by most liked
| &check; | Content is displaying correctly
| &check; | Content is responsive
| &check; | All links work correctly and navigate to the correct page

[Back to top](<#contents>)

| Status | **Navbar**
|:-------:|:--------|
| &check; | Content is responsive
| &check; | Current page displays active class
| &check; | Logged-in nav items are displayed correctly to logged-in users
| &check; | Logged-out nav items are displayed correctly to logged-out users
| &check; | Profile image and link is correct to current authenticated user
| &check; | All links work correctly and navigate to the correct page
| &check; | Mobile menu is displayed on small screens
| &check; | Mobile nav menu opens and closes correctly
| &check; | Mobile menu is closed when a user clicks away
| &check; | Mobile menu is closed when a user clicks a nav link
| &check; | Mobile menu nav toggle menu button opens and closes the mobile menu
| &check; | Nav items change styling on hover

[Back to top](<#contents>)

| Status | **Footer**
|:-------:|:--------|
| &check; | Content is responsive
| &check; | Current page displays active class
| &check; | Logged-in nav items are displayed correctly to logged-in users
| &check; | Logged-out nav items are displayed correctly to logged-out users
| &check; | All links work correctly and navigate to the correct page
| &check; | Nav items change styling on hover

[Back to top](<#contents>)

| Status | **Products Page**
|:-------:|:--------|
| &check; | Page has correct URL
| &check; | Content is displaying correctly
| &check; | Content is responsive
| &check; | All links work correctly and navigate to the correct page
| &check; | Search functionality is working
| &check; | Rigs are ordered from newest to oldest
| &check; | Rigs list infinite scroll functionality is working
| &check; | Correct content is displayed on rig cards
| &check; | Like / unlike functionality is working
| &check; | Save / unsave functionality is working
| &check; | Rig links link to correct rigs
| &check; | Profile links link to correct profiles
| &check; | No results found is displayed when there are no rigs in the list

[Back to top](<#contents>)

| Status | **Feed Page**
|:-------:|:--------|
| &check; | Page has correct URL
| &check; | Page is only visible to authenticated users
| &check; | Non-authenticated users are redirected to the home page
| &check; | Content is displaying correctly
| &check; | Content is responsive
| &check; | All links work correctly and navigate to the correct page
| &check; | Search functionality is working
| &check; | Rigs list infinite scroll functionality is working
| &check; | Correct content is displayed on rig cards
| &check; | Like / unlike functionality is working
| &check; | Save / unsave functionality is working
| &check; | Rig links link to correct rigs
| &check; | Profile links link to correct profiles
| &check; | Becoming a fan of a user adds their rigs to the feed page
| &check; | Unfanning a user removes their rigs from the feed page
| &check; | No results found is displayed when there are no rigs in the list

[Back to top](<#contents>)

| Status | **Gear Page**
|:-------:|:--------|
| &check; | Page has correct URL
| &check; | Page is only visible to authenticated users
| &check; | Non-authenticated users are redirected to the home page
| &check; | Content is displaying correctly
| &check; | Content is responsive
| &check; | Search functionality is working
| &check; | Gear list infinite scroll functionality is working
| &check; | Users can only see gear that is owned by them
| &check; | Correct content is displayed on gear cards
| &check; | Delete functionality is working
| &check; | The edit button redirects the user to the correct edit gear page
| &check; | Dropdown menu functionality is working
| &check; | No results found is displayed when there is no gear in the list
| &check; | Category badge displays correctly
| &check; | Gear status badges display correctly

[Back to top](<#contents>)

| Status | **Rigs Page**
|:-------:|:--------|
| &check; | Page has correct URL
| &check; | Page is only visible to authenticated users
| &check; | Non-authenticated users are redirected to the home page
| &check; | Content is displaying correctly
| &check; | Content is responsive
| &check; | Search functionality is working
| &check; | Rig list infinite scroll functionality is working
| &check; | Users can only see rigs that are owned by them
| &check; | Correct content is displayed on rig cards
| &check; | Like / Save buttons are not visible
| &check; | No results found is displayed when there are no rigs in the list
| &check; | Rig links link to correct rigs

[Back to top](<#contents>)

| Status | **Saved Page**
|:-------:|:--------|
| &check; | Page has correct URL
| &check; | Page is only visible to authenticated users
| &check; | Non-authenticated users are redirected to the home page
| &check; | Content is displaying correctly
| &check; | Content is responsive
| &check; | Search functionality is working
| &check; | Rigs list infinite scroll functionality is working
| &check; | Correct content is displayed on rig cards
| &check; | Like / unlike functionality is working
| &check; | Save / unsave functionality is working
| &check; | Saving a rig adds it to the list
| &check; | Unsaving a rig removes it from the list
| &check; | Users can only see their own saved rigs
| &check; | Rig links link to correct rigs
| &check; | Profile links link to correct profiles
| &check; | No results found is displayed when there are no rigs in the list

[Back to top](<#contents>)

| Status | **Profile Page**
|:-------:|:--------|
| &check; | Page has correct URL
| &check; | Page dropdown menu is only visible to authenticated users who own the profile
| &check; | Profile edit button redirects the user to the profile edit page
| &check; | Username edit button redirects the user to the username edit page
| &check; | Password edit button redirects the user to the password edit page
| &check; | User profile content is displaying correctly
| &check; | Updated profile content is displaying correctly
| &check; | Content is responsive
| &check; | Search functionality is working
| &check; | Rigs list infinite scroll functionality is working
| &check; | Correct content is displayed on rig cards
| &check; | Like / unlike functionality is working
| &check; | Save / unsave functionality is working
| &check; | Rig links link to correct rigs
| &check; | Profile links like to correct profiles
| &check; | Fan count is correct
| &check; | Idol count is correct
| &check; | Rig count is correct
| &check; | Gear count is correct
| &check; | Fan and idol counts increment correctly when becoming a fan and unfanning another user
| &check; | Popular profiles is displaying correctly
| &check; | Fan button is not displayed on the users own profile or on popular profiles 
| &check; | Fan button is working correctly
| &check; | Unfan button is working correctly

[Back to top](<#contents>)

| Status | **Sign In Page**
|:-------:|:--------|
| &check; | Page has correct URL
| &check; | Page is only visible to non-authenticated users
| &check; | Authenticated users are redirected to the home page
| &check; | Content is displaying correctly
| &check; | Content is responsive
| &check; | Form fields handle change correctly
| &check; | Field input errors are displayed to the user
| &check; | Successful submission signs the user in successfully and redirects the user back to their previous page
| &check; | Sign up link redirects the user to the sign up page

[Back to top](<#contents>)

| Status | **Sign Up Page**
|:-------:|:--------|
| &check; | Page has correct URL
| &check; | Page is only visible to non-authenticated users
| &check; | Authenticated users are redirected to the home page
| &check; | Content is displaying correctly
| &check; | Content is responsive
| &check; | Form fields handle change correctly
| &check; | Field input errors are displayed to the user
| &check; | Successful submission saves the users details and redirects the user to the sign in page
| &check; | Sign in link redirects the user to the sign in page

[Back to top](<#contents>)

| Status | **Sign Out**
|:-------:|:--------|
| &check; | The sign-out button link is displayed on both site navs
| &check; | The sign-out button is only displayed to authenticated users
| &check; | Sign out functionality works correctly
| &check; | On successful sign out the user is redirected to the home page

[Back to top](<#contents>)

| Status | **Add Gear Page**
|:-------:|:--------|
| &check; | Page has correct URL
| &check; | Page is only visible to authenticated users
| &check; | Non-authenticated users are redirected to the home page
| &check; | Content is displaying correctly
| &check; | Content is responsive
| &check; | Form fields handle change correctly
| &check; | Field input errors are displayed to the user
| &check; | Successful submission creates a new instance of gear and redirects the user to the gear page
| &check; | The cancel button redirects the user to the last page they were on
| &check; | The submit button submits the form
| &check; | All fields are successfully submitted 
| &check; | Blank fields are handled correctly

[Back to top](<#contents>)

| Status | **Add Rig Page**
|:-------:|:--------|
| &check; | Page has correct URL
| &check; | Page is only visible to authenticated users
| &check; | Non-authenticated users are redirected to the home page
| &check; | Content is displaying correctly
| &check; | Content is responsive
| &check; | Form fields handle change correctly
| &check; | Field input errors are displayed to the user
| &check; | Successful submission creates a new instance of rig and redirects the user to the rig details page
| &check; | The cancel button redirects the user to the last page they were on
| &check; | The submit button submits the form
| &check; | All fields are successfully submitted 
| &check; | Blank fields are handled correctly

[Back to top](<#contents>)

| Status | **Rig Detail Page**
|:-------:|:--------|
| &check; | Page has correct URL
| &check; | Content is displaying correctly
| &check; | Content is responsive
| &check; | Image gallery is working correctly
| &check; | Dropdown menu is only displayed to authenticated users who own the rig
| &check; | Edit rig button redirects user to correct edit rig page
| &check; | Rig delete button deletes the rig and redirects the user to the last page they were on
| &check; | Profile link links to correct profile
| &check; | No comments yet message displays when there are no comments
| &check; | Comment form only displays to authenticated users
| &check; | A list of comments ordered from newest to oldest appears in a list on the correct rig
| &check; | Comment is assigned to correct user
| &check; | Comment form field handles change correctly
| &check; | Comment field input errors are displayed to the user
| &check; | Successful comment submission creates a new comment which appears at the top of the comment list
| &check; | The post button submits the comment
| &check; | The comment dropdown menu is only visible to users who are authenticated and own the comment
| &check; | The comment edit button opens the edit comment form
| &check; | The comment delete button deletes the comment and re-renders the comment list with the comment removed

[Back to top](<#contents>)

| Status | **Edit Gear Page**
|:-------:|:--------|
| &check; | Page has correct URL
| &check; | Content is displaying correctly
| &check; | Content is responsive
| &check; | Page is only visible to authenticated users who own the gear
| &check; | Non-authenticated users are redirected to the home page
| &check; | Form fields are pre-populated with the correct instance of gear
| &check; | Form fields handle change correctly
| &check; | Field input errors are displayed to the user
| &check; | Successful submission updates the correct instance of gear and returns the user to the gear page
| &check; | The cancel button redirects the user to the last page they were on
| &check; | The submit button submits the form
| &check; | All fields are successfully submitted 
| &check; | Blank fields are handled correctly
| &check; | All fields that aren't changed remain the same
| &check; | Updating the image field changes the image

[Back to top](<#contents>)

| Status | **Edit Rig Page**
|:-------:|:--------|
| &check; | Page has correct URL
| &check; | Content is displaying correctly
| &check; | Content is responsive
| &check; | Page is only visible to authenticated users who own the rig
| &check; | Non-authenticated users are redirected to the home page
| &check; | Form fields are pre-populated with the correct instance of rig
| &check; | Form fields handle change correctly
| &check; | Field input errors are displayed to the user
| &check; | Successful submission updates the correct instance of rig and returns the user to the rig details page
| &check; | The cancel button redirects the user to the last page they were on
| &check; | The submit button submits the form
| &check; | All fields are successfully submitted 
| &check; | Blank fields are handled correctly
| &check; | All fields that aren't changed remain the same
| &check; | Updating the image fields changes the images

[Back to top](<#contents>)

| Status | **Delete Gear**
|:-------:|:--------|
| &check; | The delete button is only visible in the gear dropdown menu to authenticated users who own the gear
| &check; | Clicking the delete button deletes the correct instance of gear and re-renders the gear list with the gear removed

[Back to top](<#contents>)

| Status | **Delete Rig**
|:-------:|:--------|
| &check; | The delete button is only visible in the rig dropdown menu to authenticated users who own the rig
| &check; | Clicking the delete button deletes the correct instance of rig and redirects the user to the last page they were on

[Back to top](<#contents>)

| Status | **Edit Profile Page**
|:-------:|:--------|
| &check; | Page has correct URL
| &check; | Content is displaying correctly
| &check; | Content is responsive
| &check; | Page is only visible to authenticated users who own the profile
| &check; | Non-authenticated users are redirected to the home page
| &check; | Form fields are pre-populated with the correct user profile
| &check; | Form fields handle change correctly
| &check; | Field input errors are displayed to the user
| &check; | Successful submission updates the correct user profile and returns the user to the last page they were on
| &check; | The cancel button redirects the user to the last page they were on
| &check; | The submit button submits the form
| &check; | All fields are successfully submitted 
| &check; | Blank fields are handled correctly
| &check; | All fields that aren't changed remain the same
| &check; | Updating the image fields changes the images
| &check; | Updated profile details are immediately reflected on the user profile page

[Back to top](<#contents>)

| Status | **Edit Username Page**
|:-------:|:--------|
| &check; | Page has correct URL
| &check; | Content is displaying correctly
| &check; | Content is responsive
| &check; | Page is only visible to authenticated users who own the profile
| &check; | Non-authenticated users are redirected to the home page
| &check; | Form fields are pre-populated with the correct user profile username
| &check; | Form fields handle change correctly
| &check; | Field input errors are displayed to the user
| &check; | Successful submission updates the correct user profile username and returns the user to the last page they were on
| &check; | The cancel button redirects the user to the last page they were on
| &check; | The submit button submits the form
| &check; | All fields are successfully submitted 
| &check; | Blank fields are handled correctly
| &check; | All fields that aren't changed remain the same
| &check; | Updated profile usernames are immediately reflected on the user profile page

[Back to top](<#contents>)

| Status | **Edit Password Page**
|:-------:|:--------|
| &check; | Page has correct URL
| &check; | Content is displaying correctly
| &check; | Content is responsive
| &check; | Page is only visible to authenticated users who own the profile
| &check; | Non-authenticated users are redirected to the home page
| &check; | Form fields handle change correctly
| &check; | Field input errors are displayed to the user
| &check; | Successful submission updates the correct user password and returns the user to the last page they were on
| &check; | The cancel button redirects the user to the last page they were on
| &check; | The submit button submits the form
| &check; | All fields are successfully submitted 
| &check; | Blank fields are handled correctly

[Back to top](<#contents>)

| Status | **404 Page**
|:-------:|:--------|
| &check; | The 404 page is triggered by an incorrect site URL
| &check; | Content is displaying correctly
| &check; | Content is responsive

[Back to top](<#contents>)

| Status | **Search Functionality**
|:-------:|:--------|
| &check; | Rigs can be searched for usernames
| &check; | Rigs can be searched for categories
| &check; | Rigs can be searched for attributes
| &check; | Rigs can be searched for genres
| &check; | Rigs can be searched for rig names
| &check; | Gear can be searched for gear names
| &check; | Gear can be searched for categories
| &check; | Gear can be searched for brands
| &check; | Gear can be searched for models
| &check; | Gear can be searched for descriptions

[Back to top](<#contents>)

| Status | **Like / Unlike**
|:-------:|:--------|
| &check; | When a rig is liked the like button is hidden and the unlike button appears
| &check; | When a rig is unliked the unlike button is hidden and the like button appears
| &check; | Liking a rig adds one to the rig like count
| &check; | Unliking a rig subtracts one from the rig like count
| &check; | Like and unlike buttons are only visible to authenticated users
| &check; | Like and unlike buttons are hidden on rigs that are owned by the authenticated user

[Back to top](<#contents>)

| Status | **Save / Unsave**
|:-------:|:--------|
| &check; | When a rig is saved the save button is hidden and the unsave button appears
| &check; | When a rig is unsaved the unsave button is hidden and the save button appears
| &check; | Saving a rig adds one to the rig star count
| &check; | Unsaving a rig subtracts one from the rig star count
| &check; | Save and unsave buttons are only visible to authenticated users
| &check; | Save and unsave buttons are hidden on rigs that are owned by the authenticated user
| &check; | Saving a rig adds it to the users saved list
| &check; | Unsaving a rig removes it from the users saved list

[Back to top](<#contents>)

### Input Validation Tests

This section will detail the input validation tests carried out on the Gear Addict application.

| Status | **Sign In Form**
|:-------:|:--------|
| &check; | Form cannot be submitted without a username
| &check; | Form cannot be submitted without a password

[Back to top](<#contents>)

| Status | **Sign Up Form**
|:-------:|:--------|
| &check; | Form cannot be submitted without a username
| &check; | Form cannot be submitted without a password
| &check; | Form cannot be submitted without confirming password
| &check; | Username cannot be over 30 characters in length
| &check; | Form cannot be submitted without matching password fields

[Back to top](<#contents>)

| Status | **Add Rig Form**
|:-------:|:--------|
| &check; | Form cannot be submitted without a rig name
| &check; | Rig name cannot be over 50 characters in length
| &check; | Form cannot be submitted without a category
| &check; | Form cannot be submitted without a budget
| &check; | Form cannot be submitted without an attribute 1
| &check; | Form cannot be submitted without a genre 1
| &check; | Form cannot be submitted without a description

[Back to top](<#contents>)

| Status | **Edit Rig Form**
|:-------:|:--------|
| &check; | Form cannot be submitted without a rig name
| &check; | Rig name cannot be over 50 characters in length
| &check; | Form cannot be submitted without a category
| &check; | Form cannot be submitted without a budget
| &check; | Form cannot be submitted without an attribute 1
| &check; | Form cannot be submitted without a genre 1
| &check; | Form cannot be submitted without a description

[Back to top](<#contents>)

| Status | **Add Gear Form**
|:-------:|:--------|
| &check; | Form cannot be submitted without a gear name
| &check; | Gear name cannot be over 50 characters in length
| &check; | Form cannot be submitted without a category
| &check; | Form cannot be submitted without a value
| &check; | Value cannot be less than or equal to zero

[Back to top](<#contents>)

| Status | **Edit Gear Form**
|:-------:|:--------|
| &check; | Form cannot be submitted without a gear name
| &check; | Gear name cannot be over 50 characters in length
| &check; | Form cannot be submitted without a category
| &check; | Form cannot be submitted without a value
| &check; | Value cannot be less than or equal to zero

[Back to top](<#contents>)

| Status | **Edit Profile Form**
|:-------:|:--------|
| &check; | Name cannot be over 20 characters in length
| &check; | Location cannot be over 30 characters in length

[Back to top](<#contents>)

| Status | **Edit Username Form**
|:-------:|:--------|
| &check; | Form cannot be submitted without a username
| &check; | Username cannot be over 30 characters in length

[Back to top](<#contents>)

| Status | **Edit Password Form**
|:-------:|:--------|
| &check; | Form cannot be submitted without a password
| &check; | Form cannot be submitted without confirming password
| &check; | Form cannot be submitted without matching password fields

[Back to top](<#contents>)

| Status | **Add Comment Form**
|:-------:|:--------|
| &check; | Form cannot be submitted if the content field is empty

[Back to top](<#contents>)

| Status | **Edit Comment Form**
|:-------:|:--------|
| &check; | Form cannot be submitted if the content field is empty

[Back to top](<#contents>)

### Automated Tests

Automated tests were run on the Gear Addict project using the [Jest Dom Testing Library](https://testing-library.com/docs/ecosystem-jest-dom/). Both the nav bar and footer components were tested to check that they were rendering the correct elements for logged in and logged out users. Details of the tests and a link to the test directory can be found below.

| Status | **Nav Bar Tests**
|:-------:|:--------|
| &check; | Renders sign in link
| &check; | Renders sign up link
| &check; | Renders latest link
| &check; | Renders home link
| &check; | Renders link to gear page for logged in user
| &check; | Renders link to rig page for logged in user
| &check; | Renders link to feed page for logged in user
| &check; | Renders link to saved page for logged in user
| &check; | Renders sign in and sign up buttons again on user log out

[Back to top](<#contents>)

| Status | **Footer Tests**
|:-------:|:--------|
| &check; | Renders sign in link
| &check; | Renders sign up link
| &check; | Renders latest link
| &check; | Renders home link
| &check; | Renders link to gear page for logged in user
| &check; | Renders link to rig page for logged in user
| &check; | Renders link to feed page for logged in user
| &check; | Renders link to saved page for logged in user
| &check; | Renders sign in and sign up buttons again on user log out

[Click this link to view the testing directory](https://github.com/Matthew-Hurrell/gear-addict/tree/main/src/components/__tests__)

[Back to top](<#contents>)

### Responsive Tests

Gear Addict has been tested on a diverse range of different devices and screen sizes to test for style and layout issues. Manual responsive tests were carried out using [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/), [Responsive Design Checker](https://responsivedesignchecker.com/) and [Am I Responsive](https://ui.dev/amiresponsive) as well as on a number of physical devices. All device screen sizes were tested on Chrome Dev Tools as well as Responsive Design Checker and no issues were found.

| Status | **Chrome Dev Tools**
|:-------:|:--------|
| &check; | iPhone SE
| &check; | iPhone XR
| &check; | iPhone 12 Pro
| &check; | Pixel 5
| &check; | Samsung Galaxy S8+
| &check; | Samsung Galaxy S20 Ultra
| &check; | iPad Air
| &check; | iPad Mini
| &check; | Surface Pro 7
| &check; | Surface Duo
| &check; | Galaxy Fold
| &check; | Samsung Galaxy A51/71
| &check; | Nest Hub
| &check; | Nest Hub Max
| &check; | iPhone 6/7/8
| &check; | Responsive mode

[Back to top](<#contents>)

| Status | **Responsive Design Checker**
|:-------:|:--------|
| &check; | 24" Desktop
| &check; | 23" Desktop
| &check; | 22" Desktop
| &check; | 20" Desktop
| &check; | 19" Desktop
| &check; | 15" Desktop
| &check; | 13" Notebook
| &check; | 10" Notebook
| &check; | Apple iPad Mini
| &check; | Apple iPad Retina
| &check; | Apple iPad Pro
| &check; | Amazon Kindle Fire
| &check; | Amazon Kindle Fire HD
| &check; | Asus Eee 1000
| &check; | Nexus 7
| &check; | Nexus 9
| &check; | Samsung Galaxy Tab 10
| &check; | Apple iPhone 3/4/4s
| &check; | Apple iPhone 5/5s
| &check; | Apple iPhone 6/6s/7
| &check; | Apple iPhone 6s Plus/7 Plus
| &check; | Samsung Galaxy S5/S6/S7
| &check; | Sony Xperia Z2/Z3
| &check; | Google Pixel
| &check; | Nexus 4
| &check; | Nexus 5
| &check; | Nexus 6

[Back to top](<#contents>)

### Browser Tests

The Gear Addict site has been tested on Google Chrome, Apple Safari, Microsoft Edge and Brave. Unfortunately, there is an unresolved error that is present on Safari. Due to Safari blocking cross-site tracking, the cookies used in the project are disabled, therefore preventing communication between the API and the front-end. Turning this setting off in the browser settings does resolve the problem, but this is a temporary fix. This bug is also present in the Code Institute walkthrough project. To resolve this in the future I will combine the front and back-end repositories into one and use a singular URL. But other than this, no browser errors were detected.

[Back to top](<#contents>)

### Lighthouse Tests

The Gear Addict site has been tested using the [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) [Lighthouse Tester](https://developer.chrome.com/docs/lighthouse/overview/) and has returned very good results. Performance ratings on the first lighthouse tests were lower due to large images. This was resolved by resizing and compressing the images. The final page test results can be found below.

#### Homepage

![Lighthouse Test Homepage](readme/images/lighthouse-homepage.png)

[Back to top](<#contents>)

#### Latest Page

![Lighthouse Test Latest Page](readme/images/lighthouse-latest.png)

[Back to top](<#contents>)

#### Feed Page

![Lighthouse Test Feed Page](readme/images/lighthouse-feed.png)

[Back to top](<#contents>)

#### Sign In Page

![Lighthouse Test Sign In Page](readme/images/lighthouse-sign-in.png)

[Back to top](<#contents>)

#### Sign Up Page

![Lighthouse Test Sign Up Page](readme/images/lighthouse-signup.png)

[Back to top](<#contents>)

#### Gear Page

![Lighthouse Test Gear Page](readme/images/lighthouse-gear.png)

[Back to top](<#contents>)

#### Rigs Page

![Lighthouse Test Rigs Page](readme/images/lighthouse-rigs.png)

[Back to top](<#contents>)

#### Saved Page

![Lighthouse Test Saved Page](readme/images/lighthouse-saved.png)

[Back to top](<#contents>)

#### Add Gear Page

![Lighthouse Test Add Gear Page](readme/images/lighthouse-add-gear.png)

[Back to top](<#contents>)

#### Add Rig Page

![Lighthouse Test Add Rig Page](readme/images/lighthouse-add-rig.png)

[Back to top](<#contents>)

#### Rig Details Page

![Lighthouse Test Rig Details Page](readme/images/lighthouse-rig-details.png)

[Back to top](<#contents>)

#### Profile Page

![Lighthouse Profile Page](readme/images/lighthouse-profile.png)

[Back to top](<#contents>)

#### 404 Page

![Lighthouse Test 404 Page](readme/images/lighthouse-404.png)

[Back to top](<#contents>)

## Bugs

A number of bugs presented themselves during the Gear Addict development process. Most of these bugs were resolved, but unfortunately due to time constraints, some of them weren't. This section will list the resolved and unresolved bugs.

[Back to top](<#contents>)

### Resolved

1. When the create rig form was first implemented, the image fields were not submitting unless all the fields had an image attached. The bug was caused by the image form data appends inside the on submit function not containing conditionals to check for an image. The bug was resolved by adding turnary conditionals into the image append methods to check for current files.

2. During development of the users profiles, there was a temporary bug when becoming a fan of another user through the popular profiles component. Becoming a fan of a user while on a user page was working as expected, but becoming a fan of a user while on the owner profile page was incrementing the idols count on the profile rather than the fan count. This bug was caused by incrementing the wrong field in the utils fanhelper and fanunhelper functions. The bug was resolved by incrementing the idols count in the profile is owner conditional instead of the fans count. 

[Click here to view the bug fix commit](https://github.com/Matthew-Hurrell/gear-addict/commit/6d634a89e13b897c77b6b55552fa177a15181a2f)

3. Later in development, a bug was discovered in the profile details edit form where the header image was overwriting the profile image field. This meant that when a header image was added and submitted in the profile edit form the profile header was being added into the profile image section. This was caused by a typo in the profile edit form appending the header image field to the profile image form data. The bug was resolved by simply changing the form data name to header_image to match the header field name. 

[Click here to view the bug fix commit](https://github.com/Matthew-Hurrell/gear-addict/commit/806779b6aef73a818ec7f124546f523eeea8ff1f)

4. A bug was also discovered on the homepage hottest rigs list. During development there was a duplicate rig being displayed within the list. Originally it was thought that the bug was being caused by the slice method, but it was discovered that this was originating from the axios response, which was returning two of the same rig. This issue was only visible when there were limited rigs on the database. To resolve this I changed the query to display rigs in descending like count order and then added more rigs. This seemed to resolve the problem. 

[Back to top](<#contents>)

### Unresolved

1. There is currently an ongoing issue with the Gear Addict project on Safari, which unfortunately hasn't been resolved. This is a problem which has been inherited form the Code Institute walkthrough Moments project. Regretfully, Safari blocks cross-domain cookies and prevents cross-site tracking, and as the back and front-end of this project are on different domains, the site relies on cookies for communication. This prevents communication between the front and back-end of this project on Safari and impedes the site functioning correctly. The issue can be temporarily fixed by turning off the prevent cross site tracking and cookie options within Safari, but obviously this isn't ideal as users cannot be expected to do this for the site to function correctly. As I intend to use this project for my portfolio, I will seek to resolve this issue moving forward by combining both repositories and deploying them both to one domain. This should resolve the issue in the future. 

[Back to top](<#contents>)

# Technologies Used

Here you will find a complete list of all the technologies used to help create and develop the Gear Addict front-end application.
For more information on the back-end technologies used, please view the [Gear Addict API README](https://github.com/Matthew-Hurrell/gear-addict-api/blob/main/README.md).

[Back to top](<#contents>)

## Languages

* [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML) - Provided the basic content and structure for the site.
* [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS) - Provided the styling for the site.
* [JavaScript (ES6)](https://www.javascript.com/) - Provided the interactivity and front-end functionality for the site.
* [Git](https://git-scm.com/) - Provided the version control system for the site.

[Back to top](<#contents>)

## Frameworks

* [React](https://react.dev/) - A free and open-source front-end JavaScript library for building user interfaces based on components.
* [Tailwind CSS React](https://tailwindcss.com/) - An open-source utility-first CSS framework.

[Back to top](<#contents>)

## Software

* [Balsamiq](https://balsamiq.com/) - An online cloud based software used for creating the site wireframes
* [GitHub](https://github.com/) - An internet hosting service used for version control. Used to host the Gear Addict repositories and for the project board used for project management and user stories
* [GitPod](https://www.gitpod.io/) - A cloud development environment used as the primary site code editor
* [Heroku](https://dashboard.heroku.com/) - A cloud platform used to host the Gear Addict application
* [ElephantSQL](https://www.elephantsql.com/) - A free cloud based PostgreSQL database system used for the application database
* [Cloudinary](https://cloudinary.com/) - A cloud-based video and image management platform used to store the site images
* [Slack](https://slack.com/intl/en-gb/) - An online instant messaging program used for site feedback and guidance from the [Code Institute](https://codeinstitute.net/) community
* [Draw.io](https://app.diagrams.net/) - An online diagram software used for the database schemas
* [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - A set of web developer tools built directly into the chrome browser. Used for responsiveness tests and further testing
* [Google Fonts](https://fonts.google.com/) - A web based font service by Google used to supply the site typography
* [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) - An open source automated testing tool used for site tests
* [Responsive Design Checker](https://responsivedesignchecker.com/) - An online testing tool used for responsive site testing
* [Am I Responsive](https://ui.dev/amiresponsive) - An online testing tool used for responsive site testing
* [Colour Contrast Checker](https://colourcontrast.cc/) - An online tool used to test background and text colour contrast
* [Font Awesome](https://fontawesome.com/) - A font and icon toolkit used for the Gear Addict icons
* [NPM JS](https://www.npmjs.com/) - The npm registry website used for information on npm libraries

[Back to top](<#contents>)

## Libraries

* [testing-library/jest-dom](https://testing-library.com/docs/ecosystem-jest-dom/) v5.16.5 - Custom jest matchers to test the state of the DOM
* [testing-library/react](https://testing-library.com/docs/react-testing-library/intro/) v11.2.7 - React Testing Library builds on top of DOM Testing Library by adding APIs for working with React components
* [testing-library/user-event](https://testing-library.com/docs/ecosystem-user-event/) v12.8.3 - A companion library for Testing Library that provides more advanced simulation of browser interactions than the built-in fireEvent method
* [axios](https://axios-http.com/docs/intro) v0.21.4 - A promise based HTTP client for the browser and node.js
* [fslightbox-react](https://fslightbox.com/react) v1.7.4 - A React component for displaying images and videos in a clean overlying box - this library improved user experience by allowing a full screen gallery for rig images. Users can click the view image gallery button and see the rig images in full quality. They can also use the arrow buttons to navigate between images. This library was chosen as I have previously used it multiple times in professional projects and it is reliable and user friendly
* [jwt-decode](https://www.npmjs.com/package/jwt-decode) v3.1.2 - A small browser library that helps decoding JWTs token which are Base64Url encoded
* [react](https://www.npmjs.com/package/react) v17.0.2 - A JavaScript library for creating user interfaces. This library / framework improved user experience greatly. The React library renders content faster for improved load times for the user, and because of the reuse of components, more content was developed in a shorter amount of time, which meant more features were available to the site users by the project deadline
* [react-boostrap](https://www.npmjs.com/package/react-bootstrap) v1.6.6 - An open-source css framework components built with React
* [react-dom](https://www.npmjs.com/package/react-dom) v17.0.2 - An entry point to the DOM and server renderers for React
* [react-infinite-scroll-component](https://www.npmjs.com/package/react-infinite-scroll-component) v6.1.0 - An infinite scroll component for React - this library improved user experience by allowing users to continue scrolling to load more content, rather than having to navigate to another page and wait for the page to load
* [react-router-dom](https://www.npmjs.com/package/react-router-dom) v5.3.0 - Contains bindings for using React Router in web applications
* [react-scripts](https://www.npmjs.com/package/react-scripts) v5.0.1 - Scripts and configuration used by Create React App
* [react-spinners](https://www.npmjs.com/package/react-spinners) v0.13.8 - A collection of loading spinners with React.js based on Halogen. This library enhanced the user experience by providing a visual loading spinner to display to the user when content is loading, so they are not left looking at a blank page
* [web-vitals](https://www.npmjs.com/package/web-vitals) v1.1.2 - A modular library for measuring all the web vitals metrics on real users
* [eslint](https://www.npmjs.com/package/eslint) v8.41.0 - A tool for identifying and reporting on patterns found in ECMAScript/JavaScript code
* [eslint-plugin-react](https://www.npmjs.com/package/eslint-plugin-react) v7.32.2 - React specific linting rules for eslint
* [msw](https://www.npmjs.com/package/msw) v0.35.0 - A seamless REST/GraphQL API mocking library for browser and Node.js
* [tailwindcss](https://www.npmjs.com/package/tailwindcss) v3.3.2 - A utility-first CSS framework for rapidly building custom user interfaces. I decided to work with the tailwind library rather than bootstrap because I am a big fan of the tailwind utility framework and I am very familiar with using it in a professional environment. I personally feel that it has more flexibility than bootstrap and allows for further customisation of elements. Using this framework increased my productivity throughout the project

[Back to top](<#contents>)

# Deployment
# **DEPLOYMENT PROCCESS**

**Log in Github.**

Open the repo to deploy.<br>
The one for the site is [here](!https://github.com/IvetteMcDermott/SebsStoreToys)

Steps to use this repository:

- Access to the repo in GitHub [here](https://github.com/IvetteMcDermott/SebsStoreToys).
- It can be "Fork" following the steps [here](../readme_imgs/).
- It can be "Clone" following the steps [here](../readme_imgs/).


**Log in Heroku.**

1. Click in the "New" button in the top right.
2. Select "Create New App"
3. Give a name to the App and choose a region.
4. Click in "Create App" button.
5. Click in Settings.
6. Click in Reveal Config.
7. Add Vars Config (keys):
   For this project had been need as ss below <br>

![heroku-vars](../readme_imgs/heroku-vars.jpg)

8. Go to Deploy in the nav bar. In Deploment Method, select GitHub/Connect to GitHub.
9. In Connect to GitHub, write the repository name and click in search.
10. Once the route for the repo appears under the search, click in "Connect" button.
11. The deployment can be Manual or Automatic, select the one of your preference. Automatic has the advantage of updating your deployed site as you push the commit in GitHub.
12. Verify that "Branch to deploy" is master/main.
13. Click Deploy.

![first](../readme_imgs/ss-rocket-heroku-first-time.png)


## **Getting the variables for Heroku config vars.**

**Log in Stripe.**

1. In the dashboard click developers.
2. Click in API keys.
3. Copy the Publishable Key and add it as variable to the env.py and set the variable for it in settings.
4. Repeat the point 3 with Secret Key.
5. Click in webhooks.
6. In the right side can be found the "Add Endpoint", click on it.
7. Follow the instructions to add the url + '/checkout/wh'
8. Select the listener events and save it.
9. Repeat step 3 with this new key.<br>
   This will become our STRIPE_WH_SECRET variable. <br>
   In total with the previous three, our project will have 3 related to Stripe. These will go to Heroku config vars.

![stripe](../readme_imgs/stripe-dashboard.png)


**Log in GMail (the one used for this project).**

1. In Config Vars set the EMAIL_HOST_USER variable with the email used for the project.
1. Go to settings of Google Account for the mail from step 1.
2. Search for App Password, and click in the one in Security.
3. Follow the instructions to select the device and generate the password.
4. Copy the App Password generated, add it to config vars as EMAIL_HOST_PASS.

![](/readme_docs/readme_imgs/app-password.png)


**Log in MailChimp.**

1. Go to your profile.
2. Go to extras/API Keys.
3. Copy the API Key and do like done for Stripe ones, adding them to env.py and the varible in settings.
4. Go to audience, follow the steps and create an audience list.
5. Now to get the audience list id. Go to the your audience settings, and copy the Audience ID.
6. Treat the Audience ID as a key, include it in env.py and settings.
6. Include a html form code for the subscription with mailchimp in your app, mailchimp provides few options for.
7. These 2 variables will go heroku vars as well.

![mailchimp](../readme_imgs/mailchimp-dashboard.png)


**Log in Cloudinary.**

1. Go to settings.
2. Go to Access Keys.
3. Copy the API Secret Key and do like done for Stripe ones, adding them to env.py and the varible in settings.
4. Set the directories for it in settings, according to what it will be use for.
5. This key will also go heroku vars.

![here](../readme_imgs/cloudinary-settings.png)


**Log in ElephantSQL.**

1. Select the instance for this project.
2. In the details page, an API access section can be found where the one can be copy.
3. One more time, do same steps for previous Keys in env.py and to settings.
4. Add this key to heroku vars also.

![here](../readme_imgs/elephant-dashboard.png)


**Django Key.**

You can find this one in your settings file in the project, remember to protected it and set it as the previous ones in env.py and variable in settings before commiting or you would need to generate a new one and do the mentioned steps.<br>

The Django Key generator can be found [here](https://djecrety.ir/).

## Project Deployment via Heroku

1. Create a new repository on [GitHub](https://github.com/)

2. Name the repository

3. Click the Gitpod button to open the new repository in [GitPod](https://www.gitpod.io/)

4. Once the IDE has loaded, run the terminal command `npx create-react-app . --use-npm` to install React 

5. After it has finished installing run the command `npm start` to check the app is working

6. Add a Procfile in the root directory

7. Add the following code into the Procfile - `web: serve -s build`

8. In the root package.json file in the scripts section, add the following code - `"heroku-prebuild": "npm install -g serve"`

9. Git add, commit and push changes to GitHub

10. Log-in or sign-up to [Heroku](https://dashboard.heroku.com/) and open the dashboard

11. Click on the 'New' button to add a new app

12. Name the app (it must be unique) and choose a region closest to your location

13. Click the 'Create app' button to create the app

14. Once the app is created, click the deploy tab on the app menu

15. Scroll down to deployment method and click the GitHub option

16. Make sure your profile is selected and search for the React GitHub repository name

17. Once the correct repository appears below the searchbar - click the 'Connect' button

18. Once the repository is connected, click the 'Deploy branch' button - make sure the master / main branch is selected

19. Optional - view the build logs as the app builds

20. If the build is successful, click the 'Open app' button to view the deployed app on Heroku

[Back to top](<#contents>)

# Credits

In this final section, I would like to credit the various sources that were used throughout the development of the Gear Addict project.

[Back to top](<#contents>)

## Content

* Dummy rig text copy was sourced from various posts across the [Instagram](https://www.instagram.com/) platform
* My mentor at Code Institute [Martina](https://www.linkedin.com/in/martinaterlevic/) provided much appreciated guidance on application features and content

[Back to top](<#contents>)

## Media

* Dummy image post content was sourced from various posts across the [Instagram](https://www.instagram.com/) platform
* The Gear Addict logo was created by [Anna](https://www.linkedin.com/in/anna-appleton-claydon-ba10a215/) at [We Create Digital](https://wecreate.digital/)
* Page header images were acquired from [Shutterstock](https://www.shutterstock.com/)
* Other assorted image content was acquired from [Adobe Stock](https://stock.adobe.com/uk/)

[Back to top](<#contents>)

## Code

* Code Institute's Advanced Front-end [Moments](https://moments-ci-react.herokuapp.com/) walkthrough project was used as an inspiration and template for this project. Code from the Moments application was customised and expanded on to create further features and functionality for Gear Addict.

[Back to top](<#contents>)

# Acknowledgements

This application was created as a final portfolio project submission for the Code Institute Higher National Diploma in Software Development. The course has lasted a year and has consisted of five major projects spread out throughout the year. It has been a very intense but rewarding year and I couldn't be more thankful to the Code Institute team for making my re-entry back into education a great experience. I have learnt more than I thought was possible over the last year, and I have fallen in love with my career and the tech industry. I am now working full time as a developer and I am happy to say, I do really love my job. 

I would like to take this opportunity to thank everyone who has encouraged and supported me over the last year. It has certainly been a challenging year, but I wouldn't change anything. Thank you very much to Code Institute for helping and supporting career changers like myself to get into the tech industry. Thank you to my incredibly talented mentor [Martina](https://www.linkedin.com/in/martinaterlevic/) for all your help and advice with the last project. Thank you to the Slack community for guidance and support and allowing me to occasionally vent my stress in an understanding and empathetic environment! Finally, thank you to my family and my incredibly patient girlfriend for your belief in me and encouragement to pursue my aspirations. I love and appreciate you all.

Best wishes and happy coding,

Matthew Hobbs-Hurrell

[Back to top](<#contents>)