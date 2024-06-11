import datetime
import pytz
import calendar
import os
#1st task
def get_week_number():
    year, month, day = map(int, input().split(', '))
    date = datetime.date(year, month, day)
    week_number = date.isocalendar()[1]
    return week_number

# print(get_week_number())



#2nd task
def get_monday_date():
    year, week = map(int, input().split(', '))
    date = datetime.datetime(year, 1, 1) + datetime.timedelta(days=week*7)
    date = date - datetime.timedelta(days=date.weekday())
    return f"пн {date.strftime('%d %B %H:%M:%S %Y')}"

# print(get_monday_date())



#3rd task
def get_all_sundays(year):
    date = datetime.date(year, 1, 1)
    date += datetime.timedelta(days=(6 - date.weekday()))
    sundays = []
    while date.year == year:
        sundays.append(date.strftime('%d %B %Y'))
        date += datetime.timedelta(days=7)
    return sundays

# print(get_all_sundays(2024))



#4th task
def addYears(date: datetime.date, shift: int) -> str:
    if date.month == 2 and date.day == 29:
        return f"{date.year+shift}-03-01"
    return f"{date.year+shift}-{'0' + str(date.month) if date.month < 10 else str(date.month)}-{'0' + str(date.day) if date.day < 10 else str(date.day)}"

# print(addYears(datetime.date(2015,1,1), -1)) 
# print(addYears(datetime.date(2015,1,1), 0)) 
# print(addYears(datetime.date(2015,1,1), 2)) 
# print(addYears(datetime.date(2000,2,29), 1))



#1st task
def timeGreenwich():
    greenwich = pytz.timezone('Greenwich')
    greenwich_datetime = datetime.datetime.now(greenwich)
    local_datetime = datetime.datetime.now()
    return f"Greenwich: {greenwich_datetime.strftime('%H:%M:%S')}\nLocal: {local_datetime.strftime('%H:%M:%S')}"

# print(timeGreenwich())



#2nd task
def date_diff_days(date1: datetime.date, date2: datetime.date):
    delta = date1 - date2
    return delta.days

# print(date_diff_days(datetime.date(2020, 1, 1), datetime.date(2019, 9, 11)))



#3rd task
def delta_days_to_time(delta: datetime.timedelta):
    return f'''
1. Days: {delta.days}
2. Hours: {delta.days * 24}
3. Minutes: {delta.days * 24 * 60}
4. Seconds: {delta.days * 24 * 60 * 60}'''

# print(delta_days_to_time(datetime.timedelta(days=30)))



#4th task
def generate_html_calendar(year, month):
    cal = calendar.HTMLCalendar(calendar.MONDAY)
    html_calendar = cal.formatmonth(year, month)
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Календарь {month}/{year}</title>
        <style>
            table {{
                border-collapse: collapse;
                width: 100%;
            }}
            th, td {{
                border: 1px solid black;
                padding: 10px;
                text-align: center;
            }}
            th {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        <h1>Календарь на {month}/{year}</h1>
        {html_calendar}
    </body>
    </html>
    """
    
    return html_template

# year = 2024
# month = 6
# html_calendar = generate_html_calendar(year, month)
# with open('calendar.html', 'w', encoding='utf-8') as file:
#     file.write(html_calendar)

# print("HTML-календарь создан и сохранен в файл 'calendar.html'")



#1st task
# with open('prohibited_words.txt', 'r') as proh_words:
#     proh_words_list = []
#     for word in proh_words.read().replace('.', '').split():
#         proh_words_list.append(word)
# with open('unfiltered_text.txt', 'r') as unf_text:
#     text = unf_text.read()
# for word in proh_words_list:
#     text = text.replace(word, '')
# with open('filtered_text.txt', 'w') as filt_text:
#     filt_text.write(text)



#2nd task
translit_dict = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'ye', 'ё': 'yo', 'ж': 'j', 'з': 'z',
    'и': 'i', 'й': 'yy', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
    'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'hh', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'jh',
    'ъ': '"', 'ы': 'yi', 'ь': "'", 'э': 'e', 'ю': 'yu', 'я': 'ya',
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'YE', 'Ё': 'YO', 'Ж': 'J', 'З': 'Z',
    'И': 'I', 'Й': 'YY', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
    'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'HH', 'Ц': 'C', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'JH',
    'Ъ': '', 'Ы': 'YI', 'Ь': "", 'Э': 'E', 'Ю': 'YU', 'Я': 'YA',
}
def translit(text, direction):
    if direction == 'ru_to_en':
        return ''.join(translit_dict.get(char, char) for char in text)
    elif direction == 'en_to_ru':
        reverse_dict = {value: key for key, value in translit_dict.items()}
        result = ''
        i = 0
        while i < len(text):
            match = None
            for key in sorted(reverse_dict.keys(), key=len, reverse=True):
                if text[i:i+len(key)] == key:
                    match = key
                    break
            if match:
                result += reverse_dict[match]
                i += len(match)
            else:
                result += text[i]
                i += 1
        return result
    else:
        return 'Invalid direction'

# print(f"Choose direction:\n1. Russian to English\n2. English to Russian")
# choice = input("Enter 1 or 2: ")
# if choice == '1':
#     direction = 'ru_to_en'
# elif choice == '2':
#     direction = 'en_to_ru'
# else:
#     print("Invalid choice")
#     exit()

# input_file = input("Enter input file name without extension: ")
# output_file = input("Enter output file name without extension: ")
# try:
#     with open(input_file + '.txt', 'r') as f_in:
#         with open(output_file + '.txt', 'w') as f_out:
#             for line in f_in:
#                 translit_text = translit(line.strip(), direction)
#                 print(translit_text)
#                 f_out.write(translit_text + '\n')
#     print(f"Output saved to {output_file}.txt")
# except FileNotFoundError:
#     print(f"File '{input_file}.txt' not found")



#3rd task
def merge_files():
    merged_content = ""
    while True:
        file_name = input("Enter file name without extension or 'quit' to stop: ") + '.txt'
        if file_name.lower() == 'quit.txt':
            break
        try:
            with open(file_name, 'r') as file:
                merged_content += file.read() + '\n'
        except FileNotFoundError:
            print(f"File '{file_name}' not found")
    with open('merged_file.txt', 'w') as merged_file:
        merged_file.write(merged_content)
    print("Merged content saved to 'merged_file.txt'")

# merge_files()



#4th task
def common_characters():
    common_chars = set()
    first_file = True
    while True:
        file_name = input("Enter file name without extension or 'quit' to stop: ") + '.txt'
        if file_name.lower() == 'quit.txt':
            break
        try:
            with open(file_name, 'r') as file:
                file_chars = set(file.read())
                if first_file:
                    common_chars = file_chars
                    first_file = False
                else:
                    common_chars &= file_chars
        except FileNotFoundError:
            print(f"File '{file_name}' not found")
    with open('common_characters.txt', 'w') as output_file:
        output_file.write(''.join(common_chars))
    print("Common characters saved to 'common_characters.txt'")

# common_characters()



#1st task
# def move_files(src_dir, dest_dir):
#     for filename in os.listdir(src_dir):
#         src_file = os.path.join(src_dir, filename)
#         dest_file = os.path.join(dest_dir, filename)
#         if os.path.isfile(src_file):
#             os.rename(src_file, dest_file)
# current_dir = os.getcwd()
# video_dir = os.path.join(current_dir, 'video')
# sub_dir = os.path.join(current_dir, 'sub')
# watch_me_dir = os.path.join(current_dir, 'watch_me')
# if not os.path.exists(watch_me_dir):
#     os.makedirs(watch_me_dir)
# move_files(video_dir, watch_me_dir)
# move_files(sub_dir, watch_me_dir)



#2nd task
# current_directory = os.getcwd()
# for filename in os.listdir(current_directory):
#     if filename.endswith(".jpg"):
#         name, surname = map(str, filename[:-4].split("_"))
#         new_filename = f"{surname}_{name}.jpg"
#         os.rename(filename, new_filename)
# print("File names have been successfully renamed.")



#3rd task
# current_dir = os.getcwd()
# list_dir = os.path.join(current_dir, 'list')
# list_file_path = os.path.join(current_dir, 'list.tsv')
# if not os.path.exists(list_dir):
#     os.makedirs(list_dir)
# with open(list_file_path, 'r') as file:
#     file_names = file.read().splitlines()
# for file_name in file_names:
#     src_file = os.path.join(current_dir, file_name)
#     dest_file = os.path.join(list_dir, file_name)
#     if os.path.isfile(src_file):
#         os.rename(src_file, dest_file)



#4th task
with open(input('Enter file name without extension: ')+'.txt', 'r') as file:
    lines = file.readlines()
lines = lines[:-1]
with open('output.txt', 'w') as file:
    file.writelines(lines)
print('Last line removed and saved to output.txt')