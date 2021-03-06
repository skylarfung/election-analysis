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

#initalize varables
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0 
winning_percentage = 0
county_options = []
county_votes = {}
largest_county_turnout = ""
largest_county_count = 0



#open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #read header row
    headers = next(file_reader)

    #print each row in the CSV file
    for row in file_reader:

        #gets total votes
        total_votes += 1

        #prints the candidate names        
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #track the candidate votes
            candidate_votes[candidate_name] = 0

        #add votes for candidates
        candidate_votes[candidate_name] += 1

        #prints county
        county_name = row[1]
        if county_name not in county_options:
            county_options.append(county_name)

            #track county votes
            county_votes[county_name] = 0
        
        #add county votes
        county_votes[county_name] += 1


#using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:

    #print final vote count
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    
    print(election_results, end="")

    #save final vote count to txt file
    txt_file.write(election_results)

    #determine the county with largest turnout
    for county in county_votes:
        county_votes_tot = county_votes[county]
        county_vote_percentage = float(county_votes_tot) / float(total_votes) * 100
        county_results = (f"{county}: {county_vote_percentage:,.1f}% ({county_votes_tot:,})\n")

        print(county_results)
        txt_file.write(county_results)

        #determines county with largest turnout
        if county_votes_tot > largest_county_count:
            largest_county_count = county_votes_tot
            largest_county_turnout = county
    
    #county summary
    winning_county_summary = (
        f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"-------------------------\n")
    
    print(winning_county_summary)
    txt_file.write(winning_county_summary)

    
    #determine the percentage of votes for each candidate
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)
        txt_file.write(candidate_results)
        
        #determines winning candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate

    #summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------")

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)