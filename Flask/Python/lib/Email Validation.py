email = input().strip().split('@')
print("valid" if len(email) == 2 and email[-1].count('.') == 1 else "invalid")
