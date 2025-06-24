machine_translation_project/
│
├── README.md
├── requirements.txt
├── setup.py
│
├── config/
│   └── config.yaml                # Paths, hyperparameters, language pairs, etc.
│
├── data/
│   └── raw/                       # Downloaded raw datasets (Multi30K, etc.)
│   └── processed/                 # Tokenized, cleaned, prepared datasets
│
├── src/
│   ├── __init__.py
│   ├── data_ingestion.py         # Download and load datasets (Multi30k)
│   ├── preprocessing.py          # Tokenization, vocabulary setup, batching
│   ├── model.py                  # Transformer model architecture
│   ├── train.py                  # Trainer class with loss, optimizer, training loop
│   ├── evaluate.py               # Evaluation metrics (BLEU, etc.)
│   └── utils.py                  # Seed setter, logging, save/load helpers
│
├── notebooks/
│   └── eda.ipynb                 # Exploratory data analysis or training logs
│
├── scripts/
│   ├── run_training.py           # Main entry point for training
│   ├── run_eval.py               # Evaluation runner
│   └── predict.py                # Translate a sentence or file
│
└── outputs/
    └── models/                   # Saved models
    └── logs/                     # Logs and metrics
