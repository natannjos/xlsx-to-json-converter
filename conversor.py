import pandas as pd


def xlsx_to_json(filepath):
	result = pd.read_excel(io=filepath).to_json(orient='records')
	f = open('result.json', "w")
	f.write(result)
	f.close()

