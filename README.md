# 📊 Análise Estatística e Dashboard - Dataset Diabetes

Este projeto realiza uma Análise Exploratória de Dados (EDA) completa utilizando um conjunto de dados sobre diabetes. O objetivo é tratar inconsistências nos dados, extrair métricas estatísticas detalhadas e consolidar os resultados em um painel visual (dashboard).

---

## 🚀 Funcionalidades do Projeto

* **Tratamento e Limpeza de Dados:** Identificação de valores nulos e substituição de valores `0` incoerentes (em colunas como Glicose, Pressão Arterial, Insulina e IMC) pela média dos respectivos atributos.
* **Análise Estatística Avançada:** Cálculo de totais, médias, medianas, valores mínimos/máximos e variância.
* **Engenharia de Recursos (Feature Engineering):** Agrupamento de dados por faixas etárias (*Jovem, Adulta, Sêniora*).
* **Análise Comparativa:** Cruzamento de dados de saúde entre pacientes diagnosticados com e sem diabetes.
* **Dashboard Consolidado:** Geração de um painel visual único com gráficos integrados, paletas de cores personalizadas (*Tons de Rosa e Roxo*) e exportação automática para imagem de alta resolução (`300 DPI`).

---

## 🧱 Estrutura do Dashboard Visual

O painel final unifica quatro visões estratégicas do conjunto de dados:

1.  **Distribuição por Faixa Etária (Gráfico de Pizza):** Exibe o percentual de casos de diabetes segmentado por grupos de idade.
2.  **Média de Glicose vs. Pressão Arterial (Gráfico de Barras Duplas):** Compara lado a lado os indicadores cardinais de saúde entre os dois grupos diagnósticos.
3.  **Relação IMC vs. Espessura da Pele (Gráfico de Dispersão):** Demonstra a distribuição e correlação física dos pacientes sinalizados pelo status de diabetes.
4.  **Mapa de Calor (Heatmap de Médias Gerais):** Uma matriz de intensidade visual (`PuRd`) que evidencia a disparidade de todas as médias numéricas simultaneamente.

---

## 🛠️ Tecnologias Utilizadas

O projeto foi desenvolvido em ambiente Jupyter Notebook utilizando a linguagem **Python 3** e as seguintes bibliotecas principais:

* **[Pandas](https://pandas.pydata.org/):** Manipulação, tratamento de zeros e agrupamento de dados.
* **[Matplotlib](https://matplotlib.org/):** Estruturação da grade de subplots e exportação do arquivo final.
* **[Seaborn](https://seaborn.pydata.org/):** Plotagem dos gráficos estatísticos avançados e estilização de paletas.

---
## 🛠️ Dataset
* A base de dados foi extraída do site Kaggle.
*  [Kaggle](https://www.kaggle.com/)
* [Diabetes Dataset](https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset)

  
