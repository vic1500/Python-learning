import converter as cvtr
from converter import kgs_to_lbs # Another way of importing but it only imports specific functions

kg = cvtr.lbs_to_kg(70)
lbs = cvtr.kgs_to_lbs(50)

print("Weight in kg is: {}".format(kg))
print(f"Weight in lbs is: {lbs}")