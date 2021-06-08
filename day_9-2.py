# Nesting Lists and Dictionaries

# Nesting Lists in a Dictionary
travel_log = {
    "India": ["Mumbai", "Banglore", "Chennai"],
    "USA": ["Seattle", "Miami", "Ney York"],
}

# Nesting Dictionary in a Dictionary
travel_log = {
    "India": {"cities": ["Mumbai", "Banglore", "Chennai"], "visited": 2},
    "USA": {"cities": ["Seattle", "Miami", "Ney York"], "visited": 1},
}

# Nesting Dictionary in a List
travel_log = [
    {
        "country": "India", 
        "cities": ["Mumbai", "Banglore", "Chennai"], 
        "visited": 2
    },
    {
        "country": "USA",
        "cities": ["Seattle", "Miami", "Ney York"],
        "visited": 1
    },
]