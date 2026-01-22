# Evaluation Protocol

This document specifies the fairness-preserving evaluation protocol used in the paper.

## 1. Detection Correctness

A detection is considered correct if:

- Intersection-over-Union (IoU) ≥ 0.5 with a ground-truth face.

## 2. Treatment of Quality Rejections

Any ground-truth face that is:

- not detected, OR
- detected but rejected by the Quality Assessment Module (QAM)

is counted as a false negative for Unconditional Recall (Ru).

This prevents quality-based filtering from artificially inflating recall.

## 3. Metric Definitions

- **Ru:** computed over all ground-truth faces
- **DRc:** computed only over detections satisfying the quality threshold τ
- **MDQ:** computed only over true positive detections
- **FPR:** computed using standard FP / (FP + TN)

## 4. Evaluation Invariance

All metrics are computed:

- on raw detections
- before any post-detection enhancement
- using fixed hyperparameters selected prior to benchmarking

No CLAHE or NLM processing is applied prior to metric computation.

## 5. Dataset Usage

Evaluation is restricted to official validation splits of:

- WIDER FACE (Hard)
- FDDB (Fold 1–10)
- AFW

No test-time tuning is performed on these datasets.
