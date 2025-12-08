from datetime import datetime
class LLOrganizer():

    def __init__(self):
        self.ll = LLOrganizer()

    def create_tournament(self):
        pass

    def choose_start_date(self, start_date: str) -> datetime:

        try:
            # change string input to datetime
            start_date = datetime.strptime(start_date, "%d/%m/%Y")
            
			# check if inputted date is in the future, then not valid
            if start_date < datetime.now():
                raise ValueError("Date has to be in the future. Please enter a valid date.")
            return start_date
        except ValueError:
            raise ValueError ("Invalid date. Use DD/MM/YYYY")
    
    def choose_end_date(self, end_date) -> datetime:

        try:
            # change string input to datetime
            end_date = datetime.strptime(end_date, "%d/%m/%Y")
            
			# check if inputted date is in the future, then not valid
            if end_date <= self.ll.choose_start_date():
                raise ValueError("Date has to be after the start date. Please enter a valid date.")
            return end_date
        except ValueError:
            raise ValueError ("Invalid date. Use DD/MM/YYYY")
    

    def choose_location(self):
        pass
        

    def choose_contanct(self):
        pass


# create tournament
    # skrá tengilið
# choose location
# choose start and end date
# búa til leikjadagskrá
# getur séð persónuupplýsingar