Top 10 Python Modules for Beginners

1. Numpy

```py
import numpy as np
array = np.array([[1, 2], [3, 4]])
print(np.linalg.inv(array))  # Output: Inverse of the array

```

2. Pandas

```py
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df.describe())  # Output: Summary statistics

```

3. Scipy

```py
from scipy.optimize import minimize
result = minimize(lambda x: x**2, 0)
print(result.x)  # Output: Minimum value

```

4. Scikit-Learn

```py
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)


```

5. TensorFlow

```py
import tensorflow as tf
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=5)

```

6. Djano

```py
# In a Django project, urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

7. Flask

```py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)
```

8. Celery

```py
from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y

```

9. Sql Alchemy

```py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///:memory:')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

Base.metadata.create_all(engine)
```

10. PyTorch

```py
import torch
import torch.nn as nn

class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        return self.fc(x)

model = SimpleNN()
x = torch.randn(10)
output = model(x)
```
