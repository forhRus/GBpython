# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc
# gaaabbbcccaaaaaaaafа

path_data = r'homework\05\file1.txt' #  путь к тексту для архивации
path_rar = r'homework\05\file2.txt' #  путь к архиву
with open(path_data, 'r') as data:  #  читаем файл, для будущей архивации
    text = data.read()

def create_rar(txt: str):  #  сжимаем
    text_rar =''
    temp = txt[0]
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            temp += txt[i]
        else:
            text_rar += str(len(temp)) + temp[:1]
            temp = txt[i+1]
    else:
        text_rar += str(len(temp)) + temp[:1]  
    return text_rar  

rar = create_rar(text)  #  переменная с архивом
print(f'{text} - {rar}')

with open(path_rar, 'w') as data: #  записываем сжатцю строку в файл
    data.write(rar)

with open(path_rar, 'r') as data: #  считываем сжатую строку для восстанволения
    text1 = data.read()

def create_text(txt: str):  #  сжимаем
    temp_text = ''
    for i in range(0, len(txt), 2):
        temp_text += int(txt[i]) * txt[i+1]
    return temp_text

new_text = create_text(text1)
print(f'{text1} - {new_text}') 




