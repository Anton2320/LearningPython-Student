import numpy as np
import taskfunctions

def main():
    np.set_printoptions(threshold=np.inf)
    np.random.seed(444)
    taskfunctions.exec_first()
    taskfunctions.exec_second()

if __name__ == "__main__":
    main()
