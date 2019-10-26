class Vote:
    def __init__(self, 
                 cadence, 
                 sitting_id, 
                 voting_number, 
                 voting_desc, 
                 voting_date, 
                 voting_time, 
                 resolution_number, 
                 resolution_desc, 
                 party, 
                 deputy, 
                 vote 
                ):  
        self.cadence= cadence
        self.sitting_id = sitting_id
        self.voting_number = voting_number
        self.voting_desc = voting_desc
        self.voting_date = voting_date
        self.voting_time = voting_time
        self.resolution_number = resolution_number
        self.resolution_desc = resolution_desc
        self.party = party
        self.deputy = deputy
        self.vote = vote