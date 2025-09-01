import json
from collections import Counter

PATH = 'out.json'
with open(PATH, 'r', encoding="utf-8") as file:
    data = json.load(file)
titles = []
for dataShell in data:
    if dataShell["master_metadata_track_name"] != None:

        titles.append(dataShell["master_metadata_track_name"])
counter = Counter(titles)
mostCommon = counter.most_common(1)[0]
print("most common ", mostCommon)
print("times listened ", mostCommon[1])


sorted_list = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
for word, count in sorted_list:
    print(f"{word}: {count}")