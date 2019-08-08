class Zimu:
    def __init__(self, string):
        self.string = string

    def appear_count(self):
        dict1 = {}
        for i in self.string[:len(self.string)-1]:  # 例abcda，只取到d
            count = 1
            for j in self.string[self.string.index(i)+1:]:  # 每一次遍历判断都在i的后一位开始
                if i == j:
                    count += 1
            dict1.update({i: count})
        return dict1

    def sort(self):
        return sorted(self.appear_count().items(), key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    zimu = Zimu("abcdeabacfdec")
    print(zimu.appear_count())
    print(zimu.sort())
