import csv
from datetime import datetime

def main():
        dv_open_file = open("death_valley_2018_simple.csv", "r")

        dv_csv = csv.reader(dv_open_file, delimiter=",")

        dv_eq_data = list(dv_csv)
 
        ak_open_file = open("sitka_weather_2018_simple.csv", "r")

        ak_csv = csv.reader(ak_open_file, delimiter=",")

        ak_eq_data = list(ak_csv)
 
        dv_min_position = (auto_index(dv_eq_data)[0])
        dv_max_position = (auto_index(dv_eq_data)[1])
        dv_date_position = (auto_index(dv_eq_data)[2])
        dv_title = (auto_index(dv_eq_data)[3])
 
        ak_min_position = (auto_index(ak_eq_data)[0])
        ak_max_position = (auto_index(ak_eq_data)[1])
        ak_date_position = (auto_index(ak_eq_data)[2])
        ak_title = (auto_index(ak_eq_data)[3])
 

        dv_highs = (dv(dv_min_position,dv_max_position,dv_date_position,)[0])
        dv_lows = (dv(dv_min_position,dv_max_position,dv_date_position,)[1])
        dv_dates = (dv(dv_min_position,dv_max_position,dv_date_position,)[2])
        ak_highs = (ak(ak_min_position,ak_max_position,ak_date_position)[0])
        ak_lows = (ak(ak_min_position,ak_max_position,ak_date_position)[1])
        ak_dates = (ak(ak_min_position,ak_max_position,ak_date_position)[2])
 

        import matplotlib.pyplot as plt
 

        header_list = ["Temperature"] + ["Comparison"] + ["Between"] + [ak_title] + ['And'] + [dv_title]
        seperator = ' '
        bigtitle = seperator.join(header_list)
 
        fig,(ax1,ax2) = plt.subplots(2)
        fig.suptitle(bigtitle,fontsize=9)
 
        ax1.plot(ak_dates, ak_highs, c="red",alpha=.5)
        ax1.plot(ak_dates, ak_lows, c="blue", alpha=.5)
        ax1.fill_between(ak_dates, ak_highs, ak_lows, facecolor='blue', alpha=0.1)
        ax1.set_title(ak_title, fontsize=9)
 
        ax2.plot(dv_dates, dv_highs, c="red",alpha=.5)
        ax2.plot(dv_dates, dv_lows, c="blue", alpha=.5)
        ax2.fill_between(dv_dates, dv_highs, dv_lows, facecolor='blue', alpha=0.1)
        ax2.set_title(dv_title, fontsize=9)
 

        fig.autofmt_xdate()
        
        plt.show()
        

def auto_index(data_list):
        headers = data_list[0]
        min_position = headers.index('TMIN')
        max_position = headers.index('TMAX')
        date_position = headers.index('DATE')
        title_position = headers.index('NAME')
        title = data_list[1][title_position]
        return min_position, max_position, date_position, title
        
 
def dv (dv_min_position, dv_max_position, dv_date_position):
 
        open_file = open("death_valley_2018_simple.csv", "r")
        csv_file = csv.reader(open_file, delimiter=",")
 
        min_pos = dv_min_position
        max_pos = dv_max_position
        date_pos = dv_date_position
 
        header_row = next(csv_file)
 
        lows = []
        highs = []
        dates = []
 
        for row in csv_file:
                try:
                        high=int(row[max_pos])
                        low=int(row[min_pos])
                        the_date = datetime.strptime(row[date_pos], '%Y-%m-%d')
                
                except ValueError:
                        print(f"Missing data for {the_date}")
                else:
                        highs.append(high)
                        lows.append(low)
                        dates.append(the_date)
 
        
        
        return highs, lows, dates
 

        
 
def ak (ak_min_position,ak_max_position,ak_date_position):
        min_pos = ak_min_position
        max_pos = ak_max_position
        date_pos = ak_date_position
 
        open_file = open("sitka_weather_2018_simple.csv", "r")
        csv_file = csv.reader(open_file, delimiter=",")
 
        header_row = next(csv_file)
       
        lows = []
        highs = []
        dates = []

 
        for row in csv_file:
                lows.append(int(row[min_pos]))
                highs.append(int(row[max_pos]))
                the_date = datetime.strptime(row[date_pos], '%Y-%m-%d')
                dates.append(the_date)
 
        return highs, lows, dates 




main()