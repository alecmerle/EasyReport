import tkinter.filedialog
#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import create_engine
import pandas as pd  # Data analysis and manipulation tool
import tkinter as tk  # GUI toolkit
from tkinter import *

# reference for export buttons
filedialog = tkinter.filedialog

# Read the SQL file
query = open('Queries/RF MAC Node Query TWC.SQL', 'r')

# DB Server information
DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'
USERNAME = 'XXXXXXX'  # enter your username
PASSWORD = 'XXXXXXX'  # enter your password
HOST = 'vtgv1-vtw.csgsystems.com'  # enter the oracle db host url
PORT = 1521  # enter the oracle port number
SERVICE = 'vtw.csgsystems.com'  # enter the oracle db service name

ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD + '@' + HOST + ':' + \
                       str(PORT) + '/?service_name=' + SERVICE

engine = create_engine(ENGINE_PATH_WIN_AUTH)

# TK root declaration
root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300, bg='White', relief='raised')
canvas1.pack()
# Create label to display user input
lbl = tk.Label(canvas1, text="Enter a RF MAC Node: ")

# Label Creation
lbl.pack()

# Text box creation
inputtxtbox = tk.Text(canvas1, height=3, width=50, padx=10, pady=10)

# Add the text box to the root
inputtxtbox.pack(fill=X)


# test query
# pandas, dataframe
def runquery(nodeinput):
    global df
    df = pd.read_sql_query(query.read().replace('*NODEVARIABLE*', nodeinput), engine)
    # root.mainloop()


def exportExcel():
    global df

    export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
    df.to_excel(export_file_path, index=False, header=True)
    # root.mainloop()


def exportCSV():
    global df

    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    df.to_csv(export_file_path, index=False, header=True)


def addexportButtons():
    saveAsButtonExcel = tk.Button(text='Export as Excel', command=exportExcel, bg='green', fg='white', width=20,
                                  font=('helvetica', 10, 'bold'))
    saveAsButtonCSV = tk.Button(text='Export as CSV', command=exportCSV, bg='green', fg='white', width=20,
                                font=('helvetica', 10, 'bold'))
    # canvas1.create_window(125, 275, window=saveAsButtonExcel)
    # canvas1.create_window(150, 275, window=saveAsButtonCSV)
    saveAsButtonExcel.pack()
    saveAsButtonCSV.pack()


# Takes the input and puts it into the input variable,
def submitInput():
    input = inputtxtbox.get(1.0, "end-1c")
    lbl.config(text="Provided Input: " + input)
    lbl.pack()
    runquery(input)
    addexportButtons()


# Button Creation, when clicked call submitInput
submitButton = tk.Button(root,
                         text="Submit",
                         command=submitInput)
submitButton.pack()

root.mainloop()
