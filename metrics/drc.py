def conditional_detection_rate(tp_quality, fn_quality):
    """
    Conditional Detection Rate (DRc)
    DRc = TP_quality / (TP_quality + FN_quality)
    """
    if tp_quality + fn_quality == 0:
        return 0.0
    return tp_quality / (tp_quality + fn_quality)
