#! pyhton3
# Main code to run the Equipment Logging Program

import Create_Database
import Menu

if __name__ == '__main__':
    
    Create_Database.create_database()
    app = Menu.FrameManager()
    app.mainloop()