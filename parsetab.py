
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'left+-left*/rightUMINUSAND BOOLEAN BOOLEANDEC EQUAL FLOATDEC FNUMBER GREATER GREATEREQUAL INTDEC INUMBER LESSEQUAL LESSTHAN NAME NOTEQUAL OR PRINT SEMICOLON STRING STRINGDECcode : statement SEMICOLONstatement : INTDEC NAME is_assing\n    is_assing : "=" expression \n                | statement : FLOATDEC NAME is_assingstatement : BOOLEANDEC NAME is_assingstatement : STRINGDEC NAME is_assingstatement : PRINT \'(\' expression \')\' statement : NAME "=" expressionstatement : expressionexpression : expression \'+\' expression\n                  | expression \'-\' expression\n                  | expression \'*\' expression\n                  | expression \'/\' expression\n                  | expression \'^\' expressionexpression : expression EQUAL expression\n                  | expression NOTEQUAL expression\n                  | expression GREATER expression\n                  | expression LESSTHAN expression\n                  | expression GREATEREQUAL expression\n                  | expression LESSEQUAL expressionexpression : expression AND expression\n                  | expression OR expressionexpression : \'-\' expression %prec UMINUSexpression : \'(\' expression \')\'expression : INUMBERexpression : FNUMBERexpression :  BOOLEANexpression :  STRINGexpression : NAME'
    
_lr_action_items = {'INTDEC':([0,],[3,]),'FLOATDEC':([0,],[5,]),'BOOLEANDEC':([0,],[6,]),'STRINGDEC':([0,],[7,]),'PRINT':([0,],[8,]),'NAME':([0,3,5,6,7,9,11,18,22,25,26,27,28,29,30,31,32,33,34,35,36,37,40,],[4,17,19,20,21,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'-':([0,4,9,10,11,12,13,14,15,18,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[11,-30,11,26,11,-26,-27,-28,-29,11,11,26,-30,11,11,11,11,11,11,11,11,11,11,11,11,11,-24,11,26,26,-25,-11,-12,-13,-14,26,26,26,26,26,26,26,26,26,26,]),'(':([0,8,9,11,18,22,25,26,27,28,29,30,31,32,33,34,35,36,37,40,],[9,22,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'INUMBER':([0,9,11,18,22,25,26,27,28,29,30,31,32,33,34,35,36,37,40,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'FNUMBER':([0,9,11,18,22,25,26,27,28,29,30,31,32,33,34,35,36,37,40,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'BOOLEAN':([0,9,11,18,22,25,26,27,28,29,30,31,32,33,34,35,36,37,40,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'STRING':([0,9,11,18,22,25,26,27,28,29,30,31,32,33,34,35,36,37,40,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'$end':([1,16,],[0,-1,]),'SEMICOLON':([2,4,10,12,13,14,15,17,19,20,21,24,38,39,41,42,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,],[16,-30,-10,-26,-27,-28,-29,-4,-4,-4,-4,-30,-24,-2,-9,-5,-6,-7,-25,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-3,-8,]),'=':([4,17,19,20,21,],[18,40,40,40,40,]),'+':([4,10,12,13,14,15,23,24,38,41,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[-30,25,-26,-27,-28,-29,25,-30,-24,25,25,-25,-11,-12,-13,-14,25,25,25,25,25,25,25,25,25,25,]),'*':([4,10,12,13,14,15,23,24,38,41,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[-30,27,-26,-27,-28,-29,27,-30,-24,27,27,-25,27,27,-13,-14,27,27,27,27,27,27,27,27,27,27,]),'/':([4,10,12,13,14,15,23,24,38,41,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[-30,28,-26,-27,-28,-29,28,-30,-24,28,28,-25,28,28,-13,-14,28,28,28,28,28,28,28,28,28,28,]),'^':([4,10,12,13,14,15,23,24,38,41,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[-30,29,-26,-27,-28,-29,29,-30,-24,29,29,-25,-11,-12,-13,-14,29,29,29,29,29,29,29,29,29,29,]),'EQUAL':([4,10,12,13,14,15,23,24,38,41,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[-30,30,-26,-27,-28,-29,30,-30,-24,30,30,-25,-11,-12,-13,-14,30,30,30,30,30,30,30,30,30,30,]),'NOTEQUAL':([4,10,12,13,14,15,23,24,38,41,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[-30,31,-26,-27,-28,-29,31,-30,-24,31,31,-25,-11,-12,-13,-14,31,31,31,31,31,31,31,31,31,31,]),'GREATER':([4,10,12,13,14,15,23,24,38,41,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[-30,32,-26,-27,-28,-29,32,-30,-24,32,32,-25,-11,-12,-13,-14,32,32,32,32,32,32,32,32,32,32,]),'LESSTHAN':([4,10,12,13,14,15,23,24,38,41,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[-30,33,-26,-27,-28,-29,33,-30,-24,33,33,-25,-11,-12,-13,-14,33,33,33,33,33,33,33,33,33,33,]),'GREATEREQUAL':([4,10,12,13,14,15,23,24,38,41,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[-30,34,-26,-27,-28,-29,34,-30,-24,34,34,-25,-11,-12,-13,-14,34,34,34,34,34,34,34,34,34,34,]),'LESSEQUAL':([4,10,12,13,14,15,23,24,38,41,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[-30,35,-26,-27,-28,-29,35,-30,-24,35,35,-25,-11,-12,-13,-14,35,35,35,35,35,35,35,35,35,35,]),'AND':([4,10,12,13,14,15,23,24,38,41,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[-30,36,-26,-27,-28,-29,36,-30,-24,36,36,-25,-11,-12,-13,-14,36,36,36,36,36,36,36,36,36,36,]),'OR':([4,10,12,13,14,15,23,24,38,41,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[-30,37,-26,-27,-28,-29,37,-30,-24,37,37,-25,-11,-12,-13,-14,37,37,37,37,37,37,37,37,37,37,]),')':([12,13,14,15,23,24,38,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,],[-26,-27,-28,-29,46,-30,-24,61,-25,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'code':([0,],[1,]),'statement':([0,],[2,]),'expression':([0,9,11,18,22,25,26,27,28,29,30,31,32,33,34,35,36,37,40,],[10,23,38,41,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,]),'is_assing':([17,19,20,21,],[39,42,43,44,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> code","S'",1,None,None,None),
  ('code -> statement SEMICOLON','code',2,'p_code','compiler.py',104),
  ('statement -> INTDEC NAME is_assing','statement',3,'p_statement_declare_int','compiler.py',107),
  ('is_assing -> = expression','is_assing',2,'p_is_assing','compiler.py',115),
  ('is_assing -> <empty>','is_assing',0,'p_is_assing','compiler.py',116),
  ('statement -> FLOATDEC NAME is_assing','statement',3,'p_statement_declare_float','compiler.py',122),
  ('statement -> BOOLEANDEC NAME is_assing','statement',3,'p_statement_declare_boolean','compiler.py',126),
  ('statement -> STRINGDEC NAME is_assing','statement',3,'p_statement_declare_string','compiler.py',130),
  ('statement -> PRINT ( expression )','statement',4,'p_statement_print','compiler.py',134),
  ('statement -> NAME = expression','statement',3,'p_statement_assign','compiler.py',138),
  ('statement -> expression','statement',1,'p_statement_expr','compiler.py',144),
  ('expression -> expression + expression','expression',3,'p_expression_binop','compiler.py',148),
  ('expression -> expression - expression','expression',3,'p_expression_binop','compiler.py',149),
  ('expression -> expression * expression','expression',3,'p_expression_binop','compiler.py',150),
  ('expression -> expression / expression','expression',3,'p_expression_binop','compiler.py',151),
  ('expression -> expression ^ expression','expression',3,'p_expression_binop','compiler.py',152),
  ('expression -> expression EQUAL expression','expression',3,'p_expression_compare','compiler.py',166),
  ('expression -> expression NOTEQUAL expression','expression',3,'p_expression_compare','compiler.py',167),
  ('expression -> expression GREATER expression','expression',3,'p_expression_compare','compiler.py',168),
  ('expression -> expression LESSTHAN expression','expression',3,'p_expression_compare','compiler.py',169),
  ('expression -> expression GREATEREQUAL expression','expression',3,'p_expression_compare','compiler.py',170),
  ('expression -> expression LESSEQUAL expression','expression',3,'p_expression_compare','compiler.py',171),
  ('expression -> expression AND expression','expression',3,'p_expression_boleanas','compiler.py',190),
  ('expression -> expression OR expression','expression',3,'p_expression_boleanas','compiler.py',191),
  ('expression -> - expression','expression',2,'p_expression_uminus','compiler.py',203),
  ('expression -> ( expression )','expression',3,'p_expression_group','compiler.py',208),
  ('expression -> INUMBER','expression',1,'p_expression_inumber','compiler.py',213),
  ('expression -> FNUMBER','expression',1,'p_expression_fnumber','compiler.py',218),
  ('expression -> BOOLEAN','expression',1,'p_expression_boolean','compiler.py',223),
  ('expression -> STRING','expression',1,'p_expression_string','compiler.py',228),
  ('expression -> NAME','expression',1,'p_expression_name','compiler.py',235),
]
