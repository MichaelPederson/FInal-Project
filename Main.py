from VoteGUI import*
from VoteLogic import*

def main():

    app = QApplication([])
    window = Logic()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
