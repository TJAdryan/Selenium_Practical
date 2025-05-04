import shutil
import os
import pandas as pd
import numpy as np
import xlsxwriter

#needs sample file for testing purposes
dpns = plns.drop_duplicates(['PatientName']) 

writer = pd.ExcelWriter('N:/NursingRepor.xlsx', engine='xlsxwriter')
dpns.to_excel(writer, sheet_name='Sheet1', index=False)
workbook=writer.book
worksheet = writer.sheets['Sheet1']

format = workbook.add_format({'text_wrap': True})

# Setting the format but not setting the column width.
worksheet.set_column('A:F', None, format)

worksheet.set_column('A:A',15)
worksheet.set_column('B:G',10)
worksheet.set_column('H:H',20)
worksheet.set_column('I:J',12)


worksheet.set_landscape()
worksheet.repeat_rows(0)
format = workbook.add_format({'text_wrap': True})
worksheet.set_column('A:I',None,format)

format2 = workbook.add_format()
format2.set_top(2)
format2.set_bottom(1)
format2.set_right(1)
format2.set_left(1)

worksheet.conditional_format(1, 0, 1, plns.shape[1] -1,
{'type': 'cell',
 'criteria': '>=',
 'value': '""',
 'format': format2})
# header
header_format = workbook.add_format({'bottom': 2, 'top':2, 'left':2, 'right':2, 'bold': 1, 'italic':1, 'underline':1, 'font_size':13})
for col_num, value in enumerate(plns.columns.values):
    worksheet.write(0, col_num, value, header_format)

# data with bottom borders
format1 = workbook.add_format()
format1.set_bottom(1)
format1.set_top(1)
format1.set_right(1)
format1.set_left(1)

worksheet.conditional_format(1, 0, plns.shape[0], plns.shape[1] -1,
{'type': 'cell',
 'criteria': '>=',
 'value': '""',
 'format': format1})
worksheet.add_table(1, 0, plns.shape[0], plns.shape[1] -1,{'autofilter': True, 'style': 'Table Style Light 1'})

writer.save()




df = pd.read_csv('C:/Users/dreport/downloads/Schedule by Coordinator.csv', skiprows=[0,1,2], index_col=None, usecols=['textbox28','textbox40','textbox42','textbox43','textbox44','textbox45','textbox47','textbox48','textbox49','textbox50','textbox52'])

day = pd.Timestamp('today')
day1 = day +pd.DateOffset(days=1)
day2 = day +pd.DateOffset(days=2)
day3 = day +pd.DateOffset(days=3)
day4 = day +pd.DateOffset(days=4)
day5 = day +pd.DateOffset(days=5)
day6 = day +pd.DateOffset(days=6)

df.rename(columns={'textbox28':'Coor', 'textbox40':'Patient', 'textbox42':'Caregiver', 'textbox43': 'Schedule',
'textbox44': day.strftime('%a /%d'),'textbox45': day1.strftime('%a /%d'),'textbox47': day2.strftime('%a /%d'),
'textbox48': day3.strftime('%a /%d'),'textbox49': day4.strftime('%a /%d'),'textbox50': day5.strftime('%a /%d'),'textbox52': day6.strftime('%a /%d')}, inplace=True)

df['Coor'] =df['Coor'].str[5:-8]

df['Caregiver'].fillna('Temp', inplace=True)

df1 = df[df['Caregiver'].str.contains('Temp', case=False)]

writer = pd.ExcelWriter('C:/users/dreport/downloads/temps.xlsx', engine='xlsxwriter')

df1.to_excel(writer, sheet_name='Sheet1',index=False)
worksheet = writer.sheets['Sheet1']
workbook = writer.book



# header
header_format = workbook.add_format({'bottom': 2, 'top':2, 'left':2, 'right':2, 'bold': 1, 'italic':1, 'underline':1, 'font_size':13})
for col_num, value in enumerate(df1.columns.values):
    worksheet.write(0, col_num, value, header_format)

# data with bottom borders
format1 = workbook.add_format()
format1.set_bottom(1)
format1.set_top(1)
format1.set_right(1)
format1.set_left(1)

#snippet added to op script
format2 = workbook.add_format()
format2.set_top(2)
format2.set_bottom(1)
format2.set_right(1)
format2.set_left(1)

worksheet.conditional_format(1, 0, 1, df1.shape[1] -1,
{'type': 'cell',
 'criteria': '>=',
 'value': '""',
 'format': format2})
#end of snippet added to op script

worksheet.conditional_format(1, 0, df1.shape[0], df1.shape[1] -1,
{'type': 'cell',
 'criteria': '>=',
 'value': '""',
 'format': format1})
worksheet.add_table(1, 0, df1.shape[0], df1.shape[1] -1,{'autofilter': True, 'style': 'Table Style Light 1'})



worksheet.set_column('B:B',22)
worksheet.set_column('C:D',11)
worksheet.set_column('A:A',10)
worksheet.set_column('E:K',8.5)
worksheet.set_landscape()
worksheet.repeat_rows(0)




writer.save()
writer.close
sleep(10)



dtvar = time.strftime("%m%d-%H%M")

filepath = ('')

if os.path.exists(filepath):
    os.remove(filepath)
else:
    print('I can not remove what is not there')
    
filepath2=('C:/users/dreport/downloads/temps.xlsx')

if os.path.exists(filepath2):
    os.remove(filepath2)
else:
    print('I can not remove the second one')


##Remove pdf files from Previous Week
folder_path = ""
file_ends_with = ".xlsx"
how_many_days_old_logs_to_remove = 5
now = time.time()
only_files = []

for file in os.listdir(folder_path):
    file_full_path = os.path.join(folder_path,file)
    if os.path.isfile(file_full_path) and file.endswith(file_ends_with):
        #Delete files older than x days
        if os.stat(file_full_path).st_mtime < now - how_many_days_old_logs_to_remove * 86400: 
             os.remove(file_full_path)
             print ("\n File Removed : " , file_full_path)

##To normalize a schedule starting today and going forward 7 days
df = pd.read_csv('C://..., skiprows=[0,1,2], index_col=None)

day = pd.Timestamp('today')
day1 = day +pd.DateOffset(days=1)
day2 = day +pd.DateOffset(days=2)
day3 = day +pd.DateOffset(days=3)
day4 = day +pd.DateOffset(days=4)
day5 = day +pd.DateOffset(days=5)
day6 = day +pd.DateOffset(days=6)

df.rename(columns={'textbox28':'Coor', 'textbox40':'Patient', 'textbox42':'Caregiver', 'textbox43': 'Schedule',
'textbox44': day.strftime('%a /%d'),'textbox45': day1.strftime('%a /%d'),'textbox47': day2.strftime('%a /%d'),
'textbox48': day3.strftime('%a /%d'),'textbox49': day4.strftime('%a /%d'),'textbox50': day5.strftime('%a /%d'),'textbox52': day6.strftime('%a /%d')}, inplace=True)

df['Coor'] =df['Coor'].str[5:-8]

df['Caregiver'].fillna('Temp', inplace=True)
 
       
df1 = df[df['Caregiver'].str.contains('Temp', case=False)]



writer = pd.ExcelWriter('C:/users/dreport/downloads/Temps by Coor.xlsx')


for sheet, frame in  frames.items(): # .use .items for python 3.X
    frame.to_excel(writer, sheet_name = sheet, index=False)



worksheet1 = writer.sheets['name']
worksheet2 = writer.sheets['name]
worksheet3 = writer.sheets['name]




worksheet6 =writer.sheets['name']


worksheet7 = writer.sheets['name']

worksheet1.set_column('A:A', 10)
worksheet1.set_column('B:B', 22)
worksheet1.set_column('C:D', 11)
worksheet1.set_column('E:K', 8)
worksheet2.set_column('A:A', 10)
worksheet2.set_column('B:B', 22)
worksheet2.set_column('C:D', 11)
worksheet2.set_column('E:K', 8)
worksheet3.set_column('A:A', 10)
worksheet3.set_column('B:B', 22)
worksheet3.set_column('C:D', 11)
worksheet3.set_column('E:K', 8)
worksheet4.set_column('A:A', 10)
worksheet4.set_column('B:B', 22)
worksheet4.set_column('C:D', 11)
worksheet4.set_column('E:K', 8)
worksheet5.set_column('A:A', 10)
worksheet5.set_column('B:B', 22)
worksheet5.set_column('C:D', 11)
worksheet5.set_column('E:K', 8)
worksheet6.set_column('A:A', 10)
worksheet6.set_column('B:B', 22)
worksheet6.set_column('C:D', 11)
worksheet6.set_column('E:K', 8)
worksheet7.set_column('A:A', 10)
worksheet7.set_column('B:B', 22)
worksheet7.set_column('C:D', 11)
worksheet7.set_column('E:K', 8)
# worksheet8.set_column('A:A', 10)
# worksheet8.set_column('B:B', 22)
# worksheet8.set_column('C:D', 11)
# worksheet8.set_column('E:K', 8)
# worksheet9.set_column('A:A', 10)
# worksheet9.set_column('B:B', 22)
# worksheet9.set_column('C:D', 11)
# worksheet9.set_column('E:K', 8)




worksheet1.set_landscape()
worksheet2.set_landscape()
worksheet3.set_landscape()
worksheet4.set_landscape()
worksheet5.set_landscape()
worksheet6.set_landscape()
worksheet7.set_landscape()
# worksheet8.set_landscape()
# worksheet9.set_landscape()

worksheet1.add_table('A1:K34',{'style':'Table Style Medium 15','header_row': False})
worksheet2.add_table('A1:K34',{'style':'Table Style Medium 15','header_row': False})
worksheet3.add_table('A1:K34',{'style':'Table Style Medium 15','header_row': False})
worksheet4.add_table('A1:K34',{'style':'Table Style Medium 15','header_row': False})
worksheet5.add_table('A1:K34',{'style':'Table Style Medium 15','header_row': False})
worksheet6.add_table('A1:K34',{'style':'Table Style Medium 15','header_row': False})
worksheet7.add_table('A1:K34',{'style':'Table Style Medium 15','header_row': False})
# worksheet8.add_table('A1:K34',{'style':'Table Style Medium 15','header_row': False})
# worksheet9.add_table('A1:K34',{'style':'Table Style Medium 15','header_row': False})










# data with bottom borders
#workbook.add_format()
writer.save()
#writer.close()
f_name = ('filename')


#Send File as Email


import smtplib
from email.message import EmailMessage
from os.path import basename
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
import os


user = 
password = 
smtpsrv = "smtp.office365.com"
smtpserver = smtplib.SMTP(smtpsrv,587)
message = ''
file_location = f_name


msg = MIMEMultipart()
msg['Subject'] = ''
msg['From'] = '
msg['To'] =



 
msg.attach(MIMEText(message, 'plain'))       
   
filename = os.path.basename(file_location)
attachment = open(file_location, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        
msg.attach(part)
        
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.login(user, password)

smtpserver.send_message (msg)
smtpserver.close()


