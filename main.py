from random import randint
from copy import deepcopy


class Fuild:

    def __init__(self) -> None:
        self.input_fuild = [[tuple((i for i in range(1, 6))) for j in range(5)] for k in range(5)]
        self.result = None

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


        
    def change(self, x, y, val) -> None:
        self.input_fuild[x][y] = val

        if self.result:
            if self.result[x][y] == val:
                self.solved = True
                self.fuild = deepcopy(self.result)

            else:
                #self.result = None
                self.solved = False
                self.failed = False


    def solve(self) -> None:
        self.fuild = deepcopy(self.input_fuild)

        for i in range(5):
            for j in range(5):
                self.update((i, j))

        while not self.solved:
            if not self.failed:
                self.solve_cell()

            else:
                break

        if not self.failed:
            self.result = deepcopy(self.fuild)

        else:
            print('failed to solve')
            if input('retruy? (y/n)') == 'y':
                self.solve()



    def __str__(self) -> str:

        if not self.solved:
            self.solve()

        if not self.failed:
            answ = ''
            for i in range(5):
                for j in range(5):
                    answ += str(self.result[i][j])
                    answ += ' '

                answ += '\n'

            del self.fuild
            self.solved = False
            return answ
        
        else:
            self.failed = False
            return 'can\'t solve given layout\n'

            


def main():
    obj = Fuild()
    obj.change(0, 0, 1)
    print(obj)
    obj.change(0, 1, 1)
    print(obj)
    obj.change(0, 1, 2)
    print(obj)


    


if __name__ == '__main__':
    main()
