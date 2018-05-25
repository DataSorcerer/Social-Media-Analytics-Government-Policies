# Social Media Analytics: Government Policies

[Check out the detailed report and source code(Jupyter Notebook)](https://github.com/DataSorcerer/Social-Media-Analytics-Government-Policies/blob/master/Social_Media_Analytics_Report.ipynb) 

<b><font color="blue" size = 3>Objective:</font></b>       
 - Determining the public response to various government policies in Galway based on <b>accessing, integrating and analysing tweets</b> from Local Media house (Newspaper or Radio station) and <b>discussions on Reddit forums</b>. 
 - In other words, the task entails creating <font color="green">structured dataset</font> that captures key information <font color="brown">from free text tweets and comments</font> and use it for analysing peoples' opinion.    
 
<b><font color="blue" size = 3>Key Tasks:</font></b>    
1. Accessing Posts and Comments from Twitter and Reddit     
2. Identifying relevant	posts    
3. Analysis/ Visualization of relevant posts    
    3.1. Gauging policy popularity with Tweet/ Retweet/ Hashtag counts    
    3.2. Policy review based on Reddit submissions and comments counts    
    3.3. <font color="brown">Sentiment Analysis</font> of Tweets and Reddit comments
4. Observations and conclusion    


<b>Files:</b>
1. [Retrieve_Twitter_Data.py](https://github.com/DataSorcerer/Social-Media-Analytics-Government-Policies/blob/master/Retrieve_Twitter_Data.py): Python Script to access tweets from <b>Twitter REST API</b>       
2. [download_reddit_submissions.py](https://github.com/DataSorcerer/Social-Media-Analytics-Government-Policies/blob/master/download_reddit_submissions.py): Python Script to access Reddit submissions and comments    
3. [tweets.json](https://github.com/DataSorcerer/Social-Media-Analytics-Government-Policies/blob/master/tweets.json): Tweets collected in JSON format    
4. [galway-23-03-2018-16-47-27.json](https://github.com/DataSorcerer/Social-Media-Analytics-Government-Policies/blob/master/galway-23-03-2018-16-47-27.json): Reddit posts gathered in JSON format
5. [Policy_Counts.csv](https://github.com/DataSorcerer/Social-Media-Analytics-Government-Policies/blob/master/Policy%20Counts.csv): Summary of tweets and reddit data in a structured CSV format. This file is used for further analysis and visualization.    

<b>Python Packages Used:</b>   
- [tweepy](http://www.tweepy.org/): Access Twitter REST API for tweets       
- [praw](https://praw.readthedocs.io/): Access posts from Reddit discussion forum     
- [textblob](http://textblob.readthedocs.io/en/dev/): Text preprocessing and Sentiment Analysis     
- [pandas](https://pandas.pydata.org/): Useful data structures for analysis in Python    
- [matplotlib](https://matplotlib.org/), [seaborn](https://seaborn.pydata.org/): Data visualization     


