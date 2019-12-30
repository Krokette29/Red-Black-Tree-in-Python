#################################################################
# Author: Yuhan Huang
# Date: 2019.12.30
# Github homepage: https://github.com/Krokette29
#################################################################

import random
from RedBlackTree import *

# test for randomly insertion and deletion
treeRBT = RedBlackTree()
num_nodes = 20

# insertion
key_list = [random.randint(1000, 2000) for i in range(num_nodes)]
value_list = [random.randint(0, 100) for i in range(1, num_nodes + 1)]
random.shuffle(key_list)
print("key list: {}".format(key_list))
print("value list: {}".format(value_list))
for i in range(num_nodes):
    treeRBT.insert(key_list[i], value_list[i])

treeRBT.check_all()
treeRBT.show_paths()

# show all information of all nodes
# for i in treeRBT:
#     i.show_info()

# deletion
delete_list = [i for i in range(num_nodes)]
random.shuffle(delete_list)
for i in range(num_nodes):
    delete_index = delete_list[i]
    treeRBT.delete(key_list[delete_index])
    print("delete {} : {}".format(key_list[delete_index], value_list[delete_index]))
    treeRBT.check_all(output_information=False)

treeRBT.show_paths()
