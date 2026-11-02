
import torch
import torch.nn as nn
import time

x = torch.randn(1, 100, 16)
hyena = nn.Conv1d(16, 16, 3, padding=1)
transformer = nn.TransformerEncoder(nn.TransformerEncoderLayer(16, 4, batch_first=True), 1)

for name, model, data in [("Hyena", hyena, x.transpose(1, 2)), ("Transformer", transformer, x)]:
    start = time.time()
    output = model(data)
    print(name, "Time:", round(time.time()-start, 5), "seconds")
    print("Output shape:", output.shape)
