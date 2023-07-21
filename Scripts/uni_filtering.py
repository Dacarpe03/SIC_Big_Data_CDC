import pandas as pd


UNI_RANKS_PATH = '../Datos/unis_completed_names_changed.csv'
QUEDU_PATH = '../Datos/Datos_QEDU.csv'


if __name__ == '__main__':
	uni_ranks_df = pd.read_csv(UNI_RANKS_PATH)
	quedu_df = pd.read_csv(QUEDU_PATH)
	
	nombres_uni = quedu_df['NOMBRE_UNIV'].apply(str.strip).unique()
	print(len(nombres_uni))
	
	uni_ranks_df['nombre_regional'] = uni_ranks_df['nombre_regional'].apply(str.strip)
	nombres_ranking = uni_ranks_df['nombre_regional'].unique()
	
	
	coinciden = []
	no_coinciden = []
	for nombre in nombres_uni:
		if nombre in nombres_ranking:
			#print("SI:", nombre)
			coinciden.append(nombre)
		else:
			print("NO:", nombre)
			no_coinciden.append(nombre)
	
	uni_ranks_df = uni_ranks_df[(uni_ranks_df['nombre_regional'].apply(str.strip).isin(nombres_uni))]
	print(uni_ranks_df)
	uni_ranks_df.to_csv('../Datos/uni_rankings_final.csv', index=False)
	


