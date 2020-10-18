import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.append(19)
ages.append(26)
print(ages)
median_age=statistics.median(ages)
print(median_age)
average1=statistics.mean(ages)
average2=sum(ages)/len(ages)
print(average1)
print(average2)
range_ages=max(ages)-min(ages)
print(range_ages)
min_average=min(ages)-average1
max_average=max(ages)-average1
x = abs(min_average)
y = abs(max_average)
print(x, y)