import pandas as pd
import numpy as np
import datetime

class SyntheticData():
    def __init__(self,size):
        '''
        size: number of data points to generate
        '''
        self.n = size
        self.data = pd.DataFrame([])
    
    def generate_data(self,data, p):
        '''
        data: array/list of choices
        p: probabilities of choices
        '''
        gen_data  = np.random.choice(data, size = self.n, p = p)
        return gen_data

    def merge(self,left,right,on,how = "left",indicator = "match",validate=None):

        merged = pd.merge(
        left, # left dataframe
        right,  # joining answers to left df
        how=how, # left join
        on=on, # join on column `Parent Code`
        indicator=indicator,
        validate=validate
        )    
        return merged

    def generate_date(self,start_date = datetime.datetime(2020,2,14),end_date = datetime.datetime.now()):
        days_between = (end_date - start_date).days
        random_day = np.random.randint(low=1,high=days_between)
        random_date = start_date + datetime.timedelta(days=random_day)
        return random_date
        


# def random_genders(genders, p, size):
#     '''
#     genders: array of genders 
#     p: probability associated with those genders
#     size: number of samples to draw
#     '''
#     return np.random.choice(genders,size=size,p=p)

# def random_location()
