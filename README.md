# news_post
An app to retrieve latest news from popular online portals and post to your social media walls

This app allows you to retrieve latest news from popular technology news portals and then you can share on your LinkedIn wall.


##To  run with virtual environment:


1. install pip and set up the virtual environment

2. install dependencies with pip: `pip install -r requirements.txt`

3. follow these steps to set up your LinkedIn client_id, client_secret, redirect_uri and access_token
   update the api_config.json with your api information
   
   https://developer.linkedin.com/docs/oauth2

4. update feed_config.json with list of all news feed url that you want to feed and list of category that you want to subscribe to.

5. start the flask app with `python app.py`, then go to `localhost:5000` to see the app

##To run with Docker

1. From the root folder, run `docker build -t news_post .` to build the docker image

2. Run `docker run -p 5000:5000 -i -t news_post`

3. Open the app at `http://<docker-machine-ip-address>:5000`




 

