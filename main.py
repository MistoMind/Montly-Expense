import sheet_api
from initialisation import *
from tkinter import *

# Handle Null Persons in NON Contributors

HEADING_FONT = ("Arial", 19, "bold")


def generate_report():
    data = pd.DataFrame(sheet_api.get_data_sheet())

    persons = create_people()

    calculate_spending_all(persons, data)
    calculate_give_take(persons, data)

    for i in range(0, len(persons)):
        temp_name = Label(text=persons[i].name)
        temp_name.grid(column=0, row=i + 1)
        temp_spend = Label(text=f"{persons[i].spend}")
        temp_spend.grid(column=1, row=i + 1)
        if (persons[i].spend - persons[i].give) < 0:
            give_take = "Give"
        else:
            give_take = "Take"
        temp_give_take = Label(text=f"{give_take} {persons[i].spend-round(persons[i].give)}")
        temp_give_take.grid(column=2, row=i + 1)


window = Tk()
window.title("Month Expense Report")
window.config(padx=40, pady=40)

name_label = Label(text="Name")
name_label.grid(column=0, row=0)
name_label.config(font=HEADING_FONT)
spend_label = Label(text="Spend")
spend_label.grid(column=1, row=0)
spend_label.config(font=HEADING_FONT)
give_take_label = Label(text="Give/Take")
give_take_label.grid(column=2, row=0)
give_take_label.config(font=HEADING_FONT)
generate_button = Button(text="Generate Report", command=generate_report)
generate_button.grid(column=1, row=5)

window.mainloop()
