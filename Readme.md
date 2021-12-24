## Streamlit app

dashboard.py - this is the main file that has the Streamlit App
It has a Side Navigation Bar that has three Options:

- StockTwits: Just API calls to 'stocktwits' using Stock Symbols and printing the results
- LocalDataFrame: Using "Tips" data from seaborn datasets and showing some data
- Twitter: Calling Twitter APIs and getting tweets and displaying them


config.py
----------
This has important properties that you need for Twitter integration, you have to provide "TWITTER_BEARER" (Auth Bearer Token) to call Twitter v2.0 APIs
If you dont have a Twitter developer account, creating a new one and getting the key is simple, it would hardly take 15-20 minutes.

I had to get the Twitter User's userid by calling another API. I have removed that step in this code by creating a list of userid.



<P>
References:
<br>
------------
<br>
https://www.youtube.com/watch?v=0ESc1bh3eIg
<br>
https://developer.twitter.com/en/docs/tutorials/explore-a-users-tweets
</P>

