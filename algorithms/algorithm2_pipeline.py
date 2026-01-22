import numpy as np

def quality_aware_hybrid_pipeline(
    candidates,
    haar_scores,
    dlib_scores,
    quality_scores,
    lambda1=0.4,
    lambda2=0.6,
    tau=40
):
    """
    Reference implementation of Algorithm 2 from the paper.

    Inputs:
        candidates: list of candidate face regions (placeholders)
        haar_scores: list of Haar detector confidences F_haar(x)
        dlib_scores: list of Dlib detector confidences F_dlib(x)
        quality_scores: list of aggregated quality scores Q(x)
        lambda1, lambda2: fusion weights
        tau: quality-weighted acceptance threshold

    Returns:
        accepted_indices: indices of detections retained in final set D
        rejected_indices: indices of detections rejected by quality gating
        final_scores: list of F_combined(x)
    """

    final_scores = []
    accepted_indices = []
    rejected_indices = []

    for i in range(len(candidates)):
        E_x = lambda1 * haar_scores[i] + lambda2 * dlib_scores[i]
        Q_x = quality_scores[i]
        F_combined = E_x * Q_x

        final_scores.append(F_combined)

        if F_combined >= tau:
            accepted_indices.append(i)
        else:
            rejected_indices.append(i)

    return accepted_indices, rejected_indices, final_scores
