class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        total = []
        day = int(date[-2:]) if int(date[-2]) != 0 else int(date[-1])
        total.append(day)
        month = int(date[5:7]) if int(date[5]) != 0 else int(date[6])
        thirtyOne=[1,3,5,7,8,10,12]
        thirty= [9,4,6,11]
        eight = []
        leap = [1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016.]


        checkMonth = month-1
        i=int(checkMonth)
        
        while checkMonth != 0:
            if checkMonth in thirtyOne:
                total.append(31)
            elif checkMonth in thirty:
                total.append(30)
            else:
                if int(date[:4]) in leap and checkMonth == 2:
                    total.append(29)
                else:
                    total.append(28)
            checkMonth-=1

        return sum(total)











