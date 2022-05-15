
def csv2list(filepath):
  file = open(filepath)
  first = True
  L = []
  
  for line in file:
    if first:
      first = False
      continue
    L.append(line.strip().split(","))

  return L

people = csv2list('people.csv')

def create_email():
  
  for person in people:
    first_letter = person[1][0]
    print(person[2] + first_letter + "@gmail.com")


def count_country(people):
  
  countries = []

  for country in people:
    if country[4] not in countries:
      countries.append(country[4])

  country_count = []
  counter = []
  for country in countries:
    count = 0
    counter.append(country)
    for person in people:
      if person[4] == country:
        count += 1

    counter.append(count)
    country_count.append(counter)
    counter = []
    
    
  print (country_count)

count_country(people)
