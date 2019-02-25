# change raw data to arrays

def inOut(data,name):
	arrayData = []
	arrayDataMem = {}
	arrayDataMemList = [] 
	arrayDataDic = {}
	for i , val in enumerate(data[str(name)+'name']):
		arrayDataDic = {}
		arrayDataMem = {}
		arrayDataMemList = []
		arrayDataDic['name'] = val
		arrayDataDic['range'] = data[str(name)+'range'][i]
		memnumber = data[str(name)+'mems'][i]
		for x in range(1,int(memnumber)+1):
			arrayDataMem['name'] = data['mem'+str(name)+'name[' + str(val) + '][' + str(x) + ']'][0] 
			arrayDataMem['type'] = data['mem'+str(name)+'type[' + str(val) + '][' + str(x) + ']'][0]
			arrayDataMem['amount'] = data['mem'+str(name)+'amount[' + str(val) + '][' + str(x) + ']'][0]
			arrayDataMemList.append(arrayDataMem)
			arrayDataMem = {} 
		arrayDataDic['memship'] = arrayDataMemList
		arrayData.append(arrayDataDic)
	return arrayData

def rule(data):
	rulenumsArray = []
	rulenums = int(data['rulenums'][0])
	for i in range(1,rulenums+1):
		rulenumsArray.append(data['rule'+str(i)][0])
	return rulenumsArray
