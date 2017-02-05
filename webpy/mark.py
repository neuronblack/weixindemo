# -*- coding: utf-8 -*-
import requests
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def huada(account,password):
    data = {
        '__VIEWSTATE': '/wEPDwUKMTM5MjUxOTk4Nw9kFgJmD2QWHgICDxAPFgIeB1Zpc2libGVoZGQWAWZkAgMPEA8WAh8AaGRkZGQCBA8QDxYCHwBoZGRkZAIFDxAPFgIeBFRleHQFCeaVmeWKoeWkhGRkZGQCBg8QDxYCHwBoZGRkZAIHDxAPFgIfAQUG5a2m6ZmiZGRkZAIIDxAPFgIfAGhkZGRkAgkPEA8WAh8BBQnnj63kuLvku7tkZGRkAgoPEA8WAh8BBQbmlZnluIhkZGRkAgsPEA8WAh8BBQblrabnlJ9kZGRkAgwPEA8WAh8AaGRkZGQCDQ8QDxYCHwBoZGRkZAIODxAPFgIfAGhkZGRkAg8PEA8WAh8AaGRkZGQCEA8QDxYCHwBoZGRkZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WCQUMUmFkaW9CdXR0b240BQxSYWRpb0J1dHRvbjQFDFJhZGlvQnV0dG9uMgUMUmFkaW9CdXR0b24yBQxSYWRpb0J1dHRvbjYFDFJhZGlvQnV0dG9uNgUMUmFkaW9CdXR0b24xBQxSYWRpb0J1dHRvbjEFDFJhZGlvQnV0dG9uM8c66bWHs+JN+3yDHwHNxQznHCfZlUbTvu1dhKF3ja8z',
        'TextBox1': account,
        'TextBox2': password,
        'js': 'RadioButton3',
        'Button1': '登陆'}
    sel = requests.Session()
    sel.post('http://58.213.51.196:81/(S(3pzm2oexfqclq51pw5p3uy2g))/default.aspx', data=data)
    html = sel.get('http://58.213.51.196:81/(S(3pzm2oexfqclq51pw5p3uy2g))/student/chengji.aspx')
    data = etree.HTML(html.text)
    mark = data.xpath('//*[@id="GridView1"]/tr')
    content = ''
    bad = ''
    for i in range(2, len(mark)):
        time = mark[i].xpath('td[1]/text()')[0]
        credit = mark[i].xpath('td[8]/text()')[0]
        project_class = mark[i].xpath('td[4]/text()')[0]
        project = mark[i].xpath('td[3]/text()')[0]
        grade = mark[i].xpath('td[5]/text()')[0]
        final = time + ' ' + project + ' ' + project_class + ' ' + grade + ' ' + credit + '\n'
        content += final
    defeat = data.xpath('//*[@id="Gridview2"]/tr[2]/td/text()')
    if defeat[0].encode('utf-8') == '搜索结果为空':
        bad += '无挂科'
    else:
        lost = data.xpath('//*[@id="Gridview2"]/tr/td[3]/text()')
        for i in range(0, len(lost)):
            bad += lost[i] + ' '
    content = content + u'已挂科目:' + bad
    return content