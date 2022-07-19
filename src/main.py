from lib import *

def main():
  ShowData(Simulate(neurons=5, Tmax=10000, w=0.03))

if __name__ == "__main__":
  main()