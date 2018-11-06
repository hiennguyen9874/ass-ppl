# Bài tập lớn môn Nguyên lý nguôn ngữ lập trình
## Những thứ cần cài đặt
* **1.** ```cd /usr/local/lib```
* **2.** ```sudo wget https://www.antlr.org/download/antlr-4.7.1-complete.jar```
* **3.** Thêm hai dòng sau vào file ~/.bashrc
    + ANTLR_LIB='/usr/local/lib/antlr-4.7.1-complete.jar'
    + export ANTLR_LIB
* **4.** Chạy các lệnh sau:
    + ```sudo apt-get update```
    + ```sudo apt install -y build-essential```
    + ```sudo apt-get install python3-pip```
    + ```sudo pip3 install antlr4-python3-runtime```