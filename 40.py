import xml.etree.ElementTree as ET

# XML data
xml_data = open("flights.xml").read()

# Parse XML
root = ET.fromstring(xml_data)
william_flights = []

for flight in root.findall('flight'):
    passengers_root = flight.find("passengers")
    for person in passengers_root:
        if person.find("name").text == "William Thompson":
            william_flights.append(flight)

# print(len(william_flights))

for flight in william_flights:
    flight_number = flight.find('flight_number').text
    origin = flight.find('origin').text
    dest = flight.find('destination').text
    departure_time = flight.find('departure_time').text
    arrival_time = flight.find('arrival_time').text

    print(f"Flight Number: {flight_number}")
    print(f"Origin: {origin}")
    print(f"Destination: {dest}")
    print(f"Departure Time: {departure_time}")
    print(f"Arrival Time: {arrival_time}")
    print("-" * 50)