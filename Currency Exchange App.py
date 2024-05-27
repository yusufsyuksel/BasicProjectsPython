import requests
import json

api_key = ""
api_url = f"/v6/{api_key}/latest/"

bozulan_doviz = input("Bozulan Döviz Türü: ")
alinan_doviz = input("Alınan Döviz Türü: ")
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istersiniz?: "))

sonuc = requests.get(api_url + bozulan_doviz)
sonuc_json = json.loads(sonuc.text)

# print(sonuc_json["conversion_rates"][alinan_doviz])
print("1 {0} = {1} {2}".format(bozulan_doviz,sonuc_json["conversion_rates"][alinan_doviz], alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar, bozulan_doviz, miktar*sonuc_json["conversion_rates"][alinan_doviz], alinan_doviz))


print("Made in Gayseri")
