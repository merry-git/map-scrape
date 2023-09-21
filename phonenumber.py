import googlemaps

api_key = "YOUR API KEY"
gmaps = googlemaps.Client(key=api_key)
red_color = "\x1b[31m"
reset_color = "\x1b[0m"
green_color = "\x1b[32m"

city_name = input("Enter the city or area you want to search: ")
print("")
print("----------------------------------------------------------")
print("[recommended: establishment, restaurant, gym, car_repair]\nfull list found @ \nhttps://developers.google.com/maps/documentation/places/web-service/supported_types")
print("----------------------------------------------------------")
type = input("Enter the type of service you want to search: ")
max_results = int(input("Enter the maximum number of results you want (Max, 20 per iteration): "))

field_mapping = {
    'name': 'Name',
    'formatted_phone_number': 'Formatted Phone Number',
    'user_ratings_total': 'User Ratings Total',
}

fields = ['name', 'formatted_phone_number', 'user_ratings_total', 'website']

restaurant_info = {}

results = []
next_page_token = None

while len(results) < max_results:
    places = gmaps.places(city_name, type=type, page_token=next_page_token)
    
    results.extend(places.get('results', []))
    next_page_token = places.get('next_page_token')
    if not next_page_token:
        break

if len(results) > max_results:
    results = results[:max_results]

for place in results:
    place_id = place['place_id']
    place_details = gmaps.place(place_id, fields=fields)
    
    restaurant_name = place_details['result'].get('name', 'Unknown Restaurant')
    
    if restaurant_name not in restaurant_info:
        restaurant_info[restaurant_name] = {} 
    for key in field_mapping:
        value = place_details['result'].get(key, 'Not available')
        restaurant_info[restaurant_name][field_mapping[key]] = value


for restaurant_name, info in restaurant_info.items():
    print(f"{green_color}{restaurant_name}{reset_color}")
    for key, value in info.items():
        print(f"{red_color}{key}:{reset_color} {value}")
    print()

