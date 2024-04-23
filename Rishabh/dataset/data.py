from datasets import load_dataset

try:
    # Load the dataset
    dataset = load_dataset("medalpaca/medical_meadow_medical_flashcards")
    print(dataset)

    # Save the dataset to disk
    save_path = '/Users/icon1c/Documents/Semester 2/Natural Language Processing/NLP-Polimi-Project/Rishabh/dataset'
    dataset.save_to_disk(save_path)
    print(f"Dataset saved successfully to {save_path}")
except Exception as e:
    print(f"An error occurred: {e}")
