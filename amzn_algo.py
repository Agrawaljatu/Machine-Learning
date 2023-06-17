import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.express as px
import yfinance as yf

stock = yf.Ticker("AMZN")
data = stock.history(period="5y")
print(data.head())

data['momentum'] = data['Close'].pct_change()

figure = make_subplots(rows=2, cols=1)
figure.add_trace(go.Scatter(x=data.index,
                            y=data['Close'],
                            name='Close Price'))
figure.add_trace(go.Scatter(x=data.index,
                            y=data['momentum'],
                            name='Momentum',
                            yaxis='y2'))

figure.add_trace(go.Scatter(x=data.loc[data['momentum'] > 0].index,
                            y=data.loc[data['momentum'] > 0]['Close'],
                            mode='markers', name='Buy',
                            marker=dict(color='green', symbol='triangle-up')))

figure.add_trace(go.Scatter(x=data.loc[data['momentum'] < 0].index,
                            y=data.loc[data['momentum'] < 0]['Close'],
                            mode='markers', name='Sell',
                            marker=dict(color='red', symbol='triangle-down')))

figure.update_layout(title='Amazon Momentum Strategy',
                     xaxis_title='Date',
                     yaxis_title='Price')
figure.update_yaxes(title="Momentum", secondary_y=True)
figure.show()