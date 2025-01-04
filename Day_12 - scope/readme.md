# scope and namespace in **Python**

- Block scope doesn't count in python
- Functions create scope and namespace in **Python**

- Rules with changing global variables in **Python**:
  1. Reading global variable within function is fine
  2. To change, use global keyword within scope or function
  3. § Don't try to modify global store variables: To change, the best practice is to, pass the global value as argument to function, and then return the result to update global variables
```python

global_var = 10

def update(value):
    return value + 10

global_var = update(global_var)
```

- Constants use capitalized names
```python
PI = 3.14
```




