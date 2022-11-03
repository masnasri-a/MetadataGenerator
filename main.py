
import json

link = [
'https://raw.githubusercontent.com/masnasri-a/images/main/Combined-Greybone.png',
'https://raw.githubusercontent.com/masnasri-a/images/main/Combined-Wolfur.png',
'https://raw.githubusercontent.com/masnasri-a/images/main/Combined-Audy.png',
'https://raw.githubusercontent.com/masnasri-a/images/main/Combined-Thunderking.png',
'https://raw.githubusercontent.com/masnasri-a/images/main/Combined-BS.png',
'https://raw.githubusercontent.com/masnasri-a/images/main/Combined-Warren.png',
'https://raw.githubusercontent.com/masnasri-a/images/main/Combined-Alice.png',
'https://raw.githubusercontent.com/masnasri-a/images/main/Combined-Monkey%20Kingdom.png',
'https://raw.githubusercontent.com/masnasri-a/images/main/Combined-MonkeDAO.png',
'https://raw.githubusercontent.com/masnasri-a/images/main/Combined-Frank%20DeGods.png',
'https://raw.githubusercontent.com/masnasri-a/images/main/Combined-Burrito%20Boyz.png'
]

data = [
    'Rarity',
    'Base',
    'Outfit',
    'Weapon',
    'Headgear',
    'Eyes',
    'Mouth',
    'Background',
    'Special'
]

genus = [
    'Greybone',
    'Wolfur',
    'Auday',
    'Thunderkings',
    'BS',
    'Warren',
    'Alice',
    'Monkey Kingdom',
    'MonkeDAO',
    'Frank DeGods',
    'Burrito Boyz'
]


def mapper(param: list):
    num = 0
    for detail in param:
        print(detail)
        model = {
            "name": genus[num]+"#"+str(num+1),
            "symbol": "PR",
            "description": "Collection "+str(num+1)+"/"+str(len(genus))+" generating one on one purraria assets",
            "seller_fee_basis_points": 500,
            "external_url": "https://purrariagame.com/",
            "edition": num+1,
            "attributes": detail,
            "properties": {
                "category": "image",
                "creators": [
                    {
                        "address": "2vypN5TJppGwT4rRQW3Q6g8ezFN958XwaCM9AwVdyMKJ",
                        "share": 100
                    }
                ],
                "files": [
                    {
                        "uri": link[num],
                        "type": "image/png"
                    }
                ]
            },
            "image": link[num],
            "collection": {
                "name": "Purraria",
                "family": "Purraria"
            }
        }
        json_object = json.dumps(model, indent=4)
        num += 1
        # Writing to sample.json
        with open(str(num)+".json", "w") as outfile:
            outfile.write(json_object)


def load():
    with open('data.txt') as f:
        lines = f.readlines()
        mapping = []
        list_data = []
        num = 1
        for detail in lines:
            mapping.append({
                "trait_type": data[num-1],
                "value": detail.replace('\n', '')
            })
            num += 1
            if num == 10:
                num = 1
                list_data.append(mapping)
                mapping = []
    return list_data


if __name__ == "__main__":
    list_data = load()
    data = mapper(list_data)
