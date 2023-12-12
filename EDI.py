from docxtpl import DocxTemplate


def edi_export(doctype='sell', date='', sum=0, custumer='', seller='', goods=None):
    if doctype == 'sell':
        doc = DocxTemplate(r'templates\sell_template.docx')
        goods_list = ''
        for key, value in goods.items():
            goods_list += f"{key} x {value} "
        context = {'date': date,
                   'customer': custumer,
                   'sum': str(sum)+' руб',
                   'seller': seller,
                   'goods': goods_list}
        doc.render(context)
        doc.save(r'EDI\sell_'+date+'.docx')
        edi_export(date='12.12.2023',
                   custumer='Андрей',
                   seller='Костя',
                   goods={'готовый проект': 1})
