"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv


def main(employees):
    with open('employees.csv', 'w', encoding='utf-8', newline='') as employeefile:
        fields = ['name', 'age', 'job', 'gender']
        writer = csv.DictWriter(employeefile, fields, delimiter='\t')
        writer.writeheader()
        for person in employees:
            writer.writerow(person)


if __name__ == "__main__":
    employees = [
        {'name':'Sherley', 'age':'62', 'job':'Counsellor', 'gender':'female'},
        {'name':'Kirill', 'age':'56', 'job':'Shoemaker', 'gender':'male'},
        {'name':'Neville', 'age':'39', 'job':'Judge', 'gender':'male'},
        {'name':'Jillian', 'age':'21', 'job':'Museum Curator', 'gender':'femail'},
        {'name':'Irakliy', 'age':'42', 'job':'Author', 'gender':'male'},
    ]
    main(employees)
