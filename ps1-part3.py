
def heart_rate(age, goal):
    max_HR = 220 - age
    print(f"Your maximum heart rate is: {max_HR}")
    
    if goal == 'S':
        lower = 0.8 * max_HR
        upper = 1.0 * max_HR
    elif goal == 'E':
        lower = 0.6 * max_HR
        upper = 0.8 * max_HR
    
    print(f"Your target heart rate is between {lower:.1f} and {upper:.1f}")

user_age = int(input("What is your age? "))
user_goal = input("Is your goal speed (S) or endurance (E)? ")

heart_rate(user_age, user_goal)
