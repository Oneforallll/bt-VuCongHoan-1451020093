import pandas as pd

series_ex = {"a":[1, 3, 5, 7, 9], "b":[-2, 4, 6, 8, 22], "c":[23, 45, 44, 54, 64]}
series_data = pd.DataFrame(series_ex)
print(series_data)
print("Xuat ra cot dau cua series")
print(series_data.iloc[:, 0])