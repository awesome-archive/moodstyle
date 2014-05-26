#coding=utf-8
#!/usr/bin/env python




# def text_extract(line , word_count = 2 , type_split = '    ' ,  word_split = ' '):
#     if line and isinstance(line , (str,unicode)):
#        lineArry = [ word.strip() for word in line.split(type_split) if word.strip() != ''  ]
#        if len(lineArry) == 2:
#            word_arry = lineArry[1].split(word_split)
#            return [' '.join(word_arry[i : i + word_count]) for i in range(len(word_arry) - word_count)]
#        else:
#             raise TypeError


# if __name__ == '__main__':
#     for i in text_extract(word_count = 4 ,line = '广告    尊敬 的 客户 ： 陆丰 碣石 服务 厅 已 全面 打造 为 购机 中心 ， 新开 张 购机 低 至 五折 优惠 ， 幸运 客户 折 上 折 ， 欢迎 广大客户 前来 选购 ， 我们 将 竭诚为您服务 ！ 地址 ： 陆丰市 碣石镇 镇府路 中段 ； 电话 ： 13828932010 。 您 的 10 分 满意 , 我们 的 无限 动力 ！ 中国移动'):
#         print i




def ngram(sentence , word_term = 1 , word_split = ' '):
    if sentence:
        if word_term >= 1 and isinstance(word_term , (int , long)):
            if isinstance(sentence , (str , unicode)):
                print sentence.split(word_split)
                sentence = [ word.strip() for word in sentence.split(word_split) if word.strip() != '']
            elif not isinstance(sentence , (list , tuple)):
                raise TypeError , 'sentence must be is string or unicode or list or tuple!'
            print sentence
            return [ ' '.join(sentence[i: i + word_term]) for i in range(len(sentence) - 1) ]
        else:
            raise TypeError  , 'word_term must be bigger than 0 and type is integer' 

    else:
        raise TypeError , 'sentence is null!'


if __name__ == '__main__':
    for i in ngram('这 是 一个 ２ 元 文法!' , word_term = 2):
        print i