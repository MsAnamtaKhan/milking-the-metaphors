# When Cow Urine Cures Constipation on YouTube: Limits of LLMs in Detecting Culture-specific Health Misinformation

This repository contains the code and evaluation scripts for the paper **"Milking the Metaphors: Cultural Obfuscation in Wellness (COW) around Gomutra on YouTube using LLMs"**.

## Overview
This project presents a post-facto Large Language Model (LLM)-assisted discourse analysis of YouTube videos promoting and debunking health claims related to *gomutra* (cow urine) in India. It investigates how promotional content blends sacred traditional language with pseudo-scientific claims, creating a rhetorical register that LLMs trained on Western corpora struggle to analyze accurately. 

## Repository Structure
* `/data`: Information on how to request the dataset (see Data Access below).
* `/scripts/wer_evaluation`: Code to calculate the Word Error Rate (WER) of the automated transcriptions.
* `/scripts/f1_evaluation`: Code to calculate Precision, Recall, and F1-scores for LLM-based term extraction.
* `/scripts/cohens_kappa_analysis`: Code to calculate the inter annotator agreement for intensifiers annotation among the models.
*  `/scripts/gender_analysis`: Code for applying statistical analysis on gender.
* `/prompts`: The exact prompt templates used for GPT-4o, Gemini 2.5 Pro, and DeepSeek evaluations.

## Data Access & Ethical Considerations
The dataset consists of $N=30$ multilingual YouTube transcripts (English, Hindi, Urdu) related to gomutra discourse.

**Ethical Use Constraint:** To comply with platform guidelines and protect user privacy, no Personally Identifiable Information (PII) from viewers or commenters was collected. The aggregated dataset is released **strictly for non-commercial, academic research under an ethical use agreement**. 

*(Please mail to anamta@umich.edu to get access to data).*

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


### 3. Inter-Model Agreement (Cohen's Kappa) Evaluation
Text outputs containing intensifiers were generated using three distinct language models: Gemini, GPT-4o-mini, and DeepSeek. To evaluate the consistency and vocabulary overlap across different models and prompting conditions (Zero-shot vs. Few-shot; Formal vs. Friendly), we computed Cohen's Kappa scores on the extracted lexicon.The kappa_evaluator.py script computes inter-rater agreement using the following standard formulation:

$$\kappa=\frac{p_o-p_e}{1-p_e}$$

Where $p_o$ is the relative observed agreement among models (derived from a binary presence/absence matrix of all unique intensifiers in the corpus), and $p_e$ is the hypothetical probability of chance agreement. Agreement was analyzed pairwise at both the model level (e.g., Gemini vs. GPT-4o-mini) and the condition level (e.g., Formal vs. Friendly), with results mapped to standard interpretative thresholds.

### 4. Lexical Gender Analysis & Feature Normalization
To investigate gender-mediated differences in rhetorical strategies, we conducted a targeted lexical analysis comparing transcripts of single-speaker male and female videos. The gender_analysis.ipynb script quantifies the prevalence of five distinct linguistic categories: certainty amplifiers, universality markers, first-person singular pronouns, inclusive pronouns ("we/our"), and hyperbolic terms.To ensure a balanced comparison across transcripts of varying lengths, raw feature counts were standardized to occurrences per 1,000 words using the following formulation:

$$\text{Normalized Frequency}=\left(\frac{\text{Feature Count}}{\text{Total Tokens}}\right)\times 1000$$

The script aggregates these normalized frequencies to compute the mean usage rates for each gender cohort. This produces comparative statistical tables that surface macro-level linguistic divergences between male and female speakers across the corpus.

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
