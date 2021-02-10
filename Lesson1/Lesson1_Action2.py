import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)

data = [[68, 65, 30], [95, 76, 98], [98, 86, 88], [90, 88, 77], [80, 90, 90]]
columns = ['语文', '数学', '英语']
index = ['张飞', '关羽', '刘备', '典韦', '许褚']
df = pd.DataFrame(data=data, index=index, columns=columns)
print(df.describe())

# 按总分排序
df['总成绩'] = df.sum(axis=1)
print(df.sort_values('总成绩', ascending=False))