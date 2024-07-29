# Medical Insurance Project

## Project Overview
As a medical professional, understanding how various factors contribute to medical insurance costs can provide valuable insights for both policy-making and patient advising. This project uses a formula to estimate a person's yearly medical insurance costs based on specific factors such as age, sex, Body Mass Index (BMI), number of children, and smoking status. By analyzing these factors, we can better understand their impact on insurance cost predictions and possibly identify areas for intervention or improvement.

## Objective
The main objective of this project is to investigate how different factors affect the prediction of medical insurance costs. By using a predefined formula, we will:
- Calculate initial insurance costs.
- Analyze the impact of changing individual factors (e.g., age, BMI).
- Understand the relative importance of each factor in determining insurance costs.

## Factors Considered
- **Age:** The age of the individual.
- **Sex:** The gender of the individual (0 for female, 1 for male).
- **BMI:** Body Mass Index, a measure of body fat based on height and weight.
- **Number of Children:** The number of children/dependents covered by the insurance.
- **Smoking Status:** Smoking status of the individual (0 for non-smoker, 1 for smoker).

## Formula for Insurance Cost Estimation
The insurance cost is estimated using the following formula:

insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

## Analysis Steps
1. **Initial Calculation:** Compute the initial insurance cost using the provided formula.
2. **Age Impact:** Analyze how changing the age affects the insurance cost.
3. **BMI Impact:** Examine the effect of variations in BMI on the insurance cost.
4. **Other Factors:** Investigate the influence of sex, number of children, and smoking status on the insurance cost.
5. **Comparative Analysis:** Compare the relative impact of each factor to understand their importance.

## Usage
To use this project, simply clone the repository and run the provided Python scripts. The scripts will guide you through the steps of calculating and analyzing the insurance costs based on different factors.

```bash
git clone https://github.com/RyanAlvesQ/Medical-Insurance-Project.git
cd Medical-Insurance-Project
python "Medical Insurance Project.py"
