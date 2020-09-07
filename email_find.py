str = '''
'''

email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z]+.[a-z0-9A-Z]+",str)
print(email)
