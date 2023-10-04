
import time 
import random ,sys
import pandas as pd

def get_value_from_dice():
    # time.sleep(1)
    val=random.randint(1,6)
    # print("dice ",val)
    return val
def is_win(player,pos,grid_max_val):
    if grid_max_val == pos:
        print(player," won")
        return True
    return False

def pos_mat(grid_max_val,grid_size):
    dic={}
    j=1
    k=0
    grid=1
    kl=grid_size
    for i in range(0,grid_max_val):
        fac=i//grid_size
        j=i%grid_size
        gb=(i+1)%grid_size

        if gb==0:
            gb=grid_size


        if (fac+1)%2==0:
            gb=kl
            kl-=1
            if kl==0:
                kl=grid_size
            

        dic[i+1]=(gb,fac+1)
       
    return dic

def start_game():
    grid_size= int(input( "enter grid size"))
    print(grid_size)
    grid_max_val= grid_size*grid_size
    # print("grid",grid_max_val)
    print(pos_mat(grid_max_val,grid_size))
    dic=pos_mat(grid_max_val,grid_size)
    print("dic")
    player1 ,player2,player3,player4 = 0,0,0,0
    player_list=["Player1","Player2","Player3","Player4"]
    roll_his1=[]
    roll_his2=[]
    roll_his3=[]
    roll_his4=[]
    pos_his1=[]
    pos_his2=[]
    pos_his3=[]
    pos_his4=[]
    win=""
    current_pos1=[]
    current_pos2=[]
    current_pos3=[]
    current_pos4=[]
    mod_grid= grid_size+1
    while True:
        dice_val=get_value_from_dice()
        roll_his1.append(dice_val)
        if player1+dice_val<= grid_max_val:

            player1+=dice_val
        pos_his1.append(player1)
        current_pos1.append(dic.get(player1))

        if is_win(player_list[0] ,player1,grid_max_val):
            # sys.exit(1)
            win=player_list[0]
            break

        dice_val=get_value_from_dice()
        roll_his2.append(dice_val)
        if player2+dice_val<= grid_max_val:
            player2+=dice_val
        pos_his2.append(player2)
        current_pos2.append(dic.get(player2))

        if is_win(player_list[1] ,player2,grid_max_val):
            # sys.exit(1)
            win=player_list[1]
            break

        dice_val=get_value_from_dice()
        roll_his3.append(dice_val)
        if player3+dice_val<= grid_max_val:

            player3+=dice_val
        pos_his3.append(player3)
        current_pos3.append(dic.get(player3))

        if is_win(player_list[2] ,player3,grid_max_val):
            # sys.exit(1)
            win=player_list[2]
            break

        dice_val=get_value_from_dice()
        roll_his4.append(dice_val)
        if player4+dice_val<= grid_max_val:

            player4+=dice_val
        pos_his4.append(player4)
        current_pos4.append(dic.get(player4))
        # import ipdb;ipdb.set_trace()
        # print(pos_his1,pos_his2,pos_his3,pos_his4)
        
        if is_win(player_list[3] ,player4,grid_max_val):
            win=player_list[3]
            break
    rollhis=[]
    rollhis.append(roll_his1)
    rollhis.append(roll_his2)
    rollhis.append(roll_his3)
    rollhis.append(roll_his4)
    poshis=[]
    poshis.append(pos_his1)
    poshis.append(pos_his2)
    poshis.append(pos_his3)
    poshis.append(pos_his4)
    winstatus=[]
    for i in range(0,len(player_list)):
        if win == player_list[i]:
            winstatus.append(1)
        else:
            winstatus.append(0)
    print(winstatus)
    pos_coor=[current_pos1,current_pos2,current_pos3,current_pos4]
    data={"Players":player_list,"Dice Roll History":rollhis,"Position History":poshis,"Win Status":winstatus, "Position Coordinate":pos_coor}
    df =pd.DataFrame(data)
    print("Game is Over ",win ,"has won the game")
    print("DATAFRAME\n\n",df)


        
# 7 8 9
# 6 5 4
# 1 2 3

if __name__== "__main__":
    
    start_game()