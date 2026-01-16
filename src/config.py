import pandas as pd
import os


# df = pd.read_csv(filepath_or_buffer="../data/raw/bank-additional-full.csv",sep=";")
# ---------------------------------------
# đường dẫn thư mục gốc (root path)
# ---------------------------------------
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---------------------------------------
# đường dẫn thư mục dữ liệu (data path)
# ---------------------------------------
data_dir = os.path.join(base_dir,"data")
# đường dẫn thư mục dữ liệu thô (data raw path)
raw_data_path = os.path.join(data_dir,"raw","bank-additional-full.csv")
# đường dẫn thư mục dữ liệu đã sử lý (data processor path)
processer_data_dir = os.path.join(data_dir,"processed")


# ---------------------------------------
# đường dẫn thư mục báo cáo (reports path)
# ---------------------------------------
report_dir = os.path.join(base_dir,"reports")
eda_report_dir = os.path.join(report_dir,"eda")
eda_report_file = "report_baf.html"


# ---------------------------------------
# đường dẫn checkpoint model
# ---------------------------------------
model_dir = os.path.join(base_dir,"model")
model_file = "bank_marketing_model.pkl"
model_path = os.path.join(model_dir,model_file)


# ----------------------------------------------
# đường dẫn các nhãn và và cột(targit & features)
# ----------------------------------------------
target_col = "y"

categorical_cols = [
    "job",            # nghề nghiệp
    "marital",        # tình trạng hôn nhân
    "education",      # trình độ học vấn
    "default",        # có nợ xấu hay không
    "housing",        # có vay mua nhà hay không
    "loan",           # có vay tiêu dùng hay không
    "contact",        # hình thức liên hệ (cellular, telephone)
    "month",          # tháng liên hệ
    "day_of_week",    # ngày trong tuần
    "poutcome"        # kết quả chiến dịch trước đó
]
numerical_cols = [
    "age",  # tuổi
    "duration",  # thời gian cuộc gọi (giây)
    "campaign",  # số lần liên hệ trong chiến dịch này
    "pdays",  # số ngày kể từ lần liên hệ trước
    "previous",  # số lần liên hệ trước đó
    "emp.var.rate",  # biến động tỷ lệ việc làm
    "cons.price.idx",  # chỉ số giá tiêu dùng
    "cons.conf.idx",  # chỉ số niềm tin tiêu dùng
    "euribor3m",  # lãi suất Euribor 3 tháng
    "nr.employed"  # số lượng lao động
]

# ---------------------------------------
# tham số huấn luyện (training params)
# ---------------------------------------
test_size = 0.2
random_state = 42


