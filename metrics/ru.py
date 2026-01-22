def unconditional_recall(tp, fn_all):
    """
    Unconditional Recall (Ru)
    Ru = TP / (TP + FN_all)
    """
    if tp + fn_all == 0:
        return 0.0
    return tp / (tp + fn_all)
