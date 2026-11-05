import multiprocessing
import time

def operação(param):
    print("Iniciando a thread", param, "ID")
    for i in range(10):
        print("Rodando a thread", param, "ID")
        time.sleep(0.5)
    print("Thred",param, "ID encerrada" )

def main():
    args = [0]*5
    for i in range(5):
        args[i]=i
    with multiprocessing.Pool(processes=3) as pool:
        pool.map(operação, args)

if __name__=='__main__':
    main()