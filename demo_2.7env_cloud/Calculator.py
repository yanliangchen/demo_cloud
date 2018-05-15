#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
formula = input("请输入您的公式：").replace(" ", "")

regulars = [("([\d.]+[*][\d.]+)+", "[*]"),
            ("([\d.]+[/][\d.]+)+", "[/]"),
            ("([\d.]+[+][\d.]+)+", "[+]"),
            ("([\d.]+[-][\d.]+)+", "[-]")]

def check_int_or_float(number_string):
    rst = re.search("[\d]{1,}\.+[\d]{1,}", number_string)
    if rst == None:
        return int(number_string)
    else:
        return float(number_string)

def one(rst, regular):
    for counting_str in rst:
        rst_split = re.split(regular, counting_str)
        a = check_int_or_float(rst_split[0])
        b = check_int_or_float(rst_split[1])
        if regular == "[*]":
            counting = a * b
        elif regular == "[/]":
            counting = a / b
        elif regular == "[+]":
            counting = a + b
        elif regular == "[-]":
            counting = a - b
        else:
            pass

        counting_list.append((counting_str, counting))

def counting(regulars, formula, FLAG):
    while FLAG:
        for regular, string in regulars:
            global counting_list
            counting_list = []
            rst = re.findall(regular, formula)
            one(rst, string)

            for a,b in counting_list:
                formula = formula.replace(str(a), str(b))

        check_list = []
        for regular, string in regulars:
            rst = re.search(regular, formula)
            if rst != None:
                check_list.append(rst)

        if len(check_list) == 0:
            FLAG = False

    return formula

formula = counting(regulars, formula, True)

formula = formula.replace("(", "")
formula = formula.replace(")", "")
formula = formula.replace("--", "+")
formula = formula.replace("+-", "-")

print(eval(counting(regulars, formula, True)))