import sqlite3
import customtkinter as ctk

def get_all_data_for_menu():
    conn = sqlite3.connect('EquipmentLogs.db')
    cursor = conn.cursor()

    query = '''
    SELECT
        contact.Fname,
        contact.Lname,
        equipment.Ename,
        equipment.Department
    FROM
        contact
    INNER JOIN
        equipment
    ON
        contact.id = equipment.contact_id
    ORDER BY
        contact.Fname, contact.Lname;
    '''
    cursor.execute(query)

    results = cursor.fetchall()

    # Group data by names
    grouped_data = {}
    for row in results:
        name = f"{row[0]} {row[1]}"
        if name not in grouped_data:
            grouped_data[name] = []
        grouped_data[name].append({"Ename": row[2], "Department": row[3]})

    conn.close()

    return grouped_data


def display_data_in_frame(grouped_data):
    # Create the main window
    root = ctk.CTk()
    root.title("Equipment Logs")
    root.geometry("600x400")

    # Create a scrollable frame
    scrollable_frame = ctk.CTkScrollableFrame(root, width=580, height=380)
    scrollable_frame.pack(pady=10, padx=10, fill="both", expand=True)

    row_counter = 0
    for name, equipment_list in grouped_data.items():
        # Display the name only once for a group
        name_label = ctk.CTkLabel(scrollable_frame, text=name, font=("Arial", 14, "bold"))
        name_label.grid(row=row_counter, column=0, sticky="w", padx=10, pady=5)

        # Display all equipment for the name
        for equipment in equipment_list:
            equipment_label = ctk.CTkLabel(
                scrollable_frame,
                text=f"{equipment['Ename']} ({equipment['Department']})",
                font=("Arial", 12)
            )
            equipment_label.grid(row=row_counter, column=1, sticky="w", padx=10, pady=5)
            row_counter += 1

        # Add a spacer after each group
        row_counter += 1

    root.mainloop()


if __name__ == '__main__':
    data = get_all_data_for_menu()
    display_data_in_frame(data)