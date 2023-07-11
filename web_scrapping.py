import pandas as pd
from bs4 import BeautifulSoup
import requests

FILENAME = 'uni1.html'

WHED_URL = 'https://www.whed.net/institutions'


def getUniUrls(htmlFilename):
	"""
	Returns a list with the urls of universities with basic info
	
	Input:
		htmlFilename (string): The html to read
	
	Returns:
		uniUrls (list): A list with https links to the universitites info website
	"""
	uniUrls = []
	
	# Open the file in read mode
	with open(htmlFilename, 'r') as f:
		# Read the html text from the file
		file_text = f.read()
		
		# Parse html content with BeautifulSoup
		mySoup = BeautifulSoup(file_text, 'html5lib')
		
		# Get all 'a' tags from html that contain the universities links
		myUniversities = mySoup.find_all("a", {"class":"fancybox fancybox.iframe"}, href=True)
		
		# Loop to get the links from the 'a' tags
		for uni in myUniversities:
			uniUrls.append(uni['href'])
	
	return uniUrls
	
	
def createUnisDataFrame(uniUrls):
	"""
	Returns a dataframe with important info from the universities
	
	Input:
		uniUrls (list): A string list with the https links to the universities info
	
	Returns:
		unisDataFrame (pd.DataFrame): A dataframe with the info splitted in columns
	"""
	columns = [
		"nombre",
		"nombre_ingles",
		"nombre_regional",
		"siglas"
		]
		
	unisDataFrame = pd.DataFrame(columns=columns)
	for uniUrl in uniUrls:
		uniInfo = getUniDictionary(uniUrl, columns)


def getUniDictionary(uniUrl, columns):
	"""
	Creates a DataFrame with info from the university link
	
	Input:
		uniUrl (strint): The https link to make the request to that contains the university info
		columns (list): A list containing the name of the columns of the university info DataFrame
		
	Returns:
		uniDataFrame (pd.DataFrame): The dataframe containing university info
	"""
	response = requests.get(uniUrl)
	htmlText = response.text
	uniSoup = BeautifulSoup(uniUrl, columns)


if __name__ == "__main__":
	uniUrls = getUniUrls(FILENAME)
	uniDataframe = createUnisDataFrame(uniUrls)
		
		

