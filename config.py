# configuration settings

class GPTConfig:
    def __init__(self):
        self.block_size = 512
        self.n_layer = 8
        self.n_head = 8
        self.n_embed = 512
        self.dropout = 0.2
        self.bias = False
        self.use_rotary = False

class TrainingConfig:
    def __init__(self):
        self.batch_size = 64
        self.max_iters = 30000
        self.learning_rate = 6e-4
        self.weight_decay = 0.1
        self.grad_clip = 1.0
        self.warmup_iters = 1000
