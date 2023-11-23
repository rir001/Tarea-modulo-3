import numpy as np
import matplotlib.pyplot as plt

def get_points(n=2):
    """Genera n coordenadas aleatorias en el mapa"""
    _mapa = plt.imread("maze.png")[::, ::, 0]
    paths = []
    while len(paths) < n:
        x, y = np.random.randint(0, len(_mapa), 2)
        if _mapa[y, x] == 1 and \
            [x, y] not in [[int(n[0]), int(n[1])] for n in paths] and \
            all([7<(int(x-n[0])**2 + int(y-n[1])**2) for n in paths]):
            paths.append([x+np.random.rand()*0.6+0.2, y+np.random.rand()*0.6+0.2])

    return (np.array(paths) - len(_mapa) / 2) / 5