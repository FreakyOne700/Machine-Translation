🧠 Machine-Translation
A multilingual machine translation system built from scratch using custom datasets, tokenizers, and models. The goal is to build a flexible and modular translation pipeline that can be easily extended to new languages and models.

## 📁 Project Structure
├── Datasets/               # Preprocessed or raw language datasets  
├──── spa(Example)          # Contain source -> target translations
├── Model/                  # Model architecture and training scripts  
├──── MAIN.ipynb            # Main 
├── Tokenizer/              # Tokenizer scripts or configs (e.g., SentencePiece, BPE)  
├──── Create_Tokenizer.py
├── Create_Dataset.ipynb    # Jupyter notebook to create or preprocess datasets  
└── README.md                

## 🔧 Features

 - Multilingual support (e.g., English ↔ French, English ↔ Spanish)
 - Custom tokenizer training (SentencePiece or other)
 - Clean dataset preprocessing pipeline
 - Easy integration and extension

## 📦 Requirements

- Python 3.8+  
- PyTorch or TensorFlow  
- Hugging Face Transformers  
- SentencePiece  
- Jupyter Notebook
## 🚀 Getting Started
- Create Dataset
Open Create_Dataset.ipynb and generate your parallel corpora.
- Tokenizer Training
Use scripts under Tokenizer/ to train or load your tokenizer.
- Model Training
Modify and run training scripts inside the Model/ directory.
- Evaluation
Evaluate translation quality using BLEU, ROUGE, or other metrics.

