# Model Card

**Model:** Domain classifier (e.g., BERT) + watermarking policy.

- **Intended Use:** Detect presence of domain‑guided watermark in AI‑generated text.
- **Out‑of‑scope:** Author identification, human vs AI classification absent watermark.
- **Metrics:** Accuracy, F1, FPR/FNR at chosen threshold.
- **Ethical Considerations:** False accusations risk; communicate uncertainty; provide appeals process.
- **Caveats:** Threshold depends on domain, length normalization, paraphrase robustness.
