import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [20, 21, 22],
    'grade': [8.5, 9.0, 9.7]
}

df = pd.DataFrame(data)
print(df)
