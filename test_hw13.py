from hw13.hw13 import CaesarsCipher


def test_encryption_decryption():
    """
    Проверка шифрования и дешифрования.
    Сообщение должно быть расшифровано в исходное состояние.
    """
    test = CaesarsCipher()

    original_message = "Hello world! This is my test message!"

    encrypted_message = test.encrypt(original_message)
    message_to_decrypt = encrypted_message.split(':')[1]
    decrypted_message = test.decrypt(message_to_decrypt)

    assert original_message == decrypted_message.split(':')[1], (
        "Расшифрованное сообщение не совпадает с оригиналом!"
    )


def test_encryption_consistency():
    """
    Проверка на то, что одно и то же сообщение всегда будет шифроваться
    по-разному из-за случайного ключа.
    """

    cipher_1 = CaesarsCipher()
    cipher_2 = CaesarsCipher()

    original_message = "Test Message"

    encrypted_message_1 = cipher_1.encrypt(original_message)
    encrypted_message_2 = cipher_2.encrypt(original_message)

    assert encrypted_message_1 != encrypted_message_2, (
        "Шифрованные " "сообщения должны " "быть разными!"
    )
