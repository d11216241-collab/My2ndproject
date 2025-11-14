#猜數字遊戲
import random
def guess_number_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("歡迎來到猜數字遊戲！我已經選好了一個1到100之間的數字。")

    while True:
        user_input = input("請輸入你的猜測（或輸入 'exit' 離開遊戲）：")
        
        if user_input.lower() == 'exit':
            print(f"遊戲結束！正確的數字是 {number_to_guess}。")
            break
        
        try:
            guess = int(user_input)
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("請輸入一個介於1到100之間的數字。")
                continue
            
            if guess < number_to_guess:
                print("太低了！再試一次。")
            elif guess > number_to_guess:
                print("太高了！再試一次。")
            else:
                print(f"恭喜你！你猜對了，數字就是 {number_to_guess}。你總共猜了 {attempts} 次。")
                break
        except ValueError:
            print("無效的輸入，請輸入一個數字。")
if __name__ == "__main__":
    guess_number_game()
