# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '/home/ee2405/Downloads/sample_input.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
target_data = list(filter(lambda item: item['WDSD'] != '-99.000'  , data))
target_data = list(filter(lambda item: item['WDSD'] != '-999.000'  , target_data))
target_data = list(filter(lambda item: item['station_id'] == 'C0A880', target_data))
temp=[]
if (len(target_data) >=1): 
   for i in range (len(target_data)):
      temp.append(target_data[i]['WDSD'])
   xmax = max(temp)
   xmin = min(temp)
   r1=float(xmax)-float(xmin)
else: r1="'None'"
# Retrive ten data points from the beginning.

target_data = data[:10]
target_data = list(filter(lambda item: item['WDSD'] != '-99.000'  , data))
target_data = list(filter(lambda item: item['WDSD'] != '-999.000'  , target_data))
target_data = list(filter(lambda item: item['station_id'] == 'C0F9A0', target_data))
temp=[]
if (len(target_data) >=1): 
   for i in range (len(target_data)):
      temp.append(target_data[i]['WDSD'])
   xmax = max(temp)
   xmin = min(temp)
   r2=float(xmax)-float(xmin)
else: r2="'None'"

target_data = data[:10]
target_data = list(filter(lambda item: item['WDSD'] != '-99.000'  , data))
target_data = list(filter(lambda item: item['WDSD'] != '-999.000'  , target_data))
target_data = list(filter(lambda item: item['station_id'] == 'C0G640', target_data))
temp=[]
if (len(target_data) >=1): 
   for i in range (len(target_data)):
      temp.append(target_data[i]['WDSD'])
   xmax = max(temp)
   xmin = min(temp)
   r3=float(xmax)-float(xmin)
else: r3="'None'"

target_data = data[:10]
target_data = list(filter(lambda item: item['WDSD'] != '-99.000'  , data))
target_data = list(filter(lambda item: item['WDSD'] != '-999.000'  , target_data))
target_data = list(filter(lambda item: item['station_id'] == 'C0R190', target_data))
temp=[]
if (len(target_data) >=1): 
   for i in range (len(target_data)):
      temp.append(target_data[i]['WDSD'])
   xmax = max(temp)
   xmin = min(temp)
   r4=float(xmax)-float(xmin)
else: r4="'None'"

target_data = data[:10]
target_data = list(filter(lambda item: item['WDSD'] != '-99.000'  , data))
target_data = list(filter(lambda item: item['WDSD'] != '-999.000'  , target_data))
target_data = list(filter(lambda item: item['station_id'] == 'C0X260', target_data))
temp=[]
if (len(target_data) >=1): 
   for i in range (len(target_data)):
      temp.append(target_data[i]['WDSD'])
   xmax = max(temp)
   xmin = min(temp)
   r5=float(xmax)-float(xmin)
else: r5="'None'"
#=======================================

# Part. 4
#=======================================
# Print result
print("[['C0A880', {0}], ['C0F9A0', {1}], ['C0G640', {2}], ['C0R190', {3}], ['C0X260', {4}]]".format(r1,r2,r3,r4,r5))
#========================================