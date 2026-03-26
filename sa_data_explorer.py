#1. Display a welcome message and list all 9 SA provinces
print("Welcome to the South African Data Explorer! Here are the 9 provinces:")
print("1. Western Cape")
print("2. Eastern Cape")
print("3. Northern Cape")
print("4. Gauteng")
print("5. KwaZulu-Natal")
print("6. Mpumalanga")
print("7. Free State")
print("8. North West")
print("9. Limpopo")
#2. Ask the user to type a province name
province = input("Please enter the name of a province to explore: ")
province = province.lower()  # Convert input to lowercase for case-insensitive matching

province_data = {
    "western cape": {"Population": 7400000, "Area in km²": 129449, "Capital": "Cape Town", "Main Languages": "Afrikaans, English, Xhosa"},
    "eastern cape": {"Population": 6700000, "Area in km²": 168966, "Capital": "Bisho", "Main Languages": "Xhosa, Afrikaans, English"},
    "northern cape": {"Population": 350000, "Area in km²": 377921, "Capital": "Kimberley", "Main Languages": "Afrikaans, English"},
    "gauteng": {"Population": 16100000, "Area in km²": 19638, "Capital": "Johannesburg", "Main Languages": "Afrikaans, English"},
    "kwazulu-natal": {"Population": 11500000, "Area in km²": 94361, "Capital": "Pietermaritzburg", "Main Languages": "Zulu, English"},
    "mpumalanga": {"Population": 4500000, "Area in km²": 75382, "Capital": "Nelspruit", "Main Languages": "Afrikaans, English"},
    "free state": {"Population": 1100000, "Area in km²": 129825, "Capital": "Bloemfontein", "Main Languages": "Afrikaans, English"},
    "north west": {"Population": 1700000, "Area in km²": 132384, "Capital": "Mahikeng", "Main Languages": "Afrikaans, English"},
    "limpopo": {"Population": 2500000, "Area in km²": 125757, "Capital": "Polokwane", "Main Languages": "Sepedi, English"}
}

  
if province in province_data:
    print(f"The population of {province.capitalize()} is approximately {province_data[province]['Population']:,}.") #3. Display the population, area, capital, and main languages of the selected province and capitalizes the province name for better formatting
    print(f"The area of {province.capitalize()} is {province_data[province]['Area in km²']:,} km².")
    print(f"The capital of {province.capitalize()} is {province_data[province]['Capital']}.")
    print(f"The main languages spoken in {province.capitalize()} are {province_data[province]['Main Languages']}.")
else:
    print("Sorry, that province is not in our database. Please check your spelling and try again.")

explore_province = input("Would you like to explore another province? (yes/no): ")
explore_province = explore_province.lower()  # Convert input to lowercase for case-insensitive matching

#4. Ask the user if they want to explore another province and repeat the process if they say "yes". If they say "no", display a goodbye message and end the program.
if explore_province == "yes":
    province = input("Please enter the name of another province to explore: ")
    province = province.lower()  # Convert input to lowercase for case-insensitive matching
    if province in province_data:
        print(f"The population of {province.capitalize()} is approximately {province_data[province]['Population']:,}.")
        print(f"The area of {province.capitalize()} is {province_data[province]['Area in km²']:,} km².")
        print(f"The capital of {province.capitalize()} is {province_data[province]['Capital']}.")
        print(f"The main languages spoken in {province.capitalize()} are {province_data[province]['Main Languages']}.")
    else:
        print("Sorry, that province is not in our database. Please check your spelling and try again.")
else:
    print("Thank you for using the South African Data Explorer! Goodbye!")