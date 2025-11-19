CURRENT_YEAR = 2025

def generate_profile(age):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    
def get_user_full_name():
    return input("Enter your full name: ")

def get_user_birth_year():
    return input("Enter your birth year: ")

def convert_string_to_int(birth_year_str):
    return int(birth_year_str)

def calculate_current_age(birth_year):
    return CURRENT_YEAR - birth_year

def get_user_hobbies(hobbies):
    stop_word = "stop"

    while True:
        user_input = input("Enter a favorite hobby or type 'stop' to finish: ")
        if user_input.lower() == stop_word:
            break
        else:
            hobbies.append(user_input)
    
    return hobbies

def generate_user_profile(name, age, stage, hobbies):
    user_profile = {
        "name" : name,
        "age"  : age,
        "stage" : stage,
        "hobbies" : hobbies
    }
    
    return user_profile

def check_hobbies_list(hobbies):
    number_of_hobbies = len(hobbies)

    if number_of_hobbies == 0:
        print("You didn't mention any hobbies.")
    else:
        print(f"Favorite Hobbies ({number_of_hobbies}):")
        
        for hobby in hobbies:
            print(f"- {hobby}")


def display_user_info(user_profile):
    print(f"---")
    print(f"Profile Summary:")
    print(f"Name: {user_profile["name"]}")
    print(f"Age: {user_profile["age"]}")
    print(f"Life Stage: {user_profile["stage"]}")

    check_hobbies_list(user_profile["hobbies"])
    
    print(f"---")
    
def main():
    user_name = get_user_full_name()
    birth_year_str = get_user_birth_year()

    birth_year = convert_string_to_int(birth_year_str)
    current_age = calculate_current_age(birth_year)

    hobbies = []
    hobbies = get_user_hobbies(hobbies)

    life_stage = generate_profile(current_age)

    user_profile = generate_user_profile(user_name, current_age, life_stage, hobbies)

    display_user_info(user_profile)
    
if __name__ == "__main__":
    main()