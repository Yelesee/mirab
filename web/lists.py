import os
import xml.etree.ElementTree as et

base_path = os.path.dirname(os.path.realpath(__file__))
xml_file = os.path.join(base_path, "data/fuzzy.xml")
tree = et.parse(xml_file)
print(xml_file)

# class Fuzzy_xml:
# 	def__init__(self,input_nums,output_nums,rule_nums):
# 	def new_file(inputs,outputs,rules):


