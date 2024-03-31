from point_in_polygon import point_in_polygon
from evaluate_performance import evaluate_performance
from is_figure_inside_other import is_figure_inside_other

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import colorsys

# Parse les données
data = [line.split() for line in open("e2.poly").read().split("\n") if line]
polygons = {}
points = {}
colors = {}
for line in data:
    poly_id, x, y = line
    poly_id = int(poly_id)
    x, y = float(x), float(y)
    point_id = f"{poly_id}.{len(polygons.get(poly_id, []))}"
    points[point_id] = (x, y)
    polygons.setdefault(poly_id, []).append(point_id)
    colors.setdefault(poly_id, None)

# Génère des couleurs uniques pour chaque polygone
for poly_id in colors:
    hue = poly_id / len(colors)
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    colors[poly_id] = color

# Convertit les données de la figure en une liste de tuples
figures = []
for poly_id, point_ids in polygons.items():
    points_list = [points[point_id] for point_id in point_ids]
    polygons_list = [points_list]  # Assuming each figure has only one polygon
    figures.append((points_list, polygons_list))


# Détermine l'ordre des figures
order = is_figure_inside_other(figures)

# Affiche la solution
print([order.index(i) if i in order else -1 for i in range(len(figures))])

# Évalue les performances de l'algorithme
n_figures = 100
n_trials = 100
figures = [(np.random.rand(np.random.randint(3, 10), 2).tolist(), []) for _ in range(n_figures)]

avg_time_point_in_polygon = evaluate_performance(figures, n_trials)
print(f"Temps moyen d'exécution de point_in_polygon : {avg_time_point_in_polygon:.6f} secondes")

avg_time_ray_casting = evaluate_performance(figures, n_trials)
print(f"Temps moyen d'exécution de ray_casting : {avg_time_ray_casting:.6f} secondes")