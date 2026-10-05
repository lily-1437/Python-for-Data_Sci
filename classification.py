values = [12, -5, 0, 7, -3, 0, 18, -1]
pos = []
neg = []
zero = []
pos_count = 0
neg_count = 0
zero_count = 0
for i in values:
    if(i>0):
        pos.append(i)
        pos_count +=1
    elif i==0:
        zero.append(i)
        zero_count +=1
    else:
        neg.append(i)
        neg_count +=1

print("Postive: ", pos)
print("Zero: ", zero)
print("Negative: ", neg)
print(f"Count: {pos_count} {zero_count} {neg_count}")