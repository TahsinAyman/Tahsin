class EmailError(Exception):
    ...



email = input("Enter email: ")

if "@" in email and "." in email:
    print("Authorized")
else:
    raise EmailError("sssasd")
