import pandas as pd
import requests
from bs4 import BeautifulSoup


AD_INDEX_URL = 'https://www.adscientificindex.com/university/'
UNI_CSV = '../Datos/unis.csv'

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'}


def get_hindex(uni_soup):
	if len(uni_soup.find('tbody').find_all('td')) > 3:
		hindex_soup = uni_soup.find('tbody').find_all('td')[3]
		return int(hindex_soup.text)
	else:
		return -1

def get_fields_hindex(uni_soup):
	campos = uni_soup.find_all('td')[-12:]
	puntuaciones_campos = []
	for campo in campos:
		puntuaciones_campos.append(int(campo.text))
	return puntuaciones_campos
	
def get_uni_soup(nombre):
	nombre_nospace = nombre.replace(" ", "+")
	uni_url = f"{AD_INDEX_URL}{nombre_nospace}/"
	response = requests.get(uni_url, headers=HEADERS)
	html_text = response.text
	investigacion_soup = BeautifulSoup(html_text, 'html.parser')
	tables = investigacion_soup.find_all('table')
	return tables;
	
	
def create_ranking_df(nombre):
	columns = [
		"nombre",
		"posicion_hindex",
		"agricultura_forestal",
		"arte_diseno_cultura",
		"empresariales_administracion",
		"economicas",
		"educacion",
		"ingenieria_tecnologia",
		"historia_filosofia_teologia",
		"leyes_abogacia",
		"ciencias_salud",
		"ciencias_naturales",
		"ciencias_sociales",
		"otros"
		]
	uni_soup = get_uni_soup(nombre)
	if len(uni_soup) == 0:
		
		row_data = [nombre, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
		uni_ranking_df = pd.DataFrame([row_data], columns=columns)
		print("No:", nombre)
		return uni_ranking_df
		
	hindex = get_hindex(uni_soup[1])
	campos = get_fields_hindex(uni_soup[3])
	
	
	
	row_data = [nombre, hindex] + campos
	uni_ranking_df = pd.DataFrame([row_data], columns=columns)
	print("Si:", nombre)
	return uni_ranking_df
	
	
if __name__ == '__main__':
	
	unis_df = pd.read_csv(UNI_CSV)
	nombres_regionales = unis_df['nombre_regional']
	
	ranking_dataframes = []
	for nombre in nombres_regionales:
		uni_df = create_ranking_df(nombre)
		ranking_dataframes.append(uni_df)
		
	rankings_df = pd.concat(ranking_dataframes)
	rankings_df.to_csv('../Datos/rankings1.csv', index=False)
