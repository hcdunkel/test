# Modul customtkinter einbinden
import customtkinter

# CUSTOMTKINTER Attribute setzen
customtkinter.set_appearance_mode("dark")

# Haupt(Wurzel)-Element erzeugen
root = customtkinter.CTk()
# Größe des Windows in pixel
root.geometry("500x350")


# Methoden Definition/Implementierung
def test_function():
    print("Hallo GUI!")


# Rahmen im Hauptelement
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Elemente sequenziell anlegen
label = customtkinter.CTkLabel(master=frame, text="Rahmen Label")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Eintrag1")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Eintrag2")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Klick", command=test_function)
button.pack(pady=12, padx=10)

# Ausführungs-Schleife
root.mainloop()
