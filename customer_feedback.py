# Function to calculate positive feedback percentage
def calculate_positive_percentage(ratings):
    if len(ratings) == 0:
        return 0  # Handle case with no ratings
    positive_count = sum(1 for r in ratings if r >= 4)
    percentage = (positive_count / len(ratings)) * 100
    return percentage

# Get number of ratings from user
n = int(input("Enter number of customer ratings: "))

# Handle no ratings case
if n == 0:
    print("No ratings available.")
else:
    # Get ratings from user
    ratings = []
    for i in range(n):
        rating = int(input(f"Enter rating {i+1} (1-5): "))
        ratings.append(rating)

    # Calculate positive feedback percentage
    result = calculate_positive_percentage(ratings)
    print(f"Positive Feedback: {result:.1f}%")