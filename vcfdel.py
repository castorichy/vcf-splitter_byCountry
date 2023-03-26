import re

def check_code(phone):
    if phone[0:4] == '+254' or phone[0:2] == '07' or phone[0:2] == '01':
        return 1

def getContact(filename, outputFilename):
    data = ''
    kenCon = []

    with open(filename, 'r') as f:
        data = f.read()

    pattern = r'(?s)BEGIN:VCARD\n.*?END:VCARD\n'
    match = re.findall(pattern,data,re.DOTALL)

    for contact in match:
        pattern = r'(?s)item1.TEL:.*?\n'
        match = str(re.findall(pattern,contact,re.DOTALL))
        item = match.strip('\n').split(':')
        try:
            phone = item[1]
            if check_code(phone) != 1:
                continue
            else:
                kenCon.append(contact)
        except IndexError:
            continue
    write_to_vcf(kenCon, outputFilename)

def write_to_vcf(kenCon, file):
    kenCon = ''.join(kenCon)
    with open(file, 'w') as f:
        f.write(kenCon)
