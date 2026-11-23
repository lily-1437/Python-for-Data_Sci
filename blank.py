import numpy as np
import pandas as pd

arr = np.array([1, 2, 3])          # a NumPy array
df = pd.DataFrame({"x": arr})      # a pandas table built from it
print(df)