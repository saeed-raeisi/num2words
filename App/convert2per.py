"""
split number
convert
print
"""

hundreds = {
    "0": "",
    "1": "هزار ",
    "2": "میلیون ",
    "3": "میلیارد ",
    "4": "تریلیون ",

}

numbers = {
    "0": "",
    "1": "یک",
    "2": "دو",
    "3": "سه",
    "4": "چهار",
    "5": "پنج",
    "6": "شش",
    "7": "هفت",
    "8": "هشت",
    "9": "نه",
    "10": "ده",
    "11": "یازده",
    "12": "دوازده",
    "13": "سیزده",
    "14": "چهارده",
    "15": "پانزده",
    "16": "شانزده",
    "17": "هفده",
    "18": "هجده",
    "19": "نوزده",
    "20": "بیست",
    "30": "سی",
    "40": "چهل",
    "50": "پنجاه",
    "60": "شصت",
    "70": "هفتاد",
    "80": "هشتاد",
    "90": "نود",
    "100": "صد",
    "200": "دویست",
    "300": "سیصد",
    "400": "چهارصد",
    "500": "پانصد",
    "600": "ششصد",
    "700": "هفتصد",
    "800": "هشتصد",
    "900": "نهصد",
    "1000": "هزار",

}

output = ""


class convert2per:
    output_per = ""

    def __init__(self, number):

        # number int
        print(number)
        # split 3 digit number to list
        list = self.splite2three(number)
        print(list)
        self.convert(list, len(list))

    def splite2three(self, number):
        list = []
        while number > 0:
            list.append(number % 1000)
            number = number // 1000
        return list

    def convert(self, list, size):
        global output
        output = ""
        for i in reversed(range(size)):
            if list[i] <= 20:
                output = output + numbers.get(str(list[i]))
                if numbers.get(str(list[i])) != "":
                    output = output + " " + hundreds.get(str(i))
            elif list[i] < 100:
                output = output + self.conver2Less100(list[i])
                output = output + " " + hundreds.get(str(i))
            elif list[i] < 1000:
                output = output + self.conver2Less1000(list[i])
                # last digit
                if i != 0:
                    output = output + " " + hundreds.get(str(i))
                    # 100 000 remove "و"
                    if list[i] != 100:
                        try:
                            if list[i - 1] != 0:
                                output = output + " و "
                        except:
                            output = output

    def conver2Less100(self, number):
        # 88 80 + 8
        temp = number
        less_ten = temp % 10
        temp = temp - less_ten
        per_num = numbers.get(str(temp)) + " و " + numbers.get(str(less_ten))
        return per_num

    def conver2Less1000(self, number):
        # 888 800 + 80 + 8
        temp = number
        less_ten = temp % 10
        temp = temp - less_ten
        less_hundred = temp % 100
        temp = temp - less_hundred
        per_num = numbers.get(str(temp)) + " "
        if less_ten + less_hundred != 0:
            per_num = per_num + self.conver2Less100(less_hundred + less_ten)
        return per_num

    # get result for __init__
    def get_result(self):
        return output
