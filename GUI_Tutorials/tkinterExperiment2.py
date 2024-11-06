import sqlite3
import customtkinter as ctk
from tkinter import messagebox

# Database connection and setup
def init_db():
    """Initialize the database and create the contacts table if it doesn't exist."""
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

class ContactManager(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.title("Contact Manager")
        self.geometry("500x400")

        # Center window on screen
        self.eval('tk::PlaceWindow . center')

        # Database initialization
        init_db()

        # Frames and Widgets
        self.create_widgets()

    def create_widgets(self):
        """Create widgets for the GUI layout."""
        # Labels and entries for contact input
        self.name_label = ctk.CTkLabel(self, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.name_entry = ctk.CTkEntry(self)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.phone_label = ctk.CTkLabel(self, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.phone_entry = ctk.CTkEntry(self)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Buttons for actions
        self.add_button = ctk.CTkButton(self, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

        self.update_button = ctk.CTkButton(self, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=1, column=2, padx=10, pady=10)

        self.delete_button = ctk.CTkButton(self, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=2, column=2, padx=10, pady=10)

        # Listbox to display contacts
        self.contact_list = ctk.CTkTextbox(self, height=10, width=50)
        self.contact_list.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.contact_list.bind("<<ListboxSelect>>", self.select_contact)

        # Load contacts into listbox
        self.load_contacts()

    def load_contacts(self):
        """Load contacts from the database and display them in the listbox."""
        self.contact_list.delete("1.0", "end")  # Clear the listbox
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contacts")
        contacts = cursor.fetchall()
        conn.close()
        for contact in contacts:
            self.contact_list.insert("end", f"{contact[0]}. {contact[1]} - {contact[2]}\n")

    def add_contact(self):
        """Add a new contact to the database."""
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        if not name or not phone:
            messagebox.showwarning("Input Error", "Please enter both name and phone.")
            return
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))
        conn.commit()
        conn.close()
        self.load_contacts()
        self.clear_entries()

    def update_contact(self):
        """Update an existing contact in the database."""
        selected = self.contact_list.get("1.0", "end-1c").split("\n")
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a contact to update.")
            return
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        if not name or not phone:
            messagebox.showwarning("Input Error", "Please enter both name and phone.")
            return
        contact_id = int(selected[0].split(".")[0])
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE contacts SET name = ?, phone = ? WHERE id = ?", (name, phone, contact_id))
        conn.commit()
        conn.close()
        self.load_contacts()
        self.clear_entries()

    def delete_contact(self):
        """Delete a contact from the database."""
        selected = self.contact_list.get("1.0", "end-1c").split("\n")
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a contact to delete.")
            return
        contact_id = int(selected[0].split(".")[0])
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
        conn.commit()
        conn.close()
        self.load_contacts()
        self.clear_entries()

    def select_contact(self, event):
        """Populate entry fields when a contact is selected from the list."""
        selected = self.contact_list.get("1.0", "end-1c").split("\n")
        if selected:
            name, phone = selected[0].split(" - ")
            self.name_entry.delete(0, "end")
            self.name_entry.insert("end", name.split(". ")[1])
            self.phone_entry.delete(0, "end")
            self.phone_entry.insert("end", phone)

    def clear_entries(self):
        """Clear the input fields."""
        self.name_entry.delete(0, "end")
        self.phone_entry.delete(0, "end")

# Run the application
if __name__ == "__main__":
    app = ContactManager()
    app.mainloop()
