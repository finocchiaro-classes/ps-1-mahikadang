prior_arrests = int(input("Prior arrests: "))
local_ordinance = input("Prior arrests for local ordinance (Y/N): ")
age_at_release = int(input("Age at release: "))

risk_score = 0

if prior_arrests >= 2:
    risk_score += 1
if prior_arrests >= 5:
    risk_score += 1
if local_ordinance == "Y":
    risk_score += 1
if 18 <= age_at_release <= 24:
    risk_score += 1
if age_at_release >= 40:
    risk_score -= 1

print(f"The recidivism risk score is {risk_score}")
