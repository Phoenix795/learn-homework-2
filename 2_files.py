"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding='utf-8') as recieved_file:
        read_text = recieved_file.read()
        common_line = read_text.replace('\n', ' ').replace('  ', ' ')
        words_from_file = common_line.split(sep=' ')
        print('Длинну получившейся строки: {} символов'.format(len(common_line)))
        print('Количество слов в тексте: {}'.format(len(words_from_file)))
    
    with open('referat2.txt', 'w', encoding='utf-8') as file_with_result:
        file_with_result.write(read_text.replace('.', '!'))

if __name__ == "__main__":
    main()
