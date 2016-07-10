# news_post
An app to retrieve latest news from popular online portals and post to your social media walls

This app allows you to retrieve latest news from popular technology news portals and then you can share on your LinkedIn wall.

To set up:

1. install python, pip and virtualenv in your local environment

2. clone the project

3. set up virtual environment

4. install dependencies with pip: `pip install -r requirements.txt`

5. follow these steps to set up your LinkedIn client_id, client_secret, redirect_uri and access_token
   update the api_config.json with your api information
   
   https://developer.linkedin.com/docs/oauth2

6. update feed_config.json with list of all news feed url that you want to feed and list of category that you want to subscribe to.

7. start the flask app with `python app.py`, then go to `localhost:5000` to see the app


 

