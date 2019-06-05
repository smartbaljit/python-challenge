
#import the required libraries
import os
import csv

prof_loss_List =[]
year_List=[]


#reading the file [budget_data.csv]
csv_path=os.path.join("","Resources", "budget_data.csv")

with open(csv_path,newline="") as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")
    csv_header=next(csv_reader)

    month_count =0
    profit=0
    loss=0
    net_total=0
    prof_loss_val=0

    x=0
    
    for row in csv_reader:
        #count the number of months
        month_count+=1

        #Net total amount
        net_total=net_total+int(row[1])

        # save the years in a list called year_List
        year_List.append(row[0])

        # To Calculate the Greatest increase in profit, substract every value from the profit loss column with the previous month's value 
        # and store the values in a list called prof_loss_List
        prof_loss_val = int(row[1])-x
        prof_loss_List.append(prof_loss_val)

        x=int(row[1])

    total =0
     #calculate average
    tot=sum(prof_loss_List[1:])
    avg=tot/(month_count-1)
     
   
    #Find greatest increase in profit
    greatest_increase_profit = max(prof_loss_List)
    find_index_increase=prof_loss_List.index(max(prof_loss_List))

    #Find greatest decrease in profit
    greatest_decrease_profit=min(prof_loss_List)
    find_index_decrease=prof_loss_List.index(min(prof_loss_List))


    #Print results on the terminal                                                                    
    print("Financial Analysis ---------------- Total Months: " +str(month_count) + " Total: "+"${:}".format(net_total) + " Average Change: "+ str(round(avg,2))) 
    print("Greatest increase in profits: "+ year_List[find_index_increase] + " (" + "${:}".format(greatest_increase_profit) +")")
    print("Greatest decrease in profits: " +year_List[find_index_decrease] + " (" + "${:}".format(greatest_decrease_profit) +")")
   
       
    #Write results in a text file
    output_path = os.path.join("","Resources", "budget_data_output.txt")
    with open(output_path, "w", newline="") as outfile:
        outfile.write("Financial Analysis ---------------- Total Months: " +str(month_count) + " Total: "+"${:}".format(net_total) + " Average Change: " +str(round(avg,2)))
        outfile.write("\r\nGreatest increase in profits: "+ year_List[find_index_increase] + " (" + "${:}".format(greatest_increase_profit) +")")
        outfile.write("\r\nGreatest decrease in profits: " +year_List[find_index_decrease] + " (" + "${:}".format(greatest_decrease_profit) +")")


        