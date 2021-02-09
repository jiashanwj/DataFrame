import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)

# Step1:数据加载
df = pd.read_csv('./car_complain.csv')

# Step2:数据预处理，拆分Problem类型为多个字段
df = df.drop(['problem'], axis=1).join(df.problem.str.get_dummies(','))

# Step3:数据统计
def f(x):
    x = x.replace('一汽-大众', '一汽大众')
    return x
df['brand'] = df['brand'].apply(f)

# 对数据进行探索：品牌投诉总数
result1 = df.groupby(['brand'])['id'].agg(['count'])
print('品牌投诉总数：')
print(result1)

# 对数据进行探索：车型投诉总数
result2 = df.groupby(['car_model'])['id'].agg(['count'])
print('车型投诉总数：')
print(result2)

# 品牌平均车型投诉（降序）: 品牌投诉总数/车型数量 = 品牌平均车型投诉
temp = df.drop_duplicates(subset='car_model')
temp = temp.groupby(['brand'])['car_model'].agg(['count'])
result3 = pd.merge(left=result1, right=temp, left_on='brand', right_on='brand', how='outer')
result3['品牌平均车型投诉'] = result3['count_x'] / result3['count_y']
result3 = result3.sort_values('品牌平均车型投诉', ascending=False)
print('品牌平均车型投诉最多的为：')
print(result3.head(1))
