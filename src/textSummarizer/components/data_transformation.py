import os
from src.textSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk

from src.textSummarizer.config.configuration import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self, examples_batch):
        input_encodings = self.tokenizer(examples_batch['dialogue'], max_length=128, truncation=True)

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(examples_batch['summary'], max_length=64, truncation=True)

        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    
    def convert(self):
        data_samsum = load_from_disk(self.config.data_path)
        data_samsum_pt = data_samsum.map(self.convert_examples_to_features, batched=True)
        data_samsum_pt.save_to_disk(os.path.join(self.config.root_dir, 'data_samsum_pt'))

