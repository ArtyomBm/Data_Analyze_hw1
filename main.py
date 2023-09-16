import matplotlib.pyplot as plt
import numpy as np

age = []
revenue = []
gender = []
time = []
number = []
Agesize = {'10-20': [[], [], []], '21-30': [[], [], []], '31-40': [[], [], []],
           '41-50': [[], [], []], '51-60': [[], [], []], '61-70': [[], [], []]}
with open('Data.csv') as f:
    for i in f:
        if i.split(',')[1] == 'Age':
            continue
        age.append(int(i.split(',')[1]))
        revenue.append(float(i.split(',')[3]))
        gender.append(int(i.split(',')[2]))
        time.append(int(i.split(',')[-4]))
        number.append(int(i.split(',')[4]))
        if int(i.split(',')[1]) > 10 and int(i.split(',')[1]) < 21:
            Agesize['10-20'][0].append(int(i.split(',')[1]))
            Agesize['10-20'][1].append(float(i.split(',')[3]))
            Agesize['10-20'][2].append(float(i.split(',')[-4]))
        if int(i.split(',')[1]) > 20 and int(i.split(',')[1]) < 31:
            Agesize['21-30'][0].append(int(i.split(',')[1]))
            Agesize['21-30'][1].append(float(i.split(',')[3]))
            Agesize['21-30'][2].append(float(i.split(',')[-4]))
        if int(i.split(',')[1]) > 30 and int(i.split(',')[1]) < 41:
            Agesize['31-40'][0].append(int(i.split(',')[1]))
            Agesize['31-40'][1].append(float(i.split(',')[3]))
            Agesize['31-40'][2].append(float(i.split(',')[-4]))
        if int(i.split(',')[1]) > 40 and int(i.split(',')[1]) < 51:
            Agesize['41-50'][0].append(int(i.split(',')[1]))
            Agesize['41-50'][1].append(float(i.split(',')[3]))
            Agesize['41-50'][2].append(float(i.split(',')[-4]))
        if int(i.split(',')[1]) > 50 and int(i.split(',')[1]) < 61:
            Agesize['51-60'][0].append(int(i.split(',')[1]))
            Agesize['51-60'][1].append(float(i.split(',')[3]))
            Agesize['51-60'][2].append(float(i.split(',')[-4]))
        if int(i.split(',')[1]) > 60 and int(i.split(',')[1]) < 71:
            Agesize['61-70'][0].append(int(i.split(',')[1]))
            Agesize['61-70'][1].append(float(i.split(',')[3]))
            Agesize['61-70'][2].append(float(i.split(',')[-4]))

print("Корреляция между возрастом и выручкой: ", np.corrcoef(age, revenue)[0,1])
print("Корреляция между полом и временем, проведенным на сайте: ", np.corrcoef(gender, time)[0,1])
print("Корреляция между временем, проведенным на сайте, и выручкой: ", np.corrcoef(time, revenue)[0,1])

nums = []
for i in Agesize:
    nums.append(len(Agesize[i][0]))
plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.bar(Agesize.keys(), nums)
plt.title('Количество людей по возрасту')

sums = []
for i in Agesize:
    sums.append(sum(Agesize[i][1]))

perperson = []
for i in range(len(Agesize.keys())):
    perperson.append(sums[i]/nums[i])

total_time = []
for i in Agesize:
    total_time.append(sum(Agesize[i][2]))

plt.subplot(132)
plt.plot(Agesize.keys(), perperson)
plt.title('Выручка на человека по возрасту')

time_per_person = []
for i in range(len(Agesize.keys())):
    time_per_person.append(total_time[i]/nums[i])

plt.subplot(133)
plt.plot(Agesize.keys(), time_per_person)
plt.title('Время на сайте по возрасту')
plt.show()
