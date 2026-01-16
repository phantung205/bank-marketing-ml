import pandas as pd
from ydata_profiling import  ProfileReport
import os

# lấy tên thư mục dự án
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(BASE_DIR, "data", "raw", "bank-additional-full.csv")
report_dir = os.path.join(BASE_DIR, "reports", "eda")
report_file = "report_baf.html"

def generate_classifier_report():
    # tạo ra thư mục lưu trữ nếu nó chưa tồn tại
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    df = pd.read_csv(data_path,sep=";")

    # tạo report
    profile = ProfileReport(df,title=report_file,explorative=True)

    #  Đường dẫn đầy đủ
    report_path = os.path.join(report_dir, report_file)

    #  Ghi file (ghi đè nếu đã tồn tại)
    profile.to_file(report_path)

    print(f" Report created at: {report_path}")

if __name__ == '__main__':
    generate_classifier_report()

