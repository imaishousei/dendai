# -*- coding: utf-8 -*-
"""dendai

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10pIb85IWyXk9yax-gQXOSXE2oRYD0pbL
"""

mon={"1":"なし",
         "2":"なし",
         "3":"https://dendai.zoom.us/j/98616233730?pwd=aEMrUCt0ZzhxaW1BcENrUE15ZlphUT09",
         "4":"https://dendai.zoom.us/meeting/register/tJYtcu-tpjIqHdbhuo7hkNY1H36ua99TdfCL"}
tue={"1":"なし",
        "2":"https://dendai.zoom.us/j/93399101753?pwd=WERjWXlCQkZ1ck1qbGw0QWllMTlZdz09",
        "3":"https://dendai.zoom.us/j/94044669914",
        "4":"もうちょっと！"}
wen={"1":"https://dendai.zoom.us/j/98739046402?pwd=U3hOMFhiWlkyZnU3V0lMS0ZCK2NRQT09",
         "2":"https://dendai.zoom.us/meeting/register/tJYsc-2trD0qGdAId2OuYBH_bXMYRl9ndOAl",
         "3":"https://dendai.zoom.us/j/99899339827?pwd=QnBPK0pHakkycHIwZFNzMyswcVhYZz09",
         "4":"なし"}
thu={"1":"https://dendai.zoom.us/j/91382018091?pwd=T3JPM3JrQmNsa2liYUw5aTFlWmdFZz09",
       "2":"https://dendai.zoom.us/j/94602326239?pwd=ZW9KcUhPeXl2dHFLUDArMHhmR3cydz09",
       "3":"なし",
       "4":"なし"}
fri={"1":"なし",
      "2":"954 7234 5053",
      "3":"https://dendai.zoom.us/j/95626090877?pwd=VHgySFhLM1BtQjlxM0JGVE5LNE5EUT09",
      "4":"https://dendai.zoom.us/j/93106055915?pwd=KytmYTZKWitPT3c1dEZ4Q0lJSTRrZz09"}
      
suuri={"1":"https://dendai.zoom.us/j/91816391864?pwd=T3hUQjVRT1ZyV2lZM1hQeUd5NHh5dz09",
          "2":"https://dendai.zoom.us/j/91596730340?pwd=b3R6cEd0aFJ0N0I5T1h5Njlsemlpdz09",
          "3":"https://dendai.zoom.us/j/95074812801?pwd=SHdZT08yckF0YlN1dEFQUVVrWFkvdz09",
          "4":"https://dendai.zoom.us/j/95068918562?pwd=amt3WG9PQ3NQSXIxbWRsYkc5YWRCQT09"}
day_we = "何曜日？"
time_pr = "何時間目？"
Day_we = input(day_we)
if Day_we == "月":
  Time_pr =input(time_pr)
  dis = mon[Time_pr]
  print(dis)
if Day_we == "火":
  Time_pr =input(time_pr)
  dis = tue[Time_pr]
  print(dis)
  if Time_pr == "3":
    print("078276")
  if Time_pr == "4":
    day=input("何日？")
    if day == "1116":
      print(suuri["2"])
    elif day == "1123":
      print(suuri["2"])
    elif day == "1130":
      print(suuri["3"])
    elif day == "1207":
      print(suuri["4"])
    elif day == "1214":
      print(suuri["1"])
    
     
if Day_we == "水":
  Time_pr =input(time_pr)
  dis = wen[Time_pr]
  print(dis)
if Day_we == "木":
  Time_pr =input(time_pr)
  dis = thu[Time_pr]
  print(dis)
if Day_we == "金":
  Time_pr =input(time_pr)
  dis = fri[Time_pr]
  print(dis)
  if Time_pr == "2":
    print("004407")