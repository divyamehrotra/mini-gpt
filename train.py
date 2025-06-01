# Main training loop

from config import GPTConfig, TrainingConfig
from model import SimpleGPT
from dataset import load_dataset

def train():
    model_config = GPTConfig()
    train_config = TrainingConfig()
    model = SimpleGPT(model_config)
    dataset = load_dataset("data.txt")
    print("Training started...")

if __name__ == "__main__":
    train()
