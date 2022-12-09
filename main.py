import pandas as pd
import streamlit as st
import yfinance as yf

st.title('Lit Finance Dashboard')

tickers = ('TSLA', 'AAPL', 'MSFT', 'BTC-USD', 'ETH-USD')

dropdown = st.multiselect('Pick your assets', tickers)

start = st.date_input('Start', value=pd.to_datetime('2021-01-01'))
end = st.date_input('Start', value=pd.to_datetime('today'))


def relativeret(df):
    rel = df.pct_change()
    cumret = (1 + rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret


if len(dropdown) > 0:
    df = relativeret(yf.download(dropdown, start, end)['Adj Close'])
    st.header(f'Return of {dropdown}')
    st.line_chart(df)
