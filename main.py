import os, sys
from typing import KeysView

# directory = "C:/Users/Андрій/Desktop/dont ready program/sorter"
directory = os.path.dirname(os.path.realpath(__file__)) 
print(directory)
files = os.listdir(directory)

array_name = []

all_files_array = {}




def reversed_array(array):
	array = array[::-1]

	return array

def checked_point(sign):
	if sign == ".":  # this func check Is there dot 
		return True
	else: 
		return False

def checked_while(array):
	
	for i in range(len(array)):
		lengh_array = int(len(array))
		end_sign = int("-" + str(int(i)))		#   
		print(i)
		print(end_sign)
		if checked_point(array[end_sign]) == True:
			array = array[end_sign + 1:len(array)]
			print(array)
			return array
	return array
			
		
		

def create_array(name):
	name = list(name)
	# print(checked_point(name[1]))

	file_type_array = checked_while(name)
	file_type_Str = "".join(file_type_array) 
	all_files_array[file_type_Str] = []
	name = None
	return file_type_Str
	



def create_folder(array):
	Keys = list(array.keys())
	for i in range(len(Keys)):
		try:
			os.mkdir(directory + "/" + Keys[i])  #  this function create folder from array 
		except(RuntimeError, TypeError, NameError, ValueError, Exception):
			continue


def check_file_name(name):
		name = list(name)
		file_type_array = checked_while(name)
		file_type_Str = "".join(file_type_array)
		return file_type_Str


def sort_files(folder_array, file_array):
	Keys = list(folder_array.keys())
	for i in range(len(Keys)):
		for j in range(len(file_array)):
			if Keys[i] == check_file_name(file_array[j]):
				folder_array[Keys[i]].append(file_array[j])
	return folder_array


def put_file_folder(array):
	Keys = list(array.keys())
	for i in range(len(Keys)):
		array_fraction = list(array[Keys[i]])
		if Keys[i] == "py":
			i = i + 1
			array_fraction = list(array[Keys[i]])
		for j in range(len(array[Keys[i]])):
			try:
				os.rename(directory + "/" + array_fraction[j], directory + "/" + Keys[i] + "/" + array_fraction[j])
			except (RuntimeError, TypeError, NameError, ValueError, Exception):
				continue



for i in range(len(files)):
	create_array(files[i])

all_files_array = sort_files(all_files_array, files)


create_folder(all_files_array)

put_file_folder(all_files_array)

input()	 











