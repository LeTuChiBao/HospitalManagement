from tkinter import *
from tkinter import END
from tkinter import ttk
from tkinter import PhotoImage
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
from Ket_NoiSQL import MSSQLConnection
from PIL import Image, ImageTk
import os
class Hospital:
    def __init__(self):

        self.root = Tk()
        self.root.title("Hospital Management System")
        self.root.geometry("1900x1080+0+0")



    def mainRoleAdmin(self,username):
        self.user = username
        try:
            original_image = Image.open(r'C:\Users\bao.le\Pycode\Do_An\image\admin.png')
            original_image1 = Image.open(r'C:\Users\bao.le\Pycode\Do_An\image\admin.png')
        except Exception as e:
            print(f"Error opening image: {e}")
            raise  # Raising the exception again to stop further execution

        resized_image = original_image.resize((60, 60), Image.LANCZOS)
        self.logout_icon = ImageTk.PhotoImage(resized_image)

        resized_image1 = original_image1.resize((300, 300), Image.LANCZOS)
        self.main_icon = ImageTk.PhotoImage(resized_image1)


        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="Green", bg="white",
                         font=("time new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        img_label = Label(lbltitle, text=f"{self.user.upper()} ", image=self.logout_icon,
                          compound="right", bg="white", fg="GoldenRod", font=("Arial", 20, "bold"), padx=2, pady=6)
        img_label.pack(side=RIGHT)
        # =================Dataframe=====================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1900, height=850)

        DataMedicine = LabelFrame(Dataframe, bd=4, relief=RAISED, padx=5,
                                   font=("time new roman", 12, "bold"), text="Medicine Information")
        DataMedicine.place(x=10, y=5, width=710, height=350)

        DataPatients = LabelFrame(Dataframe, bd=4, relief=RAISED, padx=5,
                                   font=("time new roman", 12, "bold"), text="Patient Information")
        DataPatients.place(x=1140, y=5, width=710, height=350)

        DataFrameRight = LabelFrame(Dataframe, bd=4, relief=FLAT, padx=5,
                                    font=("time new roman", 12, "bold"))
        DataFrameRight.place(x=730, y=5, width=400, height=350)

        image_label = Label(DataFrameRight, image=self.main_icon, bd=20 )
        image_label.place(x=15, y=10)

        # =================== Buttons====================
        
        ButtonMedicineFrame = LabelFrame(Dataframe, bd=6, relief=RAISED,padx=10, font=("time new roman", 12, "bold"))
        ButtonMedicineFrame.place(x=10, y=360, width=710, height=60)

        ButtonPatientFrame = LabelFrame(Dataframe, bd=6, relief=RAISED,padx=10, font=("time new roman", 12, "bold"))
        ButtonPatientFrame.place(x=1140, y=360, width=710, height=60)

        # ===================Patients List frame ====================

        PatientListFrame = LabelFrame(Dataframe, bd=4, relief=RIDGE, font=("time new roman", 12, "bold"), text="Patient List")
        PatientListFrame.place(x=940, y=420, width=920, height=360)

        # ===================Medicine List  frame ====================

        MedicineListFrame = LabelFrame(Dataframe, bd=4, relief=RIDGE, font=("time new roman", 12, "bold"), text="Medicine List")
        MedicineListFrame.place(x=0, y=420, width=930, height=360)

        # =====================DataMedicine======================

        medicineNo = Label(DataMedicine, font=("arial", 12, "bold"), text="Medicine No:", padx=20,pady=10)
        medicineNo.grid(row=0, column=0, sticky=W)
        self.txtMedicineNo = Entry(DataMedicine, font=("arial", 13, "bold"), width=40)
        self.txtMedicineNo.grid(row=0, column=1, sticky=W)

        medicineType= Label(DataMedicine, text="Type Of Medicine:", font=("arial", 12, "bold"),  padx=20,pady=10)
        medicineType.grid(row=1, column=0, sticky=W)

        self.medicineType = ttk.Combobox(DataMedicine, state="readonly", font=("arial", 12, "bold"), width=50)
        self.medicineType["values"] = ("tablet", "injection")
        self.medicineType.grid(row=1, column=1, sticky=W)

        medicineName = Label(DataMedicine, font=("arial", 12, "bold"), text="Medicine Name:", padx=20,pady=10 )
        medicineName.grid(row=2, column=0, sticky=W)
        self.medicineName =ttk.Combobox(DataMedicine, state="readonly", font=("arial", 12, "bold"), width=50)
        self.medicineName["values"] = ("Vitamin A", "VitaMmin B","VitaMmin D","Acetsminophen","DM","Panadol","Cipla","Novel","Absorica")
        self.medicineName.grid(row=2, column=1, sticky=W)

        lblLot = Label(DataMedicine, font=("arial", 12, "bold"), text="Lot No:", padx=20,pady=10)
        lblLot.grid(row=3, column=0, sticky=W)
        self.txtLot = Entry(DataMedicine, font=("arial", 13, "bold"), width=52)
        self.txtLot.grid(row=3, column=1, sticky=W)

        lblissueDate = Label(DataMedicine, font=("arial", 12, "bold"), text="Issue Date:",  padx=20,pady=10)
        lblissueDate.grid(row=4, column=0, sticky=W)
        self.txtissueDate = Entry(DataMedicine, font=("arial", 13, "bold"), width=52)
        self.txtissueDate.grid(row=4, column=1, sticky=W)

        lblExpDate = Label(DataMedicine, font=("arial", 12, "bold"), text="Exp Date:",  padx=20,pady=10)
        lblExpDate.grid(row=5, column=0, sticky=W)
        self.txtExpDate = Entry(DataMedicine, font=("arial", 13, "bold"), width=52)
        self.txtExpDate.grid(row=5, column=1, sticky=W)

        lblSideEffect = Label(DataMedicine, font=("arial", 12, "bold"), text="Side Effect:",  padx=20,pady=10)
        lblSideEffect.grid(row=6, column=0, sticky=W)
        self.txtSideEffect = Entry(DataMedicine, font=("arial", 13, "bold"), width=52)
        self.txtSideEffect.grid(row=6, column=1, sticky=W)


        # -------------Data Patients---------------

        lblPatientId = Label(DataPatients, font=("arial", 12, "bold"), text="Patient Id:", padx=20,pady=10)
        lblPatientId.grid(row=0, column=0, sticky=W)
        self.txtPatientId = Entry(DataPatients, font=("arial", 12, "bold"), width=40)
        self.txtPatientId.grid(row=0, column=1, sticky=W)

        
        lblPatientPass = Label(DataPatients, font=("arial", 12, "bold"), text="Patient Password:", padx=20,pady=10)
        lblPatientPass.grid(row=1, column=0, sticky=W)
        self.txtPatientPass = Entry(DataPatients, font=("arial", 12, "bold"),  width=52)
        self.txtPatientPass.grid(row=1, column=1, sticky=W)

        lblNhsNumber = Label(DataPatients, font=("arial", 12, "bold"), text="Phone Number:", padx=20,pady=10)
        lblNhsNumber.grid(row=2, column=0, sticky=W)
        self.txtPhoneNumber = Entry(DataPatients, font=("arial", 12, "bold"),  width=52)
        self.txtPhoneNumber.grid(row=2, column=1, sticky=W)

        lblPatientname = Label(DataPatients, font=("arial", 12, "bold"), text="Patient Name:", padx=20,pady=10)
        lblPatientname.grid(row=3, column=0, sticky=W)
        self.txtPatientname = Entry(DataPatients, font=("arial", 12, "bold"),  width=52)
        self.txtPatientname.grid(row=3, column=1, sticky=W)

        lblDateOfBirth = Label(DataPatients, font=("arial", 12, "bold"), text="Date Of Birth:", padx=20,pady=10)
        lblDateOfBirth.grid(row=4, column=0, sticky=W)
        self.txtDateOfBirth = Entry(DataPatients, font=("arial", 12, "bold"),  width=52)
        self.txtDateOfBirth.grid(row=4, column=1, sticky=W)

        lblPatientAddress = Label(DataPatients, font=("arial", 12, "bold"), text="Patient Address:", padx=20,pady=10)
        lblPatientAddress.grid(row=5, column=0, sticky=W)
        self.txtPatientAddress = Entry(DataPatients, font=("arial", 12, "bold"),  width=52)
        self.txtPatientAddress.grid(row=5, column=1, sticky=W)

        userRole = Label(DataPatients, font=("arial", 12, "bold"), text="Role:", padx=20,pady=10)
        userRole.grid(row=6, column=0, sticky=W)
        self.txtuserRole =ttk.Combobox(DataPatients, state="readonly", font=("arial", 12, "bold"), width=50)
        self.txtuserRole["values"] = ("Admin", "Agent")
        self.txtuserRole.grid(row=6, column=1, sticky=W)


        # ================================Buttons Presciption===========================


        btnExit = Button(Dataframe, text="Logout", bg="gray", fg="white", font=("arial", 12, "bold"), width=29, padx=2,
                         pady=6, command=self.iLogout)
        btnExit.place(x=780, y=330, width=300, height=60)


        # ================================Buttons ButtonMedicineFrame===========================

        btnMedicineSearch = Button(DataMedicine, text="Search", bg="green", fg="white",
                                     font=("arial", 12, "bold"), width=8, padx=2,command=self.Medicine_search_and_select_row)
        btnMedicineSearch.grid(row=0, column=1, sticky=E)

        btnMedicineCreate = Button(ButtonMedicineFrame, text="Create", bg="green", fg="white",
                                     font=("arial", 12, "bold"), width=20, padx=2, pady=6, command=self.iMedicine_Create)
        btnMedicineCreate.grid(row=0, column=0, padx=6)

        btnMedicineUpdate = Button(ButtonMedicineFrame, text="Update", bg="blue", fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6 , command=self.iUpdate_Medicine)
        btnMedicineUpdate.grid(row=0, column=1, padx=6)

        btnMedicineDelete = Button(ButtonMedicineFrame, text="Delete", bg="red", fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6 , command=self.idelete_Medicine)
        btnMedicineDelete.grid(row=0, column=2, padx=6)

        # ================================Buttons ButtonPatientFrame===========================
        btnPatientSearch = Button(DataPatients, text="Search", bg="green", fg="white",
                                     font=("arial", 12, "bold"), width=8, padx=2, command=self.Patient_search_and_select_row)
        btnPatientSearch.grid(row=0, column=1, sticky=E)

        btnPatientCreate = Button(ButtonPatientFrame, text="Create", bg="green", fg="white",
                                     font=("arial", 12, "bold"), width=20, padx=2, pady=6 ,command=self.iPatient_Create)
        btnPatientCreate.grid(row=0, column=0, padx=6)

        btnPatientUpdate = Button(ButtonPatientFrame, text="Update", bg="blue", fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6 ,command=self.iUpdate_Patient)
        btnPatientUpdate.grid(row=0, column=1, padx=6)

        btnPatientDelete = Button(ButtonPatientFrame, text="Delete", bg="red", fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6 ,command=self.idelete_Patient)
        btnPatientDelete = Button(ButtonPatientFrame, text="Delete", bg="red", fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6 ,command=self.idelete_Patient)
        btnPatientDelete.grid(row=0, column=2, padx=6)


        # =================================Scrollbar MedicineListFrame========================

        # Create horizontal and vertical scrollbars
        scroll_x = ttk.Scrollbar(MedicineListFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(MedicineListFrame, orient=VERTICAL)
        # Create Treeview widget
        self.MedicineListTable = ttk.Treeview(MedicineListFrame, columns=(
            "medicineno", "typeofmedicine", "medicinename", "lotno", "issuedate", "expdate" ,"side"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        # Pack the scrollbars
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Configure scrollbars
        scroll_x.config(command=self.MedicineListTable.xview)
        scroll_y.config(command=self.MedicineListTable.yview)

        self.MedicineListTable.heading("medicineno", text="Medicine No")
        self.MedicineListTable.heading("typeofmedicine", text="Type Of Medicine")
        self.MedicineListTable.heading("medicinename", text="Medicine Name")
        self.MedicineListTable.heading("lotno", text="Lot No")
        self.MedicineListTable.heading("issuedate", text="Issue Date")
        self.MedicineListTable.heading("expdate", text="Exp Date")
        self.MedicineListTable.heading("side", text="Side Effect")

        self.MedicineListTable["show"] = "headings"
        self.MedicineListTable.pack(fill=BOTH, expand=1)

        for col in ( "medicineno", "typeofmedicine", "medicinename", "lotno", "issuedate", "expdate" ,"side"):
            self.MedicineListTable.column(col, width=100)
        self.MedicineListTable.bind("<ButtonRelease-1>", self.get_cursor_medicine_list)
        self.fatch_data_medicine_list()
        # =================================Scrollbar PatientListFrame========================

        # Create horizontal and vertical scrollbars
        scroll_x = ttk.Scrollbar(PatientListFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(PatientListFrame, orient=VERTICAL)
        # Create Treeview widget
        self.PatientListTable = ttk.Treeview(PatientListFrame, columns=(
            "username", "userpassword", "fullname", "adress", "birth", "phone", "userrole"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        # Pack the scrollbars
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Configure scrollbars
        scroll_x.config(command=self.PatientListTable.xview)
        scroll_y.config(command=self.PatientListTable.yview)

        self.PatientListTable.heading("username", text="User Name")
        self.PatientListTable.heading("userpassword", text="Password")
        self.PatientListTable.heading("fullname", text="Full Name")
        self.PatientListTable.heading("adress", text="Adress")
        self.PatientListTable.heading("birth", text="Day of Birth")
        self.PatientListTable.heading("phone", text="Phone")
        self.PatientListTable.heading("userrole", text="Role")

        self.PatientListTable["show"] = "headings"
        self.PatientListTable.pack(fill=BOTH, expand=1)

        for col in ("username", "userpassword", "fullname", "adress", "birth", "phone", "userrole"):
            self.PatientListTable.column(col, width=100)
        self.PatientListTable.bind("<ButtonRelease-1>", self.get_cursor_patient_list)
        self.fatch_data_patient_list()

        self.root.mainloop()

        # ======================Functinality Declration=====================

    def iMedicine_Create(self):
        if self.medicineType.get()=="" or self.txtMedicineNo.get()==""or self.medicineName.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                SqlSever = MSSQLConnection()
                SqlSever.connect()
                Query1 = ('INSERT INTO medicines (medicineno, typeofmedicine, medicinename, lotno, issuedate, expdate ,side) VALUES (?,?,?,?,?,?,?)')
                values =(
                    self.txtMedicineNo.get(),
                    self.medicineType.get(),
                    self.medicineName.get(),
                    self.txtLot.get(),
                    self.txtissueDate.get(),
                    self.txtExpDate.get(),
                    self.txtSideEffect.get())
                SqlSever.insert(Query1, values)
                messagebox.showinfo("Prescription", "Create Success")
            except Exception as e:
                messagebox.showerror("Error",f"Error: {e}")
            finally:
                SqlSever.close()
                self.fatch_data_medicine_list()
                self.iclear_medicine()

    def iPatient_Create(self):
        if self.txtPatientId.get() == "" or self.txtPatientname.get() == "" or self.txtPhoneNumber.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                SqlSever = MSSQLConnection()
                SqlSever.connect()
                Query1 = ( 'INSERT INTO users (username, userpassword, fullname, adress, birth, phone ,userrole) VALUES (?,?,?,?,?,?,?)')
                values = (
                    self.txtPatientId.get(),
                    self.txtPatientPass.get(),
                    self.txtPatientname.get(),
                    self.txtPatientAddress.get(),
                    self.txtDateOfBirth.get(),
                    self.txtPhoneNumber.get(),
                    self.txtuserRole.get())
                SqlSever.insert(Query1, values)
                messagebox.showinfo("Patient", "Create Success")
            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}")
            finally:
                SqlSever.close()
                self.fatch_data_patient_list()
                self.iclear_patient()


    def iUpdate_Medicine(self):
        if self.medicineType.get()=="" or self.txtMedicineNo.get()==""or self.medicineName.get()=="":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                SqlSever = MSSQLConnection()
                SqlSever.connect()
                Query1 = (
                    'UPDATE medicines SET typeofmedicine = ?, medicinename = ?, lotno = ?, issuedate = ?, expdate = ?, side = ? where medicineno = ? '
                )
                values = (
                    self.medicineType.get(),
                    self.medicineName.get(),
                    self.txtLot.get(),
                    self.txtissueDate.get(),
                    self.txtExpDate.get(),
                    self.txtSideEffect.get(),
                    self.txtMedicineNo.get()
                )

                SqlSever.update(Query1, values)
                messagebox.showinfo("Medicine", "Update Medicine Success")
            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}")
            finally:
                SqlSever.close()
                self.fatch_data_medicine_list()
                self.iclear_medicine()

    def iUpdate_Patient(self):
        if self.txtPatientId.get()=="" or self.txtPatientname.get()==""or self.txtPhoneNumber.get()=="":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                SqlSever = MSSQLConnection()
                SqlSever.connect()
                Query1 = (
                    'UPDATE users SET userpassword = ?, fullname = ?, adress = ?, birth = ?, phone = ?, userrole = ? WHERE username = ? '
                )
                values = (
                    self.txtPatientPass.get(),
                    self.txtPatientname.get(),
                    self.txtPatientAddress.get(),
                    self.txtDateOfBirth.get(),
                    self.txtPhoneNumber.get(),
                    self.txtuserRole.get(),
                    self.txtPatientId.get()
                )

                SqlSever.update(Query1, values)
                messagebox.showinfo("Patient", "Update Patient Success")
            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}")
            finally:
                SqlSever.close()
                self.fatch_data_patient_list()
                self.iclear_patient()
    def fatch_data_medicine_list(self):
        try:
            SqlSever = MSSQLConnection()
            SqlSever.connect()
            Query1 = ('SELECT * FROM medicines ')
            rows = SqlSever.query(Query1)
            if len(rows)!=0:
                self.MedicineListTable.delete(*self.MedicineListTable.get_children())
                for i in rows:
                    formatted_values = [str(value).strip("'") for value in i]
                    self.MedicineListTable.insert("",END,values=formatted_values)

            print("Fatch Success")
        except Exception as e:
            messagebox.showerror(f"Error: {e}")
        finally:
            SqlSever.close()
    def fatch_data_patient_list(self):
        try:
            SqlSever = MSSQLConnection()
            SqlSever.connect()
            Query1 = ("SELECT * FROM users WHERE userrole <> 'Super'")
            rows = SqlSever.query(Query1)
            if len(rows)!=0:
                self.PatientListTable.delete(*self.PatientListTable.get_children())
                for i in rows:
                    formatted_values = [str(value).strip("'") for value in i]
                    self.PatientListTable.insert("",END,values=formatted_values)

            print("Fatch Success")
        except Exception as e:
            messagebox.showerror(f"Error: {e}")
        finally:
            SqlSever.close()

    def get_cursor_medicine_list(self, event):
        cursor_row = self.MedicineListTable.focus()
        content = self.MedicineListTable.item(cursor_row)
        row = content["values"]

        self.txtMedicineNo.delete(0, END)
        self.medicineType.delete(0, END)
        self.medicineName.delete(0, END)
        self.txtLot.delete(0, END)
        self.txtissueDate.delete(0, END)
        self.txtExpDate.delete(0, END)
        self.txtSideEffect.delete(0, END)

        # Insert values into entry widgets
        self.txtMedicineNo.insert(0, row[0])
        self.medicineType.set(row[1])
        self.medicineName.set(row[2])
        self.txtLot.insert(0, row[3])
        self.txtissueDate.insert(0, row[4])
        self.txtExpDate.insert(0, row[5])
        self.txtSideEffect.insert(0, row[6])

    def get_cursor_patient_list(self, event):
        cursor_row = self.PatientListTable.focus()
        content = self.PatientListTable.item(cursor_row)
        row = content["values"]

        self.txtPatientId.delete(0, END)
        self.txtPatientPass.delete(0, END)
        self.txtPhoneNumber.delete(0, END)
        self.txtPatientname.delete(0, END)
        self.txtDateOfBirth.delete(0, END)
        self.txtPatientAddress.delete(0, END)
        self.txtuserRole.delete(0, END)

        # Insert values into entry widgets
        self.txtPatientId.insert(0, row[0])
        self.txtPatientPass.insert(0, row[1])
        self.txtPhoneNumber.insert(0, row[5])
        self.txtPatientname.insert(0, row[2])
        self.txtDateOfBirth.insert(0, row[4])
        self.txtPatientAddress.insert(0, row[3])
        self.txtuserRole.set( row[6])


    def idelete_Medicine(self):

        if self.txtMedicineNo.get() == "":
            messagebox.showerror("Error", "Reference No is required")
        else:
            iLogout = messagebox.askyesno("Delete Medicine",
                                           f"Confirm you want to delete this Medicine: \n\t {self.medicineName.get().upper()} : {self.txtMedicineNo.get().upper()}")
            if iLogout > 0:
                try:
                    SqlSever = MSSQLConnection()
                    SqlSever.connect()
                    Query1 = 'DELETE FROM medicines WHERE medicineno = ?'
                    values = self.txtMedicineNo.get()
                    SqlSever.delete(Query1, values)
                    messagebox.showinfo("Medicine", "DELETE Success")
                except Exception as e:
                    messagebox.showerror("Error", f"Error: {e}")
                finally:
                    SqlSever.close()
                    self.fatch_data_medicine_list()
                    self.iclear_medicine()

    def idelete_Patient(self):

        if self.txtPatientId.get() == "":
            messagebox.showerror("Error", "Patient ID is required")
        else:
            iLogout = messagebox.askyesno("Delete Patient",
                                           f"Confirm you want to delete this Patient: \n\t {self.txtPatientId.get().upper()}")
            if iLogout > 0:
                try:
                    SqlSever = MSSQLConnection()
                    SqlSever.connect()
                    Query1 = 'DELETE FROM users WHERE username = ?'
                    values = self.txtPatientId.get()
                    SqlSever.delete(Query1, values)
                    messagebox.showinfo("Patient", "DELETE Success")
                except Exception as e:
                    messagebox.showerror("Error", f"Error: {e}")
                finally:
                    SqlSever.close()
                    self.fatch_data_patient_list()
                    self.iclear_patient()

    def iclear_medicine(self):
        self.txtMedicineNo.delete(0, END)
        self.medicineType.set("")
        self.medicineName.set("")
        self.txtLot.delete(0, END)
        self.txtissueDate.delete(0, END)
        self.txtExpDate.delete(0, END)
        self.txtSideEffect.delete(0, END)

    def iclear_patient(self):
        self.txtPatientId.delete(0, END)
        self.txtPatientPass.delete(0, END)
        self.txtPhoneNumber.delete(0, END)
        self.txtPatientname.delete(0, END)
        self.txtDateOfBirth.delete(0, END)
        self.txtPatientAddress.delete(0, END)
        self.txtuserRole.set("")

    def Medicine_search_and_select_row(self):
        if (self.txtMedicineNo.get() != ""):
            medicineNo = str(self.txtMedicineNo.get())
            search_value = medicineNo
            check = 0

            for child in self.MedicineListTable.get_children():
                values = self.MedicineListTable.item(child, 'values')

                if search_value in values:
                    check+=1
                    print(search_value,values)
                    # Select the row
                    self.MedicineListTable.selection_set(child)

                    # Focus on the selected row
                    self.MedicineListTable.focus(child)

                    # Scroll to make the selected row visible
                    self.MedicineListTable.see(child)

                    self.get_cursor_medicine_list(self)

                    break
            if check == 0:
                messagebox.showinfo("Search Medicine", f"Not found {search_value.upper()}")
        else:
            messagebox.showwarning("Search Medicine", "Please Input Medicine No")
    def Patient_search_and_select_row(self):
        if (self.txtPatientId.get() != ""):
            PatientId = str(self.txtPatientId.get())
            search_value = PatientId
            check = 0
            for child in self.PatientListTable.get_children():
                values = self.PatientListTable.item(child, 'values')

                if search_value in values:
                    check += 1
                    # Select the row
                    self.PatientListTable.selection_set(child)

                    # Focus on the selected row
                    self.PatientListTable.focus(child)

                    # Scroll to make the selected row visible
                    self.PatientListTable.see(child)

                    self.get_cursor_patient_list(self)
                    break
            if check == 0:
                messagebox.showinfo("Search Medicine", f"Not found {search_value.upper()}")
        else:
            messagebox.showwarning("Search Patient", "Please Input Patient Id")
    def iLogout(self):
        iLogout = messagebox.askyesno("Hospital Management System","Confirm you want to logout")
        if iLogout > 0:
            self.root.destroy()
            from gui_login import LoginWindow
            loginPage = LoginWindow()
            loginPage.UIlogin_window()
            return

if __name__ == '__main__':
    a = Hospital()
    a.mainRoleAdmin('Admin')