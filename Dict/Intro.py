# Here We gave different values for same key anyhow insertion order is preserved for ford key for the version above 3.5
vehicles = {
    "ford": "Fiesta",
    "Kawaski": "Maruthi",
    "ford" : "Fiesta 7",
}
# Updating the values preserve the insertion order of the key:
vehicles["ford"] = "Fiesta 8"

# one way of getting values from dict
print(vehicles["ford"])

# another way of getting values from dict
print(vehicles.get("Kawaski"))
# strings inside the dict are case sensitive
print(vehicles.get("KAWaski"))  # ---> returns none
# print(vehicles["FORD"])   #---> throws error

# Adding items to dictionary Version above 3.5 preserve insertion order
vehicles["toy"] = "glider"
vehicles["toys"] = "gliders"


#deleting items
del vehicles["Kawaski"]
#del vehicles["Notexistkey"]   #--->KeyError: 'Notexistkey'
result = vehicles.pop('Notexistkey',None) #--->Instead of throwing Key Error,it gets value that we passed in pop() that is  None
print(f'the result is {result}')  #--->Prints the result is None
print()
# Iterating over dict:
for key, value in vehicles.items():
    print(f'The key is {key} and value is {value}')
