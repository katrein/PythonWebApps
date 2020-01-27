def calc_user_age_secs():
    age_input = input("Please enter your age: ")
    age_secs = sum(age_input * 365 * 24 * 60 * 60)
    return "You have lived for {} seconds".format(age_secs)

print(calc_user_age_secs)
