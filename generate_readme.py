import pandas as pd
import constants


def format_data(data, sort='学校', sep='\t'):
    '''
    功能：将以 sep 分割的表格数据 格式化 为按学校或学科排列的数据
    参数：sort 学校/学科
    '''
    assert(sort in ('学校', '学科'))
    the_other = '学科' if sort == '学校' else '学校'
    result = ''
    last = ''
    for line in data.iterrows():
        xx, xk, jg, tc = line.iloc[range(4)]
        if xx == '学校':
            continue
        # 若按学科排列，则将 xx 和 xk 数据对调
        # 即变量 xx 代指分组依据，xk 代表组内的不同数据标签
        if sort == '学科':
            xx, xk = xk, xx
        if last != xx:
            last = xx
            result += f'\n### {xx}\n\n'
            result += f'''| {the_other} | 等级/结果 | 推测等级或第四轮等级 |
    | -------------- | ------------------------------ | -------------------- |\n'''
        result += f'| {xk} | {jg} | {tc} |\n'
    return result

def generate():
    data = pd.read_table('original_data.csv', sep=",", encoding='gbk')
    order_by_school = format_data(data, sort='学校')
    order_by_discipline = format_data(data, sort='学科')
    text = constants.TEMPLATE_README.format(order_by_school=order_by_school, order_by_discipline=order_by_discipline)
    return text

with open('README.md', 'w') as f:
    f.write(generate())