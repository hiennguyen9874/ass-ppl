Bài tập lớn PPL

cd /usr/local/lib
sudo wget https://www.antlr.org/download/antlr-4.7.1-complete.jar
thêm dòng này vào cuối file 
nano ~/.bashrc

ANTLR_LIB='/usr/local/lib/antlr-4.7.1-complete.jar'
export ANTLR_LIB

sudo apt-get update
sudo apt install -y build-essential
sudo apt-get install python3-pip
sudo pip3 install antlr4-python3-runtime