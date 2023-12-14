from docxtpl import DocxTemplate
from openpyxl import Workbook
from openpyxl import load_workbook


def edi_export(doctype='sell', date='',
               reciever='', sender='',
               goods=None,
               pass_num=0, pass_date='', pass_exp_date=''):
    """
    Export to docx and xlsx file

    :param doctype: type of document - one of [sell,pass,invoice,move, arrival, write-off]
    :param date: date of document creation
    :param reciever: one who recieves goods
    :param sender: one who sends goods
    :param goods: dict of goods transfered or dict of a good properties
    :param pass_num: passport number
    :param pass_date: date passport issued
    :param pass_exp_date: date passport expires
    :return: names of the files created
    """

    if doctype == 'sell':
        wb = load_workbook(r'templates\sell_template.xlsx')
        ws = wb.active
        doc = DocxTemplate(r'templates\sell_template.docx')
        goods_list = ''
        total = 0
        for key, value in goods.items():
            a = [key]
            a.extend(list(value.values()))
            ws.append(a)
            total += value['amount'] * value['price']
            goods_list += f"{key} x {value['amount']} "
        context = {'date': date,
                   'customer': reciever,
                   'sum': str(total)+' руб',
                   'seller': sender,
                   'goods': goods_list}
        doc.render(context)
        doc.save(r'EDI\sell_'+date+'.docx')
        wb.save(r'EDI\sell_' + date + '.xlsx')
        return r'EDI\sell_'+date+'.docx', r'EDI\sell_' + date + '.xlsx'

    if doctype == 'pass':
        doc = DocxTemplate(r'templates\pass_template.docx')
        prop_list = '\n'
        for key, value in goods[list(goods.keys())[0]].items():
            if key != 'exp_date':
                prop_list += f"{key} : {str(value)} \n"
        context = {'name': list(goods.keys())[0],
                   'exp_date': goods[list(goods.keys())[0]]['exp_date'],
                   'pass_num': pass_num,
                   'pass_date': pass_date,
                   'pass_exp_date': pass_exp_date,
                   'properties': prop_list}
        doc.render(context)
        doc.save(r'EDI\pass_' + date + '.docx')
        return r'EDI\pass_' + date + '.docx'

edi_export(date='12.12.2023',
           reciever='Андрей',
           sender='Костя',
           goods={'готовый проект': {'amount': 1,
                                     'price': 1000,
                                     'mass': 'very heavy'
                                     }})
edi_export(doctype='passport',
           pass_num=1707,
           date='12.13.2023',
           pass_date='11.13.2023',
           pass_exp_date='не ограничен',
           goods={'готовый проект': {'душность': 100,
                                     'стабильность': 0.1,
                                     'масса': 'very heavy',
                                     'exp_date': 'не ограничен'
                                     }})
