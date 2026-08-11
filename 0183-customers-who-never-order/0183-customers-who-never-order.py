import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders_something = orders["customerId"]
    customers_zero = customers[~customers['id'].isin(orders_something)]
    customers_zero = customers_zero[["name"]]
    customers_zero.columns = ["Customers"]    
    return customers_zero