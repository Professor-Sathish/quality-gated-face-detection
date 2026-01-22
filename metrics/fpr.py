def false_positive_rate(fp, tn):
    """
    False Positive Rate (FPR)
    FPR = FP / (FP + TN)
    """
    if fp + tn == 0:
        return 0.0
    return fp / (fp + tn)
