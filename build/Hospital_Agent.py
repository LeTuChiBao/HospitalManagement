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



    def mainRoleAgent(self,username):
        self.user = username
        try:
            original_image1 = Image.open(r'C:\Users\bao.le\Pycode\Do_An\image\user.png')
        except Exception as e:
            print(f"Error opening image: {e}")
            raise  # Raising the exception again to stop further execution

        resized_image1 = original_image1.resize((380, 300), Image.LANCZOS)
        self.main_icon = ImageTk.PhotoImage(resized_image1)

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="Green", bg="white",
                         font=("time new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # =================Dataframe=====================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1900, height=850)

        DataMedicine = LabelFrame(Dataframe, bd=4, relief=RAISED, padx=5,
                                   font=("time new roman", 12, "bold"), text="Medicine Information")
        DataMedicine.place(x=2, y=5, width=450, height=350)
        
        DataNotes = LabelFrame(Dataframe, bd=4, relief=RAISED, padx=5,
                                   font=("time new roman", 12, "bold"), text="Notes")
        DataNotes.place(x=460, y=5, width=470, height=350)

        DataPatients = LabelFrame(Dataframe, bd=4, relief=RAISED, padx=5,
                                   font=("time new roman", 12, "bold"), text="Patient Information")
        DataPatients.place(x=940, y=5, width=470, height=350)

        DataFrameRight = LabelFrame(Dataframe, bd=4, relief=FLAT, padx=5,
                                    font=("time new roman", 12, "bold"))
        DataFrameRight.place(x=1420, y=5, width=420, height=280)

        image_label = Label(DataFrameRight, image=self.main_icon, bd=0 )
        image_label.place(x=10, y=10)

        ButtonPrescriptionFrame = LabelFrame(Dataframe, bd=6, relief=FLAT,padx=10,pady=2, font=("time new roman", 12, "bold"))
        ButtonPrescriptionFrame.place(x=1530, y=290, width=200, height=80)
        # =================== Buttons====================
        
        ButtonPatientFrame = LabelFrame(DataPatients, bd=10, relief=FLAT,padx=10, font=("time new roman", 12, "bold"))
        ButtonPatientFrame.place(x=140, y=250, width=180, height=60)

        # ===================Details frame ====================

        DetailsFrame = LabelFrame(Dataframe, bd=4, relief=RIDGE, font=("time new roman", 12, "bold"), text="Prescription History")
        DetailsFrame.place(x=0, y=370, width=1870, height=400)

        # =====================DataMedicine======================

        medicineNo = Label(DataMedicine, font=("arial", 12, "bold"), text="Medicine No:", padx=2,pady=6)
        medicineNo.grid(row=0, column=0, sticky=W)
        self.txtMedicineNo = Entry(DataMedicine, font=("arial", 13, "bold"), width=30)
        self.txtMedicineNo.grid(row=0, column=1, sticky=W)

        medicineType= Label(DataMedicine, text="Type Of Medicine", font=("arial", 12, "bold"), padx=2, pady=6)
        medicineType.grid(row=1, column=0, sticky=W)

        self.medicineType = Entry(DataMedicine, font=("arial", 12, "bold"),width=30)
        self.medicineType.grid(row=1, column=1, sticky=W)

        medicineName = Label(DataMedicine, font=("arial", 12, "bold"), text="Medicine Name:", padx=2, pady=6)
        medicineName.grid(row=2, column=0, sticky=W)
        self.medicineName =Entry(DataMedicine, font=("arial", 12, "bold"),width=30)
        self.medicineName.grid(row=2, column=1, sticky=W)

        lblLot = Label(DataMedicine, font=("arial", 12, "bold"), text="Lot No:", padx=2, pady=6)
        lblLot.grid(row=3, column=0, sticky=W)
        self.txtLot = Entry(DataMedicine, font=("arial", 13, "bold"), width=30)
        self.txtLot.grid(row=3, column=1, sticky=W)

        lblissueDate = Label(DataMedicine, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblissueDate.grid(row=4, column=0, sticky=W)
        self.txtissueDate = Entry(DataMedicine, font=("arial", 13, "bold"), width=30)
        self.txtissueDate.grid(row=4, column=1, sticky=W)

        lblExpDate = Label(DataMedicine, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=6)
        lblExpDate.grid(row=5, column=0, sticky=W)
        self.txtExpDate = Entry(DataMedicine, font=("arial", 13, "bold"), width=30)
        self.txtExpDate.grid(row=5, column=1, sticky=W)

        lblSideEffect = Label(DataMedicine, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=6, column=0, sticky=W)
        self.txtSideEffect = Entry(DataMedicine, font=("arial", 13, "bold"), width=30)
        self.txtSideEffect.grid(row=6, column=1, sticky=W)

        # ----------------------notes Infor----------------------
        lblPrescriptionNo = Label(DataNotes, font=("arial", 12, "bold"), text="Prescription No:", padx=2, pady=6)
        lblPrescriptionNo.grid(row=0, column=0, sticky=W)
        self.txtPrescriptionNo = Entry(DataNotes, font=("arial", 12, "bold"), width=30)
        self.txtPrescriptionNo.grid(row=0, column=1, sticky=W)

        lblFurtherInfo = Label(DataNotes, font=("arial", 12, "bold"), text="Further Information:", padx=2 , pady=6)
        lblFurtherInfo.grid(row=1, column=0, sticky=W)
        self.txtFurtherInfo = Entry(DataNotes, font=("arial", 12, "bold"), width=30)
        self.txtFurtherInfo.grid(row=1, column=1, sticky=W)

        lblBloodPressure = Label(DataNotes, font=("arial", 12, "bold"), text="Blood Pressure:", padx=2, pady=6)
        lblBloodPressure.grid(row=2, column=0, sticky=W)
        self.txtBloodPressure = Entry(DataNotes, font=("arial", 12, "bold"), width=30)
        self.txtBloodPressure.grid(row=2, column=1, sticky=W)

        lblStorage = Label(DataNotes, font=("arial", 12, "bold"), text="Storage Advice:", padx=2, pady=6)
        lblStorage.grid(row=3, column=0, sticky=W)
        self.txtStorage = Entry(DataNotes, font=("arial", 12, "bold"), width=30)
        self.txtStorage.grid(row=3, column=1, sticky=W)

        lblDose = Label(DataNotes, font=("arial", 12, "bold"), text="Dose", padx=2, pady=4)
        lblDose.grid(row=4, column=0, sticky=W)
        self.txtDose = Entry(DataNotes, font=("arial", 13, "bold"), width=30)
        self.txtDose.grid(row=4, column=1, sticky=W)

        lblDailyDose = Label(DataNotes, font=("arial", 12, "bold"), text="Dailly Dose:", padx=2, pady=4)
        lblDailyDose.grid(row=5, column=0, sticky=W)
        self.txtDailyDose = Entry(DataNotes, font=("arial", 13, "bold"), width=30)
        self.txtDailyDose.grid(row=5, column=1, sticky=W)

        # -------------Data Patients---------------

        lblPatientId = Label(DataPatients, font=("arial", 12, "bold"), text="Patient Id:", padx=2, pady=6)
        lblPatientId.grid(row=0, column=0, sticky=W)
        self.txtPatientId = Entry(DataPatients, font=("arial", 12, "bold"), width=30)
        self.txtPatientId.grid(row=0, column=1, sticky=W)

        
        lblPatientPass = Label(DataPatients, font=("arial", 12, "bold"), text="Patient Password:", padx=2, pady=6)
        lblPatientPass.grid(row=1, column=0, sticky=W)
        self.txtPatientPass = Entry(DataPatients, font=("arial", 12, "bold"), width=30)
        self.txtPatientPass.grid(row=1, column=1, sticky=W)

        lblNhsNumber = Label(DataPatients, font=("arial", 12, "bold"), text="Phone Number:", padx=2, pady=6)
        lblNhsNumber.grid(row=2, column=0, sticky=W)
        self.txtPhoneNumber = Entry(DataPatients, font=("arial", 12, "bold"), width=30)
        self.txtPhoneNumber.grid(row=2, column=1, sticky=W)

        lblPatientname = Label(DataPatients, font=("arial", 12, "bold"), text="Patient Name:", padx=2, pady=6)
        lblPatientname.grid(row=3, column=0, sticky=W)
        self.txtPatientname = Entry(DataPatients, font=("arial", 12, "bold"), width=30)
        self.txtPatientname.grid(row=3, column=1, sticky=W)

        lblDateOfBirth = Label(DataPatients, font=("arial", 12, "bold"), text="Date Of Birth:", padx=2, pady=6)
        lblDateOfBirth.grid(row=4, column=0, sticky=W)
        self.txtDateOfBirth = Entry(DataPatients, font=("arial", 12, "bold"), width=30)
        self.txtDateOfBirth.grid(row=4, column=1, sticky=W)

        lblPatientAddress = Label(DataPatients, font=("arial", 12, "bold"), text="Patient Address:", padx=2, pady=6)
        lblPatientAddress.grid(row=5, column=0, sticky=W)
        self.txtPatientAddress = Entry(DataPatients, font=("arial", 12, "bold"), width=30)
        self.txtPatientAddress.grid(row=5, column=1, sticky=W)

        userRole = Label(DataPatients, font=("arial", 12, "bold"), text="Role:", padx=2, pady=6)
        userRole.grid(row=6, column=0, sticky=W)
        self.txtuserRole =Entry(DataPatients, font=("arial", 12, "bold"),width=30)
        self.txtuserRole.grid(row=6, column=1, sticky=W)


        # ================================Buttons Presciption===========================

        btnExit = Button(ButtonPrescriptionFrame, text="Logout", bg="gray", fg="white", font=("arial", 12, "bold"), width=16, padx=2,
                         pady=6, command=self.iLogout)
        btnExit.grid(row=0, column=0, padx=2)



        # ================================Buttons ButtonPatientFrame===========================


        btnPatientUpdate = Button(ButtonPatientFrame, text="Update", bg="blue", fg="white", font=("arial", 12, "bold"), width=10, padx=2, pady=2 ,command=self.iUpdate_Patient)
        btnPatientUpdate.grid(row=0, column=1, padx=6)

        # =================================Scrollbar========================

        # Create horizontal and vertical scrollbars
        scroll_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)
        # Create Treeview widget
        self.hospital_table = ttk.Treeview(DetailsFrame, columns=(
        "presciptionno", "medicineno", "username", "furtherinfo", "bloodpressure", "storageadvice", "dose", "dailydose"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        # Pack the scrollbars
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Configure scrollbars
        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("presciptionno", text="Presciption No")
        self.hospital_table.heading("medicineno", text="Medicine No.")
        self.hospital_table.heading("username", text="Patient Id")
        self.hospital_table.heading("furtherinfo", text="Further Info")
        self.hospital_table.heading("bloodpressure", text="Blood Pressure")
        self.hospital_table.heading("storageadvice", text="Storage Advice")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("dailydose", text="Daily Dose")

        self.hospital_table["show"] = "headings"
        self.hospital_table.pack(fill=BOTH, expand=1)

        for col in ("presciptionno", "medicineno", "username", "furtherinfo", "bloodpressure", "storageadvice", "dose", "dailydose"):
            self.hospital_table.column(col, width=100)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor_prescription_history)
        self.fatch_data_prescription_history()
        self.Patient_search_Data()
        self.root.mainloop()

        # ======================Functinality Declration=====================



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
    def fatch_data_prescription_history(self):
        try:
            SqlSever = MSSQLConnection()
            SqlSever.connect()
            Query1 = ('SELECT * FROM presciptions where username = ?')
            value1 = (self.user)
            rows = SqlSever.query(Query1,value1)
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

    def get_cursor_prescription_history(self, event):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        self.clearFromMedicine()
        self.clearFromPatient()
        self.clearFromNotes()


        # Insert values into entry widgets
        self.txtPrescriptionNo.insert(0, row[0])
        # self.txtMedicineNo.config(state=DISABLED)
        self.txtMedicineNo.insert(0, row[1])
        self.txtPatientId.insert(0, row[2])
        self.txtFurtherInfo.insert(0, row[3])
        self.txtBloodPressure.insert(0, row[4])
        self.txtStorage.insert(0, row[5])
        self.txtDose.insert(0, row[6])
        self.txtDailyDose.insert(0, row[7])
        self.Medicine_search_Data()
        self.Patient_search_Data()

        self.iPrescription()

    def clearFromNotes(self):

        self.txtPrescriptionNo.delete(0, END)
        self.txtMedicineNo.delete(0, END)
        self.txtPatientId.delete(0, END)
        self.txtFurtherInfo.delete(0, END)
        self.txtBloodPressure.delete(0, END)
        self.txtStorage.delete(0, END)
        self.txtDose.delete(0, END)
        self.txtDailyDose.delete(0, END)
    def clearFromMedicine(self):

        self.txtMedicineNo.config(state="normal")
        self.txtMedicineNo.delete(0, END)
        self.medicineType.delete(0, END)
        self.medicineName.delete(0, END)
        self.txtLot.delete(0, END)
        self.txtissueDate.delete(0, END)
        self.txtExpDate.delete(0, END)
        self.txtSideEffect.delete(0, END)


    def clearFromPatient(self):
        self.txtPatientId.config(state="normal")
        self.txtPatientId.delete(0, END)
        self.txtPatientPass.delete(0, END)
        self.txtPhoneNumber.delete(0, END)
        self.txtPatientname.delete(0, END)
        self.txtDateOfBirth.delete(0, END)
        self.txtPatientAddress.delete(0, END)
        self.txtuserRole.delete(0, END)
    def iPrescription(self):
        from PrescriptionDetail import Prescription

        MedicineNo: str = self.txtMedicineNo.get()
        Medicinetype: str = self.medicineType.get()
        MedicineName: str = self.medicineName.get()
        Medicinelot: str = self.txtLot.get()
        MedicineissueDate: str = self.txtissueDate.get()
        MedicineExpDate: str = self.txtExpDate.get()
        MedicineSideEffect: str = self.txtSideEffect.get()
     # --------------Note---------

        NotePrescriptionNo: str = self.txtPrescriptionNo.get()
        NoteFurther: str = self.txtFurtherInfo.get()
        NoteBlood: str = self.txtBloodPressure.get()
        NoteStorage: str = self.txtStorage.get()
        NoteDose: str = self.txtDose.get()
        NoteDaillyDose: str = self.txtDailyDose.get()

        PaientID: str = self.txtPatientId.get()
        PatientPhone: str = self.txtPhoneNumber.get()
        PatientName: str = self.txtPatientname.get()
        PatientBirth: str = self.txtDateOfBirth.get()
        PatientAddress: str = self.txtPatientAddress.get()


        prescription_instance = Prescription(MedicineNo,Medicinetype,MedicineName,Medicinelot,MedicineissueDate,MedicineExpDate,MedicineSideEffect,
                                             NotePrescriptionNo,NoteFurther,NoteBlood,NoteStorage,NoteDose,NoteDaillyDose,
                                             PaientID,PatientPhone,PatientName,PatientBirth,PatientAddress)
        prescription_instance.Detail()



  
    def Medicine_search_Data(self):
        if (self.txtMedicineNo.get() == ""):
            messagebox.showwarning("Warning", "txtMedicineNo is not null")
        else:
            try:
                SqlSever = MSSQLConnection()
                SqlSever.connect()
                Query1 = ("SELECT * FROM medicines WHERE medicineno = ? ")
                value1 = self.txtMedicineNo.get()
                rows = SqlSever.query(Query1, value1)
                if len(rows) != 0:
                    self.txtMedicineNo.config(state="disabled")
                    self.medicineType.insert(0,rows[0][1])
                    self.medicineName.insert(0,rows[0][2])
                    self.txtLot.insert(0, rows[0][3])
                    self.txtissueDate.insert(0, rows[0][4])
                    self.txtExpDate.insert(0, rows[0][5])
                    self.txtSideEffect.insert(0, rows[0][6])
            except Exception as e:
                messagebox.showerror(f"Error: {e}")
            finally:
                SqlSever.close()
    def Patient_search_Data(self):
        try:
            SqlSever = MSSQLConnection()
            SqlSever.connect()
            Query1 = ("SELECT * FROM users WHERE username = ? ")
            value1 = self.user
            rows = SqlSever.query(Query1, value1)
            if len(rows) != 0:
                self.clearFromPatient()
                self.txtPatientId.insert(0, rows[0][0])
                self.txtPatientId.config(state="disabled")
                self.txtPatientPass.insert(0, rows[0][1])
                self.txtPhoneNumber.insert(0, rows[0][5])
                self.txtPatientname.insert(0, rows[0][2])
                self.txtDateOfBirth.insert(0, rows[0][4])
                self.txtPatientAddress.insert(0, rows[0][3])
                self.txtuserRole.insert(0, rows[0][6])
        except Exception as e:
            messagebox.showerror(f"Error: {e}")
        finally:
            SqlSever.close()
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
    a.mainRoleAgent('user1')