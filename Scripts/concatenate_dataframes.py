import pandas as pd

DF_1 = '../Datos/uni1.csv'
DF_2 = '../Datos/uni2.csv'
RESULT_DF_NAME = '../Datos/unis.csv'


if __name__ == '__main__':
	df1 = pd.read_csv(DF_1)
	df2 = pd.read_csv(DF_2)
	
	df_concat = pd.concat([df1, df2], ignore_index=True, sort=False)
	df_concat.to_csv(RESULT_DF_NAME, index=False)
