
Authorization looks familiar? The login and registration functionalities are adapted from the [Flaskr Tutorial](http://flask.pocoo.org/docs/1.0/tutorial/).

Organization of the app:

*app.py. is the main program*
- Blueprints allow for something to replicated easily. While this is not significant for a small application like this kanban board, it is useful for larger projects. Blueprints are used in the app.py and the auth.py files, and are referred to by the decorator via @bp.route('/') .
- Each function is decorated with a @login_required. This function is imported from the auth.py file, and requires a user to be logged in to continue. If no user is logged in, it redirects to the auth/login.html page.
- See comments about particular functions in the app.py file itself.

*auth.py handles registration and login*
- When a user registers, uniqueness of username is ensured and a hashed password is stored in the database.
- When a user logs in, the hashed password is verified against the database.
- a 'g' variable provides application context, and in this case saves the logged in user in the session (via Cookies). This helps the app run more smoothly as it can quickly verify a logged in user. The session clears after a logout.

*db.py sets up the database*
- Functions to initiate the database, get the database and close the connection.
- Initiates the database based on the schema.sql file.
- *flask init-db* has to be run in the terminal before running the app

*schema.sql defines the structure of the database*
- user table: id (primary key), username (unique), password (hashed)
- task table: id (primary key), user_id (foreign key to user), created (timestamp), body, category, deleted

*Templates store the html files*
- The base.html provides the register and login bar on the top, which persists throughout any pages clicked.
- The auth/login.html and auth/register.html show login or registration functionalities (username and password).
- The app/home.html file is the main page that shows the kanban board and tasks to do.
- This design allows to flexibly add more pages where necessary while adhering to a basic core structure.

*Static stores css and images*
- The style.css provides the styling to the authorization components as well as the kanban board.
- The bugs.jpg might be the most important component of this project, as its sole purpose is to lighten up the user's day.
