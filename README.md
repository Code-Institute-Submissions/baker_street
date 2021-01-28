# Baker Street Escape Room Adventures
* This site is for a fictional escape room (these are 'puzzle rooms' where you go in as a team and have to race the set timer to complete all of the challenges or puzzles and 'escape' in the alloted time) that has a Sherlock Holmes theme. Customers will be able to view the an explanation as to what an escape room is, the available rooms, their available dates and times and be able to book these time slots.
## UX
* This site is aimed at people who are experienced escape room players and for people who have never played one before and may not know what they are.
### User Stories
* As a customer I want to be able to easily navigate the site so that I can enjoy my experience on the website
* As a customer I want to be able to see what products the escape room has to offer so that I can decide if I would like to visit.
* As a customer I want to be able to see individual escape room challenges in more detail so that I can decide which one I like the best.
* As a customer I want to be able to view the escape room experience options and available dates and times so that I can book an escape room experience on the date and time I would like.
* As a customer I want to be able to easily pay for my selected option so that I can decide if I would like to visit.
* As a customer I want to be able to see what products the escape room has to offer so that I can visit the escape room by paying online in advance.
*  As a customer I want to recieve an email when I have completed my booking so that I know that my booking was successful and be reminded of the time and date of my booked expeirence.
* As a customer I want to be able to register an account so that I can access the areas only those with accounts can access, view my info.
* As a customer I want to recieve an email once I have registered for my account so that I know the registration ws successful.	
* As a customer I want to be able to easily login and out of my acount to see my personal info, past/future bookings. See my score/time from previous visits
* As a customer I would like to see a leaderboard so I can see what times other teams got so that I can compete with them
* As a  member of staff I want to be able to Login and logout so that I can change available times, cancel/amend bookings and complete other administrative duties.

## Features
### Navbar - This allows the user to easily navigate the site with single clicks. I feel that each list item in the navbar gives a good indication o what is to be expecting of the page it links to.
* Home and 'logo links- both link to the 'Home' page which gives the user general information about the service provided, who it is aimed at and an FAQ section.
* Our Rooms page- Gives a description of the backstor of each room and provides a button which links to that rooms individual booking page.
* Book Now booking pages- Allows the user to book the selected room chossing a number of players, date and time they wish to play. Once complete the user can submit their choices and is taken to the next stage of the booking process which is to put in their personal details and card information.
* Leaderboards page- This shows the user the top 3 best times that previous teams have completed each room in. This is editable from the admin page.
In this section, you should go over the different parts of your project, and describe each in a sentence or so.
* Contact Us page- Page with contact info and opening hours for users. I have also added a map using google maps api- see below.
* Log In page- Not yet functional

### Google Map
* I added a Google map to the contacts page as it is something a customer would expect when booking to visit a location. The address itself is fake but is on Baker Street in Ballincollig as it states on the contact page. This choice was a nod to the name of the Escape Room and also a viable rough location if this was for a real escape room.
* ~~Currently the map does not function perfectly. While you can still see the map fairly well, it is greyed out and has a 'for development purposes only' watermark.~~ This issue was caused by not having my env variable set properly and then not changing the var name in the view when it was changed in settings and in the contact.html file.

### Login/Register
* This feature was setup using Allauth which was downloaded through the terminal. I edited the allauth templates so that they would suit the styling of the rest of the site.
* 
## Design

### Site theme   
* The original idea for doing a site based on an escape room came from working in one myself a few years ago. As for a Sherlock Holmes theme, that from recently watching a Sherlcok Holmes series and the title of the escape room part from being where the character lived, it is also my last name.
* Due to the choice of theme for the escape room, I wanted to give the site a Victorian look. This is why I have chosen the parchment background throughout and use Calligraffitti as the main font family as I felt it has the look of handwritting which suits the era as there were no computers. 

### Font family
* I found that Calligraffitti font suited the site well for it's theme whilst also being easy to read. During testing I found that changing the general-text which is everything but the headers and sub headers to black improved readability across the site. Beacuse of the main background the red colour could be difficult for some.
* I also chose to bolden the navbar and navbar dropdown text on hover to make it easier for the user to discern what their pointer is focused on.

### Colour scheme
* I chose a deep red (#8D0424) as the main colour for the headers and footers as I felt that it gave a plush feel and complemented the main background image. It also allowed the text in the navbar to stand out well. I used the same colour throughtout for the text to stay with a simple colour pallet and also because I felt it was easy to read against the background image.
* For  standalone buttons on the site, I chose Bootstraps 'danger' class for colour so they would still be in keeping with the rest of the sites colour scheme whilst being different enough to stand out.
### Background
* I originally decided to use a dirty white/ cream colour for my background as I felt it complimented the sites theme and would contrast nicely with the red and black. When searching for potential background images I settled upon parchment-background.jpg as I thought it's textured look and colour fitted the theme nicely and also worked well with the main colours I had chosen the navbar and text.

### Images
* I had originally envisioned 'Sherlock' related images of a deer stalker hat, magnifiying glass etc for the three rooms. However, when looking online, many of the images were either not appropriate or were too different in style, I couldn't find three that went nicely together. That is why I decided to use another parchment background with writting on them as if they were a note. This also tied in nicely with the game rooms themselves as all three rooms have a note or message as per their description. 

## Deployment
 * I chose to use Heroku to deploy my site. Deployed site- https://baker-street-escaperoom.herokuapp.com/
 * To do this I logged into Heroku my account, created   the app and connected it to my GitHub repository directly through Heroku. As Heroku dos not deal with static files I set up an account with Amazon Web Services to handle these. 
 * Within AWS(Amazon Web Services), I used the S3 service and created a 'bucket' to store my files and named it the same as my heroku app, setting the region of er-west-1, unblocked Public Access and then created the bucket. I turned on static website hosting in the proporties tab. In the permissions tab, I pasted in a CORS configuration provided by Code Institue which sets up the access between my Heroku and this bucket. I had to create a security policy using the AWS policy generator. Finally, in the Access Control List tab and set the list objects permission to Everyone.
 * I need to create a user to access the created bucket, using IAM(Identity and Access Management). I created a group for the user to live in, then an access policy granting the group access to the S3 bucket and then create the user and assign them to the group to use the policy to access the static files.
 * To connect django to the S3 bucket, I installed boto3 and django-storages and added storages to seetings.py installed apps. I set up an if statment in settings.py to only use the AWS keys that had been set as config vars in Heroku, on the Heroku app. 
 * AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com' tells django where the static files are coming from.
 * Here is a link to my GitHub repo- https://github.com/NickBaker11/baker_street
 
## Testing 
#### As part of my testing I will use the User stories as a base
1. As a customer I want to be able to easily navigate the site so that I can enjoy my experience on the website.
  * To test the navigation of my site, I manually clicked on each desired link to see if it would take me to the kind of page I desired. I also asked friends to take themselves through the site to test navigation and they found it a smooth experience.
2. As a customer I want to be able to see what products the escape room has to offer so that I can decide if I would like to visit.
  * Click into Our Rooms on the navabar. The user is taken to Our Rooms page which gives a backstory to each of the three rooms or products that the site offers.
3. As a customer I want to be able to view the escape room experience options and available dates and times so that I can book an escape room experience on the date and time I would like.
 * Click into Our Rooms on the navabr and select the desired room or select the desired room from the three choices in the Book Now dropdown in the navbar. 
 * Once the user has chosen the desired room, they can go into the date and time dropdowns which will show what is available. 
4. As a customer I want to be able to easily pay for my selected option so that I can decide if I would like to visit.
   * Click into Our Rooms on the navabr and select the desired room or select the desired room from the three choices in the Book Now dropdown in the navbar. 
  * Select a choice from each of the three options, number of players, date and time then hit submit. If any of the forms are not filled in and you hit submit, a warning will pop up asking you to fill out the incomplete field. With all fields filled, hit submit.
  * You are then taken to the checkout page. You have to fill in each form section. Currently, if you hit submit the form will not go through, however, there is no warning box for the specific form line not filled in. Once all of the form lines are filled in and you hit submit, the form posts and the user is taken to the success_checkout page which currently has a short message saying an email will be sent to the one the user input into the form.
5. As a customer I want to be able to register an account so that I can access the areas only those with accounts can access, view my info.
 * Click on 'Login' in the navbar, click on 'Register' in the dropdown. Fill in the form with the requested details and hit 'Sign Up'.
 *  As a customer I want to recieve an email when I have completed my booking so that I know that my booking was successful and be reminded of the time and date of my booked expeirence.
6. As a customer I would like to see a leaderboard so I can see what times other teams got so that I can compete with them
 * On the navbar, click on the 'leaderbords' link. This bring the user to the Leaderboards page that shows the 3 best scroes for each room. Of course, this not being a real escape room, these times are made up.
* As a customer I want to recieve an email once I have registered for my account so that I know the registration ws successful.	
* As a customer I want to be able to easily login and out of my acount to see my personal info, past/future bookings. 

## Technologies used
* Bootsrap is used throughout the site, mainly assisting with layout grids and breakpoints. https://getbootstrap.com/docs/5.0/getting-started/introduction/
* Stripe is used for the ecommerce, allowing users to proccess a fake card payment. https://stripe.com/en-ie

## Features to implement in the future
* 

## Issues

## Credits
### Content

### Media
None of the images used are my own
* sherlock-holmes-shadow.jpg is from https://www.history.com/news/was-sherlock-holmes-based-on-a-real-person
* watson!_img.jpg, study_in_pink_img.jpg and moriarty_img.jpg all use the same background which is taken https://www.pinterest.co.uk/pin/839288080541763732/. The text overwritten was done by myself using the program Paint 3D
* I did not write in the location where I found this image initally and now cannot find it -parchment-background.jpg . This image is not my own and was taken from a now unknown source online.

### Acknowledgements
* Code Institues Boutique Ado provided lots of guidance on this project in terms of how to lay things out, what downloads were needed to make certain thing work such as AWS, and how to set up Stripe.

This project is for educational purposes only.