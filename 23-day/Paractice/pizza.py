def keepcoding(stomach):
    if stomach == "yes":
        return "Hello sir! please deliver 10 pizza to my Home i am hungry."

    else:
        return "Keep coding."

user_input = input("Are you hungry? yes or No:")
print(keepcoding(user_input))
