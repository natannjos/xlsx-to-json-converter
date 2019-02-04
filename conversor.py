import pandas as pd


def xlsx_to_json(filepath):
	print('Rodou')
	result = pd.read_excel(io=filepath).to_json(orient='records')
	f = open('result.json', "w")
	f.write(result)
	f.close()
	print('Terminou')
