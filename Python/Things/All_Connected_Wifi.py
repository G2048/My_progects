import subprocess
#Getting meta data of the wifi network
meta_data = subprocess.check_output(['netsh','wlan','show','profiles'])
#Decoding meta data from byte to string
data = meta_data.decode('utf-8', errors='backslashreplace')

#Spliting data by line by line string to list
data = data.split("\n")
#Creating a list of wifi names
names = []

#Travers the list
for i in data:
	#Find "All User Profile" in ech item as this item will have the wifi name
	if "All User Profile" in i:
		#If found split the item in order to get only the name
		i = i.split(':')
		#Item at index 1 will be the wifi name
		i = i[1:-1]
		#Appeding the wifi name in the list
		names.append(i)

#Printing the wifi names
print("All wifi that system has connected to are")		
print('-----------------------------------------')
for name in names:
	print(name)		