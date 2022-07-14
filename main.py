#!/usr/bin/python3
import twint

c = twint.Config()
c.Hide_output = True
c.Store_csv = True
c.Count = True
c.Search = "refugee OR immigrant OR migrant OR immigration"

output = "tweets_2019_"
since = "2019-"
until = "2019-"

for i in range(1,12):
    if i > 8:
        c.Output = output + str(i) + ".csv"
        c.Since = since + str(i) + "-" + "01"
        c.Until = until + str(i) + "-" + "30"
        print("Running..." + output + str(i) + ".csv")
        twint.run.Search(c)
        print("finished" + output + str(i) + ".csv")
    elif (i == 2):
        c.Output = output + "0" + str(i) + ".csv"
        c.Since = since + "0" + str(i) + "-" + "01"
        c.Until = until + "0" + str(i) + "-" + "28"
        print("Running..." + output + "0" + str(i) + ".csv")
        twint.run.Search(c)
        print("finished" + output + "0" + str(i) + ".csv")
    else:
        c.Output = output + "0" + str(i) + ".csv"
        c.Since = since + "0" + str(i) + "-" + "01"
        c.Until = until + "0" + str(i) + "-" + "30"
        print("Running..." + output + "0" + str(i) + ".csv")
        twint.run.Search(c)
        print("finished" + output + "0" + str(i) + ".csv")

# for i in range(7):
#      print(output + str(i + 6) + ".csv")
#      print(since + str(i + 6) + "-" + "01")
#      print(until + str(i + 6) + "-" + "30")

print("finished")
