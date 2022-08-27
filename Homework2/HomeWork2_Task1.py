#Question 1
my_list=["Unurtuvshin", 18, 2004, 6, 25, "MUIS"]
print(my_list) #Listee hevleh
print(my_list[0]) #Ehnii elementiig hevleh
print(my_list[-4:5]) #Suuleesee 4duh elementees ehneesee 6dahi element hurtelh hevleh
print(type(my_list)) #my_list-iin turliig hevleh
my_list[1] = 17 #2-r elementiig uurchluh
my_list.insert(3, "nemelt") #4-r bair luu element nemeh
my_list2=("nemelt", "list")
my_list.extend(my_list2) #my_list2-iig araas ni zalgah
my_list.remove("nemelt") #nemelt gesen elementiig urdaas ni 1 udaa hasah
my_list.pop(1) #2r element hasah, herev ()-dotor bairshil zaahgui bol suuliin elementiig hasna
del my_list[1] #2r elemntiig hasah
#Question 2
import datetime #Yg yu import hiij baigaag asuuh
udur_str = "2004-06-25" #String-dee utga ugsun
udur_date = datetime.datetime.strptime(udur_str, "%Y-%m-%d") #String ee datetime huvisagch bolgoson, davhar datetime gej avj baigaag asuuh
my_str = udur_date.strftime("%Y onii %m sariin %d udur tursun baina") #Datetime huvisagchaa string bolgoson
print(my_str) #String-ee hevleh
