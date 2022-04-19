# Open the data file
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total votes counter
total_votes = 0
# Declare Candidate Options list
candidate_options = []
# Declare Candidate Votes dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    #To do: read and analyze data
    file_reader = csv.reader(election_data)
    # Print the header row
    headers = next(file_reader)
    
    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]
        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add it to the candidate name from each row
            candidate_options.append(candidate_name)
            # Begin tracking each candidate's vote  count
            candidate_votes[candidate_name] = 0
        # Add a vote to each candidate's count
        candidate_votes[candidate_name] += 1
    
# Save the results to text file
# Using the with statement with the "w" mode we will write data to the file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal
    election_results = (
        f"\nColorado Election Results\n"
        f"----------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------------\n")
    print(election_results, end="")

    # Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the candiate list
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print out each candidate's name, vote count, and percentage of votes to the terminal
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print each candidate, their vote count, and percentage to the terminal
        print(candidate_results)
        # Save the candidate results to the text file
        txt_file.write(candidate_results)

        #Determine the winning vote count and candidate
        #Determine if the vote is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
    # Print the winning candidate's results to the terminal
    winning_candidate_summary = (
        f"_______________________\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"_______________________\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)


