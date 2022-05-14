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
  email = []
  first_letter = (person[1](0))
  for person in people:
    print(person[2] + first_letter + "@gmail.com")




def count_country(people):
  countries = []

  for country in people:
    if country[4] not in countries:
      countries.append(country[4])
  print (countries)

#count_country(people)
create_email()