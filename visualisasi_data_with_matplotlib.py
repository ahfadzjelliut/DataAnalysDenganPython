import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


table = pd.read_csv("")
table.head()
x_label = table['a']
plt.bar(x=np.arange(len(x_label)),height=table['a'])
plt.show()
