import torch
import torch.nn as nn
import torch.optim as optim


##### Reproducibility
SEED = 2

random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
torch.cuda.manual_seed(SEED)
torch.backends.cudnn.deterministic = True