import binascii
class GardenbabyTranslator():
    def __init__(self):
        self.hex_2_gardenbaby_dictionary = {
        '0': '阿卡',
        '1': '哇卡',
        '2': '米卡',
        '3': '玛卡',
        '4': '呣',
        '5': '玛卡·巴卡',
        '6': '阿巴',
        '7': '雅卡',
        '8': '伊卡',
        '9': '噢',
        'a': '哈姆',
        'b': '达姆',
        'c': '阿卡嗙',
        'd': '咿',
        'e': '呀',
        'f': '呦'
        }
        self.gardenbaby_2_hex_dictionary = {v: k for k, v in self.hex_2_gardenbaby_dictionary.items()}

    def gardenbaby_2_hex(self, gardenbaby_code):
        out = ''
        try:
            gardenbaby_code = gardenbaby_code.split()
            str_list = list(gardenbaby_code)
            for i in range(len(str_list)):
                c = str_list[i]
                out += self.gardenbaby_2_hex_dictionary[c]
        except KeyError as e:
            raise Exception('Not a gardenbaby code!') from e
        return out


gardenbaby_code = input("请输入要解码的gardenbaby-code：")
t = GardenbabyTranslator
hex_code = t().gardenbaby_2_hex(gardenbaby_code)
text=binascii.unhexlify(hex_code)
print(text.decode('utf-8'))
