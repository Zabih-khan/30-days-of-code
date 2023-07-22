##Given the meal price (base cost of a meal), tip percent (the percentage of the
##meal price being added as tip), and tax percent (the percentage of the meal
##price being added as tax) for a meal,find and print the meal's total cost.
##Round the result to the nearest integer

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here    
    tip=tip_percent/100*meal_cost

    tax=tax_percent/100*meal_cost
    total=meal_cost+tip+tax
    
    print("Total cost:",round(total))
    

if __name__ == '__main__':
    meal_cost = float(input("Enter meal cost").strip())

    tip_percent = int(input("Enter tip_percent").strip())

    tax_percent = int(input("Enter tax_percent").strip())

    solve(meal_cost, tip_percent, tax_percent)
