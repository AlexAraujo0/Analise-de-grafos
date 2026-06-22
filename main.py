print("Aplicação inicializando, aguarde.")
print("-"*33)

from grafo import Grafo
from app import iniciar

def main():
    """Gera o grafo e inicializa a aplicação Dash."""
    grafo = Grafo()
    #Altere o primeiro parâmetro para gerar a quantidade de nós de pessoas que preferir, use a mesma seed se quiser reproduzir os dados.
    G = grafo.gerar(800, seed=4)
    html_grafo = grafo.visualizar(html=True)
    
    iniciar(html_grafo, G)


if __name__ == "__main__":
    main()
