names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Add your code here
total_cost = 0
for adding in actual_insurance_costs:
  total_cost += adding

print ("Total cost: " + str(total_cost))

average_cost = total_cost / len(actual_insurance_costs)

print ("Average Insurance Cost: " + str(average_cost) + " dollars.")

for i in range(len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  print("The insurance cost for " + str(name) + " is " + str(insurance_cost) + " dollars.")
  if insurance_cost > average_cost:
    print("The insurance cost for " + str(name) + " is above average.")
  elif insurance_cost < average_cost:
    print("The insurance cost for " + str(name) + " is below average.")
  else:
    print ("The insurance cost for " + str(name) + " is equal to the average.")

#If you look closely at actual_insurance_costs and 
#estimated_insurance_costs, you will notice that each of the actual 
#insurance costs are 10% higher than the estimated insurance costs.
#Using a list comprehension, create a new list called #pdated_estimated_costs, which has each element in 
#estimated_insurance_costs multiplied by 11/10.

updated_estimated_costs = [num * 11/10 for num in estimated_insurance_costs]

print(updated_estimated_costs)

