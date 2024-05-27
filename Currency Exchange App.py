import requests
import json

api_key = "6babf42a9cb75b6de08db4c1"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("Bozulan Döviz Türü: ")
alinan_doviz = input("Alınan Döviz Türü: ")
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istersiniz?: "))

sonuc = requests.get(api_url + bozulan_doviz)
sonuc_json = json.loads(sonuc.text)

# print(sonuc_json["conversion_rates"][alinan_doviz])
print("1 {0} = {1} {2}".format(bozulan_doviz,sonuc_json["conversion_rates"][alinan_doviz], alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar, bozulan_doviz, miktar*sonuc_json["conversion_rates"][alinan_doviz], alinan_doviz))


print("Made in Gayseri")