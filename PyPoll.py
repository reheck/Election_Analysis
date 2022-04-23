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
# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
most_county = ""
mostcounty_count = 0
mostcounty_percentage = 0


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
        # 3: Extract the county name from each row.
        county_name = row[1]
        #If the candidate does not match any existing county
        if candidate_name not in candidate_options:
            # Add it to the candidate name from each row
            candidate_options.append(candidate_name)
            # Begin tracking each candidate's vote  count
            candidate_votes[candidate_name] = 0
        # Add a vote to each candidate's count
        candidate_votes[candidate_name] += 1
        # 4a: Write an if statement that checks that the county does not match any existing county in the county list.
        if county_name not in county_options:
            # 4b: Add the existing county to the list of counties.
                county_options.append(county_name)
            # 4c: Begin tracking the county's vote count.
                county_votes[county_name] = 0
        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)
    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        c_votes = county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county.
        c_vote_percentage = float(c_votes) / float(total_votes) * 100
         # 6d: Print the county results to the terminal.
        county_results = (
            f"{county_name}: {c_vote_percentage:.1f}% ({c_votes:,})\n")
        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (c_votes > mostcounty_count) and (c_vote_percentage > mostcounty_percentage):
            mostcounty_count = c_votes
            mostcounty_percentage = c_vote_percentage
            most_county = county_name

    # 7: Print the county with the largest turnout to the terminal.
    most_county_summary = (
        f"_______________________\n"
        f"Largest County Turnout: {most_county}\n"
        f"_______________________\n")
    print(most_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(most_county_summary)
    # Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the candiate list
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print out each candidate's name, vote count, and percentage of votes to the terminal
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


