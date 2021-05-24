import pandas as pd
import numpy as np
from urllib.request import urlretrieve
import matplotlib.pyplot as plt
import seaborn as sns
import statistics

# 1. real homeless dataset from website gov.ie. Link in Project Report
# 2. import data Relational Database or API or Web Scraping
url = "https://data.usmart.io/org/ae1d5c14-c392-4c3f-9705-537427eeb413/resource?resourceGUID=fa85b876-e753-4a60-b3fb-bb4f2dd0a6c3"
response = urlretrieve(url, "Homeless Report March 2021")
print(response)

# download CSV dataframe
Homeless21 = pd.read_csv("Homelessness Report March 2021.csv", index_col = 0)
print(Homeless21)
#3
#Checking for missing data in the whole dataframe, shows no missing VALUES
print(Homeless21.isna())
#cheking for missing data in columns
print(Homeless21.isna().any())

#dataframe shows no missing values however if it did I would use Homeless.fillna(0) to fix data

#manipulating data
print(Homeless21.head())
print(Homeless21.tail())
print(Homeless21.info())
#converting objects to floats
Homeless21 = Homeless21.apply(lambda x: pd.to_numeric(x.astype(str).str.replace(',',''), errors='coerce'))
print(Homeless21.info())
print(Homeless21)

print(Homeless21["Total Adults"].mean())
print(Homeless21["Total Adults"].median())
print(Homeless21["Total Adults"].max())
print(Homeless21["Total Adults"].min())

# The .agg() method allows to apply custom functions to a DataFrame, as well as apply functions to more than one column
# of a DataFrame at once

def iqr(column):
    return column.quantile(0.80) - column.quantile(0.30)

print(Homeless21["Total Adults"].agg(iqr))
print(Homeless21["Male Adults"].agg(iqr))
#Column selection by using the iqr function with .agg() to print the IQR
# of Total Adults, Male Adults and Female Adults in that order.
print(Homeless21[["Total Adults", "Male Adults", "Female Adults"]].agg(iqr))
#include median and mean
print(Homeless21[["Total Adults", "Male Adults", "Female Adults"]].agg([iqr, np.median]))
print(Homeless21[["Total Adults","Male Adults", "Female Adults"]].agg([iqr, np.mean]))


#descriobe shows count, mean, std, min, 25%, 50%, 75%, max in the data frame
print(Homeless21.describe())
print(Homeless21.isna().any())
#The groupby() function returns a GroupBy object. It describes how the rows of the original data set has been split.
# the GroupBy object .groups variable is a dictionary whose keys are the computed unique groups and corresponding
# values being the axis labels belonging to each group.
print(Homeless21.groupby(['Female Adults']).groups.keys())
print(statistics.mean(Homeless21.groupby(['Female Adults']).groups.keys()))
print(statistics.mean(Homeless21.groupby(['Male Adults']).groups.keys()))
# Number of non-null unique network entries (output 9)
print(Homeless21['Female Adults'].nunique())
print(Homeless21.groupby('Female Adults').first())

#selecting rows using loc and iloc using row names and indexing
print(Homeless21.loc[["Dublin", "Mid-West", "South-East"]])
print(Homeless21.iloc[[0,3,6], [1,2,3]])
print(Homeless21.iloc[:, [1,2,3]])

#sorting by index values
print(Homeless21.sort_index())

#sorting from lowest to highest
print(Homeless21.sort_values("Number of Single-Parent families"))
#from highest to lowest number
print(Homeless21.sort_values("Number of Single-Parent families", ascending=False))

#rows with Families >200
print(Homeless21[Homeless21["Number of Single-Parent families"] > 200])

#filter only those data points where Number of Families is more than 10  and less than 600
print(Homeless21[(Homeless21["Number of Families"]>10) & (Homeless21["Number of Families"]<600)])

#Itterows and loops
#Below shows all columns
for val in Homeless21 :
    print(val)
# all columns and rows one by one
for lab, row in Homeless21.iterrows() :
    print(lab)
    print(row)
# region and total Adults
for lab, row in Homeless21.iterrows() :
    print(str(lab) + ": " + str(row["Total Adults"]))

#merge data frames

Homeless20 = pd.read_csv("Homelessness Report March 2020.csv", index_col = 0)
print(Homeless20)

Homeless20 = Homeless20.apply(lambda x: pd.to_numeric(x.astype(str).str.replace(',',''), errors='coerce'))
print(Homeless20.head())
print(Homeless20.shape)

#merge on dataframes to see the scale of changes
outer_homeless_merge = pd.merge(Homeless21, Homeless20, on="Region" , how="outer")
print(outer_homeless_merge)
print(outer_homeless_merge.shape)
#append two dataframes  and ignore the fact that they may have overlapping indexes.
result = Homeless21.append(Homeless20, ignore_index=True, sort=False)
print(result)
# merge by using concat
result1 = pd.concat([Homeless21, Homeless20], axis=0)
print(result1)
print(result1.shape)

#4 python
#Use functions to create reusable code.

# resusable function created in the loop using dictionaries
TotAdults3 = {"Dublin": 4094,
              "Mid-East": 338,
              "Midlands": 67,
              "Mid-West": 284,
              "North-East": 85,
              "North-West": 80,
              "South-East": 184,
              "South-West": 486,
              "West": 277}
new_dict = {}

def set_benchmark(parameter):
  for key, value in TotAdults3.items():
    if value <= parameter:
      new_dict[key] = value
  print(new_dict)

set_benchmark(300)


#creatig a list
TotAdults = ["Dublin", 4094, "Mid-East", 338, "Midlands", 67, "Mid-West", 284, "North-East", 85, "North-West", 80, "South-East", 184, "South-West", 486, "West", 277]
print(TotAdults)
TotAdults2 = [["Dublin", 4094],
              ["Mid-East", 338],
              ["Midlands", 67],
              ["Mid-West", 284],
              ["North-East", 85],
              ["North-West", 80],
              ["South-East", 184],
              ["South-West", 486],
              ["West", 277]]
print(TotAdults2)
print(type(TotAdults))
print(type(TotAdults2))
MidPart = TotAdults[2:8]
print(MidPart)

print(TotAdults2[3][1])

print(TotAdults[7])

NorthData = TotAdults[9] + TotAdults[11]
print(NorthData)

#Numpy
#converting dataframe to numpy
Home_Array = Homeless21.to_numpy()
print(Home_Array)
print(type(Home_Array))

#using list for 2D Numpy conversion

np_TotalAdults2 = np.array(TotAdults2)
print(np_TotalAdults2.shape)
print(np_TotalAdults2)

TotAdults3 = [["Dublin", 4515],
              ["Mid-East", 317],
              ["Midlands", 97],
              ["Mid-West", 331],
              ["North-East", 112],
              ["North-West", 69],
              ["South-East", 218],
              ["South-West", 550],
              ["West", 343]]

np_TotalAdults3 = np.array(TotAdults3)
print(np_TotalAdults3)

print(type(np_TotalAdults2))

print(type(np_TotalAdults3))
#new arrays
FemaleAdults21 = [1387, 107, 27, 87, 20, 23, 51, 142, 109]
FemaleAdults20 = [1742, 126, 44, 132, 48, 19, 56, 205, 153]
#converting string to float
FemaleAdult21_Array = np.array(FemaleAdults21)
FemaleAdult20_Array = np.array(FemaleAdults20)

print("Alert, Homelessness is rising: ",FemaleAdult21_Array)

#test if each element of a 1-D array is also present in a second array
print(np.in1d(FemaleAdult21_Array, FemaleAdult20_Array))

#creating a new array - the average of every consecutive triplet of elements of a given array
arr1 = np.array([1387, 107, 27, 87, 20, 23, 51, 142, 109])
print(arr1)
result = np.mean(arr1.reshape(-1, 3), axis=1)
print(result)


# #creating a new data frame to show describe() output on Total adultsplt using an existing dataframe

Home21_Desc21 = pd.DataFrame(Homeless21['Total Adults'].describe().tolist(), columns = ['Total Adultsplt21'])
print(Home21_Desc21.describe())

Home20_Desc20 = pd.DataFrame(Homeless20['Total Adults'].describe().tolist(), columns = ['Total Adultsplt20'])
print(Home20_Desc20.describe())

combine_Homeless_Desc = pd.concat([Home21_Desc21, Home20_Desc20], axis=1, join="inner")
print(combine_Homeless_Desc)


#plot corr
#Using to find the pairwise correlation of all columns in the dataframe.

combine_Homeless = pd.concat([Homeless21, Homeless20], ignore_index=True)
print(combine_Homeless)
print(combine_Homeless.describe())

total_columns = combine_Homeless.columns
num_col = combine_Homeless._get_numeric_data().columns
cat_col = list(set(total_columns)-set(num_col))
print(combine_Homeless.describe())
print(combine_Homeless.info())

for i in cat_col:
   if i in ['source']:
      continue
   plt.figure(figsize=(10, 5))
   chart = sns.countplot(data=combine_Homeless,
   x=i,
   palette='Set1')
   chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
   plt.show()

corrmat = combine_Homeless.corr()
print(corrmat)

plt.figure(figsize=(13, 6))
sns.heatmap(corrmat, vmax=1, annot=True, linewidths=.5)
plt.xticks(rotation=30, horizontalalignment='right')
plt.show()

#cormat2
cormat2 = combine_Homeless_Desc.corr()
print(cormat2)

plt.figure(figsize=(13, 6))
sns.heatmap(corrmat, vmax=1, annot=True, linewidths=.5)
plt.xticks(rotation=30, horizontalalignment='right')
plt.show()
#two corrmat results are the same for both descrie data frames concat and the inital dataframes concat

#plot for two data points in each region

quarter_20_21_total=[0,0,0,0,0,0,0,0,0]
for region in range(0,9):
    quarter_20_21_total[region] = [Homeless20[region:region + 1]["Total Adults"][0], Homeless21[region:region + 1]["Total Adults"][0]]

figure,axis = plt.subplots(3, 3)
axis[0, 0].plot(quarter_20_21_total[0])
axis[0, 0].set_title("Dublin")
axis[0, 1].plot(quarter_20_21_total[1])
axis[0, 1].set_title("Mid-East")
axis[0, 2].plot(quarter_20_21_total[2])
axis[0, 2].set_title("Midlands")
axis[1, 0].plot(quarter_20_21_total[3])
axis[1, 0].set_title("Mid-West")
axis[1, 1].plot(quarter_20_21_total[4])
axis[1, 1].set_title("North-East")
axis[1, 2].plot(quarter_20_21_total[5])
axis[1, 2].set_title("North-West")
axis[2, 0].plot(quarter_20_21_total[6])
axis[2, 0].set_title("South-East")
axis[2, 1].plot(quarter_20_21_total[7])
axis[2, 1].set_title("South-West")
axis[2, 2].plot(quarter_20_21_total[8])
axis[2, 2].set_title("West")

plt.show()

