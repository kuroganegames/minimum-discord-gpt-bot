# coding:utf-8

def text_cleaner(s_input, l_remove):
    for i_remove in l_remove:
        s_input = s_input.replace(i_remove, "")
    s_input = s_input.replace("$", "")
    return s_input
