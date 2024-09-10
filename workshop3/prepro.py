import os
import pandas as pd

# 현재 폴더에 있는 모든 파일들의 목록을 읽음
file_list = os.listdir()

# xlsx 확장자를 가지는 파일만 필터링
xlsx_files = [file for file in file_list if file.endswith('.xlsx')]

# 필터링된 데이터프레임을 저장할 리스트
filtered_dataframes = []

# xlsx 파일을 pandas DataFrame으로 읽으며 상위 5행을 건너뜀
for file in xlsx_files:
    # 파일 읽기
    df = pd.read_excel(file, sheet_name="프로그램일자별리스트", skiprows=5)
    print(f'{file}')

    # 프로그램명 컬럼에 '사랑꾼' 또는 '고딩'이 포함된 데이터 필터링
    # filtered_df = df[df['프로그램명'].str.contains('금쪽|신랑수업', na=False)]
    filtered_df = df[df['프로그램명'].str.contains(r'사랑꾼\(본\)|고딩.*\(본\)', na=False)]
    # print(filtered_df)
    # 필터링된 데이터프레임 리스트에 추가
    filtered_dataframes.append(filtered_df)

# 모든 데이터프레임을 하나로 합침
if filtered_dataframes:
    combined_df = pd.concat(filtered_dataframes, ignore_index=True)
else:
    combined_df = pd.DataFrame()  # 필터링된 데이터가 없을 경우 빈 데이터프레임 생성

# output 폴더가 없으면 생성
output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# combined_df를 output 폴더에 result.csv로 저장
output_path = os.path.join(output_dir, 'result2.csv')
combined_df.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"Filtered data saved to {output_path}")