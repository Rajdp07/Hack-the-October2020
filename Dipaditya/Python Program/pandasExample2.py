import pandas as pd

# cars = pd.read_csv("cars.csv")
cars = pd.read_csv("cars.csv", index_col=0)

print(cars)

# Print out country column as Pandas Series
print(cars["country"])
print(type(cars["country"]))
# Print out country column as Pandas DataFrame
print(cars[["country"]])
print(type(cars[["country"]]))
# Print out DataFrame with country and drives_right columns
print(cars[["country", "drives_right"]])
print()
# Print out first 3 observations
print(cars[0:3])
print()
# Print out fourth, fifth and sixth observation
print(cars[3:6])
print()

# Print out observation for Japan
print(cars.loc["JAP"])
print(cars.iloc[2])
# Print out observations for Australia and Egypt
print(cars.loc[["AUS", "EG"]])
print(cars.iloc[[1, -1]])
