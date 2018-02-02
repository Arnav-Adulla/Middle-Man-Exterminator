# 

import urllib
import urllib.request
from bs4 import BeautifulSoup
import re 
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget 
from kivy.app import App
from kivy.graphics import Color
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.modalview import ModalView
import kivy

from kivy.uix.image import Image
from kivy.app import App
from kivy.uix.button import Label
 
def cleanhtml(raw_html):
      cleanr = re.compile('<.*?>')
      cleantext = re.sub(cleanr, '', raw_html)
      return cleantext



class Star_Gazer(App):
    def build(self):
        
        self.layout = BoxLayout(padding = 5, orientation = 'vertical', spacing = 5)
        
        #label 1
        self.label_crop = Label(text = 'Your Crop:', size_hint = [0.1, 0.1])
        self.layout.add_widget(self.label_crop)
         #first input
        self.txt1 = TextInput(text='', multiline=True)
        self.layout.add_widget(self.txt1)
       
        #label 2
        self.label_price = Label(text = 'Your Price:', size_hint = [0.1, 0.1])
        self.layout.add_widget(self.label_price)
        #second input
        self.txt2 = TextInput(text='', multiline=True)
        self.layout.add_widget(self.txt2)
        # 3rd label
        self.label_market = Label(text = 'Your Market:', size_hint = [0.1, 0.1])
        self.layout.add_widget(self.label_market)
        #third input
        self.txt3 = TextInput(text='', multiline=True)
        self.layout.add_widget(self.txt3)
        
        # second layout box
        self.layout2 = FloatLayout(size = [300,300], pos_hint={'x': 1, 'center_y': .5})
        self.layout.add_widget(self.layout2)
        #buttons
        self.btn1 = Button(text='Submit', background_color = [0.09, 0.41, 1, 1.5], size_hint = [0.48,0.48], pos=[12,50],
                      font_size = '30sp', font_name = 'Calibri')
        
        self.btn1.bind(on_press=self.submit_form)
        
 
        self.layout2.add_widget(self.btn1)
        self.btn2 = Button(text="Save",  background_color = [0.09, 0.41, 1, 1.5], size_hint = [0.48,0.48],pos=[405,50],
                        font_size = '30sp', font_name = 'Calibri')
        self.btn2.bind(on_press=self.save)
        self.layout2.add_widget(self.btn2)
        
        return self.layout 

    def back(self, button):
        self.layout.clear_widgets()

        
        #label 1
        label_crop = Label(text = 'Your Crop:', size_hint = [0.1, 0.1])
        self.layout.add_widget(label_crop)
         #first input
        self.txt1 = TextInput(text='', multiline=True)
        self.layout.add_widget(self.txt1)
       
        #label 2
        label_price = Label(text = 'Your Price:', size_hint = [0.1, 0.1])
        self.layout.add_widget(label_price)
        #second input
        self.txt2 = TextInput(text='', multiline=True)
        self.layout.add_widget(self.txt2)
        # 3rd label
        label_market = Label(text = 'Your Market:', size_hint = [0.1, 0.1])
        self.layout.add_widget(label_market)
        #third input
        self.txt3 = TextInput(text='', multiline=True)
        self.layout.add_widget(self.txt3)
        
        # second layout box
      
        layout2 = FloatLayout(size = [300,300], pos_hint={'x': 1, 'center_y': .5})
        self.layout.add_widget(layout2)
        #buttons
        btn1 = Button(text='Submit', background_color = [0.09, 0.41, 1, 1.5], size_hint = [0.48,0.48], pos=[12,50],
                      font_size = '30sp', font_name = 'Calibri')
        
        btn1.bind(on_press=self.submit_form)
        
 
        layout2.add_widget(btn1)
        btn2 = Button(text="Save",  background_color = [0.09, 0.41, 1, 1.5], size_hint = [0.48,0.48],pos=[405,50],
                        font_size = '30sp', font_name = 'Calibri')
        btn2.bind(on_press=self.save)
        layout2.add_widget(btn2)
        

        


    def submit_form(self, button1) :
        crop1 = self.txt1.text
        price1 = self.txt2.text
        market1 = self.txt3.text
        crop = str(crop1).lower().strip()
        crop = crop.title()
        price = str(price1).lower().strip()
        market = str(market1).lower().strip()
        self.layout.clear_widgets()
        
        

        #get data if market there print 5 + market index value else pass
        print(crop)
        
                
              
        if crop == 'Corn':

          with urllib.request.urlopen("https://www.krishimaratavahini.kar.nic.in/MainPage/DailyMrktPriceRep2.aspx?Rep=Var&CommCode=4&VarCode=8&Date=09/01/2018&CommName=Maize%20/%20%E0%B2%AE%E0%B3%86%E0%B2%95%E0%B3%8D%E0%B2%95%E0%B3%86%E0%B2%9C%E0%B3%8B%E0%B2%B3&VarName=Hybrid/Local%20/%20%E0%B2%B9%E0%B3%88%E0%B2%AC%E0%B3%8D%E0%B2%B0%E0%B2%BF%E0%B2%A1%E0%B3%8D%20%E0%B2%B8%E0%B3%8D%E0%B2%A5%E0%B2%B3%E0%B3%80%E0%B2%AF") as url:
             data_page = url.read()
          soup = BeautifulSoup(data_page)
          values = soup.findAll('td')
          value_list = []
          for farmer_value in values[12:150]:
                  final_value = cleanhtml(str(farmer_value))
                  value_list.append(final_value)
          
  
       
          if market in value_list and market != '':
                  index_value = value_list.index(market)          
                  with urllib.request.urlopen("https://www.ncdex.com/MarketData/LiveFuturesQuotes.aspx") as url:
                      data_page = url.read()
                  soup = BeautifulSoup(data_page)
                  values = soup.findAll('td')
                  profit_list = []
                  for farmer_value in values[23:10000]:
                      final_value = cleanhtml(str(farmer_value))
                      final_value = ' '.join(final_value.split())

                      profit_list.append(final_value)

                  if crop in profit_list:
                        index = profit_list.index(crop)
                        profit = profit_list[index + 7]  
                        final = float(value_list[index_value + 5])
                        print(final / 100)
                        str_final = str( final / 100 - final / 100 *.238)
                        output_label = TextInput(text='Your Selling Price: ' + str_final + "    Today's Profit: " + profit, font_size = '40sp',size_hint = [1,.8])
                        self.layout.add_widget(output_label)
                  else:
                        final = float(value_list[index_value + 5])
                        print(final / 100)
                        str_final = str( final / 100 - final / 100 *.238)
                        output_label = TextInput(text='Your Selling Price: ' + str_final + "   Unsure about today's profit", font_size = '40sp',size_hint = [1,.8])
                        self.layout.add_widget(output_label)

                                          
          else:

          
                  with urllib.request.urlopen("https://www.ncdex.com/MarketData/LiveFuturesQuotes.aspx") as url:
                      data_page = url.read()
                  soup = BeautifulSoup(data_page)
                  values = soup.findAll('td')
                  profit_list = []
                  for farmer_value in values[23:10000]:
                      final_value = cleanhtml(str(farmer_value))
                      final_value = ' '.join(final_value.split())

                      profit_list.append(final_value)
                  if crop in profit_list:
                        index = profit_list.index(crop)
                        profit = profit_list[index + 7]  
                        final = int(value_list[5])
                        str_final = str( final / 100 - final / 100 *.238)
                        output_label = TextInput(text='Your Selling Price: ' + str_final + "    Today's Profit: " + profit, font_size = '40sp',size_hint = [1,.8])
                        self.layout.add_widget(output_label)
                        print(final / 100)
                  else:
                        final = int(value_list[5])
                        str_final = str( final / 100 - final / 100 *.238)
                        output_label = TextInput(text='Your Selling Price: ' + str_final + "    Unsure about today's profit", font_size = '40sp',size_hint = [1,.8])
                        self.layout.add_widget(output_label)
                        print(final / 100)

        elif crop == 'Red':
            with urllib.request.urlopen("https://www.krishimaratavahini.kar.nic.in/MainPage/DailyMrktPriceRep2.aspx?Rep=Var&CommCode=1&VarCode=71&Date=18/01/2018&CommName=Wheat%20/%20%E0%B2%97%E0%B3%8B%E0%B2%A7%E0%B2%BF&VarName=Red%20/%20%E0%B2%95%E0%B3%86%E0%B2%82%E0%B2%AA%E0%B3%81") as url:
                data_page = url.read()

            soup = BeautifulSoup(data_page)
            values = soup.findAll('td')
            value_list = []
            for farmer_value in values[12:18]:
                final_value = cleanhtml(str(farmer_value))
                value_list.append(final_value)
            if market in value_list and market != '':
                  index_value = value_list.index(market)          
                  with urllib.request.urlopen("https://www.ncdex.com/MarketData/LiveFuturesQuotes.aspx") as url:
                      data_page = url.read()
                  soup = BeautifulSoup(data_page)
                  values = soup.findAll('td')
                  profit_list = []
                  for farmer_value in values[23:10000]:
                      final_value = cleanhtml(str(farmer_value))
                      final_value = ' '.join(final_value.split())

                      profit_list.append(final_value)

                  if crop in profit_list:
                        index = profit_list.index(crop)
                        profit = profit_list[index + 7]  
                        final = float(value_list[index_value + 5])
                        print(final / 100)
                        str_final = str( final / 100 - final / 100 *.238)
                        output_label = TextInput(text='Your Selling Price: ' + str_final + "    Today's Profit: " + profit, font_size = '40sp', size_hint = [1,.8])
                        self.layout.add_widget(output_label)
                  else:
                        final = float(value_list[index_value + 5])
                        print(final / 100)
                        str_final = str( final / 100 - final / 100 *.238)
                        output_label = TextInput(text='Your Selling Price: ' + str_final + "   Unsure about today's profit", font_size = '40sp', size_hint = [1,.8])
                        self.layout.add_widget(output_label)

                                          
            else:

          
                  with urllib.request.urlopen("https://www.ncdex.com/MarketData/LiveFuturesQuotes.aspx") as url:
                      data_page = url.read()
                  soup = BeautifulSoup(data_page)
                  values = soup.findAll('td')
                  profit_list = []
                  for farmer_value in values[23:10000]:
                      final_value = cleanhtml(str(farmer_value))
                      final_value = ' '.join(final_value.split())

                      profit_list.append(final_value)
                  if crop in profit_list:
                        index = profit_list.index(crop)
                        profit = profit_list[index + 7]  
                        final = int(value_list[5])
                        str_final = str( final / 100 - final / 100 *.238)
                        output_label = TextInput(text='Your Selling Price: ' + str_final + "    Today's Profit: " + profit, font_size = '40sp', size_hint = [1,.8])
                        self.layout.add_widget(output_label)
                        print(final / 100)
                  else:
                        final = int(value_list[5])
                        str_final = str( final / 100 - final / 100 *.238)
                        output_label = TextInput(text='Your Selling Price: ' + str_final + "    Unsure about today's profit", font_size = '40sp', size_hint = [1,.8])
                        self.layout.add_widget(output_label)
                        print(final / 100)

        elif crop == 'Wheat':
           
            with urllib.request.urlopen("https://www.krishimaratavahini.kar.nic.in/MainPage/DailyMrktPriceRep2.aspx?Rep=Com&CommCode=1&VarCode=7&Date=09/01/2018&CommName=Wheat%20/%20%E0%B2%97%E0%B3%8B%E0%B2%A7%E0%B2%BF&VarName=Bansi%20/%20%E0%B2%AC%E0%B2%A8%E0%B3%8D%E0%B2%B8%E0%B2%BF") as url:
                data_page = url.read()

            soup = BeautifulSoup(data_page)
            values = soup.findAll('td')
            value_list = []
            for farmer_value in values[12:118]:
                final_value = cleanhtml(str(farmer_value))
                value_list.append(final_value)
       
            if market in value_list and market != '':
                  index_value = value_list.index(market)          
                  with urllib.request.urlopen("https://www.ncdex.com/MarketData/LiveFuturesQuotes.aspx") as url:
                      data_page = url.read()
                  soup = BeautifulSoup(data_page)
                  values = soup.findAll('td')
                  profit_list = []
                  for farmer_value in values[23:10000]:
                      final_value = cleanhtml(str(farmer_value))
                      final_value = ' '.join(final_value.split())

                      profit_list.append(final_value)

                  if crop in profit_list:
                        index = profit_list.index(crop)
                        profit = profit_list[index + 7]  
                        final = float(value_list[index_value + 5])
                        print(final / 100)
                        str_final = str( final / 100 - final / 100 *.238)
                        output_label = TextInput(text='Your Selling Price: ' + str_final + "    Today's Profit: " + profit, font_size = '40sp', size_hint = [1,.8])
                        self.layout.add_widget(output_label)
                  else:
                        final = float(value_list[index_value + 5])
                        print(final / 100)
                        str_final = str( final / 100 - final / 100 *.238)
                        output_label = TextInput(text='Your Selling Price: ' + str_final + "   Unsure about today's profit", font_size = '40sp', size_hint = [1,.8])
                        self.layout.add_widget(output_label)

                                          
            else:

          
                  with urllib.request.urlopen("https://www.ncdex.com/MarketData/LiveFuturesQuotes.aspx") as url:
                      data_page = url.read()
                  soup = BeautifulSoup(data_page)
                  values = soup.findAll('td')
                  profit_list = []
                  for farmer_value in values[23:10000]:
                      final_value = cleanhtml(str(farmer_value))
                      final_value = ' '.join(final_value.split())

                      profit_list.append(final_value)
                  if crop in profit_list:
                        index = profit_list.index(crop)
                        profit = profit_list[index + 7]  
                        final = int(value_list[5])
                        str_final = str( final / 100 - final / 100 *.238)
                        output_label = TextInput(text='Your Selling Price: ' + str_final + "    Today's Profit: " + profit, font_size = '40sp', size_hint = [1,.8])
                        self.layout.add_widget(output_label)
                        print(final / 100)
                  else:
                        final = int(value_list[5])
                        str_final = str( final / 100 - final / 100 *.238)
                        output_label = TextInput(text='Your Selling Price: ' + str_final + "    Unsure about today's profit", font_size = '40sp', size_hint = [1,.8])
                        self.layout.add_widget(output_label)
                        print(final / 100)


        elif crop == 'Lemon':
            with urllib.request.urlopen("https://www.krishimaratavahini.kar.nic.in/MainPage/DailyMrktPriceRep2.aspx?Rep=Var&CommCode=180&VarCode=1&Date=09/01/2018&CommName=Lime%20(Lemon)%20/%20%E0%B2%A8%E0%B2%BF%E0%B2%82%E0%B2%AC%E0%B3%86%E0%B2%B9%E0%B2%A3%E0%B3%8D%E0%B2%A3%E0%B3%81&VarName=Lime%20(Lemon)%20/%20%E0%B2%A8%E0%B2%BF%E0%B2%82%E0%B2%AC%E0%B3%86%E0%B2%B9%E0%B2%A3%E0%B3%8D%E0%B2%A3%E0%B3%81") as url:
                data_page = url.read()
        
            soup = BeautifulSoup(data_page)
            values = soup.findAll('td')
            value_list = []
            for farmer_value in values[12:30]:
                final_value = cleanhtml(str(farmer_value))
                value_list.append(final_value)
            if market in value_list and market != '':
                  index_value = value_list.index(market)          
                  with urllib.request.urlopen("https://www.ncdex.com/MarketData/LiveFuturesQuotes.aspx") as url:
                      data_page = url.read()
                  soup = BeautifulSoup(data_page)
                  values = soup.findAll('td')
                  profit_list = []
                  for farmer_value in values[23:10000]:
                      final_value = cleanhtml(str(farmer_value))
                      final_value = ' '.join(final_value.split())

                      profit_list.append(final_value)

                  if crop in profit_list:
                        index = profit_list.index(crop)
                        profit = profit_list[index + 7]  
                        final = float(value_list[index_value + 5])
                        print(final / 100)
                        str_final = str( final / 100 - final / 100 *.238)
                        output_label = TextInput(text='Your Selling Price: ' + str_final + "    Today's Profit: " + profit, font_size = '40sp', size_hint = [1,.8])
                        self.layout.add_widget(output_label)
                  else:
                        final = float(value_list[index_value + 5])
                        print(final / 100)
                        str_final = str( final / 100 - final / 100 *.238)
                        output_label = TextInput(text='Your Selling Price: ' + str_final + "   Unsure about today's profit", font_size = '40sp', size_hint = [1,.8])
                        self.layout.add_widget(output_label)

                                          
            else:

          
                  with urllib.request.urlopen("https://www.ncdex.com/MarketData/LiveFuturesQuotes.aspx") as url:
                      data_page = url.read()
                  soup = BeautifulSoup(data_page)
                  values = soup.findAll('td')
                  profit_list = []
                  for farmer_value in values[23:10000]:
                      final_value = cleanhtml(str(farmer_value))
                      final_value = ' '.join(final_value.split())

                      profit_list.append(final_value)
                  if crop in profit_list:
                        index = profit_list.index(crop)
                        profit = profit_list[index + 7]  
                        final = int(value_list[5])
                        str_final = str( final / 100 - final / 100 *.238)
                        output_label = TextInput(text='Your Selling Price: ' + str_final + "    Today's Profit: " + profit, font_size = '40sp', size_hint = [1,.8])
                        self.layout.add_widget(output_label)
                        print(final / 100)
                  else:
                        final = int(value_list[5])
                        str_final = str( final / 100 - final / 100 *.238)
                        output_label = TextInput(text='Your Selling Price: ' + str_final + "    Unsure about today's profit", font_size = '40sp', size_hint = [1,.8])
                        self.layout.add_widget(output_label)
                        print(final / 100)

        elif crop == 'Navane':
            with urllib.request.urlopen("https://www.krishimaratavahini.kar.nic.in/MainPage/DailyMrktPriceRep2.aspx?Rep=Com&CommCode=121&VarCode=1&Date=09/01/2018&CommName=Navane%20/%20%E0%B2%A8%E0%B2%B5%E0%B2%A3%E0%B3%86&VarName=Navane%20Hybrid%20/%20%E0%B2%A8%E0%B2%B5%E0%B2%A3%E0%B3%86%20%E0%B2%B9%E0%B3%88%E0%B2%AC%E0%B3%8D%E0%B2%B0%E0%B2%BF%E0%B2%A1%E0%B3%8D") as url:
                data_page = url.read()
        
            soup = BeautifulSoup(data_page)
            values = soup.findAll('td')
            value_list = []
            for farmer_value in values[12:76]:
                final_value = cleanhtml(str(farmer_value))
                value_list.append(final_value)
            if market in value_list and market != '':
                  index_value = value_list.index(market)          
                  with urllib.request.urlopen("https://www.ncdex.com/MarketData/LiveFuturesQuotes.aspx") as url:
                      data_page = url.read()
                  soup = BeautifulSoup(data_page)
                  values = soup.findAll('td')
                  profit_list = []
                  for farmer_value in values[23:10000]:
                      final_value = cleanhtml(str(farmer_value))
                      final_value = ' '.join(final_value.split())

                      profit_list.append(final_value)

                  if crop in profit_list:
                        index = profit_list.index(crop)
                        profit = profit_list[index + 7]  
                        final = float(value_list[index_value + 5])
                        print(final / 100)
                        str_final = str( final / 100 - final / 100 *.238)
                        output_label = TextInput(text='Your Selling Price: ' + str_final + "    Today's Profit: " + profit, font_size = '40sp', size_hint = [1,.8])
                        self.layout.add_widget(output_label)
                  else:
                        final = float(value_list[index_value + 5])
                        print(final / 100)
                        str_final = str( final / 100 - final / 100 *.238)
                        output_label = TextInput(text='Your Selling Price: ' + str_final + "   Unsure about today's profit", font_size = '40sp', size_hint = [1,.8])
                        self.layout.add_widget(output_label)

                                          
            else:

          
                  with urllib.request.urlopen("https://www.ncdex.com/MarketData/LiveFuturesQuotes.aspx") as url:
                      data_page = url.read()
                  soup = BeautifulSoup(data_page)
                  values = soup.findAll('td')
                  profit_list = []
                  for farmer_value in values[23:10000]:
                      final_value = cleanhtml(str(farmer_value))
                      final_value = ' '.join(final_value.split())

                      profit_list.append(final_value)
                  if crop in profit_list:
                        index = profit_list.index(crop)
                        profit = profit_list[index + 7]  
                        final = int(value_list[5])
                        str_final = str( final / 100 - final / 100 *.238)
                        output_label = TextInput(text='Your Selling Price: ' + str_final + "    Today's Profit: " + profit, font_size = '40sp', size_hint = [1,.8])
                        self.layout.add_widget(output_label)
                        print(final / 100)
                  else:
                        final = int(value_list[5])
                        str_final = str( final / 100 - final / 100 *.238)
                        output_label = TextInput(text='Your Selling Price: ' + str_final + "    Unsure about today's profit", font_size = '40sp', size_hint = [1,.8])
                        self.layout.add_widget(output_label)
                        print(final / 100)

        else:
            output_label = TextInput(text='You have likely misspelled the name of your crop or have not input a crop', font_size = '40sp', size_hint = [1,.8])
            self.layout.add_widget(output_label)
            
            print('You have likely misspelled the name of your crop or have not input a crop')
        #write out string or integer to list considering all possible crop names
        button_back = Button(text = 'Back',background_color = [0.09, 0.41, 1, 1.5], size_hint = [1,0.48], pos=[12,50],
                      font_size = '50sp', font_name = 'Calibri'
                             )
        button_back.bind(on_press = self.back)
        self.layout.add_widget(button_back)
        if price == "":
            return
        if price != float or int:
              return
            
        
        
     

        
    #save button command
    def save(self, button2):
      crop = self.txt1.text.strip()
      price = self.txt2.text.strip()
      if crop == "":
            self.layout.clear_widgets()
            output_label = TextInput(text= 'No crop has been inputted',font_size = '40sp')
            self.layout.add_widget(output_label)
            button_back = Button(text = 'Back',background_color = [0.09, 0.41, 1, 1.5], size_hint = [1,0.48], pos=[12,50],
                      font_size = '50sp', font_name = 'Calibri'
                             )
            button_back.bind(on_press = self.back)
            self.layout.add_widget(button_back)
            return

      for dkey in item_dict.keys() :
            sum1 = 0.0
      for i in item_dict[dkey] :
            if price == int or float:
                  sum1 = sum1 + float(i)


            avg = sum1/len(item_dict[dkey])
      self.layout.clear_widgets()
      output_label = TextInput(text= 'Farmer average is: ' + str(avg),font_size = '40sp')
      self.layout.add_widget(output_label)
      button_back = Button(text = 'Back',background_color = [0.09, 0.41, 1, 1.5], size_hint = [1,0.48], pos=[12,50],
                      font_size = '50sp', font_name = 'Calibri'
                             )
      button_back.bind(on_press = self.back)
      self.layout.add_widget(button_back)
      data_directory = open('Values.txt', 'a')
      data_directory.writelines('\n')
      data_directory.write(str(dkey))
      data_directory.write('+$+')
      data_directory.write(str(avg))
      data_directory.close()
        

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


Star_gazer = Star_Gazer()
Star_gazer.run()
 

