class LinearSearch:
    """Линейный поиск"""

    def find_x(self, seq, x):
        """Дана последовательность чисел N.
        Найти первое (левое) вхождение положительного числа X в нее или вывести -1,
        если число Х не встречалось"""
        ans = -1
        for i in range(len(seq)):
            # цикл запишет последнее подходящее число, для этого проверяем было ли оно найдено раньше
            # я бы сломал цикл после нахождения, чтобы не бежать до конца
            if ans == -1 and seq[i] == x:
                ans = i
        return ans

    def find_right_x(self, seq, x):
        """Дана последовательность чисел N.
        Найти последнее (правое) вхождение положительного числа X в нее или вывести -1,
        если число Х не встречалось"""
        ans = -1
        for i in range(len(seq)):
            # цикл запишет последнее подходящее число, для этого ранее реализованная проверка не нужна
            if seq[i] == x:
                ans = i
        return ans

    def finde_max_first(self, seq):
        """Найти максимальное число в последовательности"""
        ans = seq[0]
        for i in seq:
            if i > ans:
                ans = i
        return ans

    def finde_max_second(self, seq):
        """Найти максимальное число в последовательности
        чтобы не копировать объекты в переменную, проще сохранять цикл,
        но такой метод работает дольше"""
        ans = 0
        for i in range(len(seq)):
            if seq[i] > seq[ans]:
                ans = i
        return seq[ans]

    def finde_max_2(self, seq):
        """Найти максимальное число последовательности и второе по величине число
        (такое, которое будет максимальным, если вычеркнуть из последовательности максимальное число)"""

        max_1 = max(seq[0], seq[1])
        max_2 = min(seq[0], seq[1])
        # цикл необходимо делать от 2 чтобы max_2 не переписался
        for i in range(2, len(seq)):
            if seq[i] > max_1:
                max_2 = max_1
                max_1 = seq[i]
            elif seq[i] > max_2:
                max_2 = seq[i]

        return (max_1, max_2)

    def finde_miniven(self, seq):
        """Найти минимальное четное число в последовательности или вывести -1,
        если такого не существует"""
        ans = -1
        for i in range(len(seq)):
            if seq[i] % 2 == 0 and (ans == -1 or seq[i] < ans):
                ans = seq[i]
        return ans

    def short_worlds_first(self, worlds):
        """Вывести все самые короткие слова через пробел"""
        min_len = len(worlds[0])
        for world in worlds:
            if len(world) < min_len:
                min_len = len(world)
        ans = ""
        for world in worlds:
            if len(world) == min_len:
                ans += world + " "
        return ans

    def short_worlds_second(self, worlds):
        """Вывести все самые короткие слова через пробел"""
        # быстрее
        min_len = len(worlds[0])
        for world in worlds:
            if len(world) < min_len:
                min_len = len(world)
        # нуден список чтобы не переписывать все время строку, строка не изменяемый объект
        ans = []
        for world in worlds:
            if len(world) == min_len:
                ans.append(world)
        # формируем строку один раз
        return " ".join(ans)

    def rle(self, s):
        """Нужно написать функцию, которая будет считать количество букв и выводить цифра-буква"""
        last_symbol = [s[0]]
        ans = []
        for i in s[1:]:
            if i != last_symbol[0]:
                ans.append(f"{len(last_symbol)}{last_symbol[0]}")
                last_symbol = [i]
            else:
                last_symbol.append(i)
        ans.append(f"{len(last_symbol)}{last_symbol[0]}")

        return "".join(ans)
