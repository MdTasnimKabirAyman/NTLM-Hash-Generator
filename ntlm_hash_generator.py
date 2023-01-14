import hashlib

print('Enter "break" as input to exit the script')
def ntlm_hash(string):
    m = hashlib.new('md4', string.encode('utf-16le')).digest()
    return m.hex().upper()

input_str = input("Enter the string to generate the NTLM hash: ")
while input_str!='break':
    print(ntlm_hash(input_str))
    input_str = input("Enter the string to generate the NTLM hash: ")
    
