#Introducing message
print("This program can calculate the theory performance of Intel 7th Core CPU."+
	  "\nBased on a simplify fact that the performace of Intel CPUs are nearly"+
	  " unchange after Hasewell."+ "\nSo the performance of them can be"+
	  " simplify as the following formular:"+
	  "\n\t\tPerformance=Core number X Hyperthread coeffcient X max frequency of all cores X Architecture Coefficient."+
	  "(if CPU supports Hyperthread technology,the coefficient is 1.25,"+
	  "otherwise it is 1,for Architecture Coefficient,Lake series=1.1 ; Well series=1; Zen series=1)" )
import json
#Load json file
filename= "cpu_performance.json"
with open(filename) as f:
	pop_data= json.load(f)
	
#Quit button setting and cpu check setting
quit_button=True


while quit_button:
	cpu_1_check=True
	cpu_2_check=True
	#CPU_1 check
	while cpu_1_check:
		name_1=input("\n\nPlease input the first model of CPU which you want to "+
		"compare with formate like:i7-7700K or r7-1800X.\n")
		for pop_dict_1 in pop_data:
			if name_1==pop_dict_1["Model Name"]:
				cpu_1_check=False
		if cpu_1_check:
			print("The database doesn't have the information of this CPU."+
		          "\nPlease input again.")
	
	#Author special message-1
	if name_1=="i5-7640X":
			print("Why are you want to compare this bullshit CPU?"+
				  "Which price is the same as i7 and performance as i5")
	if "i9" in name_1:
		print("Wow, a rich man?")
	#Extract cpu_1 info
	for pop_dict_1_1 in pop_data:
		if pop_dict_1_1["Model Name"]==name_1:
			core_1=int(pop_dict_1_1["Cores"])
			all_cores_freq_1=float(pop_dict_1_1["All Cores Frequency"])
			if pop_dict_1_1["Hyper Thread support"]=="y":
				hts_coe_1=1.25
			else:
				hts_coe_1=1
			if "lake" in pop_dict_1["Code Name"]:
				architecture_coe_1=1.1
			else:
				architecture_coe_1=1
			#Data missing message_1
			if "TE" in pop_dict_1["Model Name"]:
				print("CPUs which end of TE are lack of data, the result "+
					  "will be calculated as its Max frequency.")
			if "R" in pop_dict_1["Model Name"]:
				print("CPUs which end of R are lack of data, the result "+
					  "will be calculated as its Max frequency.")
			  
	#CPU_2 check
	while cpu_2_check:
		name_2=input("\n\nPlease input the second model of CPU which you want to "+
		"compare with formate like:i7-7700K or r7-1800X.\n")
		if name_2==name_1:
			print("What do you think I all concernd!This is a tool, not a"+
			      " toy!")
			continue
		for pop_dict_2_2 in pop_data:
			if name_2==pop_dict_2_2["Model Name"]:
				cpu_2_check=False
		if cpu_2_check:
			print("The database doesn't have the information of this CPU."+
		          "\nPlease input again.")
	#Author special message
	if name_1=="i5-7640X":
		print("Why are you want to compare this bullshit CPU?"+
			  "which price is the same as i7 and performance as i5")
	if ("i9" not in name_1)and ("i9" in name_2):
		print("Wow, a rich man?")
	if ("i9" in name_1)and ("i9" in name_2):
		print("Close the program and buy the most expensive one !!!")
	#Extract cpu_2 info
	for pop_dict_2_2 in pop_data:
		if pop_dict_2_2["Model Name"]==name_2:
			core_2=int(pop_dict_2_2["Cores"])
			all_cores_freq_2=float(pop_dict_2_2["All Cores Frequency"])
			if pop_dict_2_2["Hyper Thread support"]=="y":
				hts_coe_2=1.25
			else:
				hts_coe_2=1
			if "lake" in pop_dict_2_2["Code Name"]:
				architecture_coe_2=1.1
			else:
				architecture_coe_2=1
			#Data missing message_2
			if "TE" in pop_dict_2_2["Model Name"]:
				print("CPUs which end of TE are lack of data, the result "+
					  "will be calculated as its Max frequency.")
			if "R" in pop_dict_2_2["Model Name"]:
				print("CPUs which end of R are lack of data, the result "+
					  "will be calculated as its Max frequency.")
	
	#Calculating	
	result_1=core_1*hts_coe_1*all_cores_freq_1*architecture_coe_1
	result_2=core_2*hts_coe_2*all_cores_freq_2*architecture_coe_2
	performace_1=(result_1/result_2)*100
	performace_2=round(performace_1, 2)
	print("\n\n"+name_1+ "=" + str(performace_2) +"% " + name_2)
	#End the program
	quit_confirm=input("If you want to quit, please input 'q'\n")
	if quit_confirm!="q":
		continue
	else:
		break
	



	
