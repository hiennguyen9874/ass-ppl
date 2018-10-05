Set environment variable ANTLR_LIB to the file antlr-4.7.1-complete.jar in your computer
Change current directory to initial/src where there is file run.py
Type: python3 run.py gen 
Then type: python3 run.py test LexerSuite
Then type: python3 run.py test ParserSuite
Then type: python3 run.py test ASTGenSuite
Then type: python3 run.py test CheckSuite
Then type: python3 run.py test CodeGenSuite

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

chữ thường chữ hoa giống nhau
xử lý lỗi phải error_char
antlr 
"abcdef" khi in ra không tính "" chỉ in ra chữ
input = """xyz"abc"xyz"""
->"xyz,abcdef,xyz,<EOF>" xyz là id,abcdef là string

"abcdef 
check online chỉ có 10 test

với scala antlr có sp vẽ cây parse tree 
-> tìm lỗi: kiểm tra token, có đúng kết quả ko, dùng tool vẽ cây parse tree 
sửa 
- bình thường python run.py gen
- python run.py draw test//testcase/202.txt

cài jdk

comment đoạn 6 dòng đâu
chỉnh languge = java
tất cả những đoạn viết bằng python comment 
raise error_char

//chạy 
python run.py gen
// ra kết quả 
// trong thư mục target có các file .java
// chạy 
javac -cp $ANTLR_LIB ../target/main/mc/parser/*.java    //$ cho linux %% cho windows //đường dẫn thư mục tới file .java
java -cp $ANTLR_LIB:../target/main/mc/parser org.antlr.v4.gui.TestRig MP program -gui test/testcase/202.text ";" cho win, ":" cho linux
// MP.g4
// program kí hiệu bắt đầu của cái cây
// lệnh 2 đường dẫn thư mục tới các file .class
version 1.2 sửa file MP.g4 đặc tả mới của MP


javac -cp $ANTLR_LIB ../target/main/mc/parser/*.java
grun 

input="123\k123" -> output=?
1:=1 -> đúng hay sai

var i : array [ 1-1 .. 1+1 ] of integer;

var a , b , c : integer ;

            d : array [ 1 .. 5 ] of integer ;

            e , f : real ;