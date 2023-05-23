import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_rows',15)
pd.set_option('display.max_columns',20)
pd.set_option('display.precision',2)
df = pd.read_csv('Mithish_CSV.csv') 
df.set_index("Sno",drop=True, inplace=True)
ans="Yes"
while ans=="Y" or ans=="y" or ans=="Yes" or ans=="yes":
    print("Airline Database")
    print("Please choose from the available options:")
    print("1.To print the entire the database")
    print("2.To get information of the dataframe and their datatypes")
    print("3.To display the specific columns by its heading")
    print("4.To display the information of a route by the index number")
    print("5.To find the total number of rows and columns")
    print("6.To display the details of the first 'n' data")
    print("7.To display the details of the last 'n' data")
    print("8.To display the details of the route whose fare is more than a specified amount")
    print("9.To display the details of the route having highest and lowest rating")
    print("10.To display all the headings of the dataframe")
    print("11.To add a new row")
    print("12.To delete a row")
    print('13.To plot a graph between destination and rating')
    print("14.Exit")
    opt=int(input('Enter the option you would like to choose'))
    if opt==1:
        print("The entire database:")
        print(df)
    elif opt==2:
        print("The database information is")
        print(df.info)
    elif opt==3:
        print("The available headings are:",df.columns)
        n=int(input("Enter number of columns whoose details must be displayed:"))
        for i in range(n):
            heading=input("Enter the column heading:")
            print(df.loc[:,[heading]])
    elif opt==4:
        y=int(input("Enter the index"))
        x=y-1
        yx=df.iloc[[x]]
        print("The ",y," route is")
        print(yx)
   
    elif opt==5:
        print("The total number of rows and columns are:")
        (a,b)=(df.shape)
        print("The total number of rows is",a)
        print("The total number of columns is",b)
    elif opt==6:
        h=int(input("Enter the number of routes "))
        print(df.head(h))
    elif opt==7:
        t=int(input("Enter the number of routes "))
        print(df.tail(t))
    elif opt==8:
        r_df=df[["Airline","CostInAED"]]
        a=int(input("Enter the amount"))
        res=r_df[(r_df["CostInAED"]>=a)]
        print("The routes whose fare is more than ",a)
        print(res)
    elif opt==9:
        print("Highest rating")
        maxi=df["Rating"].max()
        print(df.loc[df.Rating==maxi,:])
        print("Lowest Rating")
        mini=df["Rating"].min()
        print(df.loc[df.Rating==mini,:])
    elif opt==10:
        print("The headings are")
        print(df.columns)
    elif opt==11:
        print("The options for the new row are:")
        x={'Sno':21,'Airline':'Delta','FlightNo':410,'Origin':'Dubai DXB','Destination':'Atlanta',
           'DepartureTime':130,'ArrivalTime':2130,'Aircraft':777,'Duration':1400,'MaxPax':300,
           'CostInAED':5500,'Rating':2.6,'IFE':'Y'}
        y={'Sno':21,'Airline':'Air New Zealand','FlightNo':30,'Origin':'Dubai DXB','Destination':'Auckland',
           'DepartureTime':130,'ArrivalTime':1530,'Aircraft':777,'Duration':1700,'MaxPax':300,
           'CostInAED':5500,'Rating':4.5,'IFE':'Y'}
        print("The options are:")
        print(x)
        print(y)
        op=input("Enter x or y:")
        if op=="x":
            '''sa=input("Enter which row you want to add, a or b:")'''
            df=df.append(a,ignore_index=True)
            print("The dataframe is:",df)
        elif op=="y":
            df=df.append(b,ignore_index=True)
            print("The dataframe is:",df)
        else:
            print("Enter valid option")
    elif opt==12:
        r=int(input("Enter the index of the row you want to delete"))
        df.drop(df.index[r])
        print(df.loc[0:r,:])
    elif opt==13:
        dest=df.Destination
        rate=df.Rating
        plt.plot(dest,rate)
        plt.xlabel('Destination',fontsize=11)
        plt.xticks(rotation=45)
        plt.ylabel('Rating',fontsize=11)
        plt.yticks(rotation=90)
        plt.show()
        
    elif opt==14:
        break
    
        
