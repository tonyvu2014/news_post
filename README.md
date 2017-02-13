<a href="https://badge.fury.io/py/scikit-learn"><img alt="Python27" src="https://camo.githubusercontent.com/352488c0cbba0e8f6da11ae0761444dd0c93489c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d322e372d626c75652e737667" data-canonical-src="https://img.shields.io/badge/python-2.7-blue.svg" style="max-width:100%;">
</a>

# news_post
An app to retrieve latest news from popular online portals through feeds.

This app allows you to configure categories and feeds to retrieve latest news from popular news portals.

The technologies used are:

- python 2.7
- flask 0.11.1
- redis 2.10.0
- gunicorn 19.6.0 
- twitter bootstrap
- font-awesome 


##Usage

1. Go to category to add/remove category that you want to subscribe to

2. Go to feed to add/remove feed url that you want to get the news from

3. Go to homepage to see the latest news

4. From homepage, click on `Update News` to refresh the page 


##To  run with virtual environment:


1. Install pip and set up the virtual environment

2. Install dependencies with pip: `pip install -r requirements.txt`

3. Go into virtual environment

5. Start the flask app with `gunicorn app:app`, then go to `localhost:8000` to see the app

   or you can start the app with supervisor `supervisord -c conf/supervisord.conf`

##To run with Docker

1. From the root folder, run `docker build -t news_post .` to build the docker image

2. Run `docker run -p 8000:8000 -i -t news_post`

3. Open the app at `http://<docker-machine-ip-address>:8000`

   _Note: To find out the docker machine ip address you can use command `docker-machine ip default`_




 

