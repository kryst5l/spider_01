from pyecharts import Bar
bar = Bar("�ҵĵ�һ��ͼ��", "�����Ǹ�����")
bar.add("��װ", ["����", "��ë��", "ѩ����", "����", "�߸�Ь", "����"], [5, 20, 36, 10, 75,100],is_more_utils=True,is_label_emphasis=True)
bar.show_config()
bar.render()

