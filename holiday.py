destinations = ["London", "Madrid", "Paris"]

#  ask for user's input: destination
while True:
    city_flight = input("Please choose your destination from the list: London, Madrid, Paris:").capitalize()
    if city_flight in destinations:
        print(f"Your destination is:{city_flight}")
        break
    else:
        print("Wrong destination.")
        continue 

#  ask for user's input: number of nights
while True:
    try: 
        num_nights = int(input("Enter the number of nights:"))
        print(f"You will be staying {num_nights} nights")
        break
    except ValueError:
        print("Please enter a valid number")

#  ask for user's input: rental days:
while True: 
    try: 
        rental_days = int(input("Enter the number of days for car rental:"))
        print(f"You will rent the car for {rental_days} days")
        break
    except ValueError: 
        print("Please enter a valid number of days:") 

#  create the function 'hotel_cost': it takes num_nights as argument and returns a total cost for the hotel stay:
def hotel_cost(num_nights): 
    return num_nights * 60
print(f"The cost of the hotel is £{hotel_cost(num_nights)}")

#  create the function 'plane_cost': it takes parameter city_flight as argument and uses if/else statement to return the cost of flight
def plane_cost(city_flight):
    if city_flight == "London":
        return 50
    elif city_flight == "Madrid":
        return 70
    elif city_flight == "Paris":
        return 90
    else:
        raise ValueError ("Invalid input")
print(f"The cost of the flight is £{plane_cost(city_flight)}")

#  create the function 'car_rent' that takes parameter 'rental_days' as argument and returns the total cost of car rental
def car_rent(rental_days):
    return rental_days * 30
print(f"The cost of renting your car is £{car_rent(rental_days)}")

#  create the function 'holiday_cost' that takes all three parameters as arguments and returns a total cost of holiday
def holiday_cost(city_flight,rental_days, num_nights):
    sum = hotel_cost(num_nights)+plane_cost(city_flight)+car_rent(rental_days)
    return sum
print(f"The total cost of your holiday is: £{holiday_cost(city_flight, rental_days,num_nights)}")
        

