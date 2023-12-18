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



    def mainRoleSuper(self,username):
        self.user = username
        # self.logout_icon = PhotoImage(file=r'C:\Users\bao.le\Pycode\Do_An\image\super.png')
        script_directory = os.path.dirname(os.path.abspath(__file__))

        # Load and resize the icon image
        image_path = os.path.join(script_directory, "image", "super.png")
        print(image_path)  # Check the printed path in the console

        try:
            original_image = Image.open(r'C:\Users\bao.le\Pycode\Do_An\image\super.png')
        except Exception as e:
            print(f"Error opening image: {e}")
            raise  # Raising the exception again to stop further execution

        resized_image = original_image.resize((60, 60), Image.LANCZOS)
        self.logout_icon = ImageTk.PhotoImage(resized_image)



        print(self.user)
        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="Green", bg="white",
                         font=("time new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        img_label = Label(lbltitle, text=f"{self.user.upper()} ", image=self.logout_icon,
                          compound="right", bg="white", fg="GoldenRod", font=("Arial", 20, "bold"), padx=2, pady=6)
        img_label.pack(side=RIGHT)
        # =================Dataframe=====================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1900, height=850)

        DataMedicine = LabelFrame(Dataframe, bd=10, relief=RAISED, padx=5,
                                   font=("time new roman", 12, "bold"), text="Medicine Information")
        DataMedicine.place(x=2, y=5, width=450, height=350)
        
        DataNotes = LabelFrame(Dataframe, bd=10, relief=RAISED, padx=5,
                                   font=("time new roman", 12, "bold"), text="Notes")
        DataNotes.place(x=460, y=5, width=470, height=350)

        DataPatients = LabelFrame(Dataframe, bd=10, relief=RAISED, padx=5,
                                   font=("time new roman", 12, "bold"), text="Patient Information")
        DataPatients.place(x=940, y=5, width=450, height=350)

        DataFrameRight = LabelFrame(Dataframe, bd=10, relief=RAISED, padx=5,
                                    font=("time new roman", 12, "bold"), text="Prescription")
        DataFrameRight.place(x=1400, y=5, width=460, height=350)

        # =================== Buttons====================

        ButtonPrescriptionFrame = LabelFrame(Dataframe, bd=6, relief=RAISED,padx=10,pady=2, font=("time new roman", 12, "bold"), text="Buttons")
        ButtonPrescriptionFrame.place(x=0, y=540, width=1870, height=80)
        
        ButtonMedicineFrame = LabelFrame(DataMedicine, bd=4, relief=FLAT,padx=10, font=("time new roman", 12, "bold"))
        ButtonMedicineFrame.place(x=0, y=250, width=420, height=60)
        
        ButtonPatientFrame = LabelFrame(DataPatients, bd=10, relief=FLAT,padx=10, font=("time new roman", 12, "bold"))
        ButtonPatientFrame.place(x=0, y=250, width=420, height=60)

        # ===================Details frame ====================

        DetailsFrame = LabelFrame(Dataframe, bd=10, relief=RIDGE, font=("time new roman", 12, "bold"), text="Prescription History")
        DetailsFrame.place(x=0, y=620, width=1870, height=190)

        # ===================Patients List frame ====================

        PatientListFrame = LabelFrame(Dataframe, bd=10, relief=RIDGE, font=("time new roman", 12, "bold"), text="Patient List")
        PatientListFrame.place(x=935, y=360, width=930, height=180)

        # ===================Medicine List  frame ====================

        MedicineListFrame = LabelFrame(Dataframe, bd=10, relief=RIDGE, font=("time new roman", 12, "bold"), text="Medicine List")
        MedicineListFrame.place(x=0, y=360, width=930, height=180)

        # =====================DataMedicine======================

        medicineNo = Label(DataMedicine, font=("arial", 12, "bold"), text="Medicine No:", padx=2,pady=6)
        medicineNo.grid(row=0, column=0, sticky=W)
        self.txtMedicineNo = Entry(DataMedicine, font=("arial", 13, "bold"), width=30)
        self.txtMedicineNo.grid(row=0, column=1, sticky=W)

        medicineType= Label(DataMedicine, text="Type Of Medicine", font=("arial", 12, "bold"), padx=2, pady=6)
        medicineType.grid(row=1, column=0, sticky=W)

        self.medicineType = ttk.Combobox(DataMedicine, state="readonly", font=("arial", 12, "bold"),width=28)
        self.medicineType["values"] = ("tablet", "injection")
        self.medicineType.grid(row=1, column=1, sticky=W)

        medicineName = Label(DataMedicine, font=("arial", 12, "bold"), text="Medicine Name:", padx=2, pady=6)
        medicineName.grid(row=2, column=0, sticky=W)
        self.medicineName =ttk.Combobox(DataMedicine, state="readonly", font=("arial", 12, "bold"),width=28)
        self.medicineName["values"] = ("Vitamin A", "VitaMmin B","VitaMmin D","Acetsminophen","DM","Panadol","Cipla","Novel","Absorica")
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
        self.txtuserRole =ttk.Combobox(DataPatients, state="readonly", font=("arial", 12, "bold"),width=28)
        self.txtuserRole["values"] = ("Super", "Admin", "Agent")
        self.txtuserRole.grid(row=6, column=1, sticky=W)

        # ===============================DataFrameRight==========================
        self.txtPrescription = Text(DataFrameRight, font=("arial", 12, "bold"), width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # ================================Buttons Presciption===========================

        btnPrescription = Button(ButtonPrescriptionFrame, text="Presciption", bg="DarkCyan", fg="white", font=("arial", 12, "bold"),
                                 width=29, padx=2, pady=6, command=self.iPrescription)
        btnPrescription.grid(row=0, column=0, padx=2)

        btnPrescriptionData = Button(ButtonPrescriptionFrame, text="Presciption Data", bg="green", fg="white",
                                     font=("arial", 12, "bold"), width=29, padx=2, pady=6,
                                     command=self.iPrescription_Create)
        btnPrescriptionData.grid(row=0, column=1, padx=2)

        btnUpdate = Button(ButtonPrescriptionFrame, text="Update", bg="blue", fg="white", font=("arial", 12, "bold"), width=29,
                           padx=2, pady=6, command=self.iUpdate_presciption)
        btnUpdate.grid(row=0, column=2, padx=2)

        btnClear = Button(ButtonPrescriptionFrame, text="Clear", bg="gray", fg="white", font=("arial", 12, "bold"), width=29,
                          padx=2, pady=6, command=self.iclear_presciption_history)
        btnClear.grid(row=0, column=3, padx=2)

        btnDelete = Button(ButtonPrescriptionFrame, text="Delete", bg="red", fg="white", font=("arial", 12, "bold"), width=29,
                           padx=2, pady=6, command=self.idelete_presciption_history)
        btnDelete.grid(row=0, column=4, padx=2)

        btnExit = Button(ButtonPrescriptionFrame, text=f"Logout", bg="GoldenRod", fg="white", font=("arial", 12, "bold"), width=29, padx=2,
                         pady=6, command=self.iLogout)
        btnExit.grid(row=0, column=5, padx=2)


        # ================================Buttons ButtonMedicineFrame===========================

        btnMedicineCreate = Button(ButtonMedicineFrame, text="Create", bg="green", fg="white",
                                     font=("arial", 12, "bold"), width=10, padx=2, pady=2, command=self.iMedicine_Create)
        btnMedicineCreate.grid(row=0, column=0, padx=6)

        btnMedicineUpdate = Button(ButtonMedicineFrame, text="Update", bg="blue", fg="white", font=("arial", 12, "bold"), width=10, padx=2, pady=2 , command=self.iUpdate_Medicine)
        btnMedicineUpdate.grid(row=0, column=1, padx=6)

        btnMedicineDelete = Button(ButtonMedicineFrame, text="Delete", bg="red", fg="white", font=("arial", 12, "bold"), width=10, padx=2, pady=2 , command=self.idelete_Medicine)
        btnMedicineDelete.grid(row=0, column=2, padx=6)

        # ================================Buttons ButtonPatientFrame===========================


        btnPatientCreate = Button(ButtonPatientFrame, text="Create", bg="green", fg="white",
                                     font=("arial", 12, "bold"), width=10, padx=2, pady=2 ,command=self.iPatient_Create)
        btnPatientCreate.grid(row=0, column=0, padx=6)

        btnPatientUpdate = Button(ButtonPatientFrame, text="Update", bg="blue", fg="white", font=("arial", 12, "bold"), width=10, padx=2, pady=2 ,command=self.iUpdate_Patient)
        btnPatientUpdate.grid(row=0, column=1, padx=6)

        btnPatientDelete = Button(ButtonPatientFrame, text="Delete", bg="red", fg="white", font=("arial", 12, "bold"), width=10, padx=2, pady=2 ,command=self.idelete_Patient)
        btnPatientDelete.grid(row=0, column=2, padx=6)

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
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor_prescription_history)
        self.fatch_data_prescription_history()

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

    def iPrescription_Create(self):
        if self.medicineType.get()=="" or self.txtMedicineNo.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                SqlSever = MSSQLConnection()
                SqlSever.connect()
                Query1 = ('INSERT INTO hospital (Nameoftablets , Reference_No , dose ,Numbersoftablets, lot, issuedate, expdate,dailydose,storage,nhsnumber ,patientname ,DOB ,patientaddress ) VALUES '
                              '(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)')
                # Query1 = ('INSERT INTO hospital VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)')
                values =(
                    self.medicineType.get(),
                    self.txtMedicineNo.get(),self.txtDose.get(),
                    self.medicineName.get(),
                    self.txtLot.get(),
                    self.txtissueDate.get(),
                    self.txtExpDate.get(),
                    self.txtDailyDose.get(),
                    self.txtStorage.get(),
                    self.txtPhoneNumber.get(),
                    self.txtPatientname.get(),
                    self.txtDateOfBirth.get(),
                    self.txtPatientAddress.get())
                SqlSever.insert(Query1, values)
                messagebox.showinfo("Prescription", "Create Success")
            except Exception as e:
                messagebox.showerror("Error",f"Error: {e}")
            finally:
                SqlSever.close()
                self.fatch_data_prescription_history()
                self.iclear_presciption_history()
                
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

    def iUpdate_presciption(self):
        if self.medicineType.get() == "" or self.txtMedicineNo.get() == "":
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
                    self.medicineType.get(),
                    self.txtDose.get(),
                    self.medicineName.get(),
                    self.txtLot.get(),
                    self.txtissueDate.get(),
                    self.txtExpDate.get(),
                    self.txtDailyDose.get(),
                    self.txtStorage.get(),
                    self.txtPhoneNumber.get(),
                    self.txtPatientname.get(),
                    self.txtDateOfBirth.get(),
                    self.txtPatientAddress.get(),
                    self.txtMedicineNo.get(),
                )
                SqlSever.update(Query1, values)
                messagebox.showinfo("Success", "Update Success")
            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}")
            finally:
                SqlSever.close()
                self.fatch_data_prescription_history()
                self.iclear_presciption_history()

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
    def fatch_data_prescription_history(self):
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
            Query1 = ('SELECT * FROM users ')
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
    def get_cursor_prescription_history(self, event):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]

        self.medicineType.delete(0, END)
        self.txtMedicineNo.delete(0, END)
        self.txtDose.delete(0, END)
        self.medicineName.delete(0, END)
        self.txtLot.delete(0, END)
        self.txtissueDate.delete(0, END)
        self.txtExpDate.delete(0, END)
        self.txtDailyDose.delete(0, END)
        self.txtStorage.delete(0, END)
        self.txtPhoneNumber.delete(0, END)
        self.txtPatientname.delete(0, END)
        self.txtDateOfBirth.delete(0, END)
        self.txtPatientAddress.delete(0, END)

        # Insert values into entry widgets
        self.medicineType.set(row[0])
        self.txtMedicineNo.insert(0, row[1])
        # self.txtMedicineNo.config(state=DISABLED)
        self.txtDose.insert(0, row[2])
        self.medicineName.insert(0, row[3])
        self.txtLot.insert(0, row[4])
        self.txtissueDate.insert(0, row[5])
        self.txtExpDate.insert(0, row[6])
        self.txtDailyDose.insert(0, row[7])
        self.txtStorage.insert(0, row[8])
        self.txtPhoneNumber.insert(0, row[9])
        self.txtPatientname.insert(0, row[10])
        self.txtDateOfBirth.insert(0, row[11])
        self.txtPatientAddress.insert(0, row[12])

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
    def iPrescription(self):
        if self.medicineType.get() and self.txtMedicineNo.get():
            self.txtPrescription.delete('1.0', 'end')

        self.txtPrescription.insert(END,"Name Of Tablets :\t\t\t"+self.medicineType.get()+"\n")
        self.txtPrescription.insert(END, "Reference No :\t\t\t" + self.txtMedicineNo.get() + "\n")
        self.txtPrescription.insert(END, "Dose :\t\t\t" + self.txtDose.get() + "\n")
        self.txtPrescription.insert(END, "Number Of Tablets :\t\t\t" + self.medicineName.get() + "\n")
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
        self.txtPrescription.insert(END, "NHS Number :\t\t\t" + self.txtPhoneNumber.get() + "\n")
        self.txtPrescription.insert(END, "Patient Name :\t\t\t" + self.txtPatientname.get() + "\n")
        self.txtPrescription.insert(END, "Date Of Birth :\t\t\t" + self.txtDateOfBirth.get() + "\n")
        self.txtPrescription.insert(END, "Patient Address :\t\t\t" + self.txtPatientAddress.get() + "\n")

    def idelete_presciption_history(self):

        if self.txtMedicineNo.get() == "":
            messagebox.showerror("Error", "Reference No is required")
        else:
            iLogout = messagebox.askyesno("Hospital Management System",
                                           f"Confirm you want to delete this Prescription: \n\t {self.medicineType.get()} : {self.txtMedicineNo.get()}")
            if iLogout > 0:
                try:
                    SqlSever = MSSQLConnection()
                    SqlSever.connect()
                    Query1 = 'DELETE FROM hospital WHERE Reference_No = ?'
                    values = self.txtMedicineNo.get()
                    SqlSever.delete(Query1, values)
                    messagebox.showinfo("Prescription", "DELETE Success")
                except Exception as e:
                    messagebox.showerror("Error", f"Error: {e}")
                finally:
                    SqlSever.close()
                    self.fatch_data_prescription_history()
                    self.iclear_presciption_history()

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
    def iclear_presciption_history(self):
        self.txtMedicineNo.delete(0, END)
        self.medicineType.set("")
        self.medicineName.set("")
        self.txtLot.delete(0, END)
        self.txtissueDate.delete(0, END)
        self.txtExpDate.delete(0, END)
        self.txtSideEffect.delete(0, END)
        self.txtPrescriptionNo.delete(0, END)
        self.txtFurtherInfo.delete(0, END)
        self.txtBloodPressure.delete(0, END)
        self.txtStorage.delete(0, END)
        self.txtDose.delete(0, END)
        self.txtDailyDose.delete(0, END)
        self.txtPatientId.delete(0,END)
        self.txtPatientPass.delete(0,END)
        self.txtPhoneNumber.delete(0,END)
        self.txtPatientname.delete(0, END)
        self.txtDateOfBirth.delete(0, END)
        self.txtPatientAddress.delete(0, END)
        self.txtuserRole.set("")
        self.txtPrescription.delete('1.0', 'end')

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
    a.mainRoleSuper('Super')