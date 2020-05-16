from janome.tokenizer import Tokenizer
import random

def generate_tweet(sentense):
    tokenizer = Tokenizer()

    # print(sentense)
    word_list = tokenizer.tokenize(sentense, wakati=True)
    part_list = [token.part_of_speech.split(',')[0] for token in tokenizer.tokenize(sentense)]
    base_word_list = [token.base_form for token in tokenizer.tokenize(sentense)]
    try:
        del word_list[word_list.index('#'):len(word_list)]
        del base_word_list[base_word_list.index('#'):len(base_word_list)]
    except:
        pass
    try:
        del word_list[word_list.index('https'):len(word_list)]
        del base_word_list[base_word_list.index('https'):len(base_word_list)]
    except:
        pass
    # print(word_list)
    # print(part_list)
    # print(base_word_list)
    part_cnt = 0
    cnt = 0
    gen_sentense = ''
    for (word, part) in zip(word_list, part_list):
        if part == '名詞':
            part_cnt += 1
        gen_sentense += word
        if part_cnt == part_list.count('名詞'):
            # print("cnt :{}".format(cnt))
            # print("word_list :{}".format(word_list))
            for i in range(cnt, len(word_list)):
                # print("i :{}".format(i))
                if part_list[i] == ('動詞') or part_list[i] == ('形容詞'):
                    for j in range(cnt + 1, i):
                        # print("j :{}".format(j))
                        # print("word_list[j] :{}".format(word_list[j]))
                        gen_sentense += word_list[j]
                    gen_sentense += (base_word_list[i] + "の")
                    break
            break
        cnt += 1
    gen_sentense += "って普通だよね……？" if random.random() > 0.1 else "って普通じゃなかったんだ……"
    # print(gen_sentense)

    return gen_sentense