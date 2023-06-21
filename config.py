dCity = '长春'
aCity = '太原'

date1 = '20230721'  # eg：20230721
date2 = '20230722'
date3 = '20230723'


app_id = 'your app_id'
app_secret = 'your app_secret'
user_id = 'your user_id'
# user_id2 = ''
template_id = 'your template_id'

def initDate():
    dateList = []
    if date1 != '':
        dateList.append(date1)
    if date2 != '':
        dateList.append(date2)
    if date3 != '':
        dateList.append(date3)

    return dateList
