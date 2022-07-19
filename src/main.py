from lib import *
import time

def main():
  #simulação exemplo

  ShowData(Simulate(Tmax=200, w=0.5, o=10, seed=123234))
  ShowData(Simulate(Tmax=200, w=0.5, o=10, seed=int(32452345)))
  ShowData(Simulate(Tmax=200, w=0.5, o=10, seed=int(928734)))

if __name__ == "__main__":
  main()


