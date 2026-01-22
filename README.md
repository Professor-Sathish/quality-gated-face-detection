# Quality-Gated Face Detection - Reproducibility Package

This repository provides a reproducibility scaffold for the paper:

"A Hybrid Viola-Jones Pipeline with Hierarchical CNN Verification for Quality-Gated Face Detection"

It exposes the exact decision logic, evaluation metrics and benchmarking protocol used in the manuscript.

---

## What this repository contains

- A reference implementation of Algorithm 2 (quality-aware hybrid detection pipeline logic)  
- Task-oriented evaluation metrics:
  - Unconditional Recall (Ru)  
  - Conditional Detection Rate (DRc)  
  - Mean Detection Quality (MDQ)  
  - False Positive Rate (FPR)  
- The evaluation protocol used for fairness-preserving benchmarking

---

## What this repository does NOT contain

- Full face detection models  
- Trained CNN weights  
- Dataset files  
- Image preprocessing or enhancement code

These components are intentionally excluded to avoid licensing issues and to keep the focus on methodological transparency rather than deployment code.

---

## Purpose

This code is intended to:

- Demonstrate how detection confidence and quality are fused  
- Make metric definitions explicit and verifiable  
- Show how fairness is preserved when applying quality-based filtering  
- Allow independent reimplementation and audit of evaluation logic

---

## Citation

If you use this code or build upon it, please cite:

R. Sathish et al.,  
"A Hybrid Viola-Jones Pipeline with Hierarchical CNN Verification for Quality-Gated Face Detection", 2025.
