# Try to import env
try:
    import env
except:
    print('Warning: no env.py file found. You will need to supply your own credentials!')

def libraries():
    """
    Import libraries. Takes no arguments and returns None
    """
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import env
    
    from scipy import stats
    from pydataset import data
    
    return None
    

def get_db_url(db_name,user=env.user,password=env.password,host=env.host):
    """
    At least needs you to supply a database name (db_name)

    Depends on env
    """
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'

def get_letter_grade(grade):
    """
    Returns a letter grade for an integer given

    Parameters
    ----------
    grade : int
        Expects an integer likely between 0 and 100.

    Returns
    -------
    str
        Based on value given, returns letter grade F-A as string.

    """
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'