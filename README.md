# Headlines

Python Application to retrieve headlines from multiple news sources. This uses the News API(https://newsapi.org/), and is modeled after Apple News app, that aggregates and displays articles from selected news sources. In it's current state, this application has the basics for creating a simple Headlines/News Dashboard with a front of tool like Angular, and further expanded with building in user registeration and user preferences with MYSQL and further Python functionality built in.

Setup
-------
First, you must visit https://newsapi.org/, to sign up for an account. Once signed up, you will provided with an api key, that you then must use to set in the config.py file. Also in the config file set the app_url variable to the root url the application will reside. Once your key and app_url are set, navigate to the news folder and run "chalice local" to launch the application.

Navigate to the news folder and run 'pip install -r requirements.txt' to install required packages into your enviroment. Then run 'chalice local' to launch the app locally.

There are two endpoints to the application:

The first, 'GET /sources/{category}', returns a list of available top news sources, and can be filtered based upon the category you pass into the url. the category param can be left blank, as by default the News API will return will all avaliable resource from the 'https://newsapi.org/v1/sources?language=en' endpoint. If a category, the enpoint that is hit will be 'https://newsapi.org/v1/sources?category={category}&language=en', no api key required. 

Valid categories are business, entertainment, gaming, general, music, politics, science-and-nature, sport, and technology. Upon success, a list of sources will be returned including the name, description, and url of the news source. If you pass in an incorrect value you will be presented with a 404 and a message with a list of accepted params. Currently the url values are incomplete as I was not able to retrieve the application root url to prepend to the field value, which would result in an internal application value that ties directly into the second endpoint.

The second endpoint is 'GET /source/{source_id}', displays up to 10 of the latest or top articles from the specified news source. Example external call example, 'https://newsapi.org/v1/articles?source=the-next-web&sortBy=latest&apiKey=apiKey', and requires an api key for this call. News source id's can be retrieved from the previous '/sources/{category}' endpoint. 
