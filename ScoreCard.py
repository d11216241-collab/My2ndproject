#分數計算功能設計
#1.	設計簡單的分數計算器：輸入考試成績，程式自動計算平均分數。
#2.	加入錯誤處理：遇到非數字輸入時，提示「請輸入有效分數」。
#3.	每次修改後，使用 GitHub 進行版本管理，留下註解。
def calculate_average_score():
    scores = []
    print("歡迎使用分數計算器！請輸入考試成績，輸入 'done' 完成輸入。")

    while True:
        user_input = input("請輸入分數（或輸入 'done' 完成）：")
        
        if user_input.lower() == 'done':
            break
        
        try:
            score = float(user_input)
            if score < 0 or score > 100:
                print("請輸入一個介於0到100之間的有效分數。")
                continue
            scores.append(score)
        except ValueError:
            print("請輸入有效分數。")
    
    if scores:
        average_score = sum(scores) / len(scores)
        print(f"平均分數為：{average_score:.2f}")
    else:
        print("沒有輸入任何分數。")

if __name__ == "__main__":
    calculate_average_score()

# GitHub 版本管理註解範例：
# v1.0 - 初始版本，實現基本的分數計算功能。
# v1.1 - 加入錯誤處理，提示非數字輸入。
# v1.2 - 限制分數範圍在0到100之間。
# v1.3 - 改進輸出格式，顯示平均分數至小數點後兩位。
