import numpy as np
import matplotlib.pyplot as plt


def get_points(n=2):
    """Genera n coordenadas aleatorias en el mapa"""
    _mapa = plt.imread("maze.png")[::, ::, 0]
    paths = []
    while len(paths) < n:
        x, y = np.random.randint(0, len(_mapa), 2)
        if (_mapa[y, x] == 1) and [y, x] not in paths:
            if all([np.linalg.norm(np.array([y, x]) - np.array(p)) > 10 for p in paths]):
                paths.append([y, x])

    for n in range(len(paths)): paths[n] += 0.4 + np.random.rand(2) * 0.2

    return (np.array(paths) - (len(_mapa) / 2)) / 5