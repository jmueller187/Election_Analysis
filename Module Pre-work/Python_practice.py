# counties = ["Arapahoe","Denver","Jefferson"]
# # if "El Paso" in counties:
# #     print("El Paso is in the list of counties.")
# # else:
# #     print("El Paso is not in the list of counties.")

# # for county in counties:
# #     print(county)
# # for i in range(len(counties)):
# #     print(counties[i])
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# # for county in counties_dict.keys():
# #     print(county)

for county, voters in counties_dict.items():
    print(f"{county} has {voters:,} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(f"The county of {county_dict['county']} has {county_dict['registered_voters']:,} registered voters.")
