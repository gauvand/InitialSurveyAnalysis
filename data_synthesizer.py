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
        


# def random_genders(genders, p, size):
#     '''
#     genders: array of genders 
#     p: probability associated with those genders
#     size: number of samples to draw
#     '''
#     return np.random.choice(genders,size=size,p=p)

# def random_location()
