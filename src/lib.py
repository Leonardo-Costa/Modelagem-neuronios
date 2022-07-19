import numpy as np
import math
import random
from matplotlib import pyplot as plt
from tqdm import tqdm


def H(v):
    """Retorna 1 se o parâmetro for maior ou igual a um limiar mínimo

    Args:
        v (float): limiar mínimo

    Returns:
        int: 1 ou 0
    """
  
    return 1 if v >= 0 else 0
  
def ShowData(content, t=0.5):
    """Exibe os gráficos da simulção realizada

    Args:
        content (list): Dados da simulação
        t (float, optional): limiar de excitação do neurônio. Defaults to 0.5.
    """
    fig = plt.figure("Degree of a random graph", figsize=(10, 10))
    axgrid = fig.add_gridspec(3, 2)

    ax1 = fig.add_subplot(axgrid[0, 0:])
    ax1.set_title('Oscilação de neurônios')
    ax1.set_xlabel('tempo')
    ax1.set_ylabel('Excitação do neurônio')
    for i in range(len(content)):
        ax1.plot(content[i])

    discretizado = []
    for i in range(len(content)):
        discretizado.append([])
        for j in range(len(content[i])):
            discretizado[i].append(1 + 0.1 * i if content[i][j] > t else None)

    ax2 = fig.add_subplot(axgrid[1, 0:])
    for i in range(len(content)):
        ax2.scatter(list(range(len(discretizado[i]))), discretizado[i])
    plt.show()

def Simulate(DT=0.01, Tmax=1000, neurons=5, t=0.5, w=0.3, e=0.02, a=6, B=0.1, p=0, I=0.1, o=15, seed=10):
    """Realiza a simulação com os parâmetros passados

    Args:
        DT (float, optional): passo de integração. Defaults to 0.01.
        Tmax (int, optional): tempo da simulação. Defaults to 1000.
        neurons (int, optional): número de neurônios. Defaults to 5.
        t (float, optional): limiar de exitação. Defaults to 0.5.
        w (float, optional): força de acoplamento. Defaults to 0.3.
        e (float, optional): parametros do modelo. Defaults to 0.02.
        a (int, optional): parametros do. Defaults to 6.
        B (float, optional): parametros do modelo. Defaults to 0.1.
        p (int, optional): ruido. Defaults to 0.
        I (float, optional): Excitação global. Defaults to 0.1.
        o (int, optional): amostragem. Defaults to 15.
        seed (int, optional): seed para a geração dos numeros pseudoaleatorios. Defaults to 10.

    Returns:
        list: dados da simulação
    """
    random.seed(seed)
    # Variáveis
    x = []
    y = []

    # Listas para plot
    lx = []
    ly = []

    dx = []
    dy = []
    S = [] #acoplamento

    for i in range(neurons):
        x.append(round(random.uniform(-2, 0.4), 2))
        y.append(round(random.uniform(0, 4), 2))
        dx.append(0)
        dy.append(0)
        lx.append([])
        ly.append([])
        S.append(0)

    iterations = int(Tmax / DT)

    for i in tqdm(range(iterations)):
        for j in range(neurons):
            S[j] = w * (H(x[(j + 1) % neurons] - t) + H(x[(j - 1) % neurons] - t))
        for k in range(neurons):
            dx[k] = (3 * x[k] - x[k] ** 3 + 2 - y[k] + I + p + S[k] ) * DT
            dy[k] = (e * ( a * ( 1 + math.tanh(x[k] / B)) - y[k])) * DT

            if i % o == 0:
                lx[k].append(round(x[k], 4))

            x[k] += dx[k]
            y[k] += dy[k]
        
    return lx
