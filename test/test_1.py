from IPython.display import display

import ffn
import pandas as pd

stock_no = '2330.TW'
stock_data = ffn.get([stock_no,'1101.TW'], start='2024-01-01', end='2024-12-27')
print(type(stock_data))
display(stock_data)  # 使用 display 函數來顯示資料
stock_data.plot()