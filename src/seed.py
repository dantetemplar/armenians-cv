def seed_everything(seed: int, ensure_reproducibility: bool = True) -> None:
    """
    https://pytorch.org/docs/stable/notes/randomness.html
    """
    import random
    import numpy as np
    import torch

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if ensure_reproducibility:
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
        torch.use_deterministic_algorithms(True)
        print("Deterministic behavior has been enabled.")
    print(f"Seed {seed} has been set.")
