import string
import xml.etree.ElementTree as ET

with open("employees.xml") as f_xml:
    tree = ET.parse(f_xml)
    root = tree.getroot()
    s = 0
    count = 0
    for employee in root.findall('employee'):
        count += 1
        money = employee.find("salary").text
        if money is not None:
            s += int(money)
    print (f"Суммарная зарплата: {s}, всего сотрудников: {count}")


