import openpyxl

# 엑셀파일을 python에 들고오기 위한 경로 설정
book = openpyxl.load_workbook("stats_104102.xlsx")


# 워크시트를 사용하는, 가져오는 방법
print(book.get_sheet_names())
print(book.get_sheet_by_name("stats_104102"))
sheet = book.worksheets[0]