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

# 品牌平均车型投诉（降序）
# result3 = result1.merge(df.groupby(['brand'])['car'].agg(['count'])
# result3 = df.groupby(['brand']).agg({'id':['count'], 'car_model':['count']})
# print(result3)
# result3 = df.groupby(['brand', 'car_model'])['id'].agg(['count'])
# result3 = result3.groupby(['brand'])['car_model'].agg(['count'])
# print(result3)



