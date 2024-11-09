import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products[(products['low_fats']=='Y')&(products['recyclable']=='Y')]

    df_true = df[['product_id']] 

    return df_true