import base64
code = input("Input code> ")
final = str(base64.b64encode(code, altchars=None, validate=False).decode("utf-8", "ignore"))
f = open("build.usb", "w")
f.write(final)
f.close()