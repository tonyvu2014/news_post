<a href="https://badge.fury.io/py/scikit-learn"><img alt="Python27" src="https://camo.githubusercontent.com/352488c0cbba0e8f6da11ae0761444dd0c93489c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d322e372d626c75652e737667" data-canonical-src="https://img.shields.io/badge/python-2.7-blue.svg" style="max-width:100%;">
</a>

# news_post
An app to retrieve latest news from popular online portals and post to your social media walls

This app allows you to retrieve latest news from popular technology news portals and then you can share on your LinkedIn wall.


##To  run with virtual environment:


1. Install pip and set up the virtual environment

2. Install dependencies with pip: `pip install -r requirements.txt`

3. Follow these steps to set up your LinkedIn client_id, client_secret, redirect_uri and access_token
   update the api_config.json with your api information
   
   https://developer.linkedin.com/docs/oauth2

4. Update feed_config.json with list of all news feed url that you want to feed and list of category that you want to subscribe to.

5. Start the flask app with `gunicorn app:app`, then go to `localhost:8000` to see the app

   or you can start the app with supervisor `supervisord -c conf/supervisord.conf`

##To run with Docker

1. From the root folder, run `docker build -t news_post .` to build the docker image

2. Run `docker run -p 8000:8000 -i -t news_post`

3. Open the app at `http://<docker-machine-ip-address>:8000`

   _Note: To find out the docker machine ip address you can use command `docker-machine ip default`_




 

