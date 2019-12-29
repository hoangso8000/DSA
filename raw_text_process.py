keywords=["khóa học", "tuyển dụng giáo viên","tuyển dụng trợ giảng","tuyển dụng quản lý lớp học", "tuyển dụng tư vấn khóa học", "học phí", "ưu đãi", "giảm giá", "miễn phí", "phụ phí", "combo", "trung tâm", "lịch học", "đăng ký", "free", "tuyển sinh","bằng lái xe","thi bằng lái xe","duyệt hồ","tuyển dụng vị trí","tuyển dụng","khóa học","làm thêm","việc làm","ngoài giờ","tuyển nhân viên","học việc","xoay ca","giáo viên","tìm việc","khu vực","địa chỉ","sách ","bộ sách","số lượng có hạn","thông tin sách","liên hệ","inbox", 'khoá học']
# keywords=["trung tâm bằng cấp","uy tín chất lượng","nhận làm bằng","chạy điểm","giá rẻ","dịch vụ văn bằng","uy tín","làm bằng toàn quốc","chất lượng ","chuyên nghiệp","tặng","khóa học","trị giá"]
texts=open("/home/viethoang/giaoduc.txt","r").read().split("\n")
def check(sentence, words): 
    file=open(r"/home/viethoang/petproject/data_structures_and_algorithm/new.txt","w")
    for i in range(0,len(keywords)):
        res = [all([keyword in text.lower() for keyword in keywords[i]]) for text in texts]
    last=[texts[i] for i in range(0, len(res))]
    # file=open(r"/home/viethoang/petproject/data_structures_and_algorithm/new3.txt","a")
    all_res=[]
    for i in range(0,len(last)):
        res=[keyword in last[i].lower() for keyword in keywords]
        if(res.count(True)<3) and res[0] == False and res[-1] == False:
            file.write(last[i]+'\n')
check(texts,keywords)