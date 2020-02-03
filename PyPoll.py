# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#dependencies
import csv
import os

# Assign a varable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file
with open(file_to_load) as election_data:

    #To do: perform analysis
    file_reader = csv.reader(election_data)

    #print each row in CSV file
    headers = next(file_reader)
    print(headers)



#using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:

    #write to text file
    txt_file.write("Hello World")

