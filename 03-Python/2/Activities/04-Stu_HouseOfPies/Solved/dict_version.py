shopping = 'y'

pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

pie_dict = {pie: amt for pie, amt in zip(pie_list, [0 for i in range(len(pie_list))])}

print(pie_dict)

# Display initial message
print("Welcome to the House of Pies! Here are our pies:")

# While we are still shopping...
while shopping == "y":

    # Show pie selection prompt
    print("---------------------------------------------------------------------")
    print("Pecan, Apple Crisp, Bean, Banoffee, " +
          "Black Bun, Blueberry, Buko, Burek, " +
          "Tamale, Steak ")

    pie_choice = input("Which would you like? ")

    # Add pie purchase to the pie dictionary by incrementing its value by 1
    pie_dict[pie_choice] += 1

    print("------------------------------------------------------------------------")

    # Inform the customer of the pie purchase
    print("Great! We'll have that " + pie_choice + " right out for you.")

    # Provide exit option
    shopping = input("Would you like to make another purchase: (y)es or (n)o? ")

# Once the pie list is complete
print("------------------------------------------------------------------------")

# Count instances of each pie
print("You purchased: ")

# Loop through the full pie dict and return pies that have been added to cart
for pie in pie_dict:
    if pie_dict[pie] > 0:
        pie_name = pie
        pie_count = pie_dict[pie]

        # Gather the count of each pie in the pie list and print them alongside the pies
        print(str(pie_count) + " " + pie_name)
