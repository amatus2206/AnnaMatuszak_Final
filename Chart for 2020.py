import pandas as pd
import matplotlib.pyplot as plt

jan_data=pd.read_csv("Homelessness Report January 2020.csv",index_col=0)
feb_data=pd.read_csv("Homelessness Report February 2020.csv",index_col=0)
mar_data=pd.read_csv("Homelessness Report March 2020.csv",index_col=0)
apr_data=pd.read_csv("Homelessness Report April 2020.csv",index_col=0)
may_data=pd.read_csv("Homelessness Report May 2020.csv",index_col=0)
jun_data=pd.read_csv("Homelessness Report June 2020.csv",index_col=0)
jul_data=pd.read_csv("Homelessness Report July 2020.csv",index_col=0)
aug_data=pd.read_csv("Homelessness Report August 2020.csv",index_col=0)
sep_data=pd.read_csv("Homelessness Report September 2020.csv",index_col=0)
oct_data=pd.read_csv("Homelessness Report October 2020.csv",index_col=0)
nov_data=pd.read_csv("Homelessness Report November 2020.csv",index_col=0)
dec_data=pd.read_csv("Homelessness Report December 2020.csv",index_col=0)

monthly_2020_total=[0,0,0,0,0,0,0,0,0]

for region in range(0,9):
    monthly_2020_total[region]=[jan_data[region:region+1]["Total Adults"][0], feb_data[region:region+1]["Total Adults"][0], mar_data[region:region+1]["Total Adults"][0], apr_data[region:region+1]["Total Adults"][0],may_data[region:region+1]["Total Adults"][0],jun_data[region:region+1]["Total Adults"][0],jul_data[region:region+1]["Total Adults"][0],aug_data[region:region+1]["Total Adults"][0],sep_data[region:region+1]["Total Adults"][0],oct_data[region:region+1]["Total Adults"][0],nov_data[region:region+1]["Total Adults"][0],dec_data[region:region+1]["Total Adults"][0]]
figure,axis=plt.subplots(3,3)
axis[0,0].plot(monthly_2020_total[0])
axis[0,0].set_title("Dublin")
axis[0,1].plot(monthly_2020_total[1])
axis[0,1].set_title("Mid-East")
axis[0,2].plot(monthly_2020_total[2])
axis[0,2].set_title("Midlands")
axis[1,0].plot(monthly_2020_total[3])
axis[1,0].set_title("Mid-West")
axis[1,1].plot(monthly_2020_total[4])
axis[1,1].set_title("North-East")
axis[1,2].plot(monthly_2020_total[5])
axis[1,2].set_title("North-West")
axis[2,0].plot(monthly_2020_total[6])
axis[2,0].set_title("South-East")
axis[2,1].plot(monthly_2020_total[7])
axis[2,1].set_title("South-West")
axis[2,2].plot(monthly_2020_total[8])
axis[2,2].set_title("West")

plt.show()

#he data from 2020 (month by month) which shows regional trends over the year.
# The North-West seems to have climbed over the course of the year which is unlike any other region
# maybe this is a sign of something significant