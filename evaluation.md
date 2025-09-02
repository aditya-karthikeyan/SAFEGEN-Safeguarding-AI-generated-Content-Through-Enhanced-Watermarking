# Evaluation Protocol

1. **Unit Length:** Normalize to 150‑word windows (sliding or non‑overlapping).
2. **Signal:** Count unique Red‑List terms per window (or total count; pick one consistently).
3. **Threshold:** Start at 6 per 150 words (tune via ROC/PR on your validation set).
4. **Metrics:** Report accuracy, F1, precision, recall, FPR, FNR. Include confidence intervals via bootstrap.
5. **Ablations:** Vary Red‑List percentiles, window sizes, domains, paraphrase/noise levels.
6. **Reporting:** Save results in `results/tables/` and plots in `results/figures/`.
