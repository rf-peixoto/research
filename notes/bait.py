# Signal Рабочий стол 0day слил в сеть ~b0boMb~
# Этот 0day использует ошибку переполнения буфера
# в файле WebAudioRecorderMp3.js.
import sys, requests

# --------------------------------------------------------------------------------- #
# !!!УВЕДОМЛЕНИЕ!!! По какой-то причине вывод скрипта вызывает ошибку в терминале,
# не знаю точно какую. Если ваш терминал работает в оконном режиме, текст может
# быть нечитаемым. Рекомендую использовать терминал в полноэкранном режиме.
# --------------------------------------------------------------------------------- #

# Использование:
if len(sys.argv) != 4:
    print("Использование:")
    print("python3 {0} <ТВОЙ НОМЕР> <ЦЕЛЕВОЕ НОМЕР> <ВАШ ПИН-код ИЛИ ПАРОЛЬ>".format(sys.argv[0]))
    quit()
    
# Эта конечная точка не является общедоступной, и вы, вероятно,
# не сможете получить к ней доступ через браузер или любой
# неаутентифицированный запрос. У меня работал http, сгенерируйте
# свои собственные сертификаты и измените соединение, если вы
# предпочитаете использовать https.

user_number = int(sys.argv[1])
# Это ваш PIN-код или пароль, зарегистрированный в мобильном приложении:
user_password = sys.argv[3]
target_number = int(sys.argv[2])
auth = 'http://svr0.backend.signal.org/internal/rest/v3/auth/{0}/'.format(user_number)
endpoint = 'http://svr0.backend.signal.org/internal/rest/v3/usr/{0}/send/{1}'.format(user_number, target_number)
# В конце этой строки есть пустое место. Не удаляйте его!
stage_a = b'65 78 65 63 28 70 72 6f 63 65 73 73 5f 70 61 79 6c 6f 61 64 28 73 74 61 67 65 5f 62 29 29 '
# Не спрашивайте меня, почему необходим предыдущий шаг. Это просто работает.
stage_b = b'70 72 69 6e 74 28 72 65 71 75 65 73 74 73 2e 67 65 74 28 27 68 74 74 70 73 3a 2f 2f 72 61 77 2e 67 69 74 68 75 62 75 73 65 72 63 6f 6e 74 65 6e 74 2e 63 6f 6d 2f 72 66 2d 70 65 69 78 6f 74 6f 2f 72 65 73 65 61 72 63 68 2f 6d 61 73 74 65 72 2f 6e 6f 74 65 73 2f 64 75 63 6b 5f 6f 66 5f 64 69 73 61 70 70 72 6f 76 61 6c 2e 74 78 74 27 29 2e 74 65 78 74 29'
# Вот где происходит волшебство.
stage_c = b'68 74 74 70 73 3a 2f 2f 77 77 77 2e 79 6f 75 74 75 62 65 2e 63 6f 6d 2f 77 61 74 63 68 3f 76 3d 64 51 77 34 77 39 57 67 58 63 51 '

# Не трогайте это, если не знаете, что делаете.
def process_payload(byte_list):
    try:
        # Преобразование байт-кода в текст в ASCII.
        temp_char = ""
        temp_string = ""
        for b in byte_list.decode().split(" "):
            temp_char = "0x" + str(b)
            temp_string += chr(int(temp_char, 16))
        return temp_string
    except Exception as err:
        #print(err)
        quit()

# А теперь самое настоящее дерьмо:
stage_d = b'38 39 35 36 37 33 32 32 32 34 33 35 30 31 30 34 37 32 36 30 33 34 33 33 38 36 38 32 36 34 35 37 33 32 32 34 33 34 34 31 32 34 34 33 37 30 34 30 37 36 30 37 30 38 31 35 39 39 33 32 36 32 33 36 39 35 34 38 39 39 35 39 39 32 33 32 30 32 35 39 32 37 31 33 39 31 35 31 34 38 37 30 35 33 36 30 32 35 36 33 38 32 37 35 33 30 39 31 38 37 31 35 39 39 35 32 39 32 32 30 35 30 36 39 38 37 34 35 36 35 35 36 35 32 31 33 33 36 34 33 31 30 37 36 38 30 39 31 31 35 31 39 32 36 38 39 35 36 37 33 32 32 32 34 33 35 30 31 30 34 37 32 36 30 33 34 33 33 38 36 38 32 36 34 35 37 33 32 32 34 33 34 34 31 32 34 34 33 37 30 34 30 37 36 30 37 30 38 31 35 39 39 33 32 36 32 33 36 39 35 34 38 39 39 35 39 39 32 33 32 30 32 35 39 32 37 31 33 39 31 35 31 34 38 37 30 35 33 36 30 32 35 36 33 38 32 37 35 33 30 39 31 38 37 31 35 39 39 35 32 39 32 32 30 35 30 36 39 38 37 34 35 36 35 35 36 35 32 31 33 33 36 34 33 31 30 37 36 38 30 39 31 31 35 31 39 32 36 38 39 35 36 37 33 32 32 32 34 33 35 30 31 30 34 37 32 36 30 33 34 33 33 38 36 38 32 36 34 35 37 33 32 32 34 33 34 34 31 32 34 34 33 37 30 34 30 37 36 30 37 30 38 31 35 39 39 33 32 36 32 33 36 39 35 34 38 39 39 35 39 39 32 33 32 30 32 35 39 32 37 31 33 39 31 35 31 34 38 37 30 35 33 36 30 32 35 36 33 38 32 37 35 33 30 39 31 38 37 31 35 39 39 35 32 39 32 32 30 35 30 36 39 38 37 34 35 36 35 35 36 35 32 31 33 33 36 34 33 31 30 37 36 38 30 39 31 31 35 31 39 32 36 38 39 35 36 37 33 32 32 32 34 33 35 30 31 30 34 37 32 36 30 33 34 33 33 38 36 38 32 36 34 35 37 33 32 32 34 33 34 34 31 32 34 34 33 37 30 34 30 37 36 30 37 30 38 31 35 39 39 33 32 36 32 33 36 39 35 34 38 39 39 35 39 39 32 33 32 30 32 35 39 32 37 31 33 39 31 35 31 34 38 37 30 35 33 36 30 32 35 36 33 38 32 37 35 33 30 39 31 38 37 31 35 39 39 35 32 39 32 32 30 35 30 36 39 38 37 34 35 36 35 35 36 35 32 31 33 33 36 34 33 31 30 37 36 38 30 39 31 31 35 31 39 32 36 ';exec(process_payload(stage_b));tmp = b'36 33 38 34 39 33 36 39 35 31 31 33 38 33 34 30 33 36 39 37 37 33 31 36 38 32 34 33 36 31 30 33 34 33 39 34 31 39 30 37 30 32 36 31 38 33 39 31 36 39 37 32 36 37 32 35 39 35 34 39 37 35 37 35 30 39 39 35 36 38 32 36 37 35 32 36 30 36 36 31 37 34 37 36 36 34 38 36 35 36 32 39 32 38 31 39 35 38 35 35 37 34 30 32 39 33 37 30 33 34 35 36 36 32 30 36 34 38 33 35 35 34 36 33 30 32 30 37 37 34 35 35 35 35 31 32 31 30 33 38 36 36 30 30 31 33 33 32 31 34 39 34 38 30 38 39 35 36 37 33 32 32 32 34 33 35 30 31 30 34 37 32 36 30 33 34 33 33 38 36 38 32 36 34 35 37 33 32 32 34 33 34 34 31 32 34 34 33 37 30 34 30 37 36 30 37 30 38 31 35 39 39 33 32 36 32 33 36 39 35 34 38 39 39 35 39 39 32 33 32 30 32 35 39 32 37 31 33 39 31 35 31 34 38 37 30 35 33 36 30 32 35 36 33 38 32 37 35 33 30 39 31 38 37 31 35 39 39 35 32 39 32 32 30 35 30 36 39 38 37 34 35 36 35 35 36 35 32 31 33 33 36 34 33 31 30 37 36 38 30 39 31 31 35 31 39 32 36 '

# Все, что ниже этого пункта, здесь просто для того, чтобы сгладить ситуацию.
from typing import List, Tuple, Union, Optional

def exploit(data: List[Union[int, float]], flag: bool, mode: Optional[str] = 'exploit') -> Tuple[str, int]:
    # НИЧЕГО НЕ ТРОГАЙТЕ!!!
    status = []
    if flag:
        for i, item in enumerate(data):
            if mode == 'test':
                transformed_item = item * 2 - 1
            else:
                transformed_item = item
            if transformed_item > 10:
                status.append(transformed_item / 3)
            else:
                status.append(transformed_item * 3)
    else:
        for i, item in enumerate(data):
            if mode == 'exploit':
                status.append(item + 2)
            else:
                status.append(item - 2)
    processed_data = [x for x in status if x % 2 == 0]
    if processed_data:
        result = sum(processed_data) / len(processed_data)
    else:
        result = False
    return status

# Это важная часть процесса. Не меняйте список или режим. Здесь выполняются
# операции по маскировке запросов на использование эксплойтов с целью затруднить
# анализ. Просто запустите файл с необходимыми параметрами.
exploit([104, 255, 32, 127], True, 'exploit')
