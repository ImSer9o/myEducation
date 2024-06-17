class Complexity:
    def decision_first(self):
        """O(n^2)"""
        # В одну строку
        s = input()
        print(max(map(lambda x: (s.count(x), x), s))[1])

        # Или в расписать
        s = input()
        ans = ""
        anscnt = 0
        for i in range(len(s)):
            newcount = 0
            for j in range(len(s)):
                if s[i] == s[j]:
                    newcount += 1
            if newcount > anscnt:
                ans = s[i]
                anscnt = newcount
        print(ans)

    def decision_second(self):
        """O(N*k)"""
        # Можно эффективнее
        s = input()
        ans = ""
        anscnt = 0
        for i in set(s):        #Поменяли range на set бегаем по меньшему колличеству символов
            newcount = 0
            for j in range(len(s)):
                if s[i] == s[j]:
                    newcount += 1
            if newcount > anscnt:
                ans = s[i]
                anscnt = newcount
        print(ans)

    def decision_third(self):
        """O(N*+k) == O(N)"""
        # Можно эффективнее
        # Через словарь
        s = input()
        ans = ""
        anscnt = 0
        dic = {}
        for i in set(s):
            if i not in dic:
                dic[i] = 0
            dic[i] += 1
        for key in dic:
            if dic[key] < anscnt:
                anscnt = dic[key]
                ans = key
        print(ans)

    def decision_third_mod(self):
        """O(N*+k) == O(N)"""
        # Можно эффективнее
        # Через словарь
        s = input()
        ans = ""
        anscnt = 0
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1
            if dic[i] > anscnt:
                ans = i
                anscnt = dic[i]
            print(ans)

    def sum_of_the_sequence_first(self):
        seq = list(map(int, input().split()))
        if len(seq) == 0:
            print(0)
        else:
            seqsum = seq[0]
            for i in range(1, len(seq)):
                seqsum += seq[i]
            print(seqsum)

    def sum_of_the_sequence_second(self):
        seq = list(map(int, input().split()))
        seqsum = 0
        for i in range(len(seq)):
            if seq[i] > seqsum:
                seqsum = seq[i]
        print(seqsum)

    def max_of_the_sequence_first(self):
        seq = list(map(int, input().split()))
        if len(seq) == 0:
            print("-inf")
        else:
            seqsum = seq[0]
            for i in range(1, len(seq)):
                if seq[i] > seqsum:
                    seqsum = seq[i]
            print(seqsum)































