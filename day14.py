

def print_board(board):
    for row in board:
        print(row)

if __name__ == '__main__':
    box = [['#','.'],['0','.']]
    with open('input.txt') as fp:
        box = [list(line.strip()) for line in fp.readlines()] #set box to input.txt
    print_board(box)

    for row in range(len(box)): #(for row = 0; row<box.length(); row++)
        for column in range(len(box[row])):
            #print(row, column, box[row][column])
            if box[row][column]!='.':
                continue
            
            for row2 in range(row+1, len(box)):
                if box[row2][column] == '.':
                    continue
                #if box[row2][column] == '#':
                    #break
                else:
                    if box[row2][column] == 'O':
                        box[row][column] = 'O'
                        box[row2][column] = '.'
                    break
    print()
    print_board(box)
    score = 0
    for row in range(len(box)): #(for row = 0; row<box.length(); row++)
        for column in range(len(box[row])):
            if box[row][column] == 'O':
                score += len(box)-row
    print(score)


