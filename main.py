import random

from test_card import *
import test_card_list
import test_hand_and_deck
import test_row
import test_table

print('test_card ========')
test_create()
test_score()
test_eq()
test_lt()

print('test_card_list ========')
test_card_list.test_card_list()
test_card_list.test_card_list_i()
test_card_list.test_card_list_draw()

print('test_deck ============')
test_hand_and_deck.test_deck()
test_hand_and_deck.test_hand()
test_hand_and_deck.test_hand_load()

print('test_row ============')
test_row.test_top()
test_row.test_acceptable()
test_row.test_overflow()
test_row.test_lt()
test_row.test_cut()

print('test_table ============')
test_table.test_table_rows()
test_table.table_create()
test_table.test_acceptable()