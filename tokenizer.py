from janome.tokenizer import Tokenizer
import random

def generate_tweet(sentense):
    tokenizer = Tokenizer()

    print(sentense)
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
            try:
                if part_list[cnt + 1] == ('動詞'):
                    gen_sentense += (base_word_list[cnt + 1] + "の")
                elif part_list[cnt + 2] == ('動詞'):
                    gen_sentense += (word_list[cnt + 1] + base_word_list[cnt + 2] + "の")
            except:
                pass
            break
        cnt += 1
    gen_sentense += "って普通……だよね？" if random.random() > 0.1 else "って普通じゃなかったんだ……"
    print(gen_sentense)

    return gen_sentense