class CarRental:
    def __init__(self):
        # Dictionary to store available cars and their rental prices per day
        self.available_cars = {
            "Toyota Corolla": 50,
            "Honda Civic": 60,
            "Ford Mustang": 100,
            "Tesla Model 3": 120,
            "Chevrolet Camaro": 110,
            "Nissan Altima": 70,
            "Hyundai Elantra": 55,
            "Rolls-Royce La Rose Noire Droptail": 1000,
            "Lamborghini Aventador": 1500,
            "Ferrari 488 GTB": 2000,
        }
        # Dictionary to store rented cars with customer details
        self.rented_cars = {}

    def display_cars(self):
        # Display all available cars for rent
        if not self.available_cars:
            print("\nNo cars available for rent.")
        else:
            print("\nAvailable Cars for Rent:")
            for car, price in self.available_cars.items():
                print(f"- {car}: ${price} per day")

    def rent_car(self, customer_name, car_name, days):
        # Rent a car to a customer
        if car_name in self.available_cars:
            try:
                days = int(days)  # Ensure the number of days is an integer
                if days <= 0:
                    print("\nRental duration must be at least 1 day.")
                    return
                
                # Calculate rental cost
                rental_cost = self.available_cars[car_name] * days
                # Add rental details to rented_cars dictionary
                self.rented_cars[customer_name] = (car_name, days, rental_cost)
                # Remove the rented car from available_cars
                del self.available_cars[car_name]
                
                print(f"\n{customer_name} rented {car_name} for {days} days.")
                print(f"Total cost: ${rental_cost}")
            except ValueError:
                # Handle invalid input for days
                print("\nInvalid input! Please enter a number for days.")
        else:
            # Handle case where car is not available
            print("\nCar not available or does not exist.")
    
    def return_car(self, customer_name):
        # Return a rented car
        if customer_name in self.rented_cars:
            # Retrieve rental details
            car_name, days, cost = self.rented_cars.pop(customer_name)
            # Add the car back to available_cars
            self.available_cars[car_name] = cost // days
            print(f"\n{customer_name} returned {car_name}. Thank you!")
        else:
            # Handle case where no rental record exists for the customer
            print("\nNo rental record found for this customer.")

def main():
    # Main function to run the car rental system
    rental_system = CarRental()

    while True:
        # Display menu options
        print("\nCar Rental System")
        print("1. View Available Cars")
        print("2. Rent a Car")
        print("3. Return a Car")
        print("4. Exit")

        # Get user choice
        choice = input("Enter your choice: ")

        if choice == "1":
            # Display available cars
            rental_system.display_cars()
        elif choice == "2":
            # Rent a car
            customer_name = input("Enter your name: ")
            car_name = input("Enter the car you want to rent: ")
            days = input("Enter number of rental days: ")
            rental_system.rent_car(customer_name, car_name, days)
        elif choice == "3":
            # Return a car
            customer_name = input("Enter your name: ")
            rental_system.return_car(customer_name)
        elif choice == "4":
            # Exit the system
            print("\nExiting system. Thank you for using our service!")
            break
        else:
            # Handle invalid menu choice
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
