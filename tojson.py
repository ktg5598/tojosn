import json, os, xmltodict


for root, dirs, files in os.walk(r".\2018-10-30-master", topdown=False):
    for name in files:
        xml = open(r'.\2018-10-30-master'+'\\' + name, 'r', encoding='gbk', errors='ignore').read()
        o = xmltodict.parse(xml)
        a = json.dumps(o)
        print(a)