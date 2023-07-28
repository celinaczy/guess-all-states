import csv
import pandas

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)
#
# data = pandas.read_csv("weather_data.csv")
# # print(data)
# # data_dict = data.to_dict()
# # print(data_dict)
#
# # temp_list = data["temp"].to_list()
# # print(temp_list)
# # print(sum(temp_list)/len(temp_list))
#
# # print(data["temp"].mean())
# # print(data["temp"].max())
# #
# # print(data.condition)
#
# # data in row
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# print(monday.temp*1.8 +32)

df = pandas.read_csv("squirrel_data.csv")

colors = df["Primary Fur Color"].to_list()

gray = colors.count("Gray")
cinnamon = colors.count("Cinnamon")
black = colors.count("Black")
print(gray)
print(cinnamon)
print(black)

d = {'Fur Color': ["gray", "cinnamon", "black"],
     'count': [gray, cinnamon, black]}
data_frame = pandas.DataFrame(data=d)
print(data_frame)

data_frame.to_csv("squirrel_count.csv")