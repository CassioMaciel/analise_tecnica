import plotly.graph_objs as go
import yfinance
from datetime import date
def constroi_grafico(acao, data_ini, data_final=date.today()):
    cotacao = yfinance.download(acao,
                               start=data_ini,
                               end=data_final)

    trace = go.Candlestick(x=cotacao.index,
                      open=cotacao.Open,
                      high=cotacao.High,
                      low=cotacao.Low,
                      close=cotacao.Close)
    data = [trace]
    fig = go.Figure(data=data)
    return fig


