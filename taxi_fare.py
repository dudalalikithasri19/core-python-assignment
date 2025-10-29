def calculate_fare(distance):
    base_fare = 50
    distance_fare = 10 * distance
    total = base_fare + distance_fare
    return total
n = int(input("Enter number of trips: "))
trips = []
for i in range(n):
    distance = float(input(f"Enter distance (in km) for trip {i+1}: "))
    trips.append(distance)
total_fare = 0
for i, distance in enumerate(trips, start=1):
    fare = calculate_fare(distance)
    print(f"Trip {i}: ${fare}")
    total_fare += fare
print(f"Total Fare: ${total_fare}")