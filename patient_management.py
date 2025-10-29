def search_patients_by_disease(patients, disease):
    result = [p["Name"] for p in patients if p["Disease"].lower() == disease.lower()]
    return result

n = int(input("Enter number of patients: "))

patients = []
for i in range(n):
    print(f"\nEnter details for patient {i+1}:")
    name = input("Name: ")
    age = int(input("Age: "))
    disease = input("Disease: ")
    patients.append({"Name": name, "Age": age, "Disease": disease})
    
search_disease = input("\nEnter disease to search for: ")

matching_patients = search_patients_by_disease(patients, search_disease)

if matching_patients:
    print(f"\nPatients with {search_disease}: {matching_patients}")
else:
    print(f"\nNo patients found with {search_disease}.")