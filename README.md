# Snapgram

> [Brian-Otieno](https://github.com/default-007)

# Description

This is a clone of Instagram where people share their images and videos for other users to view.
Users can sign up, login, view and post photos, search and follow other users.

## Live Link

Click [View Site](https://snapgram-007.herokuapp.com/) to visit the site

## Behavior Driven Development

| Input                                         | Behaviour                                                                                | Output                                                                                                                                 |
| --------------------------------------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| User registers for an account by filling form | Page redirects user to login page                                                        | User is redirected tpo login page                                                                                                      |
| User logs in                                  | User is taken to the home page                                                           | Redirect you to the homepage where the user is greeted with a feed of most recent photos posted                                        |
| User clicks upload button and fills the form  | The page reloads                                                                         | User's new post is displayed on the feed                                                                                               |
| User clicks on the like button                | The page reloads                                                                         | Like count of the post is increased by one value                                                                                       |
| User clicks on the comment button             | User is redirected to a page containing the single post, its comments and a comment form | A page displaring the single post is displayed                                                                                         |
| User posts a comment by filling the form      | The page reloads                                                                         | The new comment is added onto the post's comment section , showing th comment and its author, and comment count is updated in the feed |

## Screenshots

###### Home page

<img src="https://raw.githubusercontent.com/default-007/insta-lite/master/static/images/instagram.png">
 
 ###### user profile
 <img src="https://raw.githubusercontent.com/default-007/insta-lite/master/static/images/profile.png">

## User Story

- Sign in to the application to start using.
- Upload a pictures to the application.
- Search for different users using their usernames.
- See your profile with all your pictures.
- Follow other users and see their pictures on my timeline.

## Setup and Installation

To get the project .......

##### Cloning the repository:

```bash
https://github.com/default-007/Snapgram.git
```

##### Navigate into the folder and install requirements

```bash
cd Snapgram pip install -r requirements.txt
```

##### Install and activate Virtual

```bash
- python3 -m venv virtual - source virtual/bin/activate
```

##### Install Dependencies

```bash
pip install -r requirements.txt
```

##### Setup Database

SetUp your database User,Password, Host then make migrate

```bash
python manage.py makemigrations instagram
```

Now Migrate

```bash
python manage.py migrate
```

##### Run the application

```bash
python manage.py runserver
```

##### Running the application

```bash
python manage.py server
```

##### Testing the application

```bash
python manage.py test
```

Open the application on your browser `127.0.0.1:8000`.

## Technology used

- [Python3.8](https://www.python.org/)
- [Django 2.2](https://docs.djangoproject.com/en/2.2/)
- [Heroku](https://heroku.com)
- HTML5
- CSS3
- Javascript
- jQuery 3.4.1
- Bootstrap 4.3.1
- Font-Awesome
- Restful API

## Known Bugs

- There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information

If you have any question or contributions, please email me at [brianokola@gmail.com]

## License

- [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/default-007/Snapgram/blob/master/LICENSE)
- Copyright (c) 2019 **Brian Otieno**
