# Importação das bibliotecas
import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
from graficos import gerar_grafico


def iniciar(html_grafo, G):
    """Inicializa e executa a aplicação Dash.

    Cria um dashboard interativo contendo a visualização de um grafo em HTML
    e gráficos dinâmicos gerados a partir dos dados do grafo.

    Parâmetros
    ----------
    html_grafo : str
        Código HTML do grafo a ser exibido no componente Iframe.
    G : networkx.Graph
        Grafo utilizado para gerar os gráficos interativos.

    Retorno
    -------
    None
        A função inicializa e executa o servidor Dash localmente na porta 8060.
    """

    app = dash.Dash(
        __name__,
        external_stylesheets=[dbc.themes.FLATLY],
        title="Dashboard"
    )

    app.layout = dbc.Container(fluid=True, children=[

        dbc.Row(
            dbc.Col(
                html.Div(
                    className="p-3 my-3 bg-primary text-white rounded-3 shadow",
                    children=[
                        html.H2("Visualização de dados", className="fw-bold"),
                    ]
                )
            )
        ),

        dbc.Row([

            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.H5("Grafo", className="mb-3"),

                        html.Iframe(
                            id="grafo",
                            srcDoc=html_grafo,
                            style={
                                "width": "100%",
                                "height": "500px",
                                "border": "none"
                            }
                        )
                    ]),
                    className="shadow-sm"
                ),
                xs=12,
                lg=6
            ),

            dbc.Col(
                dbc.Card(
                    dbc.CardBody([

                        html.H5("Visualização de Dados", className="mb-3"),

                        dcc.Dropdown(
                            id="seletor-dados",
                            options=[
                                {"label": "Pessoas por turma", "value": "pessoas_turma"},
                                {"label": "Pessoas por interesse", "value": "pessoas_interesse"},
                                {"label": "Turma × interesse", "value": "turma_interesse"},
                                {"label": "Interesse × perfil", "value": "interesse_perfil"},
                            ],
                            value="pessoas_turma",
                            placeholder="Selecione os dados",
                            className="mb-3"
                        ),

                        dcc.Graph(
                            id="grafico-dinamico",
                            figure=gerar_grafico(G, "pessoas_turma")
                        )
                    ]),
                    className="shadow-sm"
                ),
                xs=12,
                lg=6
            )
        ], className="mb-4"),

        dbc.Row(
            dbc.Col(
                html.P(
                    "Projeto final PCD-T26. Feito por Álex Araujo",
                    className="text-center text-muted small"
                )
            )
        )
    ])

    @app.callback(
        Output("grafico-dinamico", "figure"),
        Input("seletor-dados", "value")
    )
    def atualizar_grafico(tipo_grafico):
        """Atualiza o gráfico exibido no dashboard.
    
        Parâmetros
        ----------
        tipo_grafico : str
            Tipo de gráfico selecionado no menu suspenso.
    
        Retorno
        -------
        plotly.graph_objects.Figure
            Figura atualizada de acordo com a opção selecionada.
        """
        return gerar_grafico(G, tipo_grafico)

    print("App rodando! Acesse http://localhost:8060 para visualizá-lo melhor.")
    print("-"*67)
    app.run(debug=False, port=8060, use_reloader=False)