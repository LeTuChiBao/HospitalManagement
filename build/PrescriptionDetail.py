from tkinter import *
from tkinter import END
from PIL import Image, ImageTk
import os
from tkinter import messagebox
class Prescription:
    def __init__(self,MedicineNo,Medicinetype,MedicineName,Medicinelot,MedicineissueDate,MedicineExpDate,MedicineSideEffect,
                 NotePrescriptionNo,NoteFurther,NoteBlood,NoteStorage,NoteDose,NoteDaillyDose,
                 PaientID,PatientPhone,PatientName,PatientBirth,PatientAddress):
        self.MedicineNo = MedicineNo
        self.Medicinetype = Medicinetype
        self.MedicineName = MedicineName
        self.Medicinelot = Medicinelot
        self.MedicineissueDate = MedicineissueDate
        self.MedicineExpDate = MedicineExpDate
        self.MedicineSideEffect = MedicineSideEffect

        self.NotePrescriptionNo = NotePrescriptionNo
        self.NoteFurther = NoteFurther
        self.NoteBlood = NoteBlood
        self.NoteStorage = NoteStorage
        self.NoteDose = NoteDose
        self.NoteDaillyDose = NoteDaillyDose

        self.PaientID = PaientID
        self.PatientPhone = PatientPhone
        self.PatientName = PatientName
        self.PatientBirth = PatientBirth
        self.PatientAddress = PatientAddress

        self.root = Tk()
        self.root.title("PRESCRIPTION DETAIL")
        self.root.geometry("1000x800+350+100")

        # script_directory = os.path.dirname(os.path.abspath(__file__))
        # image_path = os.path.join(script_directory, "image", "prescription.png")
        # print(image_path)
        # try:
        #     original_image = Image.open(r'C:\Users\bao.le\Pycode\Do_An\image\prescription.png')
        #
        # except Exception as e:
        #     print(f"Error opening image: {e}")
        #     raise  # Raising the exception again to stop further execution
        # resized_image = original_image.resize((350, 450), Image.LANCZOS)
        # self.logout_icon = ImageTk.PhotoImage(resized_image)



    def Detail(self):
        lbltitle = Label(self.root, bd=20, relief=FLAT, text=f"PRESCRIPTION DETAIL - {self.NotePrescriptionNo}", fg="white", bg="green",
                         font=("time new roman", 30, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # =================Dataframe=====================
        Dataframe = Frame(self.root, bd=10, relief=FLAT)
        Dataframe.place(x=0, y=100, width=1000, height=600)

        DataFrameLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=4,
                                   font=("time new roman", 12, "bold"), text="Prescription Information")
        DataFrameLeft.place(x=140, y=5, width=700, height=550)

        # =================== Buttons====================

        ButtonFrame = Frame(self.root, bd=20, relief=FLAT)
        ButtonFrame.place(x=450, y=700, width=1000, height=70)



        # ================================Buttons===========================

        btnPrintPrescription = Button(ButtonFrame, text="Print", bg="green", fg="white", font=("arial", 12, "bold"),
                                 width=23, padx=2, pady=6,command=self.print)
        btnPrintPrescription.grid(row=0, column=0, padx=4 )

        btnCancel = Button(ButtonFrame, text="Cancel", bg="gray", fg="white",
                                     font=("arial", 12, "bold"), width=23, padx=2, pady=6 ,command=self.cancel)
        btnCancel.grid(row=0, column=1, padx=4)
        # -----------------------------DATA---------------
        self.txtPrescription = Text(DataFrameLeft, font=("Lobster", 12, "normal"), width=63, height=28, padx=50, pady=6)
        self.txtPrescription.grid(row=0, column=0)
        self.loaddata()
        self.root.mainloop()

    def loaddata(self):

        if (self.NotePrescriptionNo != ""):
            self.txtPrescription.delete('1.0', 'end')

        self.txtPrescription.insert(END, "\nMedicine No :\t\t\t" + self.MedicineNo + "\n")
        self.txtPrescription.insert(END,  "Medicine Type :\t\t\t" + self.Medicinetype  + "\n")
        self.txtPrescription.insert(END,  "Medicine Name :\t\t\t" + self.MedicineName  + "\n")
        self.txtPrescription.insert(END,  "Lot No :\t\t\t" +self.Medicinelot  + "\n")
        self.txtPrescription.insert(END,  "Issue Date :\t\t\t" + self.MedicineissueDate  + "\n")
        self.txtPrescription.insert(END,  "Exp Date :\t\t\t" + self.MedicineExpDate  + "\n")
        self.txtPrescription.insert(END,  "Side Effect :\t\t\t" + self.MedicineSideEffect  + "\n")

        self.txtPrescription.insert(END,  "\nPrescription No :\t\t\t" + self.NotePrescriptionNo + "\n")
        self.txtPrescription.insert(END,  "Medicine Type :\t\t\t" + self.NoteFurther  + "\n")
        self.txtPrescription.insert(END,  "Medicine Name :\t\t\t" + self.NoteBlood  + "\n")
        self.txtPrescription.insert(END,  "Lot No :\t\t\t" +self.NoteStorage  + "\n")
        self.txtPrescription.insert(END,  "Issue Date :\t\t\t" + self.NoteDose  + "\n")
        self.txtPrescription.insert(END,  "Exp Date :\t\t\t" + self.NoteDaillyDose  + "\n")

        self.txtPrescription.insert(END,  "\nPaient ID :\t\t\t" + self.PaientID  + "\n")
        self.txtPrescription.insert(END,  "Patient Phone :\t\t\t" +self.PatientPhone  + "\n")
        self.txtPrescription.insert(END,  "Patient Name :\t\t\t" + self.PatientName  + "\n")
        self.txtPrescription.insert(END,  "Patient Birth :\t\t\t" + self.PatientBirth  + "\n")
        self.txtPrescription.insert(END,  "Patient Address :\t\t\t" + self.PatientAddress  + "\n")
        self.txtPrescription.config(state="disabled")

    def cancel(self):
        self.root.destroy()

    def print(self):
        messagebox.showinfo("Print Success", "Your Prescription print success!!!")
        self.root.destroy()


if __name__ == '__main__':
    a = Prescription("2113","2113","2113","2113","2113""2113","2113""2113","2113",
                     "No 01", "AAAA","AAAA","AAAA","AAAA","AAAA",
                     "No 01", "AAAA","AAAA","AAAA","AAAA")
    a.Detail()
    a.loaddata()