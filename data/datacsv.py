import pandas as pd

column_names = [
    "Status", "Duration", "CreditHistory", "Purpose", "CreditAmount",
    "Savings", "EmploymentSince", "InstallmentRate", "PersonalStatusSex",
    "OtherDebtors", "PresentResidence", "Property", "Age",
    "OtherInstallmentPlans", "Housing", "ExistingCredits", "Job",
    "NumberPeopleLiable", "Telephone", "ForeignWorker", "Creditability"
]

df = pd.read_csv("data/german.data", sep=' ', header=None, names=column_names)
df.to_csv("data/german_credit_data.csv", index=False)
print(" Converted to german_credit_data.csv")
