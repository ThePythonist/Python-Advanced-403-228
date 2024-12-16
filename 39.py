import xml.etree.ElementTree as ET

file = open("flights.xml").read()
root = ET.fromstring(file)
flights = root.findall("flight")
paris_flights = []

for i in flights:
    dest = i.find("destination").text
    if dest.lower() == "paris":
        paris_flights.append(i)

for i in paris_flights:
    print(i.find("flight_number").text)
