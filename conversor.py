import pandas as pd


def xlsx_to_json(filepath, lines=False):
	"""Function that converts a xlsx format file into json and creates other file with the result
	(filepath=string, lines=bool)
	The filepath parameter informs the path to the xlsx file to be converted 
	The lines parameter informs if the output will be in one or many lines
	"""
	result = pd.read_excel(io=filepath).to_json(orient='records', lines=lines)
	f = open('result.json', "w")
	f.write(result)
	f.close()

