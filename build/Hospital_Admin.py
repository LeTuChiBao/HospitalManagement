from tkinter import *
from tkinter import END
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
from Ket_NoiSQL import MSSQLConnection
class Hospital:
    def __init__(self):

        self.root = Tk()
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
    def mainRoleSuper(self,username):
        self.user = username
        print(self.user)
        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white",
                         font=("time new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # =================Dataframe=====================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1540, height=400)

        DataFrameLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                   font=("time new roman", 12, "bold"), text="Patient Information")
        DataFrameLeft.place(x=2, y=5, width=980, height=350)

        DataFrameRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                    font=("time new roman", 12, "bold"), text="Prescription")
        DataFrameRight.place(x=990, y=5, width=460, height=350)

        # =================== Buttons====================

        ButtonFrame = Frame(self.root, bd=20, relief=RIDGE)
        ButtonFrame.place(x=0, y=530, width=1540, height=70)

        # ===================Details frame ====================

        DetailsFrame = Frame(self.root, bd=20, relief=RIDGE)
        DetailsFrame.place(x=0, y=600, width=1540, height=190)

        # =====================DataFrameLeft======================
        lblNameTable = Label(DataFrameLeft, text="Name OF Table", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNameTable.grid(row=0, column=0)

        self.comNametablet = ttk.Combobox(DataFrameLeft, state="readonly", font=("arial", 12, "bold"),
                                          width=33)

        self.comNametablet["values"] = ("Nice", "Corona Vacacine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        self.comNametablet.grid(row=0, column=1)

        lblref = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Reference No:", padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        self.txtref = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        self.txtref.grid(row=1, column=1)

        lblDose = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Dose", padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        self.txtDose = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        self.txtDose.grid(row=2, column=1)

        lblNoOftablets = Label(DataFrameLeft, font=("arial", 12, "bold"), text="No Of Tablets:", padx=2, pady=6)
        lblNoOftablets.grid(row=3, column=0, sticky=W)
        self.txtNoOftablets = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        self.txtNoOftablets.grid(row=3, column=1)

        lblLot = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Lot:", padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        self.txtLot = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        self.txtLot.grid(row=4, column=1)

        lblissueDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblissueDate.grid(row=5, column=0, sticky=W)
        self.txtissueDate = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        self.txtissueDate.grid(row=5, column=1)

        lblExpDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        self.txtExpDate = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        self.txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Dailly Dose:", padx=2, pady=4)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        self.txtDailyDose = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        self.txtDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        self.txtSideEffect = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        self.txtSideEffect.grid(row=8, column=1)

        lblFurtherInfo = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Further Information:", padx=2)
        lblFurtherInfo.grid(row=0, column=2, sticky=W)
        self.txtFurtherInfo = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
        self.txtFurtherInfo.grid(row=0, column=3)

        lblBloodPressure = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Blood Pressure:", padx=2, pady=6)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        self.txtBloodPressure = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
        self.txtBloodPressure.grid(row=1, column=3)

        lblStorage = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Storage Advice:", padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        self.txtStorage = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
        self.txtStorage.grid(row=2, column=3)

        lblMedicine = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Medication:", padx=2, pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W)
        self.txtMedicine = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
        self.txtMedicine.grid(row=3, column=3)

        lblPatientId = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Id:", padx=2, pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)
        self.txtPatientId = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
        self.txtPatientId.grid(row=4, column=3)

        lblNhsNumber = Label(DataFrameLeft, font=("arial", 12, "bold"), text="NHS Number:", padx=2, pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        self.txtNhsNumber = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
        self.txtNhsNumber.grid(row=5, column=3)

        lblPatientname = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Name:", padx=2, pady=6)
        lblPatientname.grid(row=6, column=2, sticky=W)
        self.txtPatientname = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
        self.txtPatientname.grid(row=6, column=3)

        lblDateOfBirth = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Of Birth:", padx=2, pady=6)
        lblDateOfBirth.grid(row=7, column=2, sticky=W)
        self.txtDateOfBirth = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
        self.txtDateOfBirth.grid(row=7, column=3)

        lblPatientAddress = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Address:", padx=2, pady=6)
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        self.txtPatientAddress = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
        self.txtPatientAddress.grid(row=8, column=3)

        # ===============================DataFrameRight==========================
        self.txtPrescription = Text(DataFrameRight, font=("arial", 12, "bold"), width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # ================================Buttons===========================

        btnPrescription = Button(ButtonFrame, text="Presciption", bg="green", fg="white", font=("arial", 12, "bold"),
                                 width=23, padx=2, pady=6, command=self.iPrescription)
        btnPrescription.grid(row=0, column=0, padx=4)

        btnPrescriptionData = Button(ButtonFrame, text="Presciption Data", bg="green", fg="white",
                                     font=("arial", 12, "bold"), width=23, padx=2, pady=6,
                                     command=self.iPrescriptionData)
        btnPrescriptionData.grid(row=0, column=1, padx=4)

        btnUpdate = Button(ButtonFrame, text="Update", bg="green", fg="white", font=("arial", 12, "bold"), width=23,
                           padx=2, pady=6, command=self.Update)
        btnUpdate.grid(row=0, column=2, padx=4)

        btnClear = Button(ButtonFrame, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"), width=23,
                          padx=2, pady=6, command=self.iclear)
        btnClear.grid(row=0, column=3, padx=4)

        btnDelete = Button(ButtonFrame, text="Delete", bg="green", fg="white", font=("arial", 12, "bold"), width=23,
                           padx=2, pady=6, command=self.idelete)
        btnDelete.grid(row=0, column=4, padx=4)

        btnExit = Button(ButtonFrame, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2,
                         pady=6, command=self.iExit)
        btnExit.grid(row=0, column=5, padx=4)

        # =================================Scrollbar========================

        # Create horizontal and vertical scrollbars
        scroll_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)
        # Create Treeview widget
        self.hospital_table = ttk.Treeview(DetailsFrame, columns=(
        "nameofablets", "ref", "dose", "nooftablets", "lot", "issuedate", "expdate", "dailydose", "storage",
        "nhsnumber", "pname", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        # Pack the scrollbars
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Configure scrollbars
        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("nameofablets", text="Name Of Tablets")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No Of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"] = "headings"
        self.hospital_table.pack(fill=BOTH, expand=1)

        for col in ("nameofablets", "ref", "dose", "nooftablets", "lot", "issuedate", "expdate", "dailydose", "storage",
                    "nhsnumber", "pname", "dob", "address"):
            self.hospital_table.column(col, width=100)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fatch_data()

        self.root.mainloop()
        # ======================Functinality Declration=====================

    def iPrescriptionData(self):
        if self.comNametablet.get()=="" or self.txtref.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                SqlSever = MSSQLConnection()
                SqlSever.connect()
                Query1 = ('INSERT INTO hospital (Nameoftablets , Reference_No , dose ,Numbersoftablets, lot, issuedate, expdate,dailydose,storage,nhsnumber ,patientname ,DOB ,patientaddress ) VALUES '
                              '(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)')
                # Query1 = ('INSERT INTO hospital VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)')
                values =(
                    self.comNametablet.get(),
                    self.txtref.get(),self.txtDose.get(),
                    self.txtNoOftablets.get(),
                    self.txtLot.get(),
                    self.txtissueDate.get(),
                    self.txtExpDate.get(),
                    self.txtDailyDose.get(),
                    self.txtStorage.get(),
                    self.txtNhsNumber.get(),
                    self.txtPatientname.get(),
                    self.txtDateOfBirth.get(),
                    self.txtPatientAddress.get())
                SqlSever.insert(Query1, values)
                self.fatch_data()
                # messagebox.showinfo("Success", "Create Success")
            except Exception as e:
                messagebox.showerror("Error",f"Error: {e}")
            finally:
                SqlSever.close()
                self.fatch_data()
                self.iclear()

    def Update(self):
        if self.comNametablet.get() == "" or self.txtref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                SqlSever = MSSQLConnection()
                SqlSever.connect()
                Query1 = (
                    'UPDATE hospital SET Nameoftablets= ? , dose=? ,Numbersoftablets= ?, lot= ?, issuedate= ?, expdate = ?,dailydose= ?,storage= ?,nhsnumber= ? ,patientname= ? ,DOB= ? ,patientaddress= ? '
                    'WHERE Reference_No = ?'
                    )
                # Query1 = ('INSERT INTO hospital VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)')
                values = (
                    self.comNametablet.get(),
                    self.txtDose.get(),
                    self.txtNoOftablets.get(),
                    self.txtLot.get(),
                    self.txtissueDate.get(),
                    self.txtExpDate.get(),
                    self.txtDailyDose.get(),
                    self.txtStorage.get(),
                    self.txtNhsNumber.get(),
                    self.txtPatientname.get(),
                    self.txtDateOfBirth.get(),
                    self.txtPatientAddress.get(),
                    self.txtref.get(),
                )
                SqlSever.update(Query1, values)
                messagebox.showinfo("Success", "Update Success")
            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}")
            finally:
                SqlSever.close()
                self.fatch_data()
                self.iclear()
    def fatch_data(self):
        try:
            SqlSever = MSSQLConnection()
            SqlSever.connect()
            Query1 = ('SELECT * FROM hospital ')
            rows = SqlSever.query(Query1)
            if len(rows)!=0:
                self.hospital_table.delete(*self.hospital_table.get_children())
                for i in rows:
                    formatted_values = [str(value).strip("'") for value in i]
                    self.hospital_table.insert("",END,values=formatted_values)

            print("Fatch Success")
        except Exception as e:
            messagebox.showerror(f"Error: {e}")
        finally:
            SqlSever.close()

    def get_cursor(self):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]

        self.comNametablet.delete(0, END)
        self.txtref.delete(0, END)
        self.txtDose.delete(0, END)
        self.txtNoOftablets.delete(0, END)
        self.txtLot.delete(0, END)
        self.txtissueDate.delete(0, END)
        self.txtExpDate.delete(0, END)
        self.txtDailyDose.delete(0, END)
        self.txtStorage.delete(0, END)
        self.txtNhsNumber.delete(0, END)
        self.txtPatientname.delete(0, END)
        self.txtDateOfBirth.delete(0, END)
        self.txtPatientAddress.delete(0, END)

        # Insert values into entry widgets
        self.comNametablet.set(row[0])
        self.txtref.insert(0, row[1])
        # self.txtref.config(state=DISABLED)
        self.txtDose.insert(0, row[2])
        self.txtNoOftablets.insert(0, row[3])
        self.txtLot.insert(0, row[4])
        self.txtissueDate.insert(0, row[5])
        self.txtExpDate.insert(0, row[6])
        self.txtDailyDose.insert(0, row[7])
        self.txtStorage.insert(0, row[8])
        self.txtNhsNumber.insert(0, row[9])
        self.txtPatientname.insert(0, row[10])
        self.txtDateOfBirth.insert(0, row[11])
        self.txtPatientAddress.insert(0, row[12])

    def iPrescription(self):
        if self.comNametablet.get() and self.txtref.get():
            self.txtPrescription.delete('1.0', 'end')

        self.txtPrescription.insert(END,"Name Of Tablets :\t\t\t"+self.comNametablet.get()+"\n")
        self.txtPrescription.insert(END, "Reference No :\t\t\t" + self.txtref.get() + "\n")
        self.txtPrescription.insert(END, "Dose :\t\t\t" + self.txtDose.get() + "\n")
        self.txtPrescription.insert(END, "Number Of Tablets :\t\t\t" + self.txtNoOftablets.get() + "\n")
        self.txtPrescription.insert(END, "Lot :\t\t\t" + self.txtLot.get() + "\n")
        self.txtPrescription.insert(END, "Issue Date :\t\t\t" + self.txtissueDate.get() + "\n")
        self.txtPrescription.insert(END, "Exp Date :\t\t\t" + self.txtExpDate.get() + "\n")
        self.txtPrescription.insert(END,"Daily Dose :\t\t\t"+self.txtDailyDose.get()+"\n")
        self.txtPrescription.insert(END, "Side Effect :\t\t\t" + self.txtSideEffect.get() + "\n")
        self.txtPrescription.insert(END, "Funther Information :\t\t\t" + self.txtFurtherInfo.get() + "\n")
        self.txtPrescription.insert(END, "Blood Pressure :\t\t\t" + self.txtBloodPressure.get() + "\n")
        self.txtPrescription.insert(END, "Store Advice :\t\t\t" + self.txtStorage.get() + "\n")
        self.txtPrescription.insert(END, "Medicaion :\t\t\t" + self.txtMedicine.get() + "\n")
        self.txtPrescription.insert(END, "Patient Id :\t\t\t" + self.txtPatientId.get() + "\n")
        self.txtPrescription.insert(END, "NHS Number :\t\t\t" + self.txtNhsNumber.get() + "\n")
        self.txtPrescription.insert(END, "Patient Name :\t\t\t" + self.txtPatientname.get() + "\n")
        self.txtPrescription.insert(END, "Date Of Birth :\t\t\t" + self.txtDateOfBirth.get() + "\n")
        self.txtPrescription.insert(END, "Patient Address :\t\t\t" + self.txtPatientAddress.get() + "\n")



    def idelete(self):

        if self.txtref.get() == "":
            messagebox.showerror("Error", "Reference No is required")
        else:
            iExit = messagebox.askyesno("Hospital Management System",
                                           f"Confirm you want to delete this Prescription: \n\t {self.comNametablet.get()} : {self.txtref.get()}")
            if iExit > 0:
                try:
                    SqlSever = MSSQLConnection()
                    SqlSever.connect()
                    Query1 = 'DELETE FROM hospital WHERE Reference_No = ?'
                    values = self.txtref.get()
                    SqlSever.delete(Query1, values)
                    messagebox.showinfo("Success", "DELETE Success")
                except Exception as e:
                    messagebox.showerror("Error", f"Error: {e}")
                finally:
                    SqlSever.close()
                    self.fatch_data()
                    self.iclear()
    def iclear(self):
        self.txtref.config(state=NORMAL)
        self.comNametablet.set("")
        self.txtref.delete(0, END)
        self.txtDose.delete(0, END)
        self.txtNoOftablets.delete(0, END)
        self.txtLot.delete(0, END)
        self.txtissueDate.delete(0, END)
        self.txtExpDate.delete(0, END)
        self.txtDailyDose.delete(0, END)
        self.txtSideEffect.delete(0, END)
        self.txtFurtherInfo.delete(0, END)
        self.txtBloodPressure.delete(0, END)
        self.txtStorage.delete(0, END)
        self.txtMedicine.delete(0, END)
        self.txtPatientId.delete(0, END)
        self.txtNhsNumber.delete(0, END)
        self.txtPatientname.delete(0, END)
        self.txtDateOfBirth.delete(0, END)
        self.txtPatientAddress.delete(0, END)
        self.txtPrescription.delete('1.0', 'end')

    def iExit(self):
        iExit = messagebox.askyesno("Hospital Management System","Confirm you want to exit")
        if iExit > 0:
            self.root.destroy()
            return

if __name__ == '__main__':
    a = Hospital()
    a.mainRoleSuper('Super')