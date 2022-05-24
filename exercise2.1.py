def bmi(subject, weight, height):
    bmi_subject = int(weight / height**2)
    print("bmi {} = {}".format('subject' + subject, bmi_subject))

# Subject data = [weight_kg, height_m]
subjects = [
    [1, 80, 1.62],
    [2, 69, 1.53],
    [3, 80, 1.66],
    [4, 80, 1.79]
]
for subject in subjects:
    bmi_subject = bmi(str(subject[0]), subject[1], subject[2])
    