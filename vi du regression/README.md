## Yêu cầu
* Tìm vài ví dụ về bài toán regression _**trong thực tế**_
* Ghi rõ input, output và cách thu thập + xử lý data
## Bài làm
### Ví dụ 1: Dự đoán lương dựa trên số năm kinh nghiệm
* Input: Số năm kinh nghiệm của 1 người(số thực).
* Output: Mức lương dự đoán của người đó(số thực).
* Thu thập dữ liệu:
    * Tạo form thu thập thôn tin của nhân viên
    * Xin thông tin về lương và kinh nghiệm làm việc của nhân viên trong các công ty
    * Mô hình áp dụng cho từng lĩnh vực, quốc gia cụ thể(mức lương khác nhau ở lĩnh vực, quốc gia khác nhau). Vậy ta phải thu thập thông tin theo nhóm phù hợp.
* Xử lí dữ liệu:
    * Tổ chức dữ liệu thành file csv gồm 2 column: Số năm kinh nghiệm(số thực), mức lương.
    * loại bỏ các phần chứa null, số không hợp lệ như: số âm, năm kinh nghiệm và mức lương không phù hợp.
### Ví dụ 2: Dự đoán thời gian di chuyển.
Ứng dụng: Google Maps
* Input
    *Tổng hợp vị trí của tất cả người dùng (Aggregate location data)
    * Lịch sử giao thông tuyến đường trong quá khứ (Historical traffic patterns)
    * Dữ liệu chính thức địa phương ( đường một chiều, đèn đỏ…) (Local government data)
    * Thời gian di chuyển từ cộng đồng sử dụng (Real-time feedback from users)
* Output: Dự đoán thời gian di chuyển trên tuyến đường chỉ định.
* Thu thập dữ liệu:
Tất cả các thông tin trên đều được Google Maps thu thập qua nhiều nguồn:
    * Base Map Partner Program: Một lượng lớn các cơ quan nộp những dữ liệu vector chi tiết đến Google để hình thành nên “bản đồ cơ bản” và chính thống nhất.
    * Google Street View: Mục tiêu của nó là lặp lại việc di chuyển trên tất cả những con đường mà họ tìm thấy và chụp những bức ảnh 360 độ mọi nơi mà họ đến. 
    * Những vệ tinh:  Đây là một bản phối gần gũi với Google Earth, kết hợp những tấm ảnh chụp từ vệ tinh có độ phân giải cao với nhau.
    * Những dịch vụ vị trí từ người dùng: Với một cộng đồng người sử dụng cực kì lớn ( Khoảng hơn 2 tỷ người dùng android năm 2019), tuy không phải tất cả mọi người đều chia sẽ dữ liệu cá nhân tuy nhiên con số này đủ để khiến kho dữ liệu của Google vô cùng lớn, hình thành nên bản đồ lượng người đang di chuyển xung quanh bạn. Đúng vậy, nếu Google có quyền truy cập vào dữ liệu vị trí được thu thập bởi smartphone của bạn, bạn là một phần trong hệ thống cải thiện và mở rộng Maps của Google.	
* Xử lý dữ liệu:
Những loại thuật toán đã khiến Google trở thành ông hoàng như hiện nay nên có vẻ như cực kỳ phức tạp và tuyệt mật, hoạt động để làm sạch dữ liệu, tìm ra những sự mâu thuẫn, và kết hợp tất cả chúng lại với nhau để làm chúng có ích hơn. Em đề cử một vài hướng theo ý kiến cá nhân:
    * Dùng dữ liệu vector chi tiết được cung cấp để tạo nên bản đồ cơ bản.
    * Tính thời gian người dùng khác đi quãng đường trong thực tế.
    * Thực hiện so sánh với những mẫu kết quả đã thu được với quãng đường tương tự trong quá khứ
    * Kết hợp xâu chuỗi ảnh 360 độ để đánh giá ( Đường hẹp, hầm hố…)
    * Kết hợp các dữ kiện.
    https://www.makeuseof.com/tag/technology-explained-google-maps-work/
### Ví dụ 3: Dự đoán lợi nhuận thông qua chi phí quảng cáo
* Input: chi phí quảng cáo qua: (TV, radio, newspapwers)
* Output: lợi nhuận nhận được.
* Thu thập dữ liệu:
    * Tạo sheet thu thập thông tin của những quảng cáo trước đó.
* Xử lí dữ liệu:
    * Tổ chức dữ liệu dưới dạng file csv
    * Loại bỏ example có chứa feature null, âm
    * Thực hiện feature scaler hoặc mean normalization để giảm thời gian training


