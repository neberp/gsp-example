import gspread

sa = gspread.service_account()
sh = sa.open("Test")

wks = sh.worksheet("Sheet")

print('Rows: ', wks.row_count)
print('Cols: ', wks.col_count)

#print(wks.acell('A9').value)

#print(wks.get_all_records())

#wks.update('A3', 'FFFF')
wks.update('E3', '=UPPER(B2)', raw=False)