from qr_generator import generate_qr

while True:
    data = input("Enter the URL or text that you want to be generated into a QR code: ").strip()
    while data == "":
            print("Please provide some input")
            data = input("Enter the URL or text that you want to be generated into a QR code: ").strip()

    file_name = input("What should be the name of your QR? ").strip()
    while not file_name:
        print("Please provide some input")
        file_name = input("What should be the name of your QR? ").strip()
    
    file_name += ".png"

    generate_qr(data, file_name)

    print("QR Code has been generated successfully!")

    while True:
        choice = input("Do you want to generate more QR Codes? (Y/N): ").strip().lower()
        if choice == "y":
            break
        elif choice == "n":
            print("Thanks for using my QR code generator!!")
            exit()
        else:
            print("Invalid input!")
         
    
         


