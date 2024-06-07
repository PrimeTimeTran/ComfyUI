
Scatter Chart
```py
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [10, 15, 20, 25, 30],
    'size': [100, 200, 300, 400, 500]
}
df = pd.DataFrame(data)
df.plot(kind='scatter', x='x', y='y', s='size', alpha=0.5)
```
