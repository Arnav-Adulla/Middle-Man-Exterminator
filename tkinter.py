
import urllib
import urllib.request
from bs4 import BeautifulSoup
import re 
import tkinter as tk
import time
from tkinter import END
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext



def submit_form() :
    crop = ut.get("1.0",'end-1c').lower()
    price = ut2.get("1.0",'end-1c').lower()
    market = ut3.get("1.0",'end-1c').upper()
    ut.delete(1.0, END)
    ut2.delete(1.0, END)
    ut3.delete(1.0, END)
    #get data if market there print 5 + market index value else pass
    
          
    if crop == 'corn':

      with urllib.request.urlopen("https://www.krishimaratavahini.kar.nic.in/MainPage/DailyMrktPriceRep2.aspx?Rep=Var&CommCode=4&VarCode=8&Date=09/01/2018&CommName=Maize%20/%20%E0%B2%AE%E0%B3%86%E0%B2%95%E0%B3%8D%E0%B2%95%E0%B3%86%E0%B2%9C%E0%B3%8B%E0%B2%B3&VarName=Hybrid/Local%20/%20%E0%B2%B9%E0%B3%88%E0%B2%AC%E0%B3%8D%E0%B2%B0%E0%B2%BF%E0%B2%A1%E0%B3%8D%20%E0%B2%B8%E0%B3%8D%E0%B2%A5%E0%B2%B3%E0%B3%80%E0%B2%AF") as url:
         data_page = url.read()
      soup = BeautifulSoup(data_page)
      values = soup.findAll('td')
      value_list = []
      for farmer_value in values[12:150]:
              final_value = cleanhtml(str(farmer_value))
              value_list.append(final_value)
   
      if market in value_list:
        index_value = value_list.index(market)
              
        final = float(value_list[index_value + 5])
        print(final / 100)
      else:
            final = int(value_list[5])
          
            print(final / 100)
    elif crop == 'wheat':
        with urllib.request.urlopen("https://www.krishimaratavahini.kar.nic.in/MainPage/DailyMrktPriceRep2.aspx?Rep=Com&CommCode=1&VarCode=7&Date=09/01/2018&CommName=Wheat%20/%20%E0%B2%97%E0%B3%8B%E0%B2%A7%E0%B2%BF&VarName=Bansi%20/%20%E0%B2%AC%E0%B2%A8%E0%B3%8D%E0%B2%B8%E0%B2%BF") as url:
            data_page = url.read()

        soup = BeautifulSoup(data_page)
        values = soup.findAll('td')
        value_list = []
        for farmer_value in values[12:118]:
            final_value = cleanhtml(str(farmer_value))
            value_list.append(final_value)
   
        if market in value_list:
            index_value = value_list.index(market)
              
            final = float(value_list[index_value + 7])
            print(final / 100)
              
      
        
            
        else:
            final = int(value_list[7])
          
            print(final / 100)
        


    elif crop == 'lemon':
        with urllib.request.urlopen("https://www.krishimaratavahini.kar.nic.in/MainPage/DailyMrktPriceRep2.aspx?Rep=Var&CommCode=180&VarCode=1&Date=09/01/2018&CommName=Lime%20(Lemon)%20/%20%E0%B2%A8%E0%B2%BF%E0%B2%82%E0%B2%AC%E0%B3%86%E0%B2%B9%E0%B2%A3%E0%B3%8D%E0%B2%A3%E0%B3%81&VarName=Lime%20(Lemon)%20/%20%E0%B2%A8%E0%B2%BF%E0%B2%82%E0%B2%AC%E0%B3%86%E0%B2%B9%E0%B2%A3%E0%B3%8D%E0%B2%A3%E0%B3%81") as url:
            data_page = url.read()
    
        soup = BeautifulSoup(data_page)
        values = soup.findAll('td')
        value_list = []
        for farmer_value in values[12:30]:
            final_value = cleanhtml(str(farmer_value))
            value_list.append(final_value)
        if market in value_list:
            index_value = value_list.index(market)
            
            final = float(value_list[index_value + 5])
            print(final / 100)
          
            
        else:
            final = int(value_list[5])
            
            print(final / 100)
    elif crop == 'navane':
        with urllib.request.urlopen("https://www.krishimaratavahini.kar.nic.in/MainPage/DailyMrktPriceRep2.aspx?Rep=Com&CommCode=121&VarCode=1&Date=09/01/2018&CommName=Navane%20/%20%E0%B2%A8%E0%B2%B5%E0%B2%A3%E0%B3%86&VarName=Navane%20Hybrid%20/%20%E0%B2%A8%E0%B2%B5%E0%B2%A3%E0%B3%86%20%E0%B2%B9%E0%B3%88%E0%B2%AC%E0%B3%8D%E0%B2%B0%E0%B2%BF%E0%B2%A1%E0%B3%8D") as url:
            data_page = url.read()
    
        soup = BeautifulSoup(data_page)
        values = soup.findAll('td')
        value_list = []
        for farmer_value in values[12:76]:
            final_value = cleanhtml(str(farmer_value))
            value_list.append(final_value)
        if market in value_list:
            index_value = value_list.index(market)
            
            final = float(value_list[index_value + 5])
            print(final / 100)
            
            
        else:
            final = int(value_list[5])
            
            print(final / 100)
    else:
        print('You have likely misspelled the name of your crop')
    #write out string or integer to list considering all possible crop names
    if price == "":
        return
        
    if crop in item_dict.keys() :
        item_dict[crop].append(price)
    else :
        item_dict[crop] = [price,]
        
    for dkey in item_dict.keys() :
        sum1 = 0.0
        for i in item_dict[dkey] :
            sum1 = sum1 + float(i)

            avg = sum1/len(item_dict[dkey])
        
        

        print(str(dkey), 'avg = ', avg)
            
        
    return
#save button command
def save():
    crop = ut.get("1.0",'end-1c').lower()
    price = ut2.get("1.0",'end-1c').lower()
    market = ut3.get("1.0",'end-1c').upper()
    ut.delete(1.0, END)
    ut2.delete(1.0, END)
    ut3.delete(1.0, END)
    if crop == "":
        print('No crop has been inputted')
        return
    for dkey in item_dict.keys() :
        sum1 = 0.0
        for i in item_dict[dkey] :
            sum1 = sum1 + float(i)

            avg = sum1/len(item_dict[dkey])
            print(str(dkey), 'avg = ', avg)
    data_directory = open('Values.txt', 'a')
    data_directory.writelines('\n')
    data_directory.write(str(dkey))
    data_directory.write('+$+')
    data_directory.write(str(avg))
    data_directory.close()
    ut.delete(1.0, END)
    ut2.delete(1.0, END)
    
    
    
   
    
     
#root + root size
root = tk.Tk()
root.minsize(width=966, height=915)
root.maxsize(width=966, height=915)
#root title
root.title("Star Gazer- - Your Future")
#background image

background_image = tk.PhotoImage(file="Background - 7.gif")
w = background_image.width()
h = background_image.height()

painel = tk.Canvas(width=w, height=h)
painel.pack(side='top', fill='both', expand='yes')
painel.create_image(0, 0, image=background_image, anchor='nw')

#entry box
enter = tk.Entry(root, bd="3", highlightcolor='black')
enter.place(x=155, y=192)
ut = tk.Text(enter, fg="black", font="{Lucida Sans} 20", height=1.2, width=38)
ut.pack()

#entry box 2
enter2 = tk.Entry(root, bd="3", highlightcolor='black')
enter2.place(x=155, y=340)
ut2 = tk.Text(enter2, fg="black", font="{Lucida Sans} 20", height=1.2, width=38)
ut2.pack()
#entry box 3
enter3 = tk.Entry(root, bd="3", highlightcolor='black')
enter3.place(x=155, y=480)
ut3 = tk.Text(enter3, fg="black", font="{Lucida Sans} 20", height=1.2, width=38)
ut3.pack()
fo = open('Values.txt', 'r')
complete_list = fo.read().split('\n')
fo.close()
item_dict = {}
for item in complete_list: 
    item_list = item.split('+$+')
    item_dict[item_list[0]] = []
    for entry in item_list[1:] :
        item_dict[item_list[0]].append(entry)

for dkey in item_dict.keys() :
    print('dkey ', dkey, 'list items ' , item_dict[dkey])
#submit button
button = tk.Button(root,text='Submit',command=lambda:submit_form())
button.pack()
button.place(x=200, y=650)
button.configure(font = '{Sans} 20',foreground = 'white', bg ='#383a39', height=1, width=12)






save_button = button = tk.Button(root,text='Save',command=lambda:save())
save_button.pack()
save_button.place(x=600, y=650)
save_button.configure(font = '{Sans} 20',foreground = 'white', bg ='#383a39', height=1, width=12)











