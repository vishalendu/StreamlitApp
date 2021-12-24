import streamlit as st
import pandas as pd
import plotly.express as px
import plotly
import seaborn as sns
import statsmodels
import requests
import tweepy
import config

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

body = st.container()

with body:
    st.sidebar.title("Navigation  Bar")
    st.sidebar.write(f"{'-' * 50}")
    options = st.sidebar.selectbox("Choose Dashboard",('StockTwits','LocalDataFrame','Twitter'))
    match options:
        case 'StockTwits':
            symbol = st.sidebar.text_input("Symbol", value='AAPL', max_chars=5)
            r = requests.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json")
            data=r.json()
            st.title(f'Stock Selected:  {symbol}')
            st.write(f"{'-'*50}")
            for message in data['messages']:
                st.image(message['user']['avatar_url'])
                st.write(message['user']['username'])
                st.write(message['created_at'])
                st.write(message['body'])

        case 'LocalDataFrame':
            st.title('Tips Database')
            st.text('The following data is taken from the sample seaborn dataset')
            df = sns.load_dataset('tips')
            st.dataframe(df)
            fig = px.scatter(df, x="total_bill", y="tip", color="sex", symbol="smoker", size="size", size_max=10,
                             trendline='ols', symbol_sequence=[3, 101], height=800, width=1000,
                             category_orders={'day': ['Thur', 'Fri', 'Sat', 'Sun']})
            st.plotly_chart(fig, use_container_width=True)
        case 'Twitter':
            for userid in config.TWITTER_USERID:
                user = requests.get(f'https://api.twitter.com/2/users?ids={userid}&user.fields=profile_image_url', auth=BearerAuth(config.TWITTER_BEARER))
                tweets  = requests.get(f'https://api.twitter.com/2/users/{userid}/tweets', auth=BearerAuth(config.TWITTER_BEARER))
                user = user.json()['data'][0]
                tweets = tweets.json()['data']
                st.write(f"{'-' * 50}")
                st.image(f"{user['profile_image_url']}")
                st.subheader(f"{user['name']} ({user['username']})")
                for tweet in tweets:
                    st.write(f"{tweet['id']}: {tweet['text']}")


