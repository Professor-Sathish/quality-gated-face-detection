import numpy as np

def mean_detection_quality(quality_scores_tp):
    """
    Mean Detection Quality (MDQ)
    MDQ = (1 / |TP|) * sum(Q(x_i)) for i in TP
    """
    if len(quality_scores_tp) == 0:
        return 0.0
    return float(np.mean(quality_scores_tp))
