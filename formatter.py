import json, googlemaps, sys

gmaps = googlemaps.Client(key='AIzaSyDGCn_p346lVJbluOImaeJDVnQGB9ahMoc')

with open(sys.argv[1]) as file:
    data = json.loads(file.read())['features']
    clean = ""
    for each in data:
        if each['geometry']['type'] != 'Point':
            coords = each['geometry']['coordinates'][0][::-1]
        else:
            coords = each['geometry']['coordinates'][::-1]
        pos = gmaps.reverse_geocode(coords)
        address = pos[0]['formatted_address']
        address = address.replace(', France', '')
        address = ';'.join(address.split(',')[::-1])
        if not pos:
            print('not found', data['properties']['name'])
        else:
            print('.', end='')
            clean += address
            clean += ';'
            clean += each['properties']['description'].replace('\n', ' ').replace(';', ',')
            clean += '\n'

with open(sys.argv[2], 'w+') as file:
    file.write(clean)
