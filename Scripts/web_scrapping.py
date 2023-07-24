import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

FILENAME = '../Datos/uni2.html'
CSV_NAME = '../Datos/uni2.csv'



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
		mySoup = BeautifulSoup(file_text, 'html.parser')
		
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
	# Set the csv column names
	columns = [
		"nombre",
		"nombre_ingles",
		"nombre_regional",
		"siglas",
		"cuidad",
		"codigo_postal"
		]
		
	# Create an empty dataframe
	unisDataFrameList = []
	
	# Loop through the universities links and get the info
	for uniUrl in uniUrls:
		# Create the uni dataframe
		uniInfo = getUniDataFrame(uniUrl, columns)
		
		# Append the uni dataframe to the dataframe list
		unisDataFrameList.append(uniInfo)
	
	# Finally concatenate all the universities DataFrames
	unisDataFrame = pd.concat(unisDataFrameList)
	
	return unisDataFrame


def getUniDataFrame(uniUrl, columns):
	"""
	Creates a DataFrame with info from the university link
	
	Input:
		uniUrl (strint): The https link to make the request to that contains the university info
		columns (list): A list containing the name of the columns of the university info DataFrame
		
	Returns:
		uniDataFrame (pd.DataFrame): The dataframe containing university info
	"""
	# Request the html file of the university
	response = requests.get(uniUrl)
	
	# Read the html text
	htmlText = response.text
	
	# Parse the html text
	uniSoup = BeautifulSoup(htmlText, 'html.parser')
	
	# Get the name related data from the university
	uniNameData = getNameDataFromSoup(uniSoup)
	
	# Get city related data from the university
	uniCityData = getCityDataFromSoup(uniSoup)
	
	# Concatenate al university data
	uniData = uniNameData + uniCityData
	
	# Create the university DataFrame
	uniDataFrame = pd.DataFrame([uniData], columns=columns)
	
	return uniDataFrame


def getNameDataFromSoup(uniSoup):
	"""
	Searches in the parsed html text all the data of the university related to the name
	
	Input:
		uniSoup (BeautifulSoup): A parsed html text with uni info
	
	Returns:
		nameDataList (list): A list of strings containing the name, english name, regional name and initials of the university
	"""
	# Access the div tag where the name info is in the html
	detailSoup = uniSoup.find('div', {'class':'detail_right'})
	
	# Inside the above tag, get the english name div
	englishName = detailSoup.find('div').text.strip()

	# Get the unparsed names div tag (contains regional name, name and initials)
	names = detailSoup.find('div', {'class':'detail_name'}).get_text(strip=True, separator='\n').splitlines()
	
	# Parse the above div tag to get the names
	name, regionalName, initials = parseNames(names)
	return [name, englishName, regionalName, initials]


def getCityDataFromSoup(uniSoup):
	"""
	Searches in the parsed html text all the data of the university related to the city
	
	Input:
		uniSoup (BeautifulSoup): A parsed html text with uni info
	
	Returns:
		cityData (list): A string list containing name of the city, post code
	"""
	
	# Retrieve the city name
	cityName = getCityField(uniSoup, 'City')
	cityPostCode = getCityField(uniSoup, 'Post Code')
	cityData = [cityName, cityPostCode]
	return cityData


def getCityField(uniSoup, fieldName):
	"""
	Retrieves a city data field and returns it as a string
	Input:
		
	Return:
		cityField (string):
	"""
	citySoup = uniSoup.find(string=re.compile(fieldName)).parent.parent
	cityField = citySoup.find('span', {'class': 'contenu'}).text.strip()
	return cityField
		
		
def parseNames(names):
	"""
	Parses a name list into three different names if possible
	
	Input:
		names (list): A string list containing unparsed names
	"""
	# The spanish original name is in the last position of the list and it contains the initials
	nameAndInitials = names[-1].split("(")
	initials = ''
	
	# If there exists an initial, parse it
	if len(nameAndInitials) == 2:
		initials = nameAndInitials[1].replace(")", "")
	
	# The name is the first field of the last element of the names list
	name = nameAndInitials[0]
	# By default the regional name equals to the spanish name
	regionalName = name
	
	# If there is a regional name, it is in the first place of the list
	if len(names)  ==  2:
		regionalName = names[0]
	
	# Return the parsed names
	return name, regionalName, initials


def saveDataFrame(unisDataFrame, csvName):
	"""
	Saves the dataframe in the working directory, with comma as separators and no index
	Input:
		unisDataFrame (pd.DataFrame): A dataframe with scrapped data from the universities
	
	Returns:
		None
	"""
	unisDataFrame.to_csv(csvName, index=False)
	
	
if __name__ == "__main__":
	uniUrls = getUniUrls(FILENAME)
	uniDataFrame = createUnisDataFrame(uniUrls)
	saveDataFrame(uniDataFrame, CSV_NAME)
		

