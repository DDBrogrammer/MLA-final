Decision Tree Classification
https://www.youtube.com/watch?v=ZVR2Way4nwQ

- Cho 1 tập các điển dũ liệu mẫu để phân tích 
  
![img.png](img.png)

- Decision node:  chứa điều kiện để chia dữ liệu ra thành nhiều loại
- Leaf node:  chứa loại đã được phân của dữ liệu

![img_1.png](img_1.png)

- Có rất nhiều cách chia khác nhau nhưng cách tối ưu nhất là chia để tìm đc Leaf node càng sớm càng tốt như ví dụ dưới

![img_2.png](img_2.png)

- Để đạt được điều này cần tính toán Information Gain, để tính Information Gain cần tính được Entropy

![img_3.png](img_3.png)

- Pi là tỉ lệ của class i 

![img_4.png](img_4.png)

- bên trên là ví dụ với root 
- áp dụng vào các nhánh còn lại ta được:  

![img_5.png](img_5.png)

- Để tính Information Gain dùng công thức

![img_7.png](img_7.png)

- Dễ thấy IG1 > IG2 nên sẽ chọn IG2, sau đó cứ tiếp tục cho đến khi ko còn lại Decision node nào.
