import streamlit as st
import pandas as pd
import numpy as np


st.title("Sentiment Analysis of Tweets about US Airlines ✈️")
st.sidebar.title("Sentiment Analysis of Tweets 🤖")
st.markdown("**This dashboard is used to analyze sentiments of tweets** 📊 ")


@st.cache(persist=True)
def load_data():
    data = pd.read_csv('Tweets.csv')
    data['tweet_created'] = pd.to_datetime(data['tweet_created'])
    return data

data = load_data()
st.write(data)