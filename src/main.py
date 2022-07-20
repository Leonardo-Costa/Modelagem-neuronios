from lib import *
import time
import matplotlib.pyplot as plt

def main():
  #simulação exemplo

  ShowData(Simulate(Tmax=2000, w=0.2, o=100, width=20, seed=123234, I=0.5), save=True)


if __name__ == "__main__":
  main()


