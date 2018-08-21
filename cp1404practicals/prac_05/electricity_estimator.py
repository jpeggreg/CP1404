#TARIFF_11 = 0.244618
#TARIFF_31 = 0.136928

tariff_dict = {"TARIFF_11": 0.244618, "TARIFF_31": 0.136928}

print("Electricity bill estimator 2.0\n")
for key in tariff_dict:
    print(key)
cents_per_kwh = (input("Which tariff? "))
if TARIFF_11:
    cents_per_kwh = tariff_dict[key : 0]
elif TARIFF_31:
    cents_per_kwh = tariff_dict[key : 1]
else:
    print("Invalid choice")
    cents_per_kwh = float(input("\nWhich tariff? "))
daily_use = float(input("Enter the daily use in kWh. eg 4.5 :"))
days = float(input("Enter the number of days. eg 90 :"))
total_bill = cents_per_kwh * daily_use * days
print("\nEstimated bill: $" + "{:.2f}".format(total_bill))