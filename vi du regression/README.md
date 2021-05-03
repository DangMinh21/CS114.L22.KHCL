## Yêu cầu
* Tìm vài ví dụ về bài toán regression _**trong thực tế**_
* Ghi rõ input, output và cách thu thập + xử lý data
## bài làm
### Ví dụ 1: Dự đoán lương dựa trên số năm kinh nghiệm.
* Input: Số năm kinh nghiệm của 1 người(số thực).
* Output: Mức lương dự đoán của người đó(số thực).
* Thu thập dữ liệu:
    * Tạo form thu thập thôn tin của nhân viên
    * Xin thông tin về lương và kinh nghiệm làm việc của nhân viên trong các công ty
    * Mô hình áp dụng cho từng lĩnh vực, quốc gia cụ thể(mức lương khác nhau ở lĩnh vực, quốc gia khác nhau). Vậy ta phải thu thập thông tin theo nhóm phù hợp.
* Xử lí dữ liệu:
    * Tổ chức dữ liệu thành file csv gồm 2 column: Số năm kinh nghiệm(số thực), mức lương.
    * loại bỏ các phần chứa null, số không hợp lệ như: số âm, năm kinh nghiệm và mức lương không phù hợp.
