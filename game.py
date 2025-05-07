import random
import sys
print("数あてゲームを始めます10回以内に正解となる答えを当ててください。")
print("答えの数の範囲は1〜100です")

#二分探索推奨

answer=random.randrange(start=1,stop=100)
guess=int(input("あなたが予想する数字:"))
tries=1

while(guess !=answer):
    #予想が外れている限り、whileの中身を実行する
    if(guess>answer):
        print("あなたの予想した数は答えより大きいです")
    else:
        print("あなたの予想した数は答えより小さいです")
    
    tries = tries+1
    if(tries>10):
      print("残念あなたは、10回以内にこの問題に正解できませんでした。")
      
    if(tries>10):
        sys.exit()
      

    guess=int(input("あなたが予想する数字:"))

#whileが終了したため、予想が的中した。
print("正解です答えは{}でした".format(answer))
print("あなたの試行回数は{}でした".format(tries))
