print("Aplicação inicializando, aguarde.")
print("-"*33)

from grafo import Grafo
from app import iniciar

def main():
    """Gera o grafo e inicializa a aplicação Dash."""
    grafo = Grafo()
    G = grafo.gerar(2000, seed=4)
    html_grafo = grafo.visualizar(html=True)
    
    iniciar(html_grafo, G)


if __name__ == "__main__":
    main()