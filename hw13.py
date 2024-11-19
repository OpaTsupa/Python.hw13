import random
import enchant


class CaesarsCipher:
    def __init__(self) -> None:
        """
        Инициализация класса CaesarCipher.

        Класс для шифрования и дешифрования текста с использованием шифра
        Цезаря.
        Ключ для шифрования генерируется случайным образом.
        """
        self.all_symbols: str = (
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "abcdefghijklmnopqrstuvwxyz1234567890 !?."
        )
        self.all_symbols_len: int = len(self.all_symbols)
        self.enc_key: int = random.randint(0, self.all_symbols_len - 1)
 #       self.enc_key = 34

    def encrypt(self, message_to_encrypt: str) -> str:
        """
        Шифрует сообщение с использованием шифра Цезаря.

        Метод перебирает каждый символ в сообщении, находит его индекс в
        строке `all_symbols`, прибавляет к нему значение ключа и получает
        новый зашифрованный символ.
        Если новый индекс выходит за пределы строки, отсчет идет с начала.

        Аргументы:
            message_to_encrypt (str): Сообщение для шифрования.

        Возвращает:
            str: Зашифрованное сообщение, состоящее из ключа и зашифрованного
            текста.
        """
        enc_result: list[str] = []
        for symbol in message_to_encrypt:
            original_symbol_index: int = self.all_symbols.find(symbol)
            enc_symbol: str = self.all_symbols[
                (original_symbol_index + self.enc_key) % self.all_symbols_len
            ]
            enc_result.append(enc_symbol)
        return f"{self.enc_key}:{''.join(enc_result)}"

    def decrypt(self, message_to_decrypt: str) -> str:
        """
        Дешифрует зашифрованное сообщение, используя шифр Цезаря.

        Метод перебирает возможные значения ключа, пока не найдет такой,
        при котором дешифрованное сообщение состоит из слов, проверенных на
        орфографию.Для проверки используется словарь для английского языка.

        Аргументы:
            message_to_decrypt (str): Сообщение для дешифрования.

        Возвращает:
            str: Дешифрованное сообщение с подобранным ключом.
        """
        dictionary = enchant.Dict("en_US")
#        key: int = 0
#        decrypt_message: str = ''
        for key in range(self.all_symbols_len):
            decrypt_result: list[str] = []
            for symbol in message_to_decrypt:
                original_symbol_index: int = self.all_symbols.find(symbol)
                decrypt_symbol: str = self.all_symbols[
                    (original_symbol_index - key) % self.all_symbols_len
                ]
                decrypt_result.append(decrypt_symbol)
            decrypt_message = "".join(decrypt_result).split()
            meaningful_words: int = sum(
                dictionary.check(word) for word in decrypt_message
            )
            if meaningful_words >= len(decrypt_message) / 2:
                break
        return f"{key}:{' '.join(decrypt_message)}"


if __name__ == "__main__":
    test = CaesarsCipher()
    test_enc = test.encrypt("Hello world! This is my test message!")
    print(test_enc)
    test_decr = test.decrypt(test_enc.split(':')[1])
    print(test_decr)
