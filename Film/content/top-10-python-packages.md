Top 10 Python Packages

1. Numpy

```py
import numpy as np
array = np.array([1, 2, 3])
print(array)
```

2. Pandas

```py
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df)

```

3. Matplotlib

```py
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()

```

4. SciPy

```py

```

5. Scikit-learn

```py
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit([[0, 0], [1, 1]], [0, 1])

```

6. TensorFlow

```py
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
tf.print(hello)

```

7. Requests

```py
import requests
response = requests.get('https://api.github.com')
print(response.json())

```

8. Flask

```py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()

```

9. Beautiful Soup

```py
from bs4 import BeautifulSoup
html_doc = "<html><head><title>Page Title</title></head><body><p>Paragraph</p></body></html>"
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.title.string)

```

10. Pytest

```py
def test_sum():
    assert sum([1, 2, 3]) == 6

if __name__ == "__main__":
    import pytest
    pytest.main()
```
