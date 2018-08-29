TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator")
cents_per_kwh = float(input("\nWhich tariff? 11 or 31:"))
if 11:
    cents_per_kwh = TARIFF_11
elif 31:
    cents_per_kwh = TARIFF_31
daily_use = float(input("Enter the daily use in kWh. eg 4.5 :"))
days = float(input("Enter the number of days. eg 90 :"))
total_bill = cents_per_kwh * daily_use * days
print("\nEstimated bill: $" + "{:.2f}".format(total_bill))