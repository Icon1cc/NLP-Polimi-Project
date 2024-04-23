from datasets import load_dataset

# Load the dataset with timeout
dataset = load_dataset("medalpaca/medical_meadow_medical_flashcards", timeout=200)

print(dataset)
