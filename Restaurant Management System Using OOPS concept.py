#!/usr/bin/env python
# coding: utf-8

# In[6]:


class PythonCafeTalk:
    def restaurants(rp):
        print("\t\t\t\t Python Cafe Talk")
        print("\t\t\t\t Since-1997")
        print("\t\t\t\t www.fuddybuddy.com")
        print("\n\n\t\t\t\t\tMENU")
        
    def food(rp):
        x=["Indian","German","Korean","Vietnamese"]
        for k in x:
            print("\n\n",k)
            
    def german(rp):
        x=["Sauerbraten-roas beef stew ","Schweinshaxe-pork knuckle","Rinderroulade-beef roll","Bratwurst-grilled sausage","Kartoffelpuffer-potato pancake","Kartoffelkloesse-potato dumplings","Sauerkraut-fermented cabbage","Spatzle-Egg noodles"]
        y=[250,300,150,100,200,100,350,180]
        german_={"German Food Types":x,"Price":y}
        import pandas as pd
        df=pd.DataFrame(german_)
        print("\n\n German Foods \n\n")
        print(df)
        d=[]
        while x:
            x=True
            b=int(input("Enter the value position : "))
            c=int(input("Enter the Quantity:"))
            z=german_["Price"][b]
            y=z*c
            d.append(y)
            x=input("you want to reorder(yes/no):")
            if(x=="no"):
                print('Thank you')
                break
        t=sum(d)
        m=(sum(d)*0.05)
        k=t+m
        print("servicetax = 5%")
        print("Total Amount:",t,"Rupees")
        print("Total Amount Including Service Tax:",k,"Rupees")
        
        
    def korean(rp):
        x=["Kimchi","Bibimbap","Bulgogi","Jajangmyeon","Samgyeopsal","Korean fried chicken","Red rice cakes - tteokbokki"]
        y=[200,100,350,400,100,345,250]
        korean_={"Korean Food Types":x,"Price":y}
        import pandas as pd
        df=pd.DataFrame(korean_)
        print("\n\n Korean Foods \n\n")
        print(df)
        d=[]
        while x:
            x=True
            b=int(input("Enter the value position : "))
            c=int(input("Enter the Quantity:"))
            z=korean_["Price"][b]
            y=z*c
            d.append(y)
            x=input("you want to reorder(yes/no):")
            if(x=="no"):
                print('Thank you')
                break
        t=sum(d)
        m=(sum(d)*0.05)
        k=t+m
        print("servicetax = 5%")
        print("Total Amount:",t,"Rupees")
        print("Total Amount Including Service Tax:",k,"Rupees")
        
    
        
        
    def vietnamese(rp):
        x=["Pho","Bun cha","Banh mi","Banh cuon","Goi cuon"]
        y=[250,300,200,100,500]
        vietnamese_={"Vietnamese Food Types":x,"Price":y}
        import pandas as pd
        df=pd.DataFrame(vietnamese_)
        print("\n\n Vietnamese Foods \n\n")
        print(df)
        d=[]
        while x:
            x=True
            b=int(input("Enter the value position : "))
            c=int(input("Enter the Quantity:"))
            z=vietnamese_["Price"][b]
            y=z*c
            d.append(y)
            x=input("you want to reorder(yes/no):")
            if(x=="no"):
                print('Thank you')
                break
        t=sum(d)
        m=(sum(d)*0.05)
        k=t+m
        print("servicetax = 5%")
        print("Total Amount:",t,"Rupees")
        print("Total Amount Including Service Tax:",k,"Rupees")
        
    
        
    def indian(rp):
        x=["Misal Pav","Kosha Mangsho","Makki Di Roti& sarso da saag","Dhokla","Rogan Josh","Papaya Khar","Litti Chowkha","Biryani","Fish Curry"]
        y=[80,200,350,120,200,150,250,400,500]
        indian_={"Indian Food Types":x,"Price":y}
        import pandas as pd
        df=pd.DataFrame(indian_)
        print("\n\n Indian Foods \n\n")
        print(df)
        d=[]
        while x:
            x=True
            b=int(input("Enter the value position : "))
            c=int(input("Enter the Quantity:"))
            z=indian_["Price"][b]
            y=z*c
            d.append(y)
            x=input("you want to reorder(yes/no):")
            if(x=="no"):
                print('Thank you')
                break
        t=sum(d)
        m=(sum(d)*0.05)
        k=t+m
        from colorama import Fore,Back,Style
        print(Fore.BLACK+Back.RED+Style.BRIGHT+"servicetax = 5%")
        print("Total Amount:",t,"Rupees")
        print("Total Amount Including Service Tax:",k,"Rupees")
        


# In[7]:


obj=PythonCafeTalk()
obj.restaurants()
obj.food()


# In[8]:


x=input("Enter the Type of food : ")
if x=="indian":
    print(obj.indian())
elif x=="german":
    print(obj.german())
elif x=="korean":
    print(obj.korean())
elif x=="vietnamese":
    print(obj.vietnamese())
else:
    print("wrong option: \nplease again choose the right option:")


# In[ ]:





# In[ ]:





# In[ ]:




