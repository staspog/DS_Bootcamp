import sys

def caesar():
    # Проверяем количество аргументов
    if len(sys.argv) != 4:
        raise Exception("Invalid number of arguments")
    
    # Получаем аргументы
    mode = sys.argv[1]
    text = sys.argv[2]
    
    # Проверяем, что третий аргумент - число
    try:
        shift = int(sys.argv[3])
    except ValueError:
        raise Exception("Shift must be an integer")
    
    # Проверяем режим
    if mode not in ["encode", "decode"]:
        raise Exception("Incorrect mode. Use 'encode' or 'decode'")
    
    # Для декодирования сдвиг в обратную сторону
    if mode == "decode":
        shift = -shift
    
    result = ""
    
    # Обрабатываем каждый символ
    for char in text:
        # Проверяем, что символ поддерживается (не кириллица и др.)
        if ord(char) > 127 and not (32 <= ord(char) <= 126):
            raise Exception("The script does not support your language yet")
        
        # Буквы нижнего регистра
        elif 'a' <= char <= 'z':
            # Применяем сдвиг по модулю 26 (количество букв в английском алфавите)
            shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += shifted
        
        # Буквы верхнего регистра
        elif 'A' <= char <= 'Z':
            shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += shifted
        
        # Остальные символы (пробелы, цифры, знаки) не шифруем
        else:
            result += char
    
    print(result)

if __name__ == '__main__':
    try:
        caesar()
    except Exception as e:
        print(str(e))