import csv


def write(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f'{filename} has been created successfully.')


data1 = [
    ['Name', 'Major', 'Grade'],
    ['Mina', 'Computer Engineering', 16.83],
    ['Anna', 'Mechanical Engineering', 18.3],
    ['Kiarash', 'Computer Science', 19.67],
    ['Sima', 'Literature', 17.56]
]

write("students.csv", data1)
