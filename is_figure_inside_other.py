from ray_casting import ray_casting


def is_figure_inside_other(figures):
    n = len(figures)
    order = [i for i in range(n)]
    for i in range(n):
        figure_i = figures[i]
        for j in range(i+1, n):
            figure_j = figures[j]
            all_points_inside = all([ray_casting(point, figure_j[0]) for point in figure_i[0]])
            if all_points_inside:
                order[i], order[j] = order[j], order[i]
                break
    return order