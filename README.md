# Web-project
Food for all web application 

Description: 
The website is designed to provide a platform for redistribution of excess food and leftovers in households and different functions. Once the user has signed up successfully, he/she can donate food by informing the concerned team through the website, which automatically recognizes the location. We keep a track of each and every activity of the user with the help of a database. We also provide an interface for the user to help with personalized diet suggestions based upon his age and health conditions.

We used django stack for building the application. HTML, CSS, JavaScript, Bootstrap for building front end postgresql in the backend for database. 

Home Page:
The website opens up with a well designed home page. We included a few articles on food donations going on over the globe, malnutrition and its effects on the humans. Also the main motive of the website depicting the importance of food donations, making proper use of the leftovers at various functions and households, how important it is to achieve zero hunger, a step towards sustainable development. We also dynamically display the stats namely number of current users, number of food donations done through the website and total amount of  money donated. We also provided all kinds of communication to reach out to the team anytime.  

One can navigate to login, donate food, personalize diet from the home page using the links provided in the home page. 

Home.html for the html page and style.css for stylesheet of the home page.


Login Page:
An existing user can login using his email address which is authenticated and the individual password. New users can click on the sign in option to register for the app. The user can authorize the local storage whether to remember the credentials or not. In case if the user has forgotten his password, he/she can click on the forgot password option, a link will be sent to the particular authenticated email address and the user can set his new password.

Login.html, stylesheet.css for the page implementation.





Register Page:
 A new user can register with his valid email address, phone number, password and username. A verification link will be sent to the email address the user has registered with. A user cannot donate food until he successfully logged in. On successful registration the user is redirected to the login page. An existing user can also navigate to the login page.

login.html, style.css  for the page implementation.

Donate Food Page :
 Users can donate food after filling the food details, quantity, date and time of preparation. The major accomplishment of the application is it can automatically recognize the user location using GPS. Once the person has successfully submitted the details, the data is stored in the database and food details are printed for the sake of the user to view and after thanking the user it is directed back to the home page.

donate.html, donate.css  for the page implementations.

Profile Page:
 A user can view his/her profile by navigating to the profile page from the home page which is visible to the user only after the successful login of the user. The profile page includes username, first name, last name, email address, the number of donations he/she made and the total amount of money donated giving the user a clear view of all the donations he/she made till date maintaining logs for each and every donation in the database. A user can navigate to donate, personalize diet or log out of the website or go back to the home page from the profile based upon his interest. A user can make any number of donations he/she wishes to do.

profile.html, profile.css for the page implementation.

Diet page:
A user can get personalized health suggestions by filling the form based upon age, health conditions and other crucial things. We only included the basic layout of the form in the release one. We are working hard on coming up with the best dynamically suited personalized diet for the users taking all their health conditions into consideration in the second release. We made an attempt to show how important it is to maintain  a perfect balanced diet to avoid malnutrition and other health problems for our users.


 As we know health is  more important than anything for a human being to live a long life, taking food that suits his health condition is also one of the crucial things to be done. We provided this for the users irrespective of their login status. A user need not necessarily login to view his personalized diet. He/she just needs to fill the form asking his/her details and can view the personalized suggestions we provide based on health conditions in the second release. We just provided a little taste of it in the first release.

diet.html, diet.css for the implementation of diet page.


