
******************************
CS 1026 - Assignment 1 – Healthcare Wait Time Optimizer: Megan Kim
Student ID: mkim945
File created: February 6, 2025
******************************


# Define constants
VALID_SYMPTOMS = ["fever", "cough", "heart", "other"] # this is a list of the allowed symptoms
VALID_URGENCY_LEVELS = ["1", "2", "3"] # this is the list of urgency levels
HOSPITAL_NAMES = ["Victoria Hospital", "St. Joseph's Hospital", "London Health Sciences Centre"] # these will be the list of hospital names

# Wait time multipliers for hospitals
VICTORIA_PATIENTS = 15
VICTORIA_TIME = 10

JOSEPH_PATIENTS = 10
JOSEPH_TIME = 12

LONDON_PATIENTS = 20
LONDON_TIME = 8

# Take the user's input for each patient's names
patient_name = input("Enter your name: ").strip()
while patient_name == "":
    print("That is not valid input. Try again")
    patient_name = input("Enter your name: ").strip()

# Prompt the user to enter the patient symptoms, convert any input to lowercase
symptoms = input("Enter your most severe symptom (fever, cough, heart, other): ").strip().lower()
# Prevent invalid answers
while symptoms not in VALID_SYMPTOMS:
    print("That is not valid input. Try again")
    symptoms = input("Enter your most severe symptom (fever, cough, heart, other): ").strip().lower()

# Take the user's input for the urgency levels of each patient
urgency_level = input("Please enter your urgency level (1,2,3): ").strip()
# Prevent invalid answers
while urgency_level not in VALID_URGENCY_LEVELS:
    print("Please enter a valid urgency level. Try again")
    urgency_level = input("Please enter your urgency level (1 = mild, 2 = moderate, 3 = severe): ").strip()
urgency_level = int(urgency_level)

# Calculate the wait time based off of the formulas
wait_time_victoria = round((VICTORIA_PATIENTS * VICTORIA_TIME) / urgency_level, 1)
wait_time_joseph = round((JOSEPH_PATIENTS * JOSEPH_TIME) / urgency_level, 1)
wait_time_london = round((LONDON_PATIENTS * LONDON_TIME) / urgency_level, 1)

# Now we will compare the wait times to determine the fastest time
if wait_time_victoria < wait_time_london and wait_time_victoria < wait_time_joseph:
    fastest_hospital = HOSPITAL_NAMES[0]
    fastest_time = wait_time_victoria
elif wait_time_joseph < wait_time_london and wait_time_joseph < wait_time_victoria:
    fastest_hospital = HOSPITAL_NAMES[1]
    fastest_time = wait_time_joseph
else:
    fastest_hospital = HOSPITAL_NAMES[2]
    fastest_time = wait_time_london

# These are the outputs based off of each patient's input
print("\n--- Results ---")
print(f"Patient Name: {patient_name}")
print(f"Symptoms: {symptoms.capitalize()}")
print(f"Urgency Level: {urgency_level}")
print(f"{HOSPITAL_NAMES[0]} Wait Time: {wait_time_victoria} minutes")
print(f"{HOSPITAL_NAMES[1]} Wait Time: {wait_time_joseph} minutes")
print(f"{HOSPITAL_NAMES[2]} Wait Time: {wait_time_london} minutes")

# these are the resulting outputs based off of the symptoms
if symptoms == "fever":
    specialty_wait = wait_time_victoria
elif symptoms == "cough":
    specialty_wait = wait_time_joseph
elif symptoms == "heart":
    specialty_wait = wait_time_london
else:
    specialty_wait = None

if specialty_wait is not None:
    difference = round(specialty_wait - fastest_time, 1)
    print(f"Specialty hospital wait time: {specialty_wait} minutes. Fastest hospital: {fastest_hospital} with {fastest_time} minutes. Difference: {difference} minutes.")
else:
    print(f"Fastest hospital: {fastest_hospital} with {fastest_time} minutes.")
    print("No specialty hospital for your symptom.")
