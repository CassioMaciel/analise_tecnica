# -*- coding: utf-8 -*-
"""
author: Cassio Maciel Lemos
E-mail: cassio.lemos@petrobras.com.br

########################################################
                            Uso
Run this app with `python app.py` 
visit http://127.0.0.1:8050/ in your web browser.

########################################################
                    Motivação

Esse código visa criar uma página que gere o grafico 
da ação desejada, de maneira interativa, utilizando
Python e Dash
########################################################
                    Observações
Algumas funções foram buscadas em:
https://dash.plotly.com/dash-core-components/dropdown

"""

import plotly.graph_objs as go
from dash import Dash, html, dcc, Input, Output, callback
import bib_graficos
import yfinance

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Análise Técnica'),

    html.Div(children='''
        Os melhores gráficos para você tomar as melhores
        decisões
    '''),
 
    html.Div(id='Titulo_do_Graf'),
    
    dcc.Dropdown([ 'PETR4.SA' , 'VALE3.SA' , 'BBDC4.SA'], 'PETR4.SA', id='lista_suspensa'),
    
    dcc.Graph(id='grafico_candlestick')
])
            
     
@callback(
    Output('Titulo_do_Graf', 'children'),
    Input('lista_suspensa', 'value')
)
def update_output(value):
    return f'Você selecionou {value}'

@callback(
    Output('grafico_candlestick', 'figure'),
    Input('lista_suspensa', 'value')
)
def update_grafico(value):
    data = bib_graficos.constroi_grafico(value,'2016-10-1','2019-1-1')
    fig = go.Figure(data=data)
    
    fig.update_layout(
        title=value,
        yaxis_title='cotação',
        )
    return fig

if __name__ == '__main__':
    app.run(debug=True)