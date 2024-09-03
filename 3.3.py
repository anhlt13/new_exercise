gender = input("Enter your gender: ")
hemoglobin_value = int(input("Enter your hemoglobin value: "))
if gender == "Male":
    if hemoglobin_value >=117 and hemoglobin_value <=122:
        print("the hemoglobin value is normal")
    elif hemoglobin_value >=122:
        print("the hemoglobin value is high")
    else:
        print("the hemoglobin value is low")
else:
    if hemoglobin_value >=134 and hemoglobin_value <= 167:
        print("the hemoglobin value is normal")
    elif hemoglobin_value >=167:
        print("the hemoglobin value is high")
    else:
        print("the hemoglobin value is low")
