
<p align="center">
 <img src=https://i.imgur.com/C0RrESB.png>
</p>


Recomendação de músicas similares com Python

Este é um script em Python que utiliza a API do Last.fm para recomendar músicas similares a uma música escolhida pelo usuário.
Dependências

    Python 3.x
    Bibliotecas Python:
        requests
        json
        networkx
        matplotlib
        termcolor

As bibliotecas Python podem ser instaladas via pip. Por exemplo, para instalar a biblioteca networkx, execute o seguinte comando:

```pip install requests networkx matplotlib termcolor```

Como utilizar

    Obtenha uma API key do Last.fm em https://www.last.fm/api/account/create.

    Clone ou baixe este repositório.

    No arquivo main3.py, substitua a variável API_KEY pela sua API key obtida no passo 1.

    Abra um terminal ou prompt de comando na pasta do repositório e execute o seguinte comando para instalar as bibliotecas Python necessárias:



Execute o script com o seguinte comando:

    python main3.py

    Siga as instruções para digitar o nome do artista e da música desejados, e escolher as opções de número de músicas similares e recomendações.

    O script irá mostrar na tela as músicas recomendadas.

Como funciona

O script utiliza a API do Last.fm para obter uma lista de músicas similares à música escolhida pelo usuário, e em seguida cria um grafo no qual cada nó representa uma música e cada aresta representa uma similaridade entre duas músicas. A similaridade é medida com base nas "tags" associadas a cada música, que são palavras-chave que descrevem o estilo da música. Em seguida, o script utiliza o algoritmo de caminho mais curto para encontrar as músicas mais similares à música escolhida pelo usuário, e retorna as músicas com maior similaridade.
