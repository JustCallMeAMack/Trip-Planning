destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

attractions = [[], [], [], [], []]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

def add_attractions(destination, attraction):
  destination_index = get_destination_index(destination)
  attractions_for_destination = attractions[destination_index].append(attraction)
  return attractions

get_destination_index('Los Angeles, USA')
get_destination_index('Paris, France')
add_attractions('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attractions("Paris, France", ["the Louvre", ["art", "museum"]])
add_attractions("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attractions("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attractions("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attractions("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attractions("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attractions("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attractions("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attractions("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attractions("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

#test_destination_index = get_traveler_location(test_traveler)
#print(test_destination_index)

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for a in attractions_in_city:
    possible_attraction = a
    attraction_tags = a[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

#la_arts = find_attractions('Los Angeles, USA', ['art'])
#print(la_arts)

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = f"Hi {traveler[0]}, we think you'll like these places around {traveler_destination}: The {''.join(traveler_attractions)}."
  return interests_string

smills_france = get_attractions_for_traveler(['Derek Smill', 'Paris, France', ['monument']])
print(smills_france)
