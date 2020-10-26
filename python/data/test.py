# import numpy as np

# A = np.linspace(0, 2, 5)
# print(A)
# print(np.diff(A) ** 2)
# B = np.diff(A)*2
# print(B)
# print(B == np.ones(4))


import pandas as pd
import matplotlib.pyplot as plt 

df = pd.DataFrame({"国名":["日本","アメリカ","イタリア","フランス", "ロシア", "ブラジル", "イギリス"], "人口/万人":[12700, 32800, 6000, 6700, 14500, 20900, 6600]})

df = df.sort_values("人口/万人")
plt.rcParams["font.family"] = "AppleGothic"
plt.bar(df["国名"], df["人口/万人"])
plt.ylabel("人口(万人)")
plt.show()