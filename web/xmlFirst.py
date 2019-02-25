from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from ElementTree_pretty import prettify
from arrayior import inOut, rule

def dataToXml(data):
	
	rules = rule(data)
	inputs = inOut(data,'input')
	outputs = inOut(data,'output')

	arrayData = [{'name': 'Mark', 'range': '[0 21]', 'memship': [{'name': 'low', 'type': 'trapmf', 'amount': '[0 10 2 31]'}, {'name': 'high', 'type': 'trimf', 'amount': '[0 10 2 35]'}]}, {'name': 'sysmark', 'range': '[0 22]', 'memship': [{'name': 'hard', 'type': 'trimf', 'amount': '[0 10 2 32]'}]}]
	lenIn = len(inputs)
	lenOut = len(outputs)
	lenRule = len(rules)

	Fuzzy = Element('Fuzzy')

	comment = Comment('Xml File For Mirab Fuzzy Control System')
	Fuzzy.append(comment)
	Input = SubElement(Fuzzy,'Input', inputnums=str(lenIn))
	Output = SubElement(Fuzzy,'Output', outputnume=str(lenOut))
	Rule = SubElement(Fuzzy,'Rule', rulenums=str(lenRule))
	# memshipFunctions = len(arrayData[0]['memship'])
	# print(memshipFunctions)
	# print(arrayData)
	for i, val in enumerate(outputs, 1):
		output = SubElement(Output,'output'+str(i),outputmems=str(len(val['memship'])) ,name=val['name'], range=val['range'])
		for j, value in enumerate(val['memship'], 1):
			MF = SubElement(output, 'MF'+str(j), name=value['name'], type=value['type'])
			MF.text = value['amount']

	for i, val in enumerate(inputs, 1):
		input = SubElement(Input,'input'+str(i),inputmems=str(len(val['memship'])) ,name=val['name'], range=val['range'])
		for j, value in enumerate(val['memship'], 1):
			MF = SubElement(input, 'MF'+str(j), name=value['name'], type=value['type'])
			MF.text = value['amount']

	for i, val in enumerate(rules, 1):
		rule = SubElement(Rule, 'rule'+str(i))
		rule.text = val
	FuzzyFile = prettify(Fuzzy)
	return FuzzyFile


# a = ElementTree(Fuzzy).write(sys.stdout, method='xml')