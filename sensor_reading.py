readings = [21.5, None, 24.0, 31.2, -4.0, 28.5, None, 35.1]
alert = []
avg = 0
sum_i = 0
for i in readings:
    if(i== None or i<0):
        continue
    if(i>=30):
        alert.append(i)
    sum_i += i
    avg = sum_i/len(readings)
# print("Clean reading: ", )
print("Average: ", avg)
print("Alerts: ", alert)

