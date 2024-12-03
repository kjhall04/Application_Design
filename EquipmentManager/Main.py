#! pyhton3
# Main code to run the Equipment Logging Program

# import menu and create database modules
import Create_Database
import Menu

if __name__ == '__main__':

    # Create database if not already there
    Create_Database.create_database()

    # Create instance of frame manager and run program
    app = Menu.FrameManager()
    app.mainloop()