import streamlit as st
import numpy as np
from scipy.stats import norm



st.set_page_config(
  layout="wide",
  page_title="Black-Scholes Option Pricer",
  page_icon="🫃"
)

st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 300px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 300px;
        margin-left: -300px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar content
st.sidebar.title("Option Properties")
st.sidebar.divider()
st.sidebar.markdown("\n")

stockPrice = st.sidebar.number_input("current stock price:", value=100)
exercisePrice = st.sidebar.number_input("exercise price:", value=110)
rfir = st.sidebar.number_input("risk-free interest rate:", step=0.01, value = 0.05)
ttr = st.sidebar.number_input("time to expiration (*years*):", value=2)
vol = st.sidebar.number_input("volatility (σ): ", value=0.1)

d1 = ( np.log( stockPrice / exercisePrice ) + ttr * (rfir + ( pow(vol, 2) / 2) ) ) / (vol * np.sqrt(ttr))

d2 = ( np.log( stockPrice / exercisePrice ) + ttr * (rfir - ( pow(vol, 2) / 2) ) ) / (vol * np.sqrt(ttr))

callPrice = stockPrice * norm.cdf(d1) - exercisePrice * np.exp( - rfir * ttr) * norm.cdf(d2)

putPrice = np.exp(-rfir * ttr) * exercisePrice * norm.cdf(-d2) - stockPrice * norm.cdf(-d1)


st.title("▲ Black-Scholes Option Pricing Model")
st.markdown("Using the formulas for _**european**_ options, this tool takes in given properties of an option and returns the appropriate call and put prices.")

st.divider()
col1, col2 = st.columns([0.5, 0.5], gap="medium")

with col1:
  st.markdown("Formula for black-scholes pricing of a european **call option**:")
  st.latex('''
S_{o}N(d_{1})
           ''')