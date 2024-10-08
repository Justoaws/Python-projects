# Print out the last name of the second employee. Please search through the dictionary 
# below :

d = {"employees": [{"firstName": "John", "lastName": "Doe"},
                  {"firstName": "Anna", "lastName": "Smith"},
                  {"firstName": "Peter", "lastName": "Jones"}],
  "owners": [{"firstName": "Jack", "lastName": "Petter"},
             {"firstName": "Jessy", "lastName": "Petter"}]                

}

second_employee_lastname = d["employees"][1]["lastName"]
print("The last name of the second employee is:", second_employee_lastname)

