import os
import csv
csvpath = os.path.join(".", "raw_data","election_data_1.csv")

voter_id_list = []
candidate_list = []
county_list = []
total_votes = 0
total_revenue = 0
unique_candidates = []
with open(csvpath, newline='') as csvfile:
   csvreader = csv.DictReader(csvfile)
   for row in csvreader:  
       voter_id = str(row["Voter ID"])
       county = str(row["County"])
       candidate = str(row["Candidate"])
       voter_id_list.append(voter_id)
       county_list.append(county)
       candidate_list.append(candidate)
       #count total months in worksheet
       total_votes = total_votes + 1
for x in candidate_list:
      if x not in unique_candidates:
          unique_candidates.append(x)

print([unique_candidates].count)
