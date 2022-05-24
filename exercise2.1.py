def bmi_calc(sub_num, weight_kg, height_m):    
    subject = 'subject' + str(sub_num)
    bmi = int(weight_kg / height_m**2)
    print("bmi {} = {}".format(subject, bmi))

# Subject data = [weight_kg, height_m]
subjects = [
    [1, 80, 1.62],
    [2, 69, 1.53],
    [3, 80, 1.66],
    [4, 80, 1.79]
]

for sub in subjects:
    bmi_calc(sub[0], sub[1], sub[2])