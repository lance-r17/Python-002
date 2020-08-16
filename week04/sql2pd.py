# 作业背景：在数据处理的步骤中，可以使用 SQL 语句或者 pandas 加 Python 库、函数等方式进行数据的清洗和处理工作。

# 因此需要你能够掌握基本的 SQL 语句和 pandas 等价的语句，利用 Python 的函数高效地做聚合等操作。

# 请将以下的 SQL 语句翻译成 pandas 语句：

import pandas as pd
import os

pwd = os.path.dirname(os.path.realpath(__file__))
data_file = os.path.join(pwd,'data.csv')
df = pd.read_csv(data_file)

# 1. SELECT * FROM data;
print(f'输出全部内容:')
print('='*30)
print(df)
print('='*30)

# 2. SELECT * FROM data LIMIT 10;
print(f'输出前10行数据:')
print('='*30)
print(df.head(10))
print('='*30)

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
print(f'输出id列:')
print('='*30)
print(df['id'])
print('='*30)

# 4. SELECT COUNT(id) FROM data;
print(f'输出id个数:')
print('='*30)
print(df['id'].count())
print('='*30)

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
print(f'输出id<1000且age>30的数据:')
print('='*30)
print(df[df['id']<1000][df['age']>30])
print('='*30)

table1_file = os.path.join(pwd,'table1.csv')
table2_file = os.path.join(pwd,'table2.csv')
table1 = pd.read_csv(table1_file)
table2 = pd.read_csv(table2_file)

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
print(f'输出table1的id和order_id的数量:')
print('='*30)
print(table1.groupby('id').order_id.nunique())
print('='*30)

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
print(f'输出table1和table2 inner join的结果:')
print('='*30)
print(pd.merge(table1, table2, on='id', how='inner'))
print('='*30)

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
print(f'输出table1和table2拼接的结果:')
print('='*30)
print(pd.concat([table1, table2]))
print('='*30)

# 9. DELETE FROM table1 WHERE id=10;
print(f'删除table1中id=10的数据:')
print('='*30)
print(table1[table1['id'] != 10])
print('='*30)

# 10. ALTER TABLE table1 DROP COLUMN column_name;
print(f'删除table1中的order_id列:')
print('='*30)
print(table1.drop('order_id', axis = 1))
print('='*30)