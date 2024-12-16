import xmltodict
from pprint import pprint


# XML data to be parsed
xml_data = open("payments.xml").read()

# Parse XML data into a dictionary
data_dict = xmltodict.parse(xml_data)

# Access the parsed data
root = data_dict['employees']
employees = root['employee']
under30 = []

for i in employees:
    if int(i["age"]) <= 30:
        under30.append(i)

pprint(under30)
print(len(under30))
