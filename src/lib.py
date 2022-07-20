import numpy as np
import math
import random
from matplotlib import pyplot as plt
from tqdm import tqdm
from os.path import exists

def H(v):
    """Retorna 1 se o parâmetro for maior ou igual a um limiar mínimo

    Args:
        v (float): limiar mínimo

    Returns:
        int: 1 ou 0
    """
  
    return 1 if v >= 0 else 0

def FindName():
    for i in range(100):
        if not exists('data/sim-{}.png'.format(i)):
            return 'sim-{}.png'.format(i)


def ShowData(content, t=0.5, save=True, name=True):
    """Exibe os gráficos da simulção realizada

    Args:
        content (list): Dados da simulação
        t (float, optional): limiar de excitação do neurônio. Defaults to 0.5.
        save (bool, optional): define se as imagens são salvas ou nao
    """
    fig = plt.figure("Degree of a random graph", figsize=(10, 10))
    axgrid = fig.add_gridspec(2, 2)

    ax1 = fig.add_subplot(axgrid[0, 0:])
    ax1.set_title('Oscilação de neurônios')
    ax1.set_xlabel('tempo')
    ax1.set_ylabel('Excitação do neurônio')

    for j in range(len(content)):
        for k in range(len(content[j])):
            ax1.plot(content[j][k])

    [[[1]]]

    print(len(content))
    discretizado = []
    for j in range(len(content)):
        discretizado.append([])
        for k in range(len(content[j])):
            discretizado[j].append([])
            for i in range(len(content[j][k])):
                if content[j][k][i] >= t and content[j][k][i] > content[j][k][i - 1] and content[j][k][i] > content[j][k][i + 1]:
                    discretizado[j][k].append(1 + 0.01 * j + 0.001 * k)
                else:
                    discretizado[j][k].append(None)
                    
    ax2 = fig.add_subplot(axgrid[1, 0:])
    for j in range(len(content)):
        for k in range(len(content[j])):
            ax2.scatter(list(range(len(discretizado[j][k]))), discretizado[j][k], color='#DD0000')
    
    if save:
        plt.savefig("data/{}".format(FindName() if name == True else name))
    else:
        plt.show()




def Simulate(DT=0.01, Tmax=1000, width=5, t=0.5, w=0.3, e=0.02, a=6, B=0.1, p=0, I=0.1, o=15, seed=10):
    """Realiza a simulação com os parâmetros passados

    Args:
        DT (float, optional): passo de integração. Defaults to 0.01.
        Tmax (int, optional): tempo da simulação. Defaults to 1000.
        width (int, optional): lado da rede quadrada onde os neurônios estarão dispostos. Defaults to 5.
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

    for i in range(width):
        x.append([])
        y.append([])
        dx.append([])
        dy.append([])
        S.append([])
        lx.append([])
        ly.append([])
        for j in range(width):
            x[i].append(round(random.uniform(-2, 0.4), 2))
            y[i].append(round(random.uniform(0, 4), 2))
            dx[i].append(0)
            dy[i].append(0)
            S[i].append(0)
            lx[i].append([])
            ly[i].append([])

    iterations = int(Tmax / DT)

    for i in tqdm(range(iterations)):
        for j in range(width):
            for k in range(width):
                S[j][k] = w * (H(x[(j+1) % width][k] - t) + H(x[(j-1) % width][k] - t) + H(x[j][(k+1) % width] - t) + H(x[j][(k-1) % width] - t))
        for j in range(width):
            for k in range(width):
                dx[j][k] = (3 * x[j][k] - x[j][k] ** 3 + 2 - y[j][k] + I + p + S[j][k] ) * DT
                dy[j][k] = (e * ( a * ( 1 + math.tanh(x[j][k] / B)) - y[j][k])) * DT

                x[j][k] += dx[j][k]
                y[j][k] += dy[j][k]

                if i % o == 0:
                    lx[j][k].append(round(x[j][k], 4))
        
    return lx
 

 