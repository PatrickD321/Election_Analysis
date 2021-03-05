# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentages of votes each candidates who recieved votes
# 4. The total number of  votes each candidate won 
# 5. The winner of the election based on popular votes

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time
print("The time right now is ", now)
# Adding Dependecies
import csv 
import os 

# Assign a variable for the file to load and the path.
file_to_load = os.path.join( "Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("..","analysis", "election_analysis.txt")

# Intilizing Variables.
# Total vote counter.
total_votes = 0
# Candidate options list
candidate_options = []
# Candidate votes declared as dictionary.
candidates_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
     # Read the file object with the reader function.   
    file_reader = csv.reader(election_data)

    # Show the file path is working
    print(election_data)
    
    # Read the header row.
    headers = next(file_reader)
        

    # Iterate each row in CSV file.    
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name for each row.
        candidate_name = row[2]

        # If the candidate name is not the same then print the name
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Initialize the candiadtes votes.
            candidates_votes[candidate_name] = 0

        # Begin counting candidate votes.
        candidates_votes[candidate_name] += 1

# Determine the percentage of votes for candidates by looping through the counts.
for candidate_name in candidates_votes:
    # Counting the votes for each candidate
    votes = candidates_votes[candidate_name]
    # Calculate the percentage for each candidate
    votes_percentage = float(votes) / float(total_votes) * 100
    # Printing the results for each candidate
   # print(f"{candidate_name}: received {round(votes_percentage, 1)}% of vote.")
    print(f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")


    # Determine if the votes are graeter than the winning count, to declare the winner.
    if (votes > winning_count) and (votes_percentage > winning_percentage):
    # if true then set winning_count = votes and winnin_percentage = vote_percentage
        winning_count = votes 
        winning_percentage = votes_percentage
    # Set the winning candidate to the candidate's name.
        winning_candidate = candidate_name   

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


# Print the total votes.
print(total_votes)
print(candidate_options)
print(candidates_votes)


# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:
# Write some data to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("--------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
