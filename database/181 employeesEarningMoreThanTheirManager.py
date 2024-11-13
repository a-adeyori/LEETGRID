import pandas as pd

def find_employees(employee:pd.DataFrame) -> pd.DataFrame:
    merged_df=pd.merge(employee,employee,how='left', left_on='managerId',right_on='Id')

    merged_df=merged_df[merged_df['salary_employee'] > merged_df['salary_manager']]

    merged_df=merged_df.rename(columns={'name_employee':'name'})[['name']]

    return merged_df