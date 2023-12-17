# -*- coding: utf-8 -*-
"""
Autor: Cassio Maciel Lemos
E-mail: cassio.lemos@petrobras.com.br

########################################################
                            Uso
Run this app with `python app.py`
visit http://127.0.0.1:8050/ in your web browser.

########################################################
                    Motivação

Esse código visa criar uma página que gere o gráfico
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
from datetime import date, timedelta


app = Dash(__name__)

tamanho_cabecalho = "5rem"
tamanho_sidebar = "16rem"

HEADER_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": tamanho_sidebar,
    'height' : tamanho_cabecalho,
    "width": "100%",
    "background-color": "#f8f9fa",
    "margin": 0,
}

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": "5rem",
    "left": 0,
    "bottom": 0,
    "width": tamanho_sidebar,
    "background-color": "#f8f9fa",
    "margin": 0,
}
PHOTO_STYLE = {
    "position": "fixed",
    "top": tamanho_cabecalho,
    "left": tamanho_sidebar,
    "bottom": 0,
    "background-color": "white",
    "margin": 0,
}
CONTENT_STYLE = {
    "position": "fixed",
    "top": tamanho_cabecalho,
    "left": tamanho_sidebar,
    "bottom": 0,
    "right": 0,
    "background-color": "#f8f9fa",
    "margin": 0,
}

app.layout = html.Div([
    html.Div(style=HEADER_STYLE,id='cabecalho',children=[ \
        html.H1(children='''
            Os melhores gráficos para você tomar as melhores
            decisões
        ''')
    ]),
    html.Div(style=SIDEBAR_STYLE, id='menu', children=[ \
        dcc.Dropdown(['PETR4.SA', 'VALE3.SA', 'BBDC4.SA'], 'PETR4.SA', id='lista_suspensa') \
             ]),
    html.Div(style=PHOTO_STYLE, id='photo' \
             ),
    html.Div(style=CONTENT_STYLE, id='conteudo', children=[ \
        dcc.Graph(id='grafico_candlestick') \
             ]),

])



'''
@callback(
    Output('Titulo_do_Graf', 'children'),
    Input('lista_suspensa', 'value')
)
def update_output(value):
    return f'Você selecionou {value}'
'''

@callback(
    Output('grafico_candlestick', 'figure'),
    Input('lista_suspensa', 'value')
)
def update_grafico(value):
    data = bib_graficos.constroi_grafico(value, date.today()-timedelta(days=730), date.today())
    fig = go.Figure(data=data)
    
    fig.update_layout(
        title=value,
        yaxis_title='cotação',
        )
    return fig



if __name__ == '__main__':
    app.run(debug=True)
