
<div align="center">

  <p>
    Tên đề tài: Xây dựng phần mềm mô phỏng giải thuật thay thế trang OPT (Optimal Page Replacement) MHP: 012012500103-HĐH 
  </p>
  
  

<!-- Table of Contents -->
# :notebook_with_decorative_cover: Table of Contents
1.Lý thuyết:Thuật toán OPT không hoạt động độc lập, mà dựa trên cơ chế quản lý bộ nhớ phân trang. Nếu trong báo cáo chỉ giải thích OPT mà không giải thích các khái niệm nền tảng thì người đọc sẽ khó hiểu. 
- Khái niệm quản lý bộ nhớ
- Page
- Frame
- Page Fault
- Thuật toán OPT 
2.Thuật Toán
- Mô tả nguyên lý hoạt động: Giải thích bằng lời thuật toán làm gì và hoạt động theo trình tự nào. 
 	- Lưu đồ: Biểu diễn bằng sơ đồ các bước xử lý. 
- Giả mã (Pseudocode): Viết thuật toán theo dạng gần với code nhưng không phụ thuộc ngôn ngữ lập trình. 
3.So sánh với FIFO 	
- So sánh nguyên lý
- Ưu điểm, nhược điểm
- Độ phức tạp và kết quả thực nghiệm giữa OPT và FIFO 
4.Code giải thuật
Trình bày mã nguồn của chương trình mô phỏng OPT 
5.Kết quả 
	Minh họa kết quả chạy chương trình, nhận xét và đánh giá



Thành viên 1: Main Program (main.py) 
	Khởi động chương trình, liên kết các module, quản lý luồng chương trình. 
- Khởi tạo chương trình.
- Import các module.
- Điều khiển luồng thực thi.
- Kết nối giao diện với các chức năng. 
Thành viên 2: Giao diện chính (gui.py )
	Thiết kế cửa sổ, bố cục giao diện, các Label, Frame và Menu. 
- Thiết kế cửa sổ chính.
- Tạo Label, Entry, Button, Frame.
- Bố trí giao diện người dùng. 
Thành viên 3: Điều khiển giao diện (controller.py )
	Xử lý sự kiện các nút (Run, Reset, Exit), kết nối GUI với thuật toán. 
- Xử lý sự kiện các nút Run, Reset, Exit.
- Nhận dữ liệu từ GUI.
- Gọi thuật toán và trả kết quả về giao diện. 
Thành viên 4: Thuật toán OPT (opt_algorithm.py )
	Cài đặt thuật toán OPT, trả về trạng thái Frame từng bước và kết quả. 
- Cài đặt thuật toán OPT.
- Kiểm tra Hit/Fault.
- Chọn trang thay thế tối ưu.
- Trả trạng thái Frame sau mỗi bước. 
Thành viên 5: Kiểm tra dữ liệu (input_validation.py )
	Kiểm tra Frame, Reference String, xử lý dữ liệu không hợp lệ. 
- Kiểm tra số Frame hợp lệ.
- Kiểm tra Reference String.
- Thông báo lỗi khi nhập sai.
- Chuẩn hóa dữ liệu đầu vào. 
Thành viên 6: Hiển thị kết quả (result_table.py )
	Hiển thị bảng mô phỏng từng bước (Frame, Hit/Fault, trang thay thế).
- Hiển thị bảng mô phỏng từng bước.
- Hiển thị Frame sau mỗi lần truy cập.
- Hiển thị Hit/Fault và trang bị thay thế.  
Thành viên 7: Thống kê (statistics.py)
	Tính Page Fault, Hit, Hit Rate, Fault Rate và hiển thị thống kê. 
- Tính số Page Fault.
- Tính số Hit.
- Tính Hit Rate, Fault Rate.
- Hiển thị thống kê cuối chương trình. 

Thành viên 8: Kiểm thử & tích hợp (test.py, utils.py )
	Viết dữ liệu kiểm thử, hỗ trợ hàm dùng chung, kiểm tra và ghép chương trình. 

- Viết dữ liệu kiểm thử.
- Tạo các hàm dùng chung.
- Ghép các module.
- Kiểm tra lỗi toàn chương trình.
- Quản lý Git/GitHub và tiến độ nhóm. 


<!-- About the Project -->
## :star2: About the Project


<!-- Screenshots -->
### :camera: Screenshots

<div align="center"> 
  <img src="[![Screenshot-2026-07-29-134032.png](https://i.postimg.cc/vmC3QCkw/Screenshot-2026-07-29-134032.png)](https://postimg.cc/06dpnX9V)" />
</div>

<!-- Getting Started -->
## 	:toolbox: Getting Started

<!-- Prerequisites -->
### :bangbang: Prerequisites

This project uses Yarn as package manager

```bash
 npm install --global yarn
```

<!-- Installation -->
### :gear: Installation

Install my-project with npm

```bash
  yarn install my-project
  cd my-project
```
   
<!-- Running Tests -->
### :test_tube: Running Tests

To run tests, run the following command

```bash
  yarn test test
```

<!-- Run Locally -->
### :running: Run Locally

```echo "# Optimal-Page-Replacement-Algorithm-" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/HoangMon/Optimal-Page-Replacement-Algorithm-.git
git push -u origin main
}
```


<!-- Code of Conduct -->
### :scroll: Code of Conduct

Please read the [Code of Conduct](https://github.com/Louis3797/awesome-readme-template/blob/master/CODE_OF_CONDUCT.md)

<!-- FAQ -->
## :grey_question: FAQ

- Question 1

  + Answer 1

- Question 2

  + Answer 2


<!-- License -->
## :warning: License

Distributed under the no License. See LICENSE.txt for more information.


<!-- Contact -->
## :handshake: Contact

Project Link: [https://github.com/HoangMon/Optimal-Page-Replacement-Algorithm-.git)


