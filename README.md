# Milking the Metaphors: Cultural Obfuscation in Wellness (COW) around Gomutra on YouTube using LLMs

This repository contains the code and evaluation scripts for the paper **"Milking the Metaphors: Cultural Obfuscation in Wellness (COW) around Gomutra on YouTube using LLMs"**.

## Overview
This project presents a post-facto Large Language Model (LLM)-assisted discourse analysis of YouTube videos promoting and debunking health claims related to *gomutra* (cow urine) in India. It investigates how promotional content blends sacred traditional language with pseudo-scientific claims, creating a rhetorical register that LLMs trained on Western corpora struggle to analyze accurately. 

## Repository Structure
* `/data`: Information on how to request the dataset (see Data Access below).
* `/scripts/wer_evaluation`: Code to calculate the Word Error Rate (WER) of the automated transcriptions.
* `/scripts/f1_evaluation`: Code to calculate Precision, Recall, and F1-scores for LLM-based term extraction.
* `/prompts`: The exact prompt templates used for GPT-4o, Gemini 2.5 Pro, and DeepSeek evaluations.

## Data Access & Ethical Considerations
The dataset consists of $N=30$ multilingual YouTube transcripts (English, Hindi, Urdu) related to gomutra discourse.

**Ethical Use Constraint:** To comply with platform guidelines and protect user privacy, no Personally Identifiable Information (PII) from viewers or commenters was collected. The aggregated dataset is released **strictly for non-commercial, academic research under an ethical use agreement**. 

*(Note to authors: Add instructions here on how researchers can email you to request the data or link to a data-sharing agreement form).*

## Core Evaluation Scripts

### 1. Word Error Rate (WER) Calculation
Audio from the YouTube videos was transcribed using OpenAI's Whisper model (large checkpoint). To evaluate transcription fidelity, we computed the Word Error Rate (WER) on a randomly selected subset comprising 16% of the video corpus.

The `wer_calculator.py` (or `.ipynb`) script computes WER using the following standard formulation:
$$WER = \frac{S+D+I}{N}$$
Where *S* is substitutions, *D* is deletions, *I* is insertions, and *N* is the total words in the reference transcript. Our average WER across the sampled dataset was 7.04%.

### 2. Term Extraction & F1-Score Evaluation
We employed GPT-4o to identify traditional metaphors and scientific terms to analyze macro-level discourse. To quantify the model's performance against human-annotated ground truth, we calculated Precision (P), Recall (R), and the F1-score (F1) on a validated subset of transcripts.

The `f1_evaluator.py` script computes the F1 metric based on True Positives (TP), False Positives (FP), and False Negatives (FN):
$$F1 = 2 \times \frac{P \times R}{P + R}$$

## Requirements
* Python 3.8+
* `youtube-transcript-api`
* *(Add any other required libraries here, e.g., `pandas`, `scikit-learn`, `openai`)*

## Citation
If you use this code or dataset in your research, please cite our paper:

```bibtex
@inproceedings{anonymous2026milking,
  title={Milking the Metaphors: Cultural Obfuscation in Wellness (COW) around Gomutra on YouTube using LLMs},
  author={Anonymous},
  booktitle={Proceedings of the International AAAI Conference on Web and Social Media (ICWSM)},
  year={2026}
}
