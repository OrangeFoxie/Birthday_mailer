import sys
sys.path.append('E:\Data\Git\Auto_Mailer\getDataFromAPI')
from getGgSheetBirthday import Values
from datetime import datetime, date

def extractDate():
    arr1 = Values()
    arr2 = []
    for s in range(len(arr1)):
        arr2.append([
                arr1[s][0],
                arr1[s][1],
                datetime.strptime(arr1[s][2], '%d/%m/%Y').date().strftime("%d-%m"),
                arr1[s][3]])
    return arr2

def getToday():
    getDate = date.today()
    today = getDate.strftime("%d-%m")
    return today


def getUserList():
    userList = []
    extractdate = extractDate()
    gettoday = getToday()

    for s in range(len(extractdate)):
        if(extractdate[s][2]==getToday()):
            userList.append(extractdate[s])
    return userList


def getUserNameList():
    userNameList = []
    userList = getUserList()

    for s in range(len(userList)):
        userNameList.append(userList[s][1])
    return userNameList


def getUserEmailList():
    userEmailList = []
    userList = getUserList()

    for s in range(len(userList)):
        userEmailList.append(userList[s][3])
    return userEmailList


# print(getUserList())