# Virtual Columns in Pandas DataFrame

Implementation of `add_virtual_column` function that adds a computed column to a pandas DataFrame based on a mathematical expression.

## Usage

```python
from solution import add_virtual_column
import pandas as pd

fruits_sales = pd.DataFrame({
    "fruit": ["apple", "banana", "orange"],
    "quantity": [10, 5, 8],
    "price": [2.5, 1.2, 3.0]
})

sales_total = add_virtual_column(fruits_sales, "quantity * price", "total")
result_add = add_virtual_column(fruits_sales, "quantity + price", "sum")
result_sub = add_virtual_column(fruits_sales, "quantity - price", "difference")
```

## Supported operations

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)

## Running tests

```bash
pip install pytest pandas
pytest test_virtual_column\ 1.py -v
```
