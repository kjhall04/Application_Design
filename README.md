# Equipment Log Program
## User Expectations
This is a program that is used for the logging of equipment by a manager overseeing a group of people. The equipment is also attributed to users of the equipment. The database can then be manipulated by the user. The user should have the ability to add and delete records. The user can also view all records at once. Also, the user can search up data to show data connected to what is searched. Program will also be locked by username and password. The user can also update individual data values if needed.

Afterward, the program can be closed and all changes to stored data are saved.


## Storing Data
The data is stored in a database created using sqlite3. The data will be in two tables: one for names of people and one for all the equipment. Below is the data names and their corresponding data types.

### Name Data Table
|Data|Type|
|----------|-------|
|ID|Integer|
|First Name|String|
|Last Name|String|
|Phone Number|String|
|Email|String|
### Equipment Data Table:
|Data|Type|
|----------|-------|
|ID|						Integer
|Contact_ID|Integer|
|Equipment Name|String|
|Depratment|String|			
|Date Installed|String|
|Maintenance date|String|
|Decommissioned (True or False)|String|
|Decommissioned Date|String|			
### Login Data table:
|Data|Type|
|----------|-------|
|First Name|String|
|Last Name|String|
|Username|String|
|Password|String|

## Program Requirements
The program requires a few separate modules to be installed before it can be run.

customtkinter, re, sqlite3, fpdf, os, platform 

## Program Flow
Below is a diagram of the flow chart for this program.

<img src="https://github.com/kjhall04/Application_Design/blob/main/EquipmentManager/Images/FlowChart.png" width="300" />

## User Interface
Below are images of all the User Interface screens. (Note: Any data shown is fake)

<div style="display: flex;">
  <img src="https://github.com/kjhall04/Application_Design/blob/main/EquipmentManager/Images/LoginScreen.png" width="300" />
  <img src="https://github.com/kjhall04/Application_Design/blob/main/EquipmentManager/Images/SignUpScreen.png" width="300" />
  <img src="https://github.com/kjhall04/Application_Design/blob/main/EquipmentManager/Images/LoadingScreen.png" width="300" />
</div>

<div style="display: flex;">
  <img src="https://github.com/kjhall04/Application_Design/blob/main/EquipmentManager/Images/ContactDataScreen.png" width="300" />
  <img src="https://github.com/kjhall04/Application_Design/blob/main/EquipmentManager/Images/EquipmentDataScreen.png" width="300" />
	<img src="https://github.com/kjhall04/Application_Design/blob/main/EquipmentManager/Images/DatabaseScreen.png" width="300" />
</div>

<div style="display: flex;">
  <img src="https://github.com/kjhall04/Application_Design/blob/main/EquipmentManager/Images/AddContactScreen.png" width="300" />
  <img src="https://github.com/kjhall04/Application_Design/blob/main/EquipmentManager/Images/AddEquipmentScreen.png" width="300" />
</div>

<div style="display: flex;">
  <img src="https://github.com/kjhall04/Application_Design/blob/main/EquipmentManager/Images/EditContactDataScreen.png" width="300" />
  <img src="https://github.com/kjhall04/Application_Design/blob/main/EquipmentManager/Images/EditEquipmentDataScreen.png" width="300" />
</div>
