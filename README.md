# Election Analysis
## Overview of Election Audit
### A representative from the Colorado Election Committee needs the 2017 congressional election results audited and analyzed. The final output of this analysis must be a simple summary table identifying the total number of votes, breakdown of votes in each county, the county's name with the greatest voter turnout, and the winner of the election. Python was selected as the data analysis tool for this project.
## Election Audit Results
### - The total number of votes cast in this election is 369,711.
### County Vote Breakdown
#### - For Arapahoe county, there were 24,801 votes cast comprising 6.7% of the total votes.
#### - For Jefferson county, there were 38,855 votes cast comprising 10.5% of the total votes. 
#### - Denver county had the largest number of votes cast at 306,055 votes comprising 82.8% of the total votes.
### Congressional Candidate Results Breakdown
#### - Raymon Anthony Doane received 11,606 votes comprising 3.1% of the total votes.
#### - Charles Casper Stockham received 85,213 votes comprising 23.0% of the total votes.
#### - The winner of the congressional election was Diana DeGette with 272,892 votes comprising 73.8% of the total votes.
## Election-Audit Summary
### While this script is currently specific to the 2017 Colorado Congressional election data, the code can be easily modified to analyze any other election audit given a .csv file of data in the same format. The current code indirectly loads the .csv file that is saved in the Resources folder in this Election_Analysis repository. See this code below:
#### file_to_load = os.path.join("Resources", "election_results.csv")
### Simply update the path to the location where your election results .csv file is located, ensuring the name of the file is updated in the code as well, and you can analyze the new set of election results. Similarly, if you want to save the analysis to a text file, you will want to create a new .txt file so that your code does not overwrite the election analysis from the 2017 Congressional election. See the code below:
#### file_to_save = os.path.join("Analysis", "election_analysis.txt")
### Simply change the name of the .txt file in the path to the correct output file and you will have a new file with your newly analyzed results. 
### The code uses for loops and if statements with generic variable names like "total_votes" and "candidate_name" or "county_name" thereby allowing any state election that you would want to find county- and candidate-specific information about to be analyzed by this code, given the changes to the source file code as mentioned previously. This analysis only had data for three candidates and three counties. However, because the code is written using the .append function, a list of all the counties in Colorado, or any other state for that matter, could be analyzed using this code. The code below compiles a list of all counties present in the data and adds them to a new list to be used for tracking votes per county:
<img width="355" alt="image" src="https://user-images.githubusercontent.com/102757676/164912065-dfb98a62-8116-48e3-bd02-a0af9610cee2.png">
One final spectacular part of the code is to automatically return the number and percentage of votes per county, and which county had the largest turnout. The code that performs this analysis is below:
<img width="521" alt="image" src="https://user-images.githubusercontent.com/102757676/164912139-e1c48f26-9f1a-4bee-abd5-d685ae9a9d9e.png">
You can also see tht in the middle of this code above there is a print function to show the results in the terminal and then there is a piece that will write the results to your text output file. All in all, this code can be used for any state election so long as the files are in the same format as the one used in this analysis.

