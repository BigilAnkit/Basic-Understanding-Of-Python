# Creating a dictionary
country_capitals = {
    "Germany":"Berlin",
    "Canada":"Ottawa",
    "England":"London"
}

print(country_capitals)


# Valid dictionary
# integar as a key
my_dict = {1:"one",2:"Two",3:"Three"}

# Valid dictionary
# tuple as a key
my_dict = {(1,2):"one two",3:"three"}


#invalid dictionary
#error: using a list as a key is not allowed
# my_dict = {1:"Hello",[1,2]:"Hello Hi"}

# valid dictionary
# string as a key, list as a value
my_dict = {"USA":["Chicago","california","New York"]}


'''Key of dictionary must be unique'''

hogwarts_houses ={
    "Harry Potter":"Gryffindor",
    "Hermione Granger":"Gryffindor",
    "Ron Wasley":"Gryffindor",
    "Harry Potter":"Slytherin"
}

print(hogwarts_houses)


# Access Dictionary items

country_capitals = {
    "Germany":"Berlin",
    "Canada":"Ottawa",
    "England":"London"
}

# Access the value of keys
print(country_capitals["Germany"])
print(country_capitals["England"])


'''Add Items to a Dictionary'''

country_capitals = {
    "Germany":"Berlin",
    "Canada":"Ottawa"
}

country_capitals["Italy"] = "Rome"

print(country_capitals)


'''Remove Dictionary items'''

country_capitals ={
    "Germany":"Berlin",
    "Canada":"Ottawa"
}

del country_capitals["Germany"]
print(country_capitals)

"""Change the value of Italy key to Rome"""
country_capitals["Italy"]="Rome"

print(country_capitals)


# Iterate Through a Dictionary

for country in country_capitals:
    print(country)

country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome" 
}

print()

# print Dictionary keys one by one
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)


'''Find Dictionary length'''

#get dictionary length
print(len(country_capitals))

numbers = {10:"ten",20:"twenty",30:"thirty"}

print(len(numbers))


'''Dictionary Membership Test'''

file_types = {
    ".txt":"Text File",
    ".pdf":"PDF Document",
    ".jpg":"JPEG Image",
}

# use of in and not in operators
print(".pdf" in file_types)
print(".mp3" in file_types)
print(".mp3" not in file_types)