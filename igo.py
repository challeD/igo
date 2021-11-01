
roodbet = 3

boad = [[0 for i in range(roodbet)] for j in range(roodbet)]

yosoku_boad = []

def print_boad(boad):
    print("-----")
    for i in range(roodbet):
        print(boad[i])

def judge():
    for i in range(roodbet):
        for j in range(roodbet):
            if boad[i][j] == "●":
                print(i,j)
    

#i-1,jとi,j+1とi+1,jとi,j-1の判定を行う。
def yosoku(i,j):
    #北から時計回りに計算。
    if i-1 <= 0:
        if boad[i-1][j] != "●":
            boad[i-1][j] = 1
    if j+1 <= roodbet:
        if boad[i][j+1] != "●":
            boad[i][j+1] = 1
    if i+1 <= roodbet:
        if boad[i+1][j] != "●":
            boad[i+1][j] = 1
    if j-1 <= 0:
        if boad[i][j-1] != "●":
            boad[i][j-1] = 1

    yosoku_boad = boad

    print(yosoku_boad)

#yosoku()では塊の判定をした方がいい？


if __name__ == "__main__":

    boad[1][1] = "●"
    boad[1][0] = "●"
    judge()
    yosoku(1,1)
    yosoku(1,0)
    print(yosoku_boad)
    print_boad(boad)