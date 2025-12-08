from datetime import datetime
class LLOrganizer():

    def create_tournament(self):
        pass

    def choose_date(self, start_date: str) -> datetime:
        pass

        '''Checks players date of birth and if the format fits the 
        standards, then the user can continue inputting the information.'''

        try:
            # change string input to datetime
            start_date = datetime.strptime(start_date, "%d/%m/%Y")
            
			# check if inputted date is in the future, then not valid
            if start_date < datetime.now():
                raise ValueError("Date has to be in the future. Please enter a valid date.")
            return start_date
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