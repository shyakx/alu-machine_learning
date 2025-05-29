# NLP Metrics

This repository provides an overview and implementations of common evaluation metrics used in Natural Language Processing (NLP) tasks.

## Table of Contents

- [Overview](#overview)
- [Supported Metrics](#supported-metrics)
- [Installation](#installation)
- [Usage](#usage)
- [References](#references)

## Overview

NLP metrics are essential for evaluating the performance of models in tasks such as classification, translation, summarization, and more. This project covers widely-used metrics and provides examples for their application.

## Supported Metrics

- **Accuracy**
- **Precision, Recall, F1-score**
- **BLEU** (Bilingual Evaluation Understudy)
- **ROUGE** (Recall-Oriented Understudy for Gisting Evaluation)
- **METEOR**
- **Perplexity**
- **Word Error Rate (WER)**
- **Character Error Rate (CER)**

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/nlp_metrics.git
cd nlp_metrics
pip install -r requirements.txt
```

## Usage

Example usage for evaluating BLEU score:

```python
from nlp_metrics import bleu_score

reference = ["the cat is on the mat"]
candidate = ["the cat sat on the mat"]
score = bleu_score(reference, candidate)
print(f"BLEU score: {score}")
```

Refer to the [examples](examples/) directory for more.

## References

- [BLEU: Papineni et al., 2002](https://www.aclweb.org/anthology/P02-1040/)
- [ROUGE: Lin, 2004](https://aclanthology.org/W04-1013/)
- [Scikit-learn Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [NLTK Documentation](https://www.nltk.org/)

---

Feel free to contribute or raise issues!