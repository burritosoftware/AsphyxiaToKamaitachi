import json
import xml.etree.ElementTree as ET

# Getting lines of data
database = open("sdvx@asphyxia.db", "r")
datalines = database.readlines()
database.close()

xmlp = ET.XMLParser(encoding="utf-8")
musicdb = ET.parse('music_db.xml', parser=xmlp)

# Global variables to store name to refids, and store scores associated to refid
profiles = []
scores = []
scoresCleaned = []
kamaiFile = {}
kamaiFile['meta'] = {
    "game": "sdvx",
    "playtype": "Single",
    "service": "Asphyxia"
    }
kamaiScores = []
musicIDs = []

for song in musicdb.findall('music'):
    musicIDs.append({'id': song.get('id'), 'inf_ver': song.find('info').find('inf_ver').text})

# Adding profiles to variable
for dataline in datalines:
    entry = json.loads(dataline)
    if "collection" not in entry:
        break

    if entry['collection'] == "profile":
        profiles.append({'name': entry['name'], '__refid': entry['__refid']})

# User selects which profile to convert
for profile in profiles:
    index = profiles.index(profile)
    print(f"{index + 1}. {profile['name']}")
print(f"\n{str(len(profiles))} profiles found")
selection = input("Type the number corresponding to the right profile: ")
selectedProfile = profiles[int(selection) - 1]

# Adding scores to scores variable
for dataline in datalines:
    entry = json.loads(dataline)
    if "collection" not in entry:
        break

    if entry['collection'] == "music" and entry['__refid'] == selectedProfile['__refid']:
        scores.append(entry)

# Cleaning duplicates from scores
for score in scores:
    if score not in scoresCleaned:
        scoresCleaned.append(score)

print(f"\n{len(scoresCleaned)} scores found for {selectedProfile['name']}")
confirmation = input("Create batch manual file? (y/n): ")
if confirmation != "y":
    exit()

# Converting each score to Tachi batch-import
for score in scoresCleaned:

    lamp = ""
    diff = ""

    match score['clear']:
        case 0:
            lamp = "FAILED"
        case 1:
            lamp = "CLEAR"
        case 2:
            lamp = "EXCESSIVE CLEAR"
        case 3:
            lamp = "ULTIMATE CHAIN"
        case 4:
            lamp = "PERFECT ULTIMATE CHAIN"

    match score['type']:
        case 0:
            diff = "NOV"
        case 1:
            diff = "ADV"
        case 2:
            diff = "EXH"
        case 3:
            for song in musicIDs:
                if song['id'] == str(score['mid']):
                    match song['inf_ver']:
                        case 2:
                            diff = "INF"
                        case 3:
                            diff = "GRV"
                        case 4:
                            diff = "HVN"
                        case 5:
                            diff = "VVD"
                    break
        case 4:
            diff = "MXM"

    kamaiScore = {
    "score": score['score'],
    "lamp": lamp,
    "matchType": "inGameID",
    "identifier": str(score['mid']),
    "difficulty": diff,
    "timeAchieved": score['updatedAt']['$$date']
    }

    kamaiScores.append(kamaiScore)

kamaiFile['scores'] = kamaiScores

# Saving the final file
with open("batchimport.json", "w") as file:
    json.dump(kamaiFile, file)

print("File created!")