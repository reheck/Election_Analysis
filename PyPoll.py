# Open the data file
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    #To do: read and analyze data
    file_reader = csv.reader(election_data)
    # Print the header row
    headers = next(file_reader)
    print(headers)
    # Print each row in the CSV file
    #for row in file_reader:
        #print(row)

    

# Using the with statement with the "w" mode we will write data to the file
with open(file_to_save, "w") as txt_file:
    # Write some data to the file
    txt_file.write("Colorado Election Analysis")
    txt_file.write("\nCounties in the Election")
    txt_file.write("\n_________________________")
    # Write three counties to the file
    txt_file.write("\nArapahoe\nDenver\nJefferson")
    


# 1. Find the total number of votes cast
# 2. Pull a complete list of candidates who recieved votes
# 3. Find the percentage of votes each candidate won/
# 4. Count the total number of votes each candidate won
# 5. Determine the winner of the election based on the popular vote


