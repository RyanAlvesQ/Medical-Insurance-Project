names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

names.append("Priscilla")
print (names)
insurance_costs.append(8320.0)
print(insurance_costs)

medical_records = list(zip(insurance_costs,names))
print (medical_records)

num_medical_records = len(medical_records)
print ("\n There are " + str(num_medical_records) + " medical records.")

first_medical_record = medical_records[0]
print("\n Here is the first medical record: " + str(first_medical_record))

medical_records.sort()
print("\n Here are the medical records sorted by insurance cost: " + str (medical_records))

cheapest_three = medical_records[:3]
print("\n Here are the three cheapest insurance costs in our medical records: " + str(cheapest_three))

priciest_three = medical_records[-3:]
print("\n Here are the three most expensive insurance costs in our medical records: "+ str(priciest_three))

occurrences_paul = names.count("Paul")
print("\n There are " + str(occurrences_paul) + " individuals with the name Paul in our medical records.")

names_list = list(zip(names, insurance_costs))
sorted_names_list = sorted(names_list)
print("\n Here the medical records sorted alphabetically by name: " + str(sorted_names_list))
middle_five_records = sorted_names_list[3:8]
print ("\n There the middle five records: " + str(middle_five_records))


