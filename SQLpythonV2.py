# importing module
import cx_Oracle
import tkinter.filedialog
import pandas as pd  # Data analysis and manipulation tool
import tkinter as tk  # GUI toolkit
from tkinter import *

# reference for export buttons
filedialog = tkinter.filedialog

# Read the SQL file
query = open('TEST QuickSelect.sql', 'r')

# DB Server information
CONN_INFO = {
    'host': 'vtgv1-vtw.csgsystems.com',
    'port': 1521,
    'user': 'XXXXXXXXX',
    'psw': 'XXXXXXXXX',
    'service': 'vtw.csgsystems.com',
}
CONN_STR = '{user}/{psw}@{host}:{port}/{service}'.format(**CONN_INFO)


# GUI creation ========================================================#
# TK root declaration
window = tk.Tk()

canvas1 = tk.Canvas(window, width=300, height=300, bg='White', relief='raised')
canvas1.pack()
# Create label to display user input
lbl = tk.Label(canvas1, text="Enter a RF MAC Node: ")

# Label Creation
lbl.pack()

# Text box creation
inputtextbox = tk.Text(canvas1, height=3, width=50, padx=10, pady=10)

# Add the text box to the root
inputtextbox.pack(fill=X)


# FUCTIONS ---------------------- #
# =====================================================================#
def exportExcel():
    # global df
    #
    # export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
    # df.to_excel(export_file_path, index=False, header=True)
    # # root.mainloop()
    print("Excel Export Successful")


def exportCSV():
    # global df
    #
    # export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    # df.to_csv(export_file_path, index=False, header=True)
    print("CSV Export Successful")


def addexportButtons():
    saveAsButtonExcel = tk.Button(text='Export as Excel', command=exportExcel, bg='green', fg='white', width=20,
                                  font=('helvetica', 10, 'bold'))
    saveAsButtonCSV = tk.Button(text='Export as CSV', command=exportCSV, bg='green', fg='white', width=20,
                                font=('helvetica', 10, 'bold'))
    # canvas1.create_window(125, 275, window=saveAsButtonExcel)
    # canvas1.create_window(150, 275, window=saveAsButtonCSV)
    saveAsButtonExcel.pack()
    saveAsButtonCSV.pack()


def runquery(nodeinput):
    # Create the connection and execute the query
    try:

        connection = cx_Oracle.connect(CONN_STR)

        cursor = connection.cursor()

        # Now execute the sqlquery
        cursor.execute(query.read())

        # Grab all the rows retured by the query
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        print("Query successful")
        # Now add the export option buttons
        addexportButtons()

    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e)

    # by writing finally if any error occurs
    # then also we can close the all database operation
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# Takes the input and puts it into the input variable, calls the query to be ran
def submitInput():
    input = inputtextbox.get(1.0, "end-1c")
    lbl.config(text="Provided Input: " + input)
    lbl.pack()
    runquery(input)


# Button Creation, when clicked call submitInput
submitButton = tk.Button(window,
                         text="Submit",
                         command=submitInput)
submitButton.pack()

window.mainloop()
