import csv 
import json

def main():
    jsonFile = 'station-data.json'
    jsonData = ""
    with open(jsonFile) as j:
        jsonData = j.read()

    jsonList = json.loads(jsonData)
    csvFile = open('VAMentalHealthData.csv', 'w', newline='')
    csvWriter = csv.writer(csvFile)

    header = jsonList[0].keys()
    csvWriter.writerow(header)

    for record in jsonList:
        if record['ValueType'].lower() == 'percent':
            record['Value'] = convertPercentToDecimal(record['Value'])
        elif record['ValueType'].lower() == 'number':
            record['Value'] = removeCommaFromNumber(record['Value'])
        csvWriter.writerow(record.values())

    csvFile.close()
def convertPercentToDecimal(percent):
    percent = percent[:len(percent) - 1]
    percentfloat = float(percent)
    percentfloat /= 100
    return f"{percentfloat:.2}"

def removeCommaFromNumber(number):
    return number.replace(',','')

if __name__ == '__main__':
    main()

