import json

def mergeJsonFiles(filePaths):
    mergedData = []
    for path in filePaths:
        with open(path, 'r', encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                mergedData.extend(data)  # flatten lists
            else:
                mergedData.append(data)  # handle single object case
    return mergedData

filePaths = ['1.json', '2.json', '3.json', '4.json']
outFile = 'out.json'
with open(outFile, 'w') as outFil:
    json.dump(mergeJsonFiles(filePaths), outFil)