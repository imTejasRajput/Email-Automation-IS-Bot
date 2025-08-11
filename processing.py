
import pandas as pd



def clean_data(file):
    data=pd.read_excel(file)
    return data.assign(FirstName=lambda df:df.Name.str.strip().str.split(' ',),Email=lambda df:df.Email.str.strip())


