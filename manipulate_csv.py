import csv
import random

f = open("sms_report.csv")
out = open("CamelBuy&FlyPromoWeek4_201910031614.csv")
write = open("CamelBuy&FlyPromoWeek4_201910031614_copy.csv", "w")

csv_f = csv.reader(f)
csv_reader = csv.reader(out)
csv_writer = csv.writer(write)


def read_from_sms(sms_f):
    phone_numbers = []

    for index, row in enumerate(sms_f):

        if row[5] != "" and row[8] == "Positive" and row[3] == "Ghana":
            phone_numbers.append(["Nil", "Nil", "Nil", "Nil", row[5]])

    group_of_list_of_five_numbers = group_into_five(phone_numbers)

    return group_of_list_of_five_numbers


def group_into_five(phone_numbers):

    group_size = 4
    list_of_groups = [
        phone_numbers[i : i + group_size]
        for i in range(0, len(phone_numbers), group_size)
    ]
    return list(list_of_groups)


result_of_group_of_list_of_five_numbers = read_from_sms(csv_f)

for index, row in enumerate(csv_reader):
    csv_writer.writerow(row)
    five = result_of_group_of_list_of_five_numbers[index]
    csv_writer.writerows(five)

out.close()
f.close()
