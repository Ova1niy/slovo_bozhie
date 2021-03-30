# -*- coding: cp1251 -*-

from corus import load_lenta
from navec import Navec
from slovnet import NER
from ipymarkup import show_span_ascii_markup as show_markup

import text_processor as tp
import random

navec_path = 'downloads/navec_news_v1_1B_250K_300d_100q.tar'
ner_path = 'downloads/slovnet_ner_news_v1.tar'
lenta_path = 'downloads/lenta-ru-news.csv.gz'
N = 3000


def get_random_record(records):
    k = random.randint(0,N)
    record = records
    for i in range(k):
        record = next(records)
    return record, k


def get_k_record(records, k):
    record = records
    for i in range(k):
        record = next(records)
    return record


def test_on_random_record():
    records = load_lenta(lenta_path)
    record, k = get_random_record(records)
    markup = ner(record.text)
    print('This is ' + tp.BOLD + tp.RED + f'{k}' + tp.END + ' record\n')
    show_markup(markup.text, markup.spans)


def test_on_k_random_records(K):
    records = load_lenta(lenta_path)
    records_num = [i for i in range(N)]
    chosen_records_num = random.choices(records_num, k=K)
    my_records = []
    for i in chosen_records_num:
        my_records.append(get_k_record(records, i))

    print(f'This is ' + tp.BOLD + tp.RED + f'{chosen_records_num}' + tp.END + ' records\n')

    for i in range(K):
        print(tp.BOLD + tp.RED + f'{chosen_records_num[i]}' + tp.END + '\t')
        markup = ner(my_records[i].text)
        show_markup(markup.text, markup.spans)
        print('\n--------------------------\n\n')


if __name__ == '__main__':
    print()
    navec = Navec.load(navec_path)
    ner = NER.load(ner_path)
    ner.navec(navec)
    test_on_random_record()
    test_on_k_random_records(5)