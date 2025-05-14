from datetime import datetime, date

# Function to calculate the difference in days between two date objects
def calculate_date_difference(start_date, end_date):
    return (end_date - start_date).days

# Function to calculate the difference in days between two datetime objects
def calculate_datetime_difference(start_datetime, end_datetime):
    return (end_datetime.date() - start_datetime.date()).days

# Main function to demonstrate the difference between LocalDate and LocalDateTime
def main():
    # Demonstrating LocalDate (using date)
    date1 = date(2022, 5, 1)
    date2 = date(2025, 5, 14)
    
    # Difference in days between two date objects
    date_diff = calculate_date_difference(date1, date2)
    print(f"Difference in days (LocalDate): {date_diff}")  # 1095 days

    # Demonstrating LocalDateTime (using datetime)
    datetime1 = datetime(2022, 5, 1, 10, 30)
    datetime2 = datetime(2025, 5, 14, 12, 45)
    
    # Difference in days between two datetime objects
    datetime_diff = calculate_datetime_difference(datetime1, datetime2)
    print(f"Difference in days (LocalDateTime): {datetime_diff}")  # 1095 days

if __name__ == "__main__":
    main()
