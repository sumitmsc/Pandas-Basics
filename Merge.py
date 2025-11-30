import pandas as pd

emp = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["John", "Sarah", "Amit"]
})

salary = pd.DataFrame({
    "id": [1, 2, 3],
    "salary": [50000, 60000, 55000]
})

merged = pd.merge(emp, salary, on="id")

print("Merged Data:")
print(merged)
