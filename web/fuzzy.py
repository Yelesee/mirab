import re

class Fuzzy:
	def __init__(self,input_amount):
		self.input_amount = input_amount

	def fuzzification(self,functype,a,l,r,b=0):

		if functype == 'Trapezoid':
			try:
				if self.input_amount >= a and self.input_amount <= l:
					input_fuzzy = float(self.input_amount-a)/float(l-a)
				elif self.input_amount > l and self.input_amount < r:
					input_fuzzy = 1.0
				elif self.input_amount >= r and self.input_amount <= b:
					input_fuzzy = float(self.input_amount-b)/float(r-b)
				else:
					input_fuzzy = 0.0
				return input_fuzzy
			except ZeroDivisionError:
				input_fuzzy = 1.0
				return input_fuzzy

		elif functype == 'Triangle':
			try:
				if self.input_amount >= a and self.input_amount <= l:
					input_fuzzy = float(self.input_amount-a)/float(l-a)
				elif self.input_amount > l and self.input_amount <= r:
					input_fuzzy = float(self.input_amount-r)/float(l-r)
				else:
					input_fuzzy = 0.0
				return input_fuzzy
			except ZeroDivisionError:
				input_fuzzy = 1.0
				return input_fuzzy
		else:
			return None

class Rules:
	def __init__(self,rules=[],input_dicts={},rules_fuzzy_amount={},amounts_min={}):
		self.rules = rules
		self.input_dicts = input_dicts
		self.rules_fuzzy_amount = rules_fuzzy_amount
		self.amounts_min = amounts_min

	def addRule(self,rule):
		self.rules.append(rule)

	def getRules(self):
		return self.rules

	def setFuzzifiedInputs(self,input_name,input_dict):
		self.input_dicts[input_name] = input_dict

	def getFuzzifiedInputs(self):
		return self.input_dicts

	def getAmounts(self):
		for key, value in self.rules_fuzzy_amount.iteritems():
			min_value = min(value)
			self.amounts_min[key] = min_value
		return self.amounts_min

	def clearRules(self):
		self.rules = []

	def clearInputDicts(self):
		self.rules_fuzzy_amount = {}
	def processRule(self,rule,rule_number):
		rule_number = str(rule_number)
		inputs = self.input_dicts
		Output = 'PracLevel'
		items = re.findall(r'(?:IF\s|AND\s|THEN\s)(?P<token>.+?)(?=\s*(?:AND|THEN|$))',rule)
		del items[-1]
		for item in items:
			if item[0] == '(':
				x = re.search(r'^[\(A-z\s]{5}(.*)\)$',item)
				input_name_with_member = x.group(1)
				y = re.search(r'(.*)[.]',input_name_with_member)
				input_name = y.group(1)
				y = re.search(r'[.](.*)',input_name_with_member)
				input_name_member = y.group(1)
				input_name_member = input_name+'.'+input_name_member
				for key, value in inputs.iteritems():
					if key == input_name:
						for key, value in value.iteritems():
							if key == input_name_member:
								if rule_number in self.rules_fuzzy_amount:
									value = 1-value
									value = "%0.1f" % value
									value = float(value)
									self.rules_fuzzy_amount[rule_number].append(value)
								else:
									self.rules_fuzzy_amount[rule_number] = []
									self.rules_fuzzy_amount[rule_number].append(value)
			else:
				input_name_with_member = re.search(r'(.*)[.]',item)
				input_name = input_name_with_member.group(1)
				y = re.search(r'[.](.*)',item)
				input_name_member = y.group(1)
				input_name_member = input_name+'.'+input_name_member
				for key, value in inputs.iteritems():
					if key == input_name:
						for key, value in value.iteritems():
							if key == input_name_member:
								if rule_number in self.rules_fuzzy_amount:
									self.rules_fuzzy_amount[rule_number].append(value)
								else:
									self.rules_fuzzy_amount[rule_number] = []
									self.rules_fuzzy_amount[rule_number].append(value)
class FuzzyLogic(Fuzzy, Rules):
	def __init__(self,mark,study,hardness,sysmark):
		self.mark = mark
		self.study = study
		self.hardness = hardness
		self.sysmark = sysmark

	def clearInputDicts(self):
		self.input_dicts = {}

	def fuzzification(self):
		# clearInputDicts()
		mark = Fuzzy(self.mark)
		mark_fuzzy_weak = mark.fuzzification('Trapezoid',0,0,11,12.5)
		mark_fuzzy_middle = mark.fuzzification('Trapezoid',11,12.5,14.5,16)
		mark_fuzzy_good = mark.fuzzification('Trapezoid',14.5,16,17.5,18.5)
		mark_fuzzy_excellent = mark.fuzzification('Trapezoid',17.5,18.5,20,20)

		mark_dict = {'Mark.Weak': mark_fuzzy_weak, 'Mark.Middle': mark_fuzzy_middle, 'Mark.Good': mark_fuzzy_good, 'Mark.Excellent': mark_fuzzy_excellent}
		mdict = Rules()
		mdict = mdict.setFuzzifiedInputs('Mark',mark_dict)
		
		study = Fuzzy(self.study)
		study_fuzzy_low = study.fuzzification('Trapezoid',0,0,2,3)
		study_fuzzy_middle = study.fuzzification('Trapezoid',2,3,4,5)
		study_fuzzy_high = study.fuzzification('Trapezoid',4,5,6,6)

		study_dict = {'Study.Low': study_fuzzy_low, 'Study.Middle': study_fuzzy_middle, 'Study.High': study_fuzzy_high}
		sdict = Rules()
		sdict = sdict.setFuzzifiedInputs('Study',study_dict)

		hardness = Fuzzy(self.hardness)
		hardness_fuzzy_easy = hardness.fuzzification('Triangle',0,0,2)
		hardness_fuzzy_middle = hardness.fuzzification('Triangle',0,2,4)
		hardness_fuzzy_hard = hardness.fuzzification('Triangle',2,4,4)

		hardness_dict = {'Hardness.Easy': hardness_fuzzy_easy, 'Hardness.Middle': hardness_fuzzy_middle, 'Hardness.Hard': hardness_fuzzy_hard}
		hdict = Rules()
		hdict = hdict.setFuzzifiedInputs('Hardness',hardness_dict)

		sysmark = Fuzzy(self.sysmark)
		sysmark_fuzzy_weak = sysmark.fuzzification('Trapezoid',0,0,11,12.5)
		sysmark_fuzzy_middle = sysmark.fuzzification('Trapezoid',11,12.5,14.5,16)
		sysmark_fuzzy_good = sysmark.fuzzification('Trapezoid',14.5,16,17.5,18.5)
		sysmark_fuzzy_excellent = sysmark.fuzzification('Trapezoid',17.5,18.5,20,20)

		sysmark_dict = {'Sysmark.Weak': sysmark_fuzzy_weak, 'Sysmark.Middle': sysmark_fuzzy_middle, 'Sysmark.Good': sysmark_fuzzy_good, 'Sysmark.Excellent': sysmark_fuzzy_excellent}
		sysdict = Rules()
		sysdict = sysdict.setFuzzifiedInputs('Sysmark',sysmark_dict)
	def rulebase(self):
		output_amounts = {}
		x = Rules()
		x.clearRules()
		x.clearInputDicts()
		x.addRule('IF Mark.Weak AND (NOT Sysmark.Weak) THEN PracticeLevel.Middle')
		x.addRule('IF Mark.Weak AND Sysmark.Weak THEN PracticeLevel.Easy')
		x.addRule('IF Mark.Weak AND (NOT Study.Low) AND Hardness.Hard AND Sysmark.Excellent THEN PracticeLevel.Hard')
		x.addRule('IF Mark.Weak AND (NOT Study.Low) AND (NOT Hardness.Hard) AND Sysmark.Excellent THEN PracticeLevel.Difficult')
		x.addRule('IF Mark.Middle AND Sysmark.Middle THEN PracticeLevel.Middle')
		x.addRule('IF Mark.Middle AND (NOT Study.High) AND Sysmark.Weak THEN PracticeLevel.Middle')
		x.addRule('IF Mark.Middle AND Study.High AND Sysmark.Weak THEN PracticeLevel.Easy')
		x.addRule('IF Mark.Middle AND Sysmark.Good THEN PracticeLevel.Hard')
		x.addRule('IF Mark.Middle AND (NOT Study.Low) AND Sysmark.Excellent THEN PracticeLevel.Difficult')
		x.addRule('IF Mark.Middle AND Sysmark.Excellent THEN PracticeLevel.Hard')
		x.addRule('IF Mark.Good AND Sysmark.Good THEN PracticeLevel.Hard')
		x.addRule('IF Mark.Good AND Sysmark.Excellent THEN PracticeLevel.Difficult')
		x.addRule('IF Mark.Good AND Study.Low AND Hardness.Hard THEN PracticeLevel.Hard')
		x.addRule('IF Mark.Good AND (NOT Hardness.Easy) AND (NOT Sysmark.Excellent) THEN PracticeLevel.Middle')
		x.addRule('IF Mark.Excellent AND Sysmark.Excellent THEN PracticeLevel.Difficult')
		x.addRule('IF Mark.Excellent AND (NOT Sysmark.Excellent) THEN PracticeLevel.Hard')
		x.addRule('IF Mark.Excellent AND (NOT Study.Low) AND Hardness.Hard AND Sysmark.Good THEN PracticeLevel.Difficult')
		x.addRule('IF Mark.Excellent AND Sysmark.Weak THEN PracticeLevel.Middle')
		outputs = ['Easy','Middle','Hard','Difficult']
		Easy = ['2','7']
		Middle = ['1','5','6','14','18']
		Hard = ['3','8','10','11','13','16']
		Difficult = ['4','9','12','15','17']
		rules_number = {'Easy':Easy,'Middle':Middle,'Hard':Hard,'Difficult':Difficult}
		
		rules = x.getRules()
		i = 0
		for rule in rules:
			i += 1
			x.processRule(rule,i)

		a = x.rules_fuzzy_amount
		b = x.getFuzzifiedInputs()
		amounts = x.getAmounts()
		for outname, outname_vals in rules_number.iteritems():
			for key, value in amounts.iteritems():
				if key in outname_vals:
					if outname in output_amounts:
						output_amounts[outname].append(value)
					else:
						output_amounts[outname] = []
						output_amounts[outname].append(value)
		for key, value in output_amounts.iteritems():
			value = max(value)
			output_amounts[key] = value
		return output_amounts

	def defuzzification(self,output_amounts):

		practice_level_easy_rule_weight = output_amounts['Easy']
		practice_level_middle_rule_weight = output_amounts['Middle']
		practice_level_hard_rule_weight = output_amounts['Hard']
		practice_level_difficult_rule_weight = output_amounts['Difficult']

		sigma_cog = float(0)
		sigma_area = float(0)

		prac_easy = [0,0,20,35]
		prac_middle = [20,35,55,70]
		prac_hard = [55,70,85,90]
		prac_difficult = [85,90,100,100]

		cog_easy = float(prac_easy[3]**2+prac_easy[3]*prac_easy[2]+prac_easy[2]**2-prac_easy[1]**2-prac_easy[0]*prac_easy[1]-prac_easy[0]**2)/float(3*(prac_easy[3]+prac_easy[2]-prac_easy[1]-prac_easy[0]))
		cog_middle = float(prac_middle[3]**2+prac_middle[3]*prac_middle[2]+prac_middle[2]**2-prac_middle[1]**2-prac_middle[0]*prac_middle[1]-prac_middle[0]**2)/float(3*(prac_middle[3]+prac_middle[2]-prac_middle[1]-prac_middle[0]))
		cog_hard = float(prac_hard[3]**2+prac_hard[3]*prac_hard[2]+prac_hard[2]**2-prac_hard[1]**2-prac_hard[0]*prac_hard[1]-prac_hard[0]**2)/float(3*(prac_hard[3]+prac_hard[2]-prac_hard[1]-prac_hard[0]))
		cog_difficult = float(prac_difficult[3]**2+prac_difficult[3]*prac_difficult[2]+prac_difficult[2]**2-prac_difficult[1]**2-prac_difficult[0]*prac_difficult[1]-prac_difficult[0]**2)/float(3*(prac_difficult[3]+prac_difficult[2]-prac_difficult[1]-prac_difficult[0]))
		
		cog_practice_level = [cog_easy,cog_middle,cog_hard,cog_difficult]
		rule_weight_practice_level = [practice_level_easy_rule_weight,practice_level_middle_rule_weight,practice_level_hard_rule_weight,practice_level_difficult_rule_weight]

		for i in range(0,4):
			sigma_cog += float(cog_practice_level[i]*rule_weight_practice_level[i])
			sigma_area += float(rule_weight_practice_level[i])

		practice_level = float(sigma_cog/sigma_area)

		return practice_level