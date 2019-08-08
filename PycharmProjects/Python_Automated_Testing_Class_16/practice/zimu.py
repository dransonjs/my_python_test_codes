class Zimu:
    def __init__(self, string):
        self.string = string

    def appear_count(self):
        dict1 = {}
        str1 = ""
        for i in range(len(self.string)):
            count = 0
            for j in range(len(self.string)-i):
                if self.string[i] == self.string[j+i+1]:
                    count += 1
                str1 = self.string[i]
            dict1.update({str1: count})
        return dict1


if __name__ == '__main__':
    zimu = Zimu("abcba")
    zimu.appear_count()
