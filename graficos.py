import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# Definindo as cores
CORES_TURMAS = {
    "T22": "#00538A",
    "T23": "#000000",
    "T24": "#007D34",
    "T25": "#FF6800",
    "T26": "#803E75"
}

CORES_INTERESSES = {
    "CD": "#0072B2",
    "LM": "#E69F00",
    "CM": "#009E73",
    "CV": "#CC79A7",
    "HU": "#D55E00"
}


def tipo_no(attrs):
    """Classifica o tipo de um nó a partir de seus atributos.

    Parâmetros
    ----------
    attrs : dict
        Dicionário com os atributos do nó.

    Retorno
    -------
    str
        Tipo do nó: "Pessoa", "Turma", "Interesse" ou "Instituição".
    """

    if "perfil" in attrs:
        return "Pessoa"
    elif "turma" in attrs:
        return "Turma"
    elif "interesse" in attrs:
        return "Interesse"
    else:
        return "Instituição"

    
def dataframe_nos(G, apenas_pessoas=False):
    """Converte os nós do grafo em um DataFrame.

    Parâmetros
    ----------
    G : networkx.Graph
        Grafo analisado.
    apenas_pessoas : bool, opcional
        Se True, retorna apenas os nós que possuem o atributo perfil.
        O valor padrão é False.

    Retorno
    -------
    pandas.DataFrame
        DataFrame contendo os nós do grafo e seus atributos.
    """
    
    dados = []

    for no, attrs in G.nodes(data=True):
        linha = {
            "no": no,
            "tipo": tipo_no(attrs)
        }

        linha.update(attrs)
        dados.append(linha)

    df = pd.DataFrame(dados)

    if apenas_pessoas:
        if "perfil" not in df.columns:
            return pd.DataFrame()

        return df[df["perfil"].notna()].copy()

    return df

    
def figura_vazia(titulo="Sem dados disponíveis"):
    """Cria uma figura vazia para evitar erros no Dash.

    Parâmetros
    ----------
    titulo : str, opcional
        Título exibido na figura vazia.

    Retorno
    -------
    plotly.graph_objects.Figure
        Figura vazia com uma mensagem de dados insuficientes.
    """

    fig = go.Figure()

    fig.update_layout(
        title=titulo,
        xaxis={"visible": False},
        yaxis={"visible": False},
        annotations=[
            {
                "text": "Dados insuficientes.",
                "xref": "paper",
                "yref": "paper",
                "showarrow": False,
                "font": {"size": 16}
            }
        ],
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig

    
def pessoas_por_turma(G):
    """Gera um gráfico de barras com a quantidade de pessoas por turma.

    Parâmetros
    ----------
    G : networkx.Graph
        Grafo analisado.

    Retorno
    -------
    plotly.graph_objects.Figure
        Figura com a distribuição de pessoas por turma.
    """
    
    df = dataframe_nos(G, apenas_pessoas=True)

    if df.empty or "turma" not in df.columns:
        return figura_vazia("Pessoas por turma")

    contagem = (
        df["turma"]
        .value_counts()
        .reset_index()
    )

    contagem.columns = ["turma", "quantidade"]

    fig = px.bar(
        contagem,
        x="turma",
        y="quantidade",
        color="turma",
        color_discrete_map=CORES_TURMAS,
        title="Pessoas por turma",
        labels={
            "turma": "Turma",
            "quantidade": "Quantidade de pessoas"
        }
    )

    fig.update_layout(
        showlegend=False,
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig

    
def pessoas_por_interesse(G):
    """Gera um gráfico de barras com a quantidade de pessoas por interesse.

    Parâmetros
    ----------
    G : networkx.Graph
        Grafo analisado.

    Retorno
    -------
    plotly.graph_objects.Figure
        Figura com a distribuição de pessoas por área de interesse.
    """
    
    df = dataframe_nos(G, apenas_pessoas=True)

    if df.empty or "interesse" not in df.columns:
        return figura_vazia("Pessoas por interesse")

    contagem = (
        df["interesse"]
        .value_counts()
        .reset_index()
    )

    contagem.columns = ["interesse", "quantidade"]

    fig = px.bar(
        contagem,
        x="interesse",
        y="quantidade",
        color="interesse",
        color_discrete_map=CORES_INTERESSES,
        title="Pessoas por interesse",
        labels={
            "interesse": "Interesse",
            "quantidade": "Quantidade de pessoas"
        }
    )

    fig.update_layout(
        showlegend=False,
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig

    
def turma_interesse(G):
    """Gera um heatmap relacionando turmas e interesses.

    Parâmetros
    ----------
    G : networkx.Graph
        Grafo analisado.

    Retorno
    -------
    plotly.graph_objects.Figure
        Figura com a contagem de pessoas por turma e interesse.
    """
    
    df = dataframe_nos(G, apenas_pessoas=True)

    if df.empty or "turma" not in df.columns or "interesse" not in df.columns:
        return figura_vazia("Turma × interesse")

    tabela = pd.crosstab(
        df["turma"],
        df["interesse"]
    )

    fig = px.imshow(
        tabela,
        text_auto=True,
        color_continuous_scale="Cividis",
        title="Turma × interesse",
        labels={
            "x": "Interesse",
            "y": "Turma",
            "color": "Quantidade"
        }
    )

    fig.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig

    
def interesse_perfil(G):
    """Gera um gráfico de barras agrupadas relacionando interesses e perfis.

    Parâmetros
    ----------
    G : networkx.Graph
        Grafo analisado.

    Retorno
    -------
    plotly.graph_objects.Figure
        Figura com a distribuição de perfis por área de interesse.
    """
    
    df = dataframe_nos(G, apenas_pessoas=True)

    if df.empty or "interesse" not in df.columns or "perfil" not in df.columns:
        return figura_vazia("Interesse × perfil")

    contagem = (
        df.groupby(["interesse", "perfil"])
        .size()
        .reset_index(name="quantidade")
    )

    fig = px.bar(
        contagem,
        x="interesse",
        y="quantidade",
        color="perfil",
        barmode="group",
        title="Interesse × perfil",
        labels={
            "interesse": "Interesse",
            "perfil": "Perfil",
            "quantidade": "Quantidade"
        }
    )

    fig.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig


def gerar_grafico(G, tipo):
    """Gera o gráfico selecionado para uso no Dropdown do Dash.

    Parâmetros
    ----------
    G : networkx.Graph
        Grafo analisado.
    tipo : str
        Tipo de gráfico escolhido no Dropdown.

    Retorno
    -------
    plotly.graph_objects.Figure
        Figura correspondente ao tipo de gráfico selecionado. Caso o tipo seja
        inválido, retorna uma figura vazia.
    """
    
    graficos = {
        "pessoas_turma": pessoas_por_turma,
        "pessoas_interesse": pessoas_por_interesse,
        "turma_interesse": turma_interesse,
        "interesse_perfil": interesse_perfil,
    }

    if tipo not in graficos:
        return figura_vazia("Gráfico inválido")

    return graficos[tipo](G)