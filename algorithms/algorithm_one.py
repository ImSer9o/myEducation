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
        """O(N*k)"""
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
                ans =   key


























