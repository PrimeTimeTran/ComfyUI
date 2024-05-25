Top 10 Python Tips for Advanced

- Unpacking

```py
a, *b, c = [1, 2, 3, 4, 5]
# a = 1, b = [2, 3, 4], c = 5
```

- Type Hinting

```py
def greeting(name: str) -> str:
    return 'Hello ' + name
```

- Counter
- Yield
- List comprehensions
- Generator functions
- Lambda functions
- Context managers(with)
- Meta classes

```py
class Meta(type):
    def __new__(cls, name, bases, attrs):
        print(f'Creating class {name}')
        return super(Meta, cls).__new__(cls, name, bases, attrs)

class MyClass(metaclass=Meta):
    pass
```

-Coroutines

```py
import asyncio

async def main():
    print('Hello')
    await asyncio.sleep(1)
    print('World')

asyncio.run(main())
```
