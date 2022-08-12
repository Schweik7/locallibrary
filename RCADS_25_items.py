from enum import Enum
from typing import List
from collections import OrderedDict
from random import randint
import csv
import pathlib
import os
from dataclasses import dataclass, asdict, fields

os.chdir(os.path.dirname(__file__))

f = r"C:\Users\Schweik7\Documents\WeChat Files\wxid_sbhkmgp6fh7z22\FileStorage\File\2022-08\RCADS_data.csv"


@dataclass
class Person:
    序号: int = -1
    姓名: str = ""
    抑郁分数: int = -1
    焦虑分数: int = -1
    总分数: int = -1
    抑郁T分数: int = -1
    焦虑T分数: int = -1
    总T分数: int = -1


debug = True  # 当你要手动填写信息，请把True改为False
SYSMIS = 50  # 当缺失项过多时，各分项的默认值

# if debug:
#     # 自动生成模拟数据
#     grade = 6
#     sex = 1
#     RCADS25 = [randint(0, 3) for i in range(26)]  # 规定无数据是-1
#     print(
#         f"测试模拟数据：{RCADS25=}",
#     )
#     print(f"目前为测试模拟。设定为{grade}年级", end="")
#     print("男生") if sex == 1 else print("女生")
# else:
#     # 请手动输入你的信息
#     grade = 6  # 3-12年级
#     sex = 1  # 男生为1，女生为2
#     ques = OrderedDict(  # 直接在其中修改分值。-1表示未填写
#         {
#             "1.我感到悲伤或空虚。 ": -1,
#             "2.当我认为自己做得不好的时候，我会担心。 ": -1,
#             "3.自己害怕在家独处。 ": -1,
#             "4. 所有事情都不再足够有趣。 ": -1,
#             "5. 我担心家人会发生可怕的事情。 ": -1,
#             "6. 我害怕呆在拥挤的地方（如购物中心、电影院、公共汽车、繁忙的游乐场）。": -1,
#             "7. 我担心别人对自己的看法。 ": -1,
#             "8. 我的睡眠不好。 ": -1,
#             "9. 我害怕独自睡觉。 ": -1,
#             "10. 我的胃口有问题。 ": -1,
#             "11. 我会突然无缘无故地头晕或昏厥。 ": -1,
#             "12. 我必须重复做一些事情（如洗手、打扫卫生或按一定顺序摆放物品）。 ": -1,
#             "13. 我没有精力做事情。 ": -1,
#             "14. 我会突然无缘无故地开始颤抖或发抖。 ": -1,
#             "15. 我无法清晰地思考。 ": -1,
#             "16. 我觉得自己毫无价值。 ": -1,
#             "17. 我必须想一些特殊的事情（如数字或文字），来阻止坏事发生。 ": -1,
#             "18. 我思考过死亡。 ": -1,
#             "19. 我不想动。 ": -1,
#             "20. 在没有什么可害怕的情况下，我担心自己会突然感到害怕。 ": -1,
#             "21. 我很累。 ": -1,
#             "22. 我担心自己会在他人面前出丑。 ": -1,
#             "23. 我必须以某种正确的方式做一些事情，来阻止坏事发生。 ": -1,
#             "24. 我感到烦躁不安。 ": -1,
#             "25. 我担心会有坏事发生在我身上。 ": -1,
#         }
#     )
#     RCADS25 = list(ques.values())
#     RCADS25.insert(0, 0)


def NMISS(*data: List[int]) -> int:

    return data.count(-1)


def SUM(*data: List[int]) -> int:

    return sum(filter(lambda x: x != -1, data))


def get_score(score, grade, sex):
    RCADS25 = score
    # This counts the number of missing items per RCADS25-C subscale.
    RCADS25_C_Depression_Total_Missing = NMISS(
        RCADS25[1],
        RCADS25[4],
        RCADS25[8],
        RCADS25[10],
        RCADS25[13],
        RCADS25[15],
        RCADS25[16],
        RCADS25[19],
        RCADS25[21],
        RCADS25[24],
    )

    RCADS25_C_Anxiety_Total_Missing = NMISS(
        RCADS25[2],
        RCADS25[3],
        RCADS25[5],
        RCADS25[6],
        RCADS25[7],
        RCADS25[9],
        RCADS25[11],
        RCADS25[12],
        RCADS25[14],
        RCADS25[17],
        RCADS25[18],
        RCADS25[20],
        RCADS25[22],
        RCADS25[23],
        RCADS25[25],
    )

    RCADS25_C_Total_Score_Missing = NMISS(
        RCADS25[1],
        RCADS25[2],
        RCADS25[3],
        RCADS25[4],
        RCADS25[5],
        RCADS25[6],
        RCADS25[7],
        RCADS25[8],
        RCADS25[9],
        RCADS25[10],
        RCADS25[11],
        RCADS25[12],
        RCADS25[13],
        RCADS25[14],
        RCADS25[15],
        RCADS25[16],
        RCADS25[17],
        RCADS25[18],
        RCADS25[19],
        RCADS25[20],
        RCADS25[21],
        RCADS25[22],
        RCADS25[23],
        RCADS25[24],
        RCADS25[25],
    )
    print(
        f"""有{RCADS25_C_Depression_Total_Missing}道抑郁题和{RCADS25_C_Anxiety_Total_Missing}道焦虑题，共{RCADS25_C_Total_Score_Missing}题未作答"""
    )

    # This sums the items to create the RCADS25-C scale scores (NOT taking into account missing items).
    RCADS25_C_Depression_Total_raw = SUM(
        RCADS25[1],
        RCADS25[4],
        RCADS25[8],
        RCADS25[10],
        RCADS25[13],
        RCADS25[15],
        RCADS25[16],
        RCADS25[19],
        RCADS25[21],
        RCADS25[24],
    )
    RCADS25_C_Anxiety_Total_raw = SUM(
        RCADS25[2],
        RCADS25[3],
        RCADS25[5],
        RCADS25[6],
        RCADS25[7],
        RCADS25[9],
        RCADS25[11],
        RCADS25[12],
        RCADS25[14],
        RCADS25[17],
        RCADS25[18],
        RCADS25[20],
        RCADS25[22],
        RCADS25[23],
        RCADS25[25],
    )
    RCADS25_C_Total_Score_raw = SUM(
        RCADS25[1],
        RCADS25[2],
        RCADS25[3],
        RCADS25[4],
        RCADS25[5],
        RCADS25[6],
        RCADS25[7],
        RCADS25[8],
        RCADS25[9],
        RCADS25[10],
        RCADS25[11],
        RCADS25[12],
        RCADS25[13],
        RCADS25[14],
        RCADS25[15],
        RCADS25[16],
        RCADS25[17],
        RCADS25[18],
        RCADS25[19],
        RCADS25[20],
        RCADS25[21],
        RCADS25[22],
        RCADS25[23],
        RCADS25[24],
        RCADS25[25],
    )
    print(
        f"处理缺失项前，抑郁总分为{RCADS25_C_Depression_Total_raw},焦虑总分为{RCADS25_C_Anxiety_Total_raw},两者总分为{RCADS25_C_Total_Score_raw}"
    )

    ##The following syntax prorates each RCADS-C subscale raw score, adjusting for missing data (via mean replacement).
    # 按照数据缺失比例放大结果值，如缺失一半数据，将会把和扩大一倍
    if RCADS25_C_Depression_Total_Missing <= 2:
        RCADS25_C_Depression_Total_raw = (
            RCADS25_C_Depression_Total_raw / (10 - RCADS25_C_Depression_Total_Missing)
        ) * 10
    if RCADS25_C_Anxiety_Total_Missing <= 3:
        RCADS25_C_Anxiety_Total_raw = (
            RCADS25_C_Anxiety_Total_raw / (15 - RCADS25_C_Anxiety_Total_Missing)
        ) * 15
    if RCADS25_C_Total_Score_Missing <= 4:
        RCADS25_C_Total_Score_raw = (
            RCADS25_C_Total_Score_raw / (25 - RCADS25_C_Total_Score_Missing)
        ) * 25
    print(
        f"在处理缺失项以后，抑郁分为{RCADS25_C_Depression_Total_raw:.3f},焦虑分为{RCADS25_C_Anxiety_Total_raw:.3f},总分为{RCADS25_C_Total_Score_raw:.3f}"
    )
    ##This deletes all RCADS subscale raw scores that have more than the allowable amount of missing data.
    if RCADS25_C_Depression_Total_Missing > 2:
        RCADS25_C_Depression_Total_raw = SYSMIS
        print(f"抑郁缺失数据超过2题，该项分值将使用系统默认分值{SYSMIS}")
    if RCADS25_C_Anxiety_Total_Missing > 3:
        RCADS25_C_Anxiety_Total_raw = SYSMIS
        print(f"焦虑缺失数据超过3题，该项分值将使用系统默认分值{SYSMIS}")
    if RCADS25_C_Total_Score_Missing > 4:
        RCADS25_C_Total_Score_raw = SYSMIS
        print(f"总共缺失数据超4题，总分将使用系统默认分值{SYSMIS}")

    ###########T Scores for the RCADS25-C Scales (updated on 2015_02_03).#######*

    # 3~4年级男生
    if (grade <= 4) and (sex == 1):
        RCADS25_C_MDD_T = ((RCADS25_C_Depression_Total_raw - 9.90) * 10) / 4.93 + 50
    if (grade <= 4) and (sex == 1):
        RCADS25_C_Anxiety_Total_t = (
            (RCADS25_C_Anxiety_Total_raw - 15.19) * 10
        ) / 7.09 + 50
    if (grade <= 4) and (sex == 1):
        RCADS25_C_Total_Score_t = (
            (RCADS25_C_Total_Score_raw - 25.10) * 10
        ) / 11.10 + 50

    # 3~4年级女生
    if (grade <= 4) and (sex == 2):
        RCADS25_C_MDD_T = ((RCADS25_C_Depression_Total_raw - 9.68) * 10) / 4.97 + 50
    if (grade <= 4) and (sex == 2):
        RCADS25_C_Anxiety_Total_t = (
            (RCADS25_C_Anxiety_Total_raw - 16.25) * 10
        ) / 8.42 + 50
    if (grade <= 4) and (sex == 2):
        RCADS25_C_Total_Score_t = (
            (RCADS25_C_Total_Score_raw - 25.93) * 10
        ) / 12.24 + 50

    # 5~6年级男生
    if ((grade == 5) or (grade == 6)) and (sex == 1):
        RCADS25_C_MDD_T = ((RCADS25_C_Depression_Total_raw - 7.13) * 10) / 4.22 + 50
    if ((grade == 5) or (grade == 6)) and (sex == 1):
        RCADS25_C_Anxiety_Total_t = (
            (RCADS25_C_Anxiety_Total_raw - 11.63) * 10
        ) / 6.45 + 50
    if ((grade == 5) or (grade == 6)) and (sex == 1):
        RCADS25_C_Total_Score_t = ((RCADS25_C_Total_Score_raw - 18.76) * 10) / 9.38 + 50

    # 5~6年级女生
    if ((grade == 5) or (grade == 6)) and (sex == 2):
        RCADS25_C_MDD_T = ((RCADS25_C_Depression_Total_raw - 8.03) * 10) / 5.00 + 50
    if ((grade == 5) or (grade == 6)) and (sex == 2):
        RCADS25_C_Anxiety_Total_t = (
            (RCADS25_C_Anxiety_Total_raw - 13.49) * 10
        ) / 7.62 + 50
    if ((grade == 5) or (grade == 6)) and (sex == 2):
        RCADS25_C_Total_Score_t = (
            (RCADS25_C_Total_Score_raw - 21.53) * 10
        ) / 11.73 + 50

    # 7~8年级男生
    if ((grade == 7) or (grade == 8)) and (sex == 1):
        RCADS25_C_MDD_T = ((RCADS25_C_Depression_Total_raw - 7.56) * 10) / 3.75 + 50
    if ((grade == 7) or (grade == 8)) and (sex == 1):
        RCADS25_C_Anxiety_Total_t = (
            (RCADS25_C_Anxiety_Total_raw - 10.48) * 10
        ) / 5.36 + 50
    if ((grade == 7) or (grade == 8)) and (sex == 1):
        RCADS25_C_Total_Score_t = ((RCADS25_C_Total_Score_raw - 18.04) * 10) / 7.92 + 50

    # 7~8年级女生
    if ((grade == 7) or (grade == 8)) and (sex == 2):
        RCADS25_C_MDD_T = ((RCADS25_C_Depression_Total_raw - 8.08) * 10) / 4.34 + 50
    if ((grade == 7) or (grade == 8)) and (sex == 2):
        RCADS25_C_Anxiety_Total_t = (
            (RCADS25_C_Anxiety_Total_raw - 12.74) * 10
        ) / 6.22 + 50
    if ((grade == 7) or (grade == 8)) and (sex == 2):
        RCADS25_C_Total_Score_t = ((RCADS25_C_Total_Score_raw - 20.82) * 10) / 9.46 + 50

    # 9~10年级男生
    if ((grade == 9) or (grade == 10)) and (sex == 1):
        RCADS25_C_MDD_T = ((RCADS25_C_Depression_Total_raw - 7.50) * 10) / 4.18 + 50
    if ((grade == 9) or (grade == 10)) and (sex == 1):
        RCADS25_C_Anxiety_Total_t = (
            (RCADS25_C_Anxiety_Total_raw - 9.70) * 10
        ) / 5.45 + 50
    if ((grade == 9) or (grade == 10)) and (sex == 1):
        RCADS25_C_Total_Score_t = ((RCADS25_C_Total_Score_raw - 17.20) * 10) / 8.53 + 50

    # 9~10年级女生
    if ((grade == 9) or (grade == 10)) and (sex == 2):
        RCADS25_C_MDD_T = ((RCADS25_C_Depression_Total_raw - 8.14) * 10) / 4.37 + 50
    if ((grade == 9) or (grade == 10)) and (sex == 2):
        RCADS25_C_Anxiety_Total_t = (
            (RCADS25_C_Anxiety_Total_raw - 11.31) * 10
        ) / 5.33 + 50
    if ((grade == 9) or (grade == 10)) and (sex == 2):
        RCADS25_C_Total_Score_t = ((RCADS25_C_Total_Score_raw - 19.45) * 10) / 8.63 + 50

    # 11~12年级男生
    if (grade >= 11) and (sex == 1):
        RCADS25_C_MDD_T = ((RCADS25_C_Depression_Total_raw - 7.64) * 10) / 4.37 + 50
    if (grade >= 11) and (sex == 1):
        RCADS25_C_Anxiety_Total_t = (
            (RCADS25_C_Anxiety_Total_raw - 9.96) * 10
        ) / 4.32 + 50
    if (grade >= 11) and (sex == 1):
        RCADS25_C_Total_Score_t = ((RCADS25_C_Total_Score_raw - 17.60) * 10) / 7.24 + 50

    # 11~12年级女生
    if (grade >= 11) and (sex == 2):
        RCADS25_C_MDD_T = ((RCADS25_C_Depression_Total_raw - 8.59) * 10) / 3.67 + 50
    if (grade >= 11) and (sex == 2):
        RCADS25_C_Anxiety_Total_t = (
            (RCADS25_C_Anxiety_Total_raw - 11.50) * 10
        ) / 5.34 + 50
    if (grade >= 11) and (sex == 2):
        RCADS25_C_Total_Score_t = ((RCADS25_C_Total_Score_raw - 20.09) * 10) / 7.79 + 50

    print(
        f"焦虑T分数为{RCADS25_C_MDD_T:.3f}, 抑郁T分数为{RCADS25_C_Anxiety_Total_t:.3f}, 总的T分数为{RCADS25_C_Total_Score_t:.3f}"
    )

    out_grade = ["Normal", "Borderline", "Clinical"]

    # *Compute RCADS25-C scale elevations.
    RCADS25_C_Total_Elevation = SYSMIS
    if RCADS25_C_Total_Score_t < 65:
        RCADS25_C_Total_Elevation = 0
    if RCADS25_C_Total_Score_t >= 65 and RCADS25_C_Total_Score_t < 70:
        RCADS25_C_Total_Elevation = 1
    if RCADS25_C_Total_Score_t >= 70:
        RCADS25_C_Total_Elevation = 2

    RCADS25_C_Total_Elevation = out_grade[RCADS25_C_Total_Elevation]

    RCADS25_C_Depression_Elevation = SYSMIS
    if RCADS25_C_MDD_T < 65:
        RCADS25_C_Depression_Elevation = 0
    if RCADS25_C_MDD_T >= 65 and RCADS25_C_MDD_T < 70:
        RCADS25_C_Depression_Elevation = 1
    if RCADS25_C_MDD_T >= 70:
        RCADS25_C_Depression_Elevation = 2
    RCADS25_C_Depression_Elevation = out_grade[RCADS25_C_Depression_Elevation]

    RCADS25_C_Anxiety_Elevation = SYSMIS
    if RCADS25_C_Anxiety_Total_t < 65:
        RCADS25_C_Anxiety_Elevation = 0
    if RCADS25_C_Anxiety_Total_t >= 65 and RCADS25_C_Anxiety_Total_t < 70:
        RCADS25_C_Anxiety_Elevation = 1
    if RCADS25_C_Anxiety_Total_t >= 70:
        RCADS25_C_Anxiety_Elevation = 2
    RCADS25_C_Anxiety_Elevation = out_grade[RCADS25_C_Anxiety_Elevation]

    print(
        f"总评级为{RCADS25_C_Total_Elevation}, 抑郁评级为{RCADS25_C_Depression_Elevation}, 焦虑评级为{RCADS25_C_Anxiety_Elevation}"
    )
    return list(
        map(
            lambda x: round(x, 3),
            [
                RCADS25_C_Depression_Total_raw,
                RCADS25_C_Anxiety_Total_raw,
                RCADS25_C_Total_Score_raw,
                RCADS25_C_MDD_T,
                RCADS25_C_Anxiety_Total_t,
                RCADS25_C_Total_Score_t,
            ],
        )
    )


person_data_list = []
with open(f, encoding="utf-8-sig") as csvfile:  # 不用sig的话会有bom头 \uffee
    reader = csv.DictReader(csvfile)
    for row in reader:
        RCADS25 = [-1]
        insert_tmp = [row["序号"], row["您的姓名或称呼"]]
        # row=OrderedDict(row) # python 3.7以上,dict将保持插入序
        for k, v in row.items():
            if k[0].isdigit():
                RCADS25.append(int(v))
        if len(RCADS25) == 26:
            insert_tmp.extend(
                get_score(
                    score=RCADS25,
                    grade=min(int(row["您的年龄"]) - 6, 12),
                    sex={"男": 1, "女": 2}[row["您的性别"]],
                )
            )
            p = Person(*insert_tmp)
            print(p)
        else:
            print("个数不对")
        person_data_list.append(asdict(p))

with open(
    "RCADS_analysis.csv", "w", encoding="gb2312", newline=""
) as csvfile:  # newline为空才能紧凑
    writer = csv.DictWriter(csvfile, list(map(lambda x: x.name, fields(Person))))
    print(list(map(lambda x: x.name, fields(Person))))
    writer.writeheader()
    writer.writerows(person_data_list)
