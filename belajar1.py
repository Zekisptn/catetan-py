import datetime

def show_menu():
    print("Program Pencatatan")
    print("1. Tampilkan Catatan")
    print("2. Tambah Catatan Baru")
    print("3. Keluar")

def load_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
    except FileNotFoundError:
        notes = []
    return notes

def save_notes(notes):
    with open("notes.txt", "w") as file:
        file.writelines(notes)

def show_notes(notes):
    if not notes:
        print("Tidak ada catatan.")
    else:
        print("Catatan:")
        for note in notes:
            print(note.strip())

def add_note(notes):
    note = input("Masukkan catatan baru: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_note = f"[{timestamp}] {note}\n"
    notes.append(new_note)
    save_notes(notes)
    print("Catatan berhasil ditambahkan.")

notes = load_notes()

while True:
    show_menu()
    choice = input("Pilih opsi (1/2/3): ")

    if choice == "1":
        show_notes(notes)
    elif choice == "2":
        add_note(notes)
    elif choice == "3":
        print("Terima kasih! Sampai jumpa.")
        break
    else:
        print("Opsi tidak valid. Silakan coba lagi.")