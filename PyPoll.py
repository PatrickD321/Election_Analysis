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
# Import the CSV and os module.
import csv 
import os 
# Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join( "Resources", "election_results.csv")
# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: perform analysis.
    print(election_data)
     # Read the file object with the reader function.   
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("..","analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:
# Write some data to the file.
    txt_file.write("Counties in the Election23\n")
    txt_file.write("--------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
