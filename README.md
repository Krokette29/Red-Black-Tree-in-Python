# Red-Black-Tree-in-Python
RBT in Python.

## class NodeRBT:
  - get_color() -> string
  - show_info()
  - get_info_in_tuple() -> (key, value, color, size_tree)
  - reset()
  
 ## class RedBlackTree:
  - size
  - check_balance(output_information=True)
  - check_color(output_information=True)
  - check_all(self, output_information=True)
  - get_node(key, print_path=False) -> NodeRBT
  - search(key, print_path=False)
  - select(self, index) -> NodeRBT
  - get_predecessor(key) -> NodeRBT
  - get_successor(key) -> NodeRBT
  - insert(key, value)
  - delete(key)
  - str_single_path(node) -> string
  - show_paths()
  
