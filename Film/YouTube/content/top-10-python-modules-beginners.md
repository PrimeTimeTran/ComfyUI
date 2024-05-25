Top 10 Python Modules for Beginners

1. Math

```py
import math
print(math.sqrt(16))  # Output: 4.0
print(math.pi)  # Output: 3.141592653589793
```

2. Random

```py
import random
print(random.randint(1, 10))  # Output: Random number between 1 and 10
print(random.choice(['apple', 'banana', 'cherry']))  # Output: Randomly chosen item
```

3. Datetime

```py
from datetime import datetime
now = datetime.now()
print(now)  # Output: Current date and time
```

4. OS

```py
import os
print(os.getcwd())  # Output: Current working directory
os.mkdir('new_folder')  # Creates a new directory

```

5. sys

```py
import sys
print(sys.version)  # Output: Python version
sys.exit()  # Exits the program
import re
pattern = re.compile(r'\d+')
match = pattern.search('The year is 2024')
print(match.group())  # Output: 2024
```

6. JSON

```py
import json
data = {'name': 'John', 'age': 30}
json_data = json.dumps(data)
print(json_data)  # Output: '{"name": "John", "age": 30}'
parsed_data = json.loads(json_data)
print(parsed_data)  # Output: {'name': 'John', 'age': 30}


```

7. CSV

```py
import csv
with open('example.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age'])
    writer.writerow(['Alice', 30])

```

8. RE

```py
import re
pattern = re.compile(r'\d+')
match = pattern.search('The year is 2024')
print(match.group())  # Output: 2024
```

9. Collections

```py
from collections import Counter
counts = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
print(counts)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})

```

10. Itertools

```py
import itertools
for item in itertools.permutations([1, 2, 3]):
    print(item)
# Output: (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)
```
