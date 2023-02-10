import pandas as pd
import numpy as np
import constants
from pypinyin import pinyin, lazy_pinyin, Style


def format_data(df, sort='学校'):
    '''
    功能：将 dataframe 格式化 为按学校或学科排列的数据
    参数：sort 学校/学科
    '''
    assert(sort in ('学校', '学科'))
    the_other = '学科' if sort == '学校' else '学校'
    result = ''
    last = ''
    for index, line in df.iterrows():
        xx, xk, jg, tc = line[:4]
        if xx == '学校':
            continue
        # 若按学科排列，则将 xx 和 xk 数据对调
        # 即变量 xx 代指分组依据，xk 代表组内的不同数据标签
        if sort == '学科':
            xx, xk = xk, xx
        if last != xx:
            last = xx
            result += f'\n### {xx}\n\n'
            result += f'''| {the_other} | 等级（原话） | 推测等级或第四轮等级 | \n| -------------- | ------------------------------ | -------------------- |\n'''
        if line['链接'].startswith('http'):
            jg = '[{}]({})'.format(jg, line['链接']) if line['链接'].startswith('http') else line['链接']
        result += f'| {xk} | {jg} | {tc} |\n'
    return result

def generate():
    df = pd.read_table('original_data.csv', sep=",", encoding='gbk')
    df.fillna('', inplace=True)
    data_count = df.shape[0]
    
    """ # 截取所需要的数据，并去重
    sorted_df = df[['学校','学科','等级/结果','推测等级或第四轮等级']]
    sorted_df = sorted_df.drop_duplicates() """
    
    # 排序并格式化数据，按学科排列时忽略非标准学科名称的行
    df['学校拼音'] = df['学校'].map(lambda x: tuple(lazy_pinyin(x)))
    df['学科代码'] = df['学科'].map(lambda x: constants.DISCIPLINE_CODE.get(x, np.nan))
    order_by_school = format_data(df.sort_values(by=['学校拼音', '学科代码'], na_position='first'), sort='学校')
    order_by_discipline = format_data(df.dropna().sort_values(by=['学科代码', '学校拼音']), sort='学科')
    
    school_count = df['学校'].drop_duplicates().shape[0]
    discipline_count = df['学科代码'].drop_duplicates().shape[0]
    text = constants.TEMPLATE_README.format(order_by_school=order_by_school, order_by_discipline=order_by_discipline, school_count=school_count, discipline_count=discipline_count, data_count=data_count)
    return text

with open('README.md', 'w') as f:
    f.write(generate())

