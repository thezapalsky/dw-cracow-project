CREATE TABLE
   politics.votes_raw (
      cadence INT64,
      sitting_id INT64,
      voting_number INT64,
      voting_desc STRING,
      voting_date DATE,
      voting_time TIME,
      resolution_number INT64,
      resolution_description STRING,
      party STRING,
      deputy STRING,
      vote STRING
      )
 PARTITION BY
   voting_date
 CLUSTER BY
   party, deputy, vote
 OPTIONS
   ( 
     description="Raw voting data" )