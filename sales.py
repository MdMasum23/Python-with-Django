# List of daily sales (in dollars)
daily_sales = [1200, 800, 1500, 600, 2000, 700]

# Set threshold for good sales
threshold = 1000

# Extract days with sales above threshold using list comprehension
high_sales = [sale for sale in daily_sales if sale > threshold]
print("Sales above threshold:", high_sales)

# Apply a discount (e.g., 10% off)
discounted_sales = [sale * 0.9 for sale in high_sales]
print("Discounted Sales:", discounted_sales)
