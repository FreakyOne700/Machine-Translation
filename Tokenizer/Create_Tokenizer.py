from tokenizers import Tokenizer, models, trainers, pre_tokenizers

# Initialize a WordLevel tokenizer model (keeps only full words)
tokenizer = Tokenizer(models.WordLevel(unk_token="<unk>"))

# Set a pre-tokenizer to split input by whitespace
tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()

# Configure the WordLevel trainer with special tokens and vocab size
trainer = trainers.WordLevelTrainer(
    vocab_size=100000,
    special_tokens=["<pad>", "<unk>", "<s>", "</s>","<en>","<es>","<fr>"]
)

# Train the tokenizer on your dataset
tokenizer.train(files=["..\Datasets\Dataset.csv"], trainer=trainer)

# Save the tokenizer to disk
tokenizer.save("Tokenizer\\tokenizer.json")

print("Tokenizer trained and saved successfully.")