from typing import Any, List, Dict

CURRENT_YEAR: int = 2025


def generate_profile(age: int) -> str:
    """
    Determines a person's category based on age.
    """
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    else:
        return "Unknown"


def get_user_full_name() -> str:
    """
    Prompts the user to enter their full name.
    Return the name as a string.
    """
    return input("Enter your full name: ")


def get_user_birth_year() -> str:
    """
    Prompts the user to enter their birth year.
    Return the birth year as a string.
    """
    return input("Enter your birth year: ")


def convert_string_to_int(birth_year_str: str) -> int:
    """
    Converts a birth year string into an integer.
    """
    return int(birth_year_str)


def calculate_current_age(birth_year: int) -> int:
    """
    Calculates the current age based on the birth year
    """
    return CURRENT_YEAR - birth_year


def get_user_hobbies(hobbies: List[str]) -> List[str]:
    """
    This function repeatedly prompts the user to enter their favorite hobbies until they type "stop".
    The entered hobbies are added to the provided list.
    Return the updated list.
    """
    stop_word: str = "stop"

    while True:
        user_input: str = input("Enter a favorite hobby or type 'stop' to finish: ")
        if user_input.lower() == stop_word:
            break
        else:
            hobbies.append(user_input)

    return hobbies


def generate_user_profile(
    name: str, age: int, stage: str, hobbies: List[str]
) -> Dict[str, Any]:
    """
    Creates a dictionary representing a user profile.
    """
    user_profile: Dict[str, Any] = {
        "name": name,
        "age": age,
        "stage": stage,
        "hobbies": hobbies,
    }

    return user_profile


def check_hobbies_list(hobbies: List[str]) -> None:
    """
    Checks a list of hobbies and prints the count and the hobbies themselves.
    """
    number_of_hobbies: int = len(hobbies)

    if number_of_hobbies == 0:
        print("You didn't mention any hobbies.")
    else:
        print(f"Favorite Hobbies ({number_of_hobbies}):")

        for hobby in hobbies:
            print(f"- {hobby}")


def display_user_info(user_profile: Dict[str, Any]) -> None:
    """
    This function displays user information on the screen.
    """
    print(f"---")
    print(f"Profile Summary:")
    print(f"Name: {user_profile["name"]}")
    print(f"Age: {user_profile["age"]}")
    print(f"Life Stage: {user_profile["stage"]}")

    check_hobbies_list(user_profile["hobbies"])

    print(f"---")


def main() -> None:
    """
    Main function of the program. Performs the following sequence of steps:
    1. Retrieves the user's full name.
    2. Requests the user's birth year and converts it to an integer.
    3. Calculates the user's current age.
    4. Collects the user's hobbies.
    5. Determines the life stage based on age.
    6. Generates a dictionary representing the user profile.
    7. Displays the user's information on the screen.
    """
    user_name: str = get_user_full_name()
    birth_year_str: str = get_user_birth_year()

    birth_year: int = convert_string_to_int(birth_year_str)
    current_age: int = calculate_current_age(birth_year)

    hobbies: List[str] = []
    hobbies = get_user_hobbies(hobbies)

    life_stage: str = generate_profile(current_age)

    user_profile: Dict[str, Any] = generate_user_profile(
        user_name, current_age, life_stage, hobbies
    )

    display_user_info(user_profile)


if __name__ == "__main__":
    main()
