import csv

file_in = open('data_base.csv', mode='r', encoding='utf-8')
reader = csv.reader(file_in, delimiter='\t', quotechar='"')
data = [i for i in reader]
data = [[i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[1], i[3], i[4], i[5], i[2], i[0]] for i in data]
file_in.close()

file_ou = open('new_data_base.csv', mode='w', encoding='utf-8')
writer = csv.writer(file_ou, delimiter='\t', quotechar='"', lineterminator="\n")
[writer.writerow(i) for i in data]
file_ou.close()

file_in = open('new_data_base.csv', mode='r', encoding='utf-8')
reader = csv.reader(file_in, delimiter='\t', quotechar='"')
data = [i for i in reader]
file_in.close()
[print(i) for i in data[:2]]  # Нужно исправить 7, 9
