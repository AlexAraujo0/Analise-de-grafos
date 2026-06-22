<div id="topo"></div>

<p align="center">
  <img src="assets/logo-Ilum.png" alt="Logo Ilum" width="100%">
</p>

<h1 align="center">Análise de Grafos</h1>

<p align="center">
  Projeto final da disciplina <strong>Práticas de Ciência de Dados</strong> — PCD-T26.
</p>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://dash.plotly.com/">
    <img src="https://img.shields.io/badge/Dash-Dashboard-119DFF" alt="Dash">
  </a>
  <a href="https://networkx.org/">
    <img src="https://img.shields.io/badge/NetworkX-Grafos-orange" alt="NetworkX">
  </a>
  <a href="https://plotly.com/python/">
    <img src="https://img.shields.io/badge/Plotly-Visualização-3F4F75" alt="Plotly">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-GPL--3.0-blue" alt="Licença GPL 3.0">
  </a>
</p>

<hr>

<h2 id="sumario">Sumário</h2>

<ul>
  <li><a href="#descricao-do-projeto">Descrição do projeto</a></li>
  <li><a href="#setup-do-projeto">Setup do projeto</a></li>
  <li><a href="#como-executar">Como executar</a></li>
  <li><a href="#estrutura-do-projeto">Estrutura do projeto</a></li>
  <li><a href="#modulos-do-projeto">Módulos do projeto</a></li>
  <li><a href="#funcionalidades">Funcionalidades</a></li>
  <li><a href="#melhorias">Próximos passos</a></li>
  <li><a href="#observacao">Observação</a></li>
  <li><a href="#licenca">Licença</a></li>
</ul>

<hr>

<h2 id="descricao-do-projeto">Descrição do projeto</h2>

<p>
  Este projeto foi desenvolvido como atividade final da disciplina 
  <strong>Práticas de Ciência de Dados</strong>, da turma de 2026 da 
  <strong>Ilum Escola de Ciência</strong>.
</p>

<p>
  A disciplina foi ministrada pelos professores 
  <strong>Daniel R. Cassar</strong>, 
  <strong>Leandro N. Lemos</strong> e 
  <strong>James M. de Almeida</strong>, e o projeto foi desenvolvido pelo discente 
  <strong>Álex V. R. de Araujo</strong>.
</p>

<p>
  A aplicação integra geração de grafos, visualização interativa e análise de dados 
  em um dashboard web construído com <strong>Dash</strong>.
</p>

<p>
  O repositório conta com três módulos principais e um script 
  <code>main.py</code>, responsável por executar a aplicação com um conjunto de 
  dados de demonstração.
</p>

<p>
  Neste documento, são apresentadas as principais funcionalidades dos módulos e das 
  bibliotecas utilizadas. Para informações detalhadas sobre funções específicas, 
  utilize a função nativa <code>help()</code> do Python:
</p>

<pre><code>help(nome_da_funcao)</code></pre>

<hr>

<h2 id="setup-do-projeto">Setup do projeto</h2>

<p>
  Antes de executar o <code>main.py</code>, garanta que todas as dependências estejam 
  devidamente instaladas em sua máquina.
</p>

<p>
  Caso necessário, entre no diretório onde o projeto está baixado, abra o terminal e execute:
</p>

<pre><code>pip install -r requirements.txt</code></pre>

<hr>

<h2 id="como-executar">Como executar</h2>

<p>
  Após instalar as dependências, execute o projeto com o seguinte comando:
</p>

<pre><code>python main.py</code></pre>

<p>
  Em seguida, acesse a aplicação no navegador usando o endereço:
</p>

<pre><code>http://localhost:8060</code></pre>

<hr>

<h2 id="estrutura-do-projeto">Estrutura do projeto</h2>

<p>
  A estrutura principal do repositório está organizada da seguinte forma:
</p>

<pre><code>Analise-de-grafos/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── app.py
├── graficos.py
├── grafo.py
└── main.py</code></pre>

<hr>

<h2 id="modulos-do-projeto">Módulos do projeto</h2>

<h3><code>main.py</code></h3>

<p>
  Arquivo principal do projeto. Ele é responsável por criar o grafo, gerar a 
  visualização em HTML e inicializar a aplicação Dash.
</p>

<h3><code>grafo.py</code></h3>

<p>
  Contém a classe responsável pela criação, manipulação e visualização do grafo 
  utilizando a biblioteca <strong>NetworkX</strong> e a biblioteca 
  <strong>Gravis</strong>.
</p>

<h3><code>graficos.py</code></h3>

<p>
  Contém as funções responsáveis pela criação dos gráficos interativos utilizados 
  no dashboard, com apoio das bibliotecas <strong>Pandas</strong> e 
  <strong>Plotly</strong>.
</p>

<h3><code>app.py</code></h3>

<p>
  Contém a aplicação web desenvolvida com <strong>Dash</strong>, incluindo o layout 
  do dashboard, o componente de visualização do grafo e o callback responsável por 
  atualizar os gráficos dinamicamente.
</p>

<hr>

<h2 id="funcionalidades">Funcionalidades</h2>

<ul>
  <li>Geração automática de grafos.</li>
  <li>Criação de nós para pessoas, turmas, interesses e o nó central Ilum.</li>
  <li>Associação de pessoas às suas respectivas turmas e áreas de interesse.</li>
  <li>Visualização interativa do grafo.</li>
  <li>Dashboard web com gráficos dinâmicos.</li>
  <li>Análise de pessoas por turma.</li>
  <li>Análise de pessoas por interesse.</li>
  <li>Relação entre turma e interesse.</li>
  <li>Relação entre interesse e perfil.</li>
</ul>
<hr>
<h2 id="melhorias">Próximos passos</h2>

<p>Para o futuro do projeto, pretendo disponibilizar um Formulário Google por meio do qual tanto os atuais discentes quanto os egressos da Ilum possam contribuir com seus dados.</p>

<p>No formulário serão preenchidos</p>

<ul>
  <li>Turma</li>
  <li>Área de interesse</li>
  <li>Perfil</li>
</ul>

<p>Depois, transformarei estes dados em um <code>DataFrame</code> do módulo <code>pandas</code> e os usarei para gerar um modelo de previsão que alimentará a geração do grafo, fazendo-o deixar de ser aleatório e passando a ser baseado em dados reais, indicando o comportamento dos dados conforme o tamanho da população muda.</p>
<hr>

<h2 id="observacao">Observação</h2>

<p>
  Os dados utilizados neste projeto são gerados sinteticamente pelo próprio programa. 
  Portanto, como mencionado em <a href="#melhorias">Próximos passos</a>, os dados apresentados no programa são apenas para fins demonstrativos, não representando dados reais.
</p>

<hr>

<h2 id="licenca">Licença</h2>

<p>
  Este projeto está licenciado sob a licença 
  <strong>GNU General Public License v3.0</strong>.
</p>

<p>
  Para mais detalhes, consulte o arquivo <a href="LICENSE"><code>LICENSE</code></a>.
</p>

<p align="right">
  <a href="#topo">Voltar ao topo</a>
</p>
