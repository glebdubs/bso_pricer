import streamlit as st
import numpy as np
from scipy.stats import norm

st.set_page_config(
  layout="wide",
  page_title="Black-Scholes Option Pricer",
  page_icon="🫃",
  initial_sidebar_state="expanded"
)


st.html('''
<style>
.metric-box {
    width:100%;
    height:100px;
    background-color: #296317;
    border:solid;
    border-width:thick;
    color:black;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    border-radius:12px;
</style>''')


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


stockPrice = st.sidebar.number_input("$S_{o}$ - current stock price:", value=100)
exercisePrice = st.sidebar.number_input("$X$ - exercise price:", value=110)
rfir = st.sidebar.number_input("$r$ - risk-free interest rate:", step=0.01, value = 0.05)
ttr = st.sidebar.number_input("$T$ - time to expiration (*years*):", value=1)
vol = st.sidebar.number_input("$σ$ - volatility: ", value=0.2)

d1 = ( np.log( stockPrice / exercisePrice ) + ttr * (rfir + ( pow(vol, 2) / 2) ) ) / (vol * np.sqrt(ttr))

d2 = ( np.log( stockPrice / exercisePrice ) + ttr * (rfir - ( pow(vol, 2) / 2) ) ) / (vol * np.sqrt(ttr))

callPrice = stockPrice * norm.cdf(d1) - exercisePrice * np.exp( - rfir * ttr) * norm.cdf(d2)

putPrice = np.exp(-rfir * ttr) * exercisePrice * norm.cdf(-d2) - stockPrice * norm.cdf(-d1)


st.title("▲ Black-Scholes Option Pricing Model")
st.markdown("Using the formulas for _**european**_ options, this tool takes in given properties of an option and returns the appropriate call and put prices.")

st.divider()
col1, col2 = st.columns([0.5, 0.5], gap="medium")

with col1:
  st.info("Formula for black-scholes pricing of a european **call option**:")
  st.latex('''
P_{c} = S_{o}N(d_{1})-Xe^{-rT}N(d_{2})
           ''')
  st.info("Formula for black-scholes pricing of a european **put option**:")
  st.latex('''
P_{p} = e^{-rT}XN(-d_{2})-S_{0}N(-d_{1})
           ''')
  st.info("What all the letters are: ")
  cola, colb = st.columns([0.3, 0.7], gap="small")
  with cola:
    st.latex("S_{o}")
    st.latex("X")
    st.latex("r")
    st.latex("T")
    st.latex("σ")
    st.latex("N(a)")
    st.write("")
    st.write("")
    st.latex("d_{1}")
    st.write("")
    st.write("")
    st.latex("d_{2}")
  with colb:
    st.write("")
    st.html('<div style="text-align: center">stock price</div>')
    st.write("")
    st.html('<div style="text-align: center">exercise price</div>')
    st.write("")
    st.html('<div style="text-align: center">risk-free interest rate</div>')
    st.write("")
    st.html('<div style="text-align: center">time to expiration</div>')
    st.write("")
    st.html('<div style="text-align: center">volatility</div>')
    st.html('<div style="text-align: center">integral of a normal distribution from -∞ to <i>a</i></div>')
    st.latex(r'''= \frac{ln(S_{o}/X)+T(r+\frac{\sigma^{2}}{2})}{\sigma \sqrt{T}}''')
    st.latex(r'''= \frac{ln(S_{o}/X)+T(r-\frac{\sigma^{2}}{2})}{\sigma \sqrt{T}}''')

with col2:
    st.html(f'''
    <div class="metric-box", style="border-color:#87cf72;">
        <p style="margin:1px"></p>
        <p style="margin:0px;color:#87cf72"> CALL Value </p>
        <h1 style="font-size:45px;margin:0px;font-weight:bolder;color:#87cf72;margin-top:-15px">${callPrice:0.2f} </h1>
    </div>''')
    st.html(f'''
    <div class="metric-box", style="background-color: #420b0b; border-color: #de6464;">
        <p style="margin:1px"></p>
        <p style="margin:0px;color:#de6464;"> PUT Value </p>
        <h1 style="font-size:45px;margin:0px;font-weight:bolder;color:#de6464;margin-top:-15px">${putPrice:0.2f} </h1>
    </div>''')