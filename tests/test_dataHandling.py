import csv
import json

from openpyxl import load_workbook


def jsonHandling(filepath):
    with open(filepath) as data:
        formatedData = json.load(data)

    return formatedData


def test_json():
    result = jsonHandling("data/creds.json")



def csvHandling():
    with open("data/credentails.csv") as data:
        formatedData = csv.DictReader(data)
        dataList = []
        for i in formatedData:
            dataList.append(i)
        print(dataList)



def csvWrite():
    with open("data/credentails.csv", mode='a', newline="") as data:
        formatedData = csv.DictWriter(data, fieldnames=["username","password"])
        formatedData.writerow({'username': 'tripur123', 'password': 'welcome'})


# pip install openpyxl
def test_excelhandling():
        
        workbook = load_workbook("data\\sample_creds.xlsx")
        sheet = workbook["sheet1"]
        data = []
        for i in sheet.iter_rows(min_row=2, values_only=True):
            data.append(i)

        print(data)
