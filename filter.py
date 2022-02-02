import json
import csv

def filterList(cityFilter : list, countryCodeFilter : list, inFilePath : str):
    """
        This function filters a list of data in a file as a json and put it in the out file

        :param cityFilter: List of cities to filter on
        :type cityFilter: list
        :param countryCodeFilter: List of countries to filter on
        :type countryCodeFilter: list
        :param inFilePath: The path of the input file
        :type inFilePath: str
        :param outFilePath: The path of the output file
        :type outFilePath: str 
    """
    finalList = list()
    
    with open(inFilePath, encoding="utf-8") as fileIn:
            jsonIn = json.load(fileIn)

            for d in jsonIn:
                if(d["name"] in cityFilter and d["country"] in countryCodeFilter):
                    finalList.append(d)

    return finalList

if __name__=="__main__":
    with open("./resources/departements-francais.csv", encoding="utf-8") as csvFile:
        csvReader = csv.reader(csvFile, delimiter="\t")

        cityList = list()
        countryList = list()
        countryList.append("FR")

        for row in csvReader:
            cityList.append(row[3])
        
        filtered = filterList(cityList, countryList, "./resources/city.list.json")

        with open("./resources/filtered.list.json", encoding="utf-8", mode="a") as outFile:
            jsonValue = json.dumps(filtered)
            outFile.write(jsonValue)
            outFile.close()

        csvFile.close()