import re
import random


class RecipeBot:
    def __init__(self):
        self.recipes = {
            "宫保鸡丁": {
                "ingredients": ["鸡肉", "花生", "青椒", "红椒", "大葱", "姜", "蒜", "酱油", "醋", "糖", "盐"],
                "steps": [
                    "1. 鸡肉切丁，用酱油、盐腌制10分钟。",
                    "2. 热锅凉油，加入花生炒香。",
                    "3. 加入鸡肉丁，翻炒至变色。",
                    "4. 加入青椒、红椒、大葱、姜、蒜炒匀。",
                    "5. 加入糖、醋、盐，炒匀后出锅。"
                ],
                "nutrition": {"calories": 300, "protein": 25, "fat": 15}
            },
            "鱼香肉丝": {
                "ingredients": ["猪肉", "胡萝卜", "木耳", "葱", "姜", "蒜", "酱油", "醋", "糖", "淀粉"],
                "steps": [
                    "1. 猪肉切丝，用淀粉腌制15分钟。",
                    "2. 胡萝卜、木耳切丝。",
                    "3. 热锅凉油，加入猪肉炒至变色。",
                    "4. 加入胡萝卜、木耳炒匀。",
                    "5. 加入酱油、醋、糖，翻炒均匀后出锅。"
                ],
                "nutrition": {"calories": 350, "protein": 30, "fat": 20}
            },
            # 其他食谱可以继续添加
        }
        self.default_response = "对不起，我不明白你的问题。"

    def respond(self, user_input):
        user_input = user_input.lower().strip()

        # 检查如何制作食谱
        match = re.match(r'如何制作\s*(.*)', user_input)
        if match:
            dish_name = match.group(1).strip()
            if dish_name in self.recipes:
                ingredients = ", ".join(self.recipes[dish_name]["ingredients"])
                steps = "\n".join(self.recipes[dish_name]["steps"])
                nutrition = self.recipes[dish_name]["nutrition"]
                nutrition_info = f"营养信息：卡路里 {nutrition['calories']} kcal, 蛋白质 {nutrition['protein']} g, 脂肪 {nutrition['fat']} g"
                return f"制作{dish_name}所需的材料有：{ingredients}。\n制作步骤：\n{steps}\n{nutrition_info}"
            else:
                return "对不起，我没有这个食谱的信息。"

        # 随机推荐食谱
        if "推荐一个食谱" in user_input:
            dish_name = random.choice(list(self.recipes.keys()))
            return f"我推荐你试试：{dish_name}。你想知道如何制作吗？"

        # 检查食谱类型
        if "查询食谱" in user_input:
            return "我可以帮你找到各种食谱。你想要查找什么类型的食谱？"

        if "中餐" in user_input:
            return "受欢迎的中餐食谱有：宫保鸡丁、鱼香肉丝、麻婆豆腐等。"
        elif "西餐" in user_input:
            return "受欢迎的西餐食谱有：意大利面、牛排、披萨等。"
        elif "甜点" in user_input:
            return "受欢迎的甜点有：巧克力蛋糕、布朗尼、提拉米苏等。"
        elif "健康" in user_input:
            return "健康食谱推荐：蒸菜、沙拉、燕麦粥等。"

        return self.default_response


def main():
    bot = RecipeBot()

    print("欢迎来到食谱客服机器人。输入'exit'退出。")
    while True:
        user_input = input("你: ")
        if user_input.lower() == 'exit':
            break
        response = bot.respond(user_input)
        print(f"食谱机器人: {response}")


if __name__ == "__main__":
    main()
