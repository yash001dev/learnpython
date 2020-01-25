#Logical Operation
has_high_income=True
has_good_credit=True

if has_good_credit and has_high_income:
    print("Eligible Of Loan")

has_good_credit=True
has_high_income=False

if has_good_credit or has_high_income:
    print("Eligible Of Loan")
    has_good_credit=False
else:
    print("Sorry You Are Not Eligiable For Loan...")

