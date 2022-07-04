from random import choice, randint


class Fuild:

    def __init__(self) -> None:
        self.fuild = [[tuple((i for i in range(1, 6))) for j in range(5)] for k in range(5)]

        self.solved = False
        self.failed = False

    def solve_cell(self) -> None: #need to rewrite this shit at some point
        """ 
        find cell with minimum unsertanty and fill it
        """
        min_len = 5
        coord = None

        self.solved = True
        for i in range(5):
            for j in range(5):
                if isinstance(self.fuild[i][j], tuple):
                    self.solved = False

                    length = len(self.fuild[i][j])


                    if length == 0:
                        self.failed = True
                        return None

                    elif length <= min_len:
                        min_len = length
                        coord = (i, j)

        if self.solved == True:
            return None

        if coord == None:
            coord = (randint(0, 4) for i in range(2))

        if isinstance(self.fuild[coord[0]][coord[1]], int):
            print('hi')


        self.fuild[coord[0]][coord[1]] = self.fuild[coord[0]][coord[1]][randint(0, min_len - 1)]
        self.update(coord)


    def update(self, coord) -> None:
        """
        updates cells chanses when cell is desided
        """
        val = self.fuild[coord[0]][coord[1]]
        for i in range(5):
            if i != coord[0]:
                j = coord[1]
                
                if isinstance(self.fuild[i][j], tuple) and val in self.fuild[i][j]:

                    self.fuild[i][j] = list(self.fuild[i][j])
                    self.fuild[i][j].remove(val)
                    self.fuild[i][j] = tuple(self.fuild[i][j])

                    if len(self.fuild[i][j]) == 0:
                        self.failed = True
                        return None

                    elif len(self.fuild[i][j]) == 1:
                        self.fuild[i][j] = self.fuild[i][j][0]
                        self.update((i, j))
        
        for j in range(5):
            if j != coord[1]:
                i = coord[0]
                
                if isinstance(self.fuild[i][j], tuple) and val in self.fuild[i][j]:
                    
                    self.fuild[i][j] = list(self.fuild[i][j])
                    self.fuild[i][j].remove(val)
                    self.fuild[i][j] = tuple(self.fuild[i][j])

                    if len(self.fuild[i][j]) == 1:
                        self.fuild[i][j] = self.fuild[i][j]
                        self.update((i, j))        


        
    def change(self):
        pass

    def solve(self):
        while not self.solved:
            if not self.failed:
                self.solve_cell()

            else:
                print('shit')
                self.solved = True


    def __str__(self) -> str:

        if not self.solved:
            self.solve()

        if self.solved:
            answ = ''
            for i in range(5):
                for j in range(5):
                    answ += str(self.fuild[i][j])
                    answ += ' '

                answ += '\n'
            return answ


        else:
            return f'lol what {self.solved}, {self.failed}'
            


def main():
    obj = Fuild()
    print(obj)


if __name__ == '__main__':
    main()
