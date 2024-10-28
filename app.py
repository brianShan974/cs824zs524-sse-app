from flask import Flask, jsonify, render_template, request
import random
import re
from utils import are_opposite_directions


<<<<<<< HEAD
query_dict = {
    "dinosaurs": "Dinosaurs ruled the Earth 200 million years ago",
    "asteroids": "Asteroids are rocky bodies orbiting the Sun",
=======
query_templates = {
    r"What is (\d+) plus (\d+)\?": lambda m: str(int(m.group(1)) + int(m.group(2))),
    r"Which of the following numbers is the largest: (.+)\?": lambda m: str(
        max(map(int, m.group(1).split(", ")))
    ),
>>>>>>> 42d539b (query_templates)
}


def process_query(query):
    # 遍历模板，查找匹配项
    for pattern, handler in query_templates.items():
        match = re.match(pattern, query)
        if match:
            # 使用匹配项调用对应的处理函数
            return handler(match)
    return "Unknown"  # 如果没有匹配项，返回默认响应


class QueryProcessor:
    def __init__(self):
        self.templates = {}

    def add_template(self, pattern, handler):
        """添加新的查询模板"""
        self.templates[pattern] = handler

    def process(self, query):
        """根据模板匹配和处理查询"""
        for pattern, handler in self.templates.items():
            match = re.match(pattern, query)
            if match:
                return handler(match)
        return "Unknown"


app = Flask(__name__)

# Snake game state management
game_state = {
    "snake": [(100, 100), (90, 100), (80, 100)],
    "direction": "Right",
    "food": [random.randint(0, 39) * 10, random.randint(0, 39) * 10],
    "score": 0,
    "game_over": False,
}


def move_snake():
    head = list(game_state["snake"][0])
    if game_state["direction"] == "Up":
        head[1] -= 10
    elif game_state["direction"] == "Down":
        head[1] += 10
    elif game_state["direction"] == "Left":
        head[0] -= 10
    elif game_state["direction"] == "Right":
        head[0] += 10
    game_state["snake"] = [tuple(head)] + game_state["snake"][:-1]


def check_collisions():
    head = game_state["snake"][0]
    # Boundary collision
    if head[0] < 0 or head[0] >= 400 or head[1] < 0 or head[1] >= 400:
        game_state["game_over"] = True
    # Self-collision
    if head in game_state["snake"][1:]:
        game_state["game_over"] = True


def check_food():
    if game_state["snake"][0] == tuple(game_state["food"]):
        game_state["snake"].append(game_state["snake"][-1])
        game_state["food"] = [
            random.randint(0, 39) * 10,
            random.randint(0, 39) * 10,
        ]
        game_state["score"] += 10


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/game-state", methods=["GET"])
def get_game_state():
    return jsonify(game_state)


@app.route("/move", methods=["POST"])
def move():
    if game_state["game_over"]:
        return jsonify(game_state)  # Don't allow moves when the game is over

    data = request.json
    direction = data.get("direction", game_state["direction"])
    if not are_opposite_directions(direction, game_state["direction"]):
        game_state["direction"] = direction
    move_snake()
    check_collisions()
    check_food()
    return jsonify(game_state)


@app.route("/reset", methods=["POST"])
def reset_game():
    game_state["snake"] = [(100, 100), (90, 100), (80, 100)]
    game_state["direction"] = "Right"
    game_state["food"] = [
        random.randint(0, 39) * 10,
        random.randint(0, 39) * 10,
    ]
    game_state["score"] = 0
    game_state["game_over"] = False
    return jsonify(game_state)


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    return render_template("hello.html", name=input_name, age=input_age)


<<<<<<< HEAD
def process_query(query: str):
    if query.startswith("What") or query.startswith("Which"):
        if "name" in query:
            return "cszs"
        if "largest" in query:
            numbers = [int(i) for i in query.split(": ")[1][:-1].split(", ")]
            return str(max(numbers))
        if "plus" in query:
            numbers = query.split()
            return str(int(numbers[2]) + int(numbers[-1][:-1]))
    else:
        return query_dict.get(query, "Unknown")
=======
# 实例化并添加模板
processor = QueryProcessor()
processor.add_template(
    r"What is (\d+) plus (\d+)\?", lambda m: str(int(m.group(1)) + int(m.group(2)))
)
processor.add_template(
    r"Which of the following numbers is the largest: (.+)\?",
    lambda m: str(max(map(int, m.group(1).split(", ")))),
)


# 使用实例化的对象来处理查询
def process_query(query):
    return processor.process(query)
>>>>>>> 42d539b (query_templates)


@app.route("/query")
def query_route():
    query_param = request.args.get("q")
    if query_param:
        return process_query(query_param)
    else:
        return "Query parameter missing", 400


if __name__ == "__main__":
    app.run(debug=True, port=5005)
