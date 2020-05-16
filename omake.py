#-*- coding:utf-8 -*-
import datetime
import random
import pytz
import json
import pprint

pack = ["moryo"]
names = ["魍魎列島"]


def collect(day, screen_name, cmd):
    dt_now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    rand = dt_now.day % len(pack)
    p = "texts/" + pack[rand] + ".txt"
    f = open(p, "r")
    items = f.read().splitlines()
    print(items)
    item = items[random.randint(1, len(items) - 1)] if random.random() > 0.05 else items[0]
    jp = "json/" + pack[rand] + ".json"
    with open(jp) as f:
        df = json.load(f)
        pprint.pprint(df, width=40)
    if screen_name not in df:
        df[screen_name] = {'day': 0}
    my_items = df[screen_name]
    pop_day = my_items.pop('day')
    if cmd == "reset":
        del df[screen_name]
        f = open(jp, "w")
        json.dump(df, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
        return "Name先輩のおまけは全部広町がもらっておきます〜"
    elif cmd == "list":
        comp = str(len(my_items) * 10)
        result = "\n" + names[rand] + " " + "コンプ率" + comp + "％\n"
        for k, v in my_items.items():
            result += k + " " + str(v) + "\n"
        return result
    elif pop_day == dt_now.day:
        return "今日の分はもうやってるよね……？"
    else:
        if item not in my_items:
            my_items[item] = 0
        my_items[item] += 1
        comp = str(len(my_items) * 10)
        result = "\nおまけは「" + item + "」でした〜。\n\n" + names[rand] + " " + "コンプ率" + comp + "％\n"
        for k, v in my_items.items():
            result += k + " " + str(v) + "\n"
        if comp == 100:
            result += "\nコンプリートですよ〜！おめでとうございますーー！！！！"
        my_items['day'] = day
        df[screen_name] = my_items
        pprint.pprint(df, width=40)
        f = open(jp, "w")
        json.dump(df, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
        return result
