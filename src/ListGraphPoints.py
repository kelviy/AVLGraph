class ListGraphPoints:
    def __init__(self):
        self.countx = []
        self.county = []
        self.searchx = []
        self.searchy = []

    def add_count_point(self, x, y):
        self.countx.append(x)
        self.county.append(y)

    def add_search_point(self, x, y):
        self.searchx.append(x)
        self.searchy.append(y)

    def get_insert_min(self):
        return self.get_min_count(self.countx, self.county)

    def get_insert_max(self):
        return self.get_max_count(self.countx, self.county)

    def get_insert_average(self):
        return self.get_average_count(self.countx, self.county)

    def get_search_min(self):
        return self.get_min_count(self.searchx, self.searchy)

    def get_search_max(self):
        return self.get_max_count(self.searchx, self.searchy)

    def get_search_average(self):
        return self.get_average_count(self.searchx, self.searchy)

    def get_min_count(self, listx, listy):
        group = listx[0]
        min_value = listy[0]
        min_listx = []
        min_listy = []

        for i in range(len(listx)):
            if group != listx[i]:
                min_listx.append(group)
                min_listy.append(min_value)

                group = listx[i]
                min_value = listy[i]
            else:
                if min_value > listy[i]:
                    min_value = listy[i]

        min_listx.append(group)
        min_listy.append(min_value)

        return min_listx, min_listy

    def get_max_count(self, listx, listy):
        group = listx[0]
        max_value = listy[0]
        max_listx = []
        max_listy = []

        for i in range(len(listx)):
            if group != listx[i]:
                max_listx.append(group)
                max_listy.append(max_value)

                group = listx[i]
                max_value = listy[i]
            else:
                if max_value < listy[i]:
                    max_value = listy[i]

        max_listx.append(group)
        max_listy.append(max_value)

        return max_listx, max_listy

    def get_average_count(self, listx, listy):
        group = listx[0]
        sum = 0
        count = 0
        average_listx = []
        average_listy = []

        for i in range(len(listx)):
            if group != listx[i] and count != 0:
                average_listx.append(group)
                average_listy.append(round(sum / count))

                group = listx[i]
                sum = 0
                count = 0
                sum += listy[i]
                count += 1
            else:
                sum += listy[i]
                count += 1

        average_listx.append(group)
        average_listy.append(round(sum / count))

        return average_listx, average_listy