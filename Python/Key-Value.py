# Key-value хранилище

import argparse
import os
import tempfile


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
#print (tempfile.gettempdir())

# Определение флагов
parser = argparse.ArgumentParser()
parser.add_argument("--key", help="Enter the key of dictionary",action='store')
parser.add_argument("--value", help="Enter the value at dictionary",action='store')
args = parser.parse_args()

# Вспомогательный блок
dictionary = dict ()
list_1 = []
i=0
x=None
y=None

try :
    # Запись переменных
    if args.key and args.value: 
        with open(storage_path,'a+') as f: 	
            f.write('{} {} '.format(args.key,args.value))
except :
    print (' ')            

try:
	# Чтение значения по ключу        
    if args.key and not args.value:
	    with open(storage_path, 'r') as file :

	#	print (file.read()) # <class 'str'>    
	#	file.seek (0)
	#	print (file.read().split()) #<class 'list'>!!!!
#### Перемещает каретку ####   
	#	file.seek (0)
	
	    # Чтение и разбиение строки файла на элементы по знаку пробела
		    dict_lines = file.read().split() 
		    file.seek (0)
		# Запись  значений из файла в словарь
		    for n in dict_lines :
			
			    if i % 2 == 0 :
				    x=n
				    #print (x)
			    else:
				    y=dict_lines[i]
				    #print (y)

				    # Присваивание ключу нового значения через <class 'list'>
				    if args.key == x :
				        list_1.append(y)

				    dictionary [x]= list_1

			    i +=1

	    try :
	    	b = ", ".join(dictionary[args.key])
	    	print(b)
	    except KeyError:
	        print ('None')	

except :
	print (' ')





