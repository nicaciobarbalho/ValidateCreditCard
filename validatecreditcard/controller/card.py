import re

class Card(object) :

    def valid(self, number):
        prog = re.compile(r'(^(4|5|6))[0-9]{3}(-)?[0-9]{4}(-)?[0-9]{4}(-)?[0-9]{4}')



        if prog.search(number):
            number = number.replace('-', '')

            if len(number) != 16:
                return False

            prog = re.compile(r'^([0-9])\1{3,}')

            for i in range(0, 4):
                if prog.search(number[i*4:((i * 4) + 4)]):
                    return False


        else:
            return False


        return True
