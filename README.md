# Medical Question Answering with Medical Meadow Dataset

## Project Overview

This project focuses on applying Natural Language Processing techniques to analyze the Medical Meadow Medical Flashcards dataset and build a model capable of answering medical questions. The aim is to leverage machine learning models trained on a corpus of medical flashcards provided to GPT-3.5 to create accurate and relevant medical knowledge question-answer pairs.

## Dataset

The Medical Meadow Medical Flashcards dataset contains medical curriculum flashcards used to train GPT-3.5 for generating medical knowledge question-answer pairs.

- **Dataset Source:** [Medical Meadow Medical Flashcards on Hugging Face](https://huggingface.co/datasets/medalpaca/medical_meadow_medical_flashcards)
- **Relevant Paper:** [Exploration of Medical Meadow Medical Flashcards](https://arxiv.org/pdf/2304.08247.pdf)

## Tasks

1. **Preliminary Analysis:**
   - Descriptive statistics of the dataset.
   - Visualization of document clusters.
   - Indexing and keyword search capabilities.
   - Word2Vec embeddings to investigate the dataset semantics.

2. **Model Training:**
   - Training a linear classifier and comparing its performance with a deep learning model, specifically BERT, to answer medical questions.

3. **Extensions:**
   - Evaluation of model performance on related datasets.
   - Potential use of text-to-speech and speech-to-text models to enhance interaction.

## Project Structure

- `notebooks/` - Jupyter notebooks containing all the analyses and model training processes.
- `data/` - Scripts and utilities for data handling and preprocessing.
- `models/` - Trained models and their respective configurations.
- `Docs/` - Additional documentation and resources related to the project.

## Installation and Usage

Instructions for setting up the project environment and running the notebooks:

git clone https://github.com/Icon1cc/NLP-Polimi-Project.git
cd NLP-Polimi-Project
pip install -r requirements.txt

## Authors

- Rishabh Tiwari
- Dan Lionis
- Federica Vinciguerra
- Felipe Bagni