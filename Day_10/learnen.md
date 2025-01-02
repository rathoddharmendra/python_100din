
<!-- new_learnen -->
### inner function

```python
def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)
```

### storing function as a variable

```python
def add_function(n1, n2):
    return n1 + n2

new_function = add_function
new_function(5, 10)
```