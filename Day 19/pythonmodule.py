import xml.etree.ElementTree as ET
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))


# # Program to extract number
# # of rows using Python
# import xlrd

# # Give the location of the file
# loc = ("path of file")

# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)
# sheet.cell_value(0, 0)

# # Extracting number of rows
# print(sheet.nrows)

tree = ET.parse('D:\Ysquare\Python\Paython_2020_Ashish\Day 19\example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)


# PIP
