import numpy as np
import time
from is_figure_inside_other import is_figure_inside_other


def evaluate_performance(figures, n_trials):
    times = []
    for _ in range(n_trials):
        start = time.time()
        is_figure_inside_other(figures)
        end = time.time()
        times.append(end - start)
    avg_time = np.mean(times)
    return avg_time