
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'left+-left*/rightUMINUSFLOATDEC FNUMBER INTDEC INUMBER NAME PRINT STRING STRINGDECstatement : INTDEC NAME is_assing\n    is_assing : "=" expression \n                | statement : FLOATDEC NAME is_assingstatement : STRINGDEC NAME is_assingstatement : PRINT \'(\' expression \')\' statement : NAME "=" expressionstatement : expressionexpression : expression \'+\' expression\n                  | expression \'-\' expression\n                  | expression \'*\' expression\n                  | expression \'/\' expression\n                  | expression \'^\' expressionexpression : \'-\' expression %prec UMINUSexpression : \'(\' expression \')\'expression : INUMBERexpression : FNUMBERexpression :  STRINGexpression : NAME'
    
_lr_action_items = {'INTDEC':([0,],[2,]),'FLOATDEC':([0,],[4,]),'STRINGDEC':([0,],[5,]),'PRINT':([0,],[6,]),'NAME':([0,2,4,5,7,9,14,17,20,21,22,23,24,27,],[3,13,15,16,19,19,19,19,19,19,19,19,19,19,]),'-':([0,3,7,8,9,10,11,12,14,17,18,19,20,21,22,23,24,25,27,28,31,32,33,34,35,36,37,38,],[9,-19,9,21,9,-16,-17,-18,9,9,21,-19,9,9,9,9,9,-14,9,21,21,-15,-9,-10,-11,-12,21,21,]),'(':([0,6,7,9,14,17,20,21,22,23,24,27,],[7,17,7,7,7,7,7,7,7,7,7,7,]),'INUMBER':([0,7,9,14,17,20,21,22,23,24,27,],[10,10,10,10,10,10,10,10,10,10,10,]),'FNUMBER':([0,7,9,14,17,20,21,22,23,24,27,],[11,11,11,11,11,11,11,11,11,11,11,]),'STRING':([0,7,9,14,17,20,21,22,23,24,27,],[12,12,12,12,12,12,12,12,12,12,12,]),'$end':([1,3,8,10,11,12,13,15,16,19,25,26,28,29,30,32,33,34,35,36,37,38,39,],[0,-19,-8,-16,-17,-18,-3,-3,-3,-19,-14,-1,-7,-4,-5,-15,-9,-10,-11,-12,-13,-2,-6,]),'=':([3,13,15,16,],[14,27,27,27,]),'+':([3,8,10,11,12,18,19,25,28,31,32,33,34,35,36,37,38,],[-19,20,-16,-17,-18,20,-19,-14,20,20,-15,-9,-10,-11,-12,20,20,]),'*':([3,8,10,11,12,18,19,25,28,31,32,33,34,35,36,37,38,],[-19,22,-16,-17,-18,22,-19,-14,22,22,-15,22,22,-11,-12,22,22,]),'/':([3,8,10,11,12,18,19,25,28,31,32,33,34,35,36,37,38,],[-19,23,-16,-17,-18,23,-19,-14,23,23,-15,23,23,-11,-12,23,23,]),'^':([3,8,10,11,12,18,19,25,28,31,32,33,34,35,36,37,38,],[-19,24,-16,-17,-18,24,-19,-14,24,24,-15,-9,-10,-11,-12,24,24,]),')':([10,11,12,18,19,25,31,32,33,34,35,36,37,],[-16,-17,-18,32,-19,-14,39,-15,-9,-10,-11,-12,-13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,7,9,14,17,20,21,22,23,24,27,],[8,18,25,28,31,33,34,35,36,37,38,]),'is_assing':([13,15,16,],[26,29,30,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> INTDEC NAME is_assing','statement',3,'p_statement_declare_int','compiler.py',61),
  ('is_assing -> = expression','is_assing',2,'p_is_assing','compiler.py',69),
  ('is_assing -> <empty>','is_assing',0,'p_is_assing','compiler.py',70),
  ('statement -> FLOATDEC NAME is_assing','statement',3,'p_statement_declare_float','compiler.py',76),
  ('statement -> STRINGDEC NAME is_assing','statement',3,'p_statement_declare_string','compiler.py',80),
  ('statement -> PRINT ( expression )','statement',4,'p_statement_print','compiler.py',84),
  ('statement -> NAME = expression','statement',3,'p_statement_assign','compiler.py',88),
  ('statement -> expression','statement',1,'p_statement_expr','compiler.py',94),
  ('expression -> expression + expression','expression',3,'p_expression_binop','compiler.py',98),
  ('expression -> expression - expression','expression',3,'p_expression_binop','compiler.py',99),
  ('expression -> expression * expression','expression',3,'p_expression_binop','compiler.py',100),
  ('expression -> expression / expression','expression',3,'p_expression_binop','compiler.py',101),
  ('expression -> expression ^ expression','expression',3,'p_expression_binop','compiler.py',102),
  ('expression -> - expression','expression',2,'p_expression_uminus','compiler.py',115),
  ('expression -> ( expression )','expression',3,'p_expression_group','compiler.py',119),
  ('expression -> INUMBER','expression',1,'p_expression_inumber','compiler.py',123),
  ('expression -> FNUMBER','expression',1,'p_expression_fnumber','compiler.py',127),
  ('expression -> STRING','expression',1,'p_expression_string','compiler.py',131),
  ('expression -> NAME','expression',1,'p_expression_name','compiler.py',135),
]
