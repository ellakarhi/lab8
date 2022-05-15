
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


def country_count(people):
  
  countries = []

  for country in people:
    if country[4] not in countries:
      countries.append(country[4])

  count_country = []
  counter = []
  for country in countries:
    count = 0
    counter.append(country)
    for person in people:
      if person[4] == country:
        count += 1

    counter.append(count)
    count_country.append(counter)
    counter = []
    
    
  print (count_country)

def user_input():
  email = int(input("Would you like to know the created emails(1), or would you like to know the country count(2). Type in the number assigned to the task you would like to run: "))
  if email == 1:
    create_email()
  elif email == 2:
    country_count(people)
  else:
    print("You must type in either 1 or 2, please try again.")
    user_input()

  again = int(input("Would you like to run another function?Would you like to know the created emails(1), or would you like to know the country count(2). Type in the number assigned to the task you would like to run,  If you wouldn't like to run another function type in 3: "))
  if again == 1:
    create_email()
  elif again == 2:
    country_count(people)
  elif again == 3:
    exit
  else:
    print("You must type in either 1, 2 or 3 please try again.")
    user_input()
user_input()
#country_count(people)
