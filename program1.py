import qrcode
#generating data
qr=qrcode.make("This is a qr code")
#generating link
data="https://github.com/GundaAruna?tab=repositories"
qr=qrcode.make(data)
qr.save("qr1.png")
qr.show()



#send details using QRcode
qr=qrcode.QRCode(
    version=5,
    box_size=5,
    border=2
)
name=input("Enter your name: ")
age=int(input("Enter your age: "))
email=input("Enter your email: ")
mobile=int(input("Entyer your mobile: "))
#store it in a dictionary format
data={"Name":name,"Age":age,"Email":email,"Mobile":mobile}
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image()
img.save("my-details.png")
img.show()