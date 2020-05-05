# Bài tập lớn môn Nguyên lý nguôn ngữ lập trình
## Introduction
MP (Mini Pascal) is a language which consists of a subset of Pascal plus some Java language features.

The Pascal features of this language are (details will be discussed later): a few primitive types, one-dimensional arrays, control structures, expressions, compound statements (i.e., blocks), functions and procedures.

The Java features of this language are as follows:
1. MP has multiple assignments, borrowed from Java.
2. In MP, like Java, the operands of an operator are guaranteed to be evaluated in a specific evaluation order, particularly, from left to right. In Pascal, the evaluation order is left unspecified. In the case of f() + g(), for example, MP dictates that f is always evaluated before g.<br/>
For simplicity reason:
    1. There is only one dimension array in MP.
        - ```var i : array [ 1 . . 2 , 3 . . 4 ] of integer ; // ERROR```
        - ```var i : array [ 1 . . 5 ] of integer ; // CORRECT```

Conventionally, the sequence ’\n’ must be used as a new line character in MP.
## Những thứ cần cài đặt
* **1.** Cài [antlr4](https://www.antlr.org/)
    + ```cd /usr/local/lib```
    + ```sudo wget https://www.antlr.org/download/antlr-4.7.1-complete.jar```
* **3.** Thêm hai biến môi trường ~/.bashrc
    + ```echo "ANTLR_LIB='/usr/local/lib/antlr-4.7.1-complete.jar'" >> ~/.bashrc```
    + ```echo "export ANTLR_LIB" >> ~/.bashrc```
    + ```source ~/.bashrc```
* **4.** Install build essential:
    + ```sudo apt-get update```
    + ```sudo apt install -y build-essential```
* **5.** Cài pip và antlr4-python3-runtime
    + ```sudo apt-get install python3-pip```
    + ```sudo pip3 install antlr4-python3-runtime```

Mã nguồn của cả bốn bài tập [ở đây](https://github.com/hiennguyen9874/ass_ppl/tree/master/assignment4/src)
