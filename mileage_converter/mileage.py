print("How many kilometres did you run today?")
kms = input()
miles = float(kms)/1.60934
miles = round(miles, 2)
print(f"Well done. Your {kms}km is {miles} miles")
