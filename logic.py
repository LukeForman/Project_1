from PyQt6.QtWidgets import *
from gui import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
    """
    Logic of the Program
    """
    def __init__(self) -> None:
        """
        Initializes the ui and sets up logic for button presses
        """
        super().__init__()
        self.setupUi(self)
        self.vote_button.clicked.connect(lambda : self.submit())

    def submit(self) -> None:
        """
        ID handling logic, error and exception handling, and data writing and validation to csv
        """
        id = self.id_input.text().strip()
        try: 
            if not id: 
                raise ValueError
            if not id.isdigit(): 
                raise TypeError
            if not len(id) == 8: 
                raise LengthException
            if not self.jane_button.isChecked() and not self.john_button.isChecked(): 
                raise ButtonException   
            elif self.jane_button.isChecked(): 
                vote = "Jane"
            elif self.john_button.isChecked(): 
                vote = "John"
            if self.check_id(id): 
                self.write_data(id, vote)
                if self.group_status.checkedButton() is not None:
                    self.group_status.setExclusive(False)
                    self.group_status.checkedButton().setChecked(False)
                    self.group_status.setExclusive(True)     
                self.id_input.clear()   
                self.error_label.clear()   
                self.id_input.setFocus()
            else: 
                raise IdError

        except ValueError:
            self.error_label.setText("<font color='red'>Please Enter 8 Digit ID</font>")
        except TypeError:
            self.error_label.setText("<font color='orange'>Please Enter Only Numbers</font>")
        except ButtonException: 
            self.error_label.setText("<font color='green'>Please Choose A Candidate </font>")
        except LengthException: 
            self.error_label.setText("<font color='yellow'>Please Enter 8 Digits</font>")
        except IdError: 
            self.error_label.setText("<font color='Purple'>Already Voted</font>")
            
    def check_id(self, id) -> bool:
        """
        Returns True if id has not been entered yet, and False if already written to csv
        """
        try:
            with open("data.csv", "r", newline = "") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row and row[0] == id:
                        return False  
            return True 
        except FileNotFoundError:
            return True
        
    def write_data(self, id, vote) -> None:
        """
        Writes The ID and Vote to csv
        """
        with open("data.csv", "a", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([id, vote])

class ButtonException(Exception): 
    """
    Raised When User Does Not Select Button But Has Correct ID
    """
class LengthException(Exception): 
    """
    Raised When User Does Not Enter 8 Numerical Digits
    """
class IdError(Exception): 
    """
    Raised When User Enters Non-Unique ID
    """