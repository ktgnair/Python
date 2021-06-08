# Dictionary in List
# Write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.

# Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, cities):
    dictionary = {}
    dictionary["country"] = country
    dictionary["visits"] = visits
    dictionary["cities"] = cities
    travel_log.append(dictionary)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)