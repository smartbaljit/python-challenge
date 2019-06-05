
#import the required libraries

import os
import csv
import string
voter_id =[]
candidate_list=[]
candidate_dict ={}


#Function to calculate the vote percentage
def percent_calc(candidate_votecount,total_vote_count):
        candidate_percentage =candidate_votecount/total_vote_count
        return candidate_percentage


#reading the file [election_data.csv]
csv_path=os.path.join("","Resources", "election_data.csv")

with open(csv_path,newline="") as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")
    csv_header=next(csv_reader)

    vote_count=0
    khan_cnt=0
    correy_cnt=0
    li_cnt=0
    otooley_cnt=0

    for row in csv_reader:
        #count the number of votes
        vote_count+=1
        candidate=row[2]
        #for candidate in candidate_list:
         #   if candidate is not candidate_list:
          #       candidate_list.append(candidate)
        if row[2].lower()== "khan":
            khan_cnt+=1
        elif row[2].lower() == "correy":
            correy_cnt+=1
        elif row[2].lower() =="li":
            li_cnt+=1
        elif row[2].lower()=="o'tooley":
            otooley_cnt+=1


    #call the percent_calc function to calculate the vote percentage for every candidate
    khan_perc = percent_calc(khan_cnt, vote_count)
    correy_perc= percent_calc(correy_cnt, vote_count)
    li_perc= percent_calc(li_cnt, vote_count)
    otooley_perc= percent_calc(otooley_cnt, vote_count)

    # Dictionary to store vote count and vote percentage of each candidate
    candidate_dict={"Khan":[khan_perc,khan_cnt], "Correy":[correy_perc,correy_cnt], "Li":[li_perc,li_cnt], "O'Tooley":[otooley_perc,otooley_cnt]}

    #Find the candidate with max votes using function max which will give the key i.e. candidate name of the max value
    max_votes = max(candidate_dict,key=candidate_dict.get) 

    #print the results on the terminal
    print("Election Results ---------------------- Total Votes: " +str(vote_count) + "-----------------")
    
    for k, v in candidate_dict.items():
	    print(str(k) +": "+"{:.3%}".format(v[0])+ " (" +str(v[1])+")")
    
    print("Winner: " + max_votes ) 


    #create a text file to store the results
    output_path = os.path.join("","Resources", "election_data_output.txt")
    with open(output_path, "w", newline="") as outfile:
       outfile.write("Election Results ---------------------- Total Votes: " +str(vote_count) + "-----------------\r\n")
       for k, v in candidate_dict.items():
	       outfile.write(str(k) +": "+"{:.3%}".format(v[0])+ " (" +str(v[1])+")\r\n")
        
       outfile.write("Winner: " + max_votes)
        
    