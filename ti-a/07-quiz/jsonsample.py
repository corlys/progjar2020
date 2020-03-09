import json

# JSON konversi dari dictionary ke string
data = {"nama": "Andi", "nip": 12345}
strJson = json.dumps(data)
print(strJson)

# JSON konversi dari string ke dictionary
dictJson = json.loads(strJson)
print(dictJson["nama"])