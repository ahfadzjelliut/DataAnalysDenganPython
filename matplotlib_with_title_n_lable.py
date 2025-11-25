import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

table = pd.read_csv("a")
table.head()

x_label = table['a']
plt.bar(x=np.arange(len(x_label)),height=table['a'])
plt.xticks(np.arange(len(x_label)),table['a'], rotation=30)
plt.show()
