#!/usr/bin/python3
import pandas as pd
import numpy as np

def load_data_from_web_to_pandas(url, data_path):
	df = pd.read_csv(url)
	df.to_csv(data_path + 'boxdata.csv', index = False)
	return df

def clean_data_set(df, data_path):
	desc_df = df.describe()
	desc_df.to_csv(data_path + 'describing_original_data.csv')
	#print(df.dtypes)
	print(df[['beginNightLoading']].value_counts())


	'''
	Here modified data type of 'beginNightLoading' column with condition. if 'beginNightLoading' == 'Yes' then True else False
	'''
	df['beginNightLoading'] = np.where(df['beginNightLoading'] == 'Yes', True, False)
	print(df.beginNightLoading)	
	return df


if __name__=="__main__":
	data_url = 'http://drd.ba.ttu.edu/isqs6339/ex/L2.1/boxdata.csv'
	data_path = "/mnt/d/ubuntu/ttu_ms_ds/ds_bi/input_output_data/" 
	df = load_data_from_web_to_pandas(data_url, data_path)
	cdf = clean_data_set(df, data_path)

