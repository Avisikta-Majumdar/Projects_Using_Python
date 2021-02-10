import qrcode

Ytube_Link  = input("Enter any Youtube link :-")
QR = qrcode.make(Ytube_Link)
QR.save("{}.jpg".format("HustelerMotivation"))


print("We have made QR Successfully for this Link ")