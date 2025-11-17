def generate_profile(age: int) -> str:
    life_stage = ""
    if 0 <= age <= 12:
       life_stage = "Child" 
    elif 13 <= age <= 19:
       life_stage = "Teenager" 
    elif age >= 20:
       life_stage = "Adult" 
          
    return life_stage 


def main():
    user_name = ''
    birth_year_str = ''
    birth_year = 0
    current_age = 0 
    hobbies = []
    life_stage = ''
    user_profile = {}

    print("Enter your full name:")
    user_name = str(input())

    print("Enter your birth year:")
    birth_year_str = str(input())
    birth_year = int(birth_year_str)

    current_age = 2025 - birth_year
    life_stage = generate_profile(current_age)

    print("Enter a favorite hobby or type 'stop' to finish:")
    hobby_answer = str(input())
    while(hobby_answer != 'stop'):
        hobbies.append(hobby_answer)
            
        print("Enter a favorite hobby or type 'stop' to finish:")
        hobby_answer = str(input())
    
    user_profile = {
            "name" : user_name,
            "age" : current_age,
            "stage" : life_stage,
            "hobbies" : hobbies
            }

    hobbies_string = f'Favorite Hobbies({len(hobbies)}):\n'
    if hobbies:
        for hobby in user_profile["hobbies"]:
            hobbies_string+='- ' + hobby + '\n'
    else:
        hobbies_string = 'You don`t mention any hobbies.'
    hobbies_string = hobbies_string[:-1]

    print(f'''
---
Profile Summary:
Name: {user_profile["name"]}
Age: {user_profile["age"]}
Life Stage: {user_profile["stage"]}
{hobbies_string}
---
'''
          )
if __name__ == "__main__":
    main()
