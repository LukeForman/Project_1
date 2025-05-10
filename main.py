from logic import *

def main() -> None:
    """
    Main Function ~ Opens the window and runs the logic
    """
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()
    

if __name__ == "__main__": 
    main()