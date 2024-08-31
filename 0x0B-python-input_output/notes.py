# item = load_from_json_file('add_item.json')
# items = []
# items.extend(item)
# items.extend(sys.argv[1:])
# save_to_json_file(items, 'add_item.json')


# if os.path.exists(filename):
#     items = load_from_json_file(filename)
# else:
#     items = []
#
# items.extend(sys.argv[1:])
#
# save_to_json_file(items, filename)

# import requests
#
# city = 'London'
# api_key = 'your_api_key'
#
# payload = {'q': city, 'appid': api_key}
#
# response = requests.get('http://api.openweathermap.org/data/2.5/weather', params=payload)
# weather_data = response.json()
#
# print(weather_data)

# try:
#     items = load_from_json_file('add_item.json')
# except FileNotFoundError:
#     items = []
# items.extend(sys.argv[1:])
# save_to_json_file(items, 'add_item.json')
