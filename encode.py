
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


    def hex_2_gardenbaby(self, hex_code):
        out = ''
        for c in hex_code:
            try:
                out += self.hex_2_gardenbaby_dictionary[c] + ' '
            except KeyError as e:
                pass
        return out


text = input("请输入要转换的文本：")
hex_code = "".join([hex(ord(c)).replace('0x', '') for c in text])
t = GardenbabyTranslator
gardenbaby_code = t().hex_2_gardenbaby(hex_code)
print(gardenbaby_code)