TEMPLATE_README = '''# 第五轮学科评估官宣完全汇总（附出处）
收录**可公开查到**（或曾经可公开查到）的由**官方平台、官方人士**宣布的学科评估结果

- 包括：微信公众号、官网、公开直播截图、官媒
- 不包括：无法公开验证真实性的传言、聊天记录截图、转述

可按学校查看结果，也可按学科查看

第二列是**原话**，第三列对模糊性表述进行推测或者给出第四轮结果以作参考

正文只有等级数据，含**每条信息详细出处和备注**的完整数据截图可以拉到文章最后查看

146 所学校，90 个学科，近 500 条数据，整理不易，**客官点个 Star 吧～**

## 结果按学校排列（拼音序）

{order_by_school}

## 结果按学科排列

学科依门类排序，各学科内依学校拼音排序（数据不方便按等级高低排）

| 学科门类 | 一级学科（学科大类）                                         |
| -------- | ------------------------------------------------------------ |
| 哲学     | 哲学                                                         |
| 经济学   | 理论经济学、应用经济学                                       |
| 法学     | 法学、政治学、社会学、民族学、马克思主义理论、公安学         |
| 教育学   | 教育学、心理学、体育学                                       |
| 文学     | 中国语言文学、外国语言文学、新闻传播学                       |
| 历史学   | 考古学、中国史、世界史                                       |
| 理学     | 数学、物理学、化学、天文学、地理学、大气科学、海洋科学、地球物理学、地质学、生物学、系统科学、科学技术史、生态学、统计学 |
| 工学     | 力学、机械工程、光学工程、仪器科学与技术、材料科学与工程、冶金工程、动力工程及工程热物理、电气工程、电子科学与技术、信息与通信工程、控制科学与工程、计算机科学与技术、建筑学、土木工程、水利工程、测绘科学与技术、化学工程与技术、地质资源与地质工程、矿业工程、石油与天然气工程、纺织科学与工程、轻工技术与工程、交通运输工程、船舶与海洋工程、航空宇航科学与技术、兵器科学与技术、核科学与技术、农业工程、林业工程、环境科学与工程、生物医学工程、食品科学与工程、城乡规划学、风景园林学、软件工程、生物工程、安全科学与工程、公安技术、网络空间安全 |
| 农学     | 作物学、园艺学、农业资源与环境、植物保护、畜牧学、兽医学、林学、水产、草学 |
| 医学     | 基础医学、临床医学、口腔医学、公共卫生与预防医学、中医学、中西医结合、药学、中药学、特种医学、医学技术、护理学 |
| 军事学   | 军事思想及军事历史、战略学、战役学、战术学、军队指挥学、军制学、军队政治工作学、军事后勤学、军事装备学、军事训练学 |
| 管理学   | 管理科学与工程、工商管理、农林经济管理、公共管理、信息资源管理、物流管理与工程类、工业工程类、电子商务类、旅游管理类 |
| 艺术学   | 艺术学理论、音乐与舞蹈学、戏剧与影视学、美术学、设计学       |

{order_by_discipline}

## 完整数据截图（含详细出处）

![image](https://github.com/zjsxply/China-Discipline-Evaluation/blob/main/%E7%AC%AC%E4%BA%94%E8%BD%AE%E5%AD%A6%E7%A7%91%E8%AF%84%E4%BC%B0%E5%AE%98%E5%AE%A3%E7%BB%93%E6%9E%9C%E6%B1%87%E6%80%BB.png?raw=true)
'''

DISCIPLINE_CODE = {
    '哲学': 101,
    '理论经济学': 201,
    '应用经济学': 202,
    '法学': 301,
    '政治学': 302,
    '社会学': 303,
    '民族学': 304,
    '马克思主义理论': 305,
    '公安学': 306,
    '教育学': 401,
    '心理学': 402,
    '体育学': 403,
    '中国语言文学': 501,
    '外国语言文学': 502,
    '新闻传播学': 503,
    '考古学': 601,
    '中国史': 602,
    '世界史': 603,
    '数学': 701,
    '物理学': 702,
    '化学': 703,
    '天文学': 704,
    '地理学': 705,
    '大气科学': 706,
    '海洋科学': 707,
    '地球物理学': 708,
    '地质学': 709,
    '生物学': 710,
    '系统科学': 711,
    '科学技术史': 712,
    '生态学': 713,
    '统计学': 714,
    '力学': 801,
    '机械工程': 802,
    '光学工程': 803,
    '仪器科学与技术': 804,
    '材料科学与工程': 805,
    '冶金工程': 806,
    '动力工程及工程热物理': 807,
    '电气工程': 808,
    '电子科学与技术': 809,
    '信息与通信工程': 810,
    '控制科学与工程': 811,
    '计算机科学与技术': 812,
    '建筑学': 813,
    '土木工程': 814,
    '水利工程': 815,
    '测绘科学与技术': 816,
    '化学工程与技术': 817,
    '地质资源与地质工程': 818,
    '矿业工程': 819,
    '石油与天然气工程': 820,
    '纺织科学与工程': 821,
    '轻工技术与工程': 822,
    '交通运输工程': 823,
    '船舶与海洋工程': 824,
    '航空宇航科学与技术': 825,
    '兵器科学与技术': 826,
    '核科学与技术': 827,
    '农业工程': 828,
    '林业工程': 829,
    '环境科学与工程': 830,
    '生物医学工程': 831,
    '食品科学与工程': 832,
    '城乡规划学': 833,
    '风景园林学': 834,
    '软件工程': 835,
    '生物工程': 836,
    '安全科学与工程': 837,
    '公安技术': 838,
    '网络空间安全': 839,
    '作物学': 901,
    '园艺学': 902,
    '农业资源与环境': 903,
    '植物保护': 904,
    '畜牧学': 905,
    '兽医学': 906,
    '林学': 907,
    '水产': 908,
    '草学': 909,
    '基础医学': 1001,
    '临床医学': 1002,
    '口腔医学': 1003,
    '公共卫生与预防医学': 1004,
    '中医学': 1005,
    '中西医结合': 1006,
    '药学': 1007,
    '中药学': 1008,
    '特种医学': 1009,
    '医学技术': 1010,
    '护理学': 1011,
    '军事思想及军事历史': 1101,
    '战略学': 1102,
    '战役学': 1103,
    '战术学': 1104,
    '军队指挥学': 1105,
    '军制学': 1106,
    '军队政治工作学': 1107,
    '军事后勤学': 1108,
    '军事装备学': 1109,
    '军事训练学': 1110,
    '管理科学与工程': 1201,
    '工商管理': 1202,
    '农林经济管理': 1203,
    '公共管理': 1204,
    '信息资源管理': 1205,
    '物流管理与工程类': 1206,
    '工业工程类': 1207,
    '电子商务类': 1208,
    '旅游管理类': 1209,
    '艺术学理论': 1301,
    '音乐与舞蹈学': 1302,
    '戏剧与影视学': 1303,
    '美术学': 1304,
    '设计学': 1305,
}