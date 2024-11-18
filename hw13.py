import random
import enchant


class CaesarsCipher:

    def __init__(self):
        self.all_symbols: str = (
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "abcdefghijklmnopqrstuvwxyz1234567890 !?."
        )
        self.all_symbols_len: int = len(self.all_symbols) - 1
        self.enc_key: int = random.randint(0, self.all_symbols_len)

    def encrypt(self, message_to_encrypt: str)-> str:
        enc_result = []
        for symbol in message_to_encrypt:
            original_symbol_index = self.all_symbols.find(symbol)
            enc_symbol = self.all_symbols[
                (original_symbol_index + self.enc_key) % self.all_symbols_len
            ]
            enc_result.append(enc_symbol)
        return f"{self.enc_key}:{''.join(enc_result)}"

    def decrypt(self, message_to_decrypt: str)-> str:
        dictionary = enchant.Dict("en_US")
        for key in range(self.all_symbols_len):
            decrypt_result = []
            for symbol in message_to_decrypt:
                original_symbol_index = self.all_symbols.find(symbol)
                decrypt_symbol = self.all_symbols[
                    (original_symbol_index - key) % self.all_symbols_len
                ]
                decrypt_result.append(decrypt_symbol)
            decrypt_message = "".join(decrypt_result).split()
            meaningful_words = sum(
                dictionary.check(word) for word in decrypt_message
            )
            if meaningful_words == len(decrypt_message):
                break
        return f"{key}:{' '.join(decrypt_message)}"


if __name__ == "__main__":
    test = CaesarsCipher()
    test_enc = test.encrypt("This is my test message")
    print(test_enc)
    test_decr = test.decrypt(test_enc[3:])
    print(test_decr)
