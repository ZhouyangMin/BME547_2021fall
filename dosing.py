"""dosing.py
    Example program of calculating first-day dose of medicine for pediatric
        patients.
    NOTE:  This is a programming example, and should not be used for any
             type of medical treatment or diagnostics.
"""


def dose_amount():
    print("Day One Dosing Guidelines")
    print("")
    print("Choose diagnosis:")
    print("1 - Acute otitis media")
    print("2 - Acute bacterial sinusitis")
    print("3 - Community-acquired pneumonia")
    print("4 - Pharyngitis/tonsilitis")
    diagnosis = int(input("Enter a number: "))
    print("PATIENT WEIGHT")
    print("Enter patient weight followed by units of kg or lb.")
    print("Examples:  65.3 lb      21.0 kg")
    weight_input = (input("Enter weight: "))
    return diagnosis, weight_input




def unit_converstion(input_lb):
    weight = weight / 2.205
    return weight


def calculations(diagnosis, weight):
    weight_data = weight_input.split(" ")
    weight = float(weight_data[0])
    units = weight_data[1]
    if units == "lb":
        weight = unit_converstion(weight)
    dosages_mg_per_kg = [30, 10, 10, 12]
    dosage_mg_per_kgdoi = dosages_mg_per_kg[diagnosis-1]
    dosage_mg_first_day = weight * dosage_mg_per_kg
    return weight, dosage_mg_first_day


def data_ouput(weight, dosage_mg_first_day):
    print("CORRECT DOSAGE")
    print("For a patient weighing {:.1f} kg,".format(weight))
    print("  the correct dosage is {:.1f} mg the first day"
          .format(dosage_mg_first_day))


def program_driver():
    diag, w_input = info_input()
    wt, dose_1 = calculations(diag, w_input)
    data_output(wt, dose_1)

if __name__ == '__main__':
    program_driver()


