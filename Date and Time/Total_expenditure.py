
Days=int(input("How many days did you spend in your hotel?"))
hotel_price=int(input("What was the per day cost of your hotel"))
hotel_expenditure=Days*hotel_price

plane_price=int(input("Please enter how much the ticket for your flight was"))

hours=int(input("Please enter how many hours you rented the vehicle for"))
hour_price=int(input("Please enter the per-hour price for the vehicle"))
vehicle_expenditure=hours*hour_price

total_expenditure=vehicle_expenditure+plane_price+hotel_expenditure
print("Your total expenditure was:",total_expenditure)