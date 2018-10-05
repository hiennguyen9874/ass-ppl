________________ expect.py ________________
Mô tả: công cụ giúp tự sinh expect tương ứng
với solution thay vì phải viết tay.

Yêu cầu:
+ Chạy test ASTGenSuite không bị error nào.
+ Python 3.

Hướng dẫn sử dụng:
1. Đặt file expect.py trong folder src.
2. Mở terminal tại src.
3. Chạy lệnh: 
	python expect.py
Nếu lệnh thực thi python không phải là "python",
thì thay bằng lệnh này:
	<PYTHON> plot.py <PYTHON>
Trong đó <PYTHON> là lệnh thực thi python. Ví dụ nếu
lệnh thực thi python là "python3" thì chạy lệnh:
	python3 plot.py python3
4. Các expect trong ASTGenSuite đã được thay thế.

Lưu ý:
+ Các file ASTGenSuite và ASTGeneration đều được backup
lại, nếu có bất kì vấn đề nào xảy ra trong/sau quá trình
chạy thì chỉ cần lấy file backup khôi phục lại.
+ ASTGeneration chỉ chỉnh sửa tạm thời nên nếu chương trình
chạy thành công các file backup của ASTGeneration sẽ tự động
được xóa. ASTGenSuite có sự thay đổi nên file backup được
giữ lại sau khi chương trình chạy.
+ Check kĩ các file solution xem đã đúng yêu cầu đề bài
chưa rồi mới sinh expect do chương trình sinh expect theo
solution nên lúc test sẽ luôn ra đúng.

________________ plot.py ________________
Mô tả: công cụ giúp vẽ cây AST.
Yêu cầu:
+ Test nào sinh ra được output không lỗi mới vẽ
cây được.
+ Python 3.

Hướng dẫn sử dụng:
1. Đặt file plot.py trong folder src.
2. Mở terminal tại src.
3. Chạy lệnh: 
	python plot.py
Nếu lệnh thực thi python không phải là "python",
thì thay bằng lệnh này:
	<PYTHON> plot.py <PYTHON>
Trong đó <PYTHON> là lệnh thực thi python. Ví dụ nếu
lệnh thực thi python là "python3" thì chạy lệnh:
	python3 plot.py python3
4. Các hình vẽ được sinh tại test/solutions/plots/.

Lưu ý:
+ Bấm vào các node của cây để expand/collapse.
+ Các file ASTGenSuite và ASTGeneration đều được backup
lại, nếu có bất kì vấn đề nào xảy ra trong/sau quá trình
chạy thì chỉ cần lấy file backup khôi phục lại. Nếu chương
trình chạy thành công thì các file backup sẽ được xóa do
2 file này chỉ bị thay đổi tạm thời và sẽ được khôi phục
về nội dung gốc sau khi chương trình thực thi xong.
