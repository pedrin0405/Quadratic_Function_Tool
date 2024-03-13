# Quadratic_Function_Tool
 Generate Grafic calculations basic from the input you add

Pré-requisitos: Python

BAIXAR MÓDULOS
    Macbook:
        pip3 install matplotlib

    Windows:
        python -m pip install -U pip
        python -m pip install -U matplotlib


MÓDULOS
    - from os import system, name:  Módulo pra limpar o Terminal
    - import matplotlib.pyplot as plt:  Módulo para gerar o Gráfico
    
VARIÁVEIS   
    ENTRADAS
        - a, b e c: É as entradas dos Coeficientes, sendo os principais e mais importantes dados;
    CÁLCULOS
        - valor_X: Lista onde conterar os valores do Vertice X
        - valor_Y: Lista onde conterar os valores do Vertice Y
        - x1: X' da fórmula de Bhaskara
        - x2: X" da fórmula de Bhaskara
        - delta: Calculo de Delta ( Δ = b2 – 4ac)
        - Xv: Vertice de X
        - Yv: Vertice de Y

FUNÇÕES
    SCREEN
        - limpar_tela()
            * Objetivo: Identificar o Sistema Operacional e limpar o Terminal para ter 
            uma visão mais clean da saída do codigo
            * Forma de Uso: Basta simplesmente chamar a função 'limpar_tela()'

        - grafic()
            * Objetivo: Criar e apresentar o gráfico da Função
            * Forma de Uso: Chamar a função 'grafic()' introduzindo nela as entradas de [x, y, x1, x2, Xv, Yv].

        - prints()
            * Objetivo: Apresentar os print's dos calculos/resultados da equação
            * Forma de Uso: Chamar a função 'grafic()' introduzindo nela as entradas de [a, b, c, X, Y, x1, x2, delta, Xv, Yv].
    
    TRANSFORMER
        - conversor()
            * Objetivo: Ler as entradas string:'a, b e c' e converter-las em float.
                Ex: Entrada (string) = 1,1 -> Após a coversão (float) = 1.1
            * Forma de Uso: Chamar a função 'conversor()' introduzindo nela as entradas de [a, b e c]

        - function()
            * Objetivo: Ler as entradas 'a, b e c' e gera as variáveis necessárias para a criação do gráfico.
            * Forma de Uso: Chamar a função 'function()' introduzindo nela as entradas de [a, b e c]
