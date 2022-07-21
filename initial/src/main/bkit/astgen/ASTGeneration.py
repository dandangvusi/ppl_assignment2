from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
    # program: glob_var_decl_part func_decl_part EOF;
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        return Program([VarDecl(Id(ctx.ID().getText()),[],None)])

    # glob_var_decl_part: var_decl_list?;
    def visitGlob_var_decl_part(self, ctx:BKITParser.Glob_var_decl_partContext):
        pass

    # var_decl_list: var_decl var_decl_list | var_decl;
    def visitVar_decl_list(self, ctx:BKITParser.Var_decl_listContext):
        pass

    # var_decl: VAR COLON var_list SEMI;
    def visitVar_decl(self, ctx:BKITParser.Var_declContext):
        pass

    # var_list: var COMMA var_list | var;
    def visitVar_list(self, ctx:BKITParser.Var_listContext):
        pass

    # var: scalar_var | compo_var;
    def visitVar(self, ctx:BKITParser.VarContext):
        pass

    # scalar_var: ID (ASSIGN literal)?;
    def visitScalar_var(self, ctx:BKITParser.Scalar_varContext):
        pass

    # compo_var: ID dimensions (ASSIGN array_lit)?;
    def visitCompo_var(self, ctx:BKITParser.Compo_varContext):
        pass

    # func_decl_part: func_decl_list?;
    def visitFunc_decl_part(self, ctx:BKITParser.Func_decl_partContext):
        pass

    # func_decl_list: func_decl func_decl_list | func_decl;
    def visitFunc_decl_list(self, ctx:BKITParser.Func_decl_listContext):
        pass

    # func_decl: FUNCTION COLON ID func_param? func_body;
    def visitFunc_decl(self, ctx:BKITParser.Func_declContext):
        pass

    # func_param: PARAMETER COLON param_list;
    def visitFunc_param(self, ctx:BKITParser.Func_paramContext):
        pass

    # param_list: param COMMA param_list | param;
    def visitParam_list(self, ctx:BKITParser.Param_listContext):
        pass

    # param: ID | ID dimensions;
    def visitParam(self, ctx:BKITParser.ParamContext):
        pass

    # func_body: BODY COLON stmt_list ENDBODY DOT;
    def visitFunc_body(self, ctx:BKITParser.Func_bodyContext):
        pass

    # stmt_list: var_decl_stmt_list? other_stmt_list?;
    def visitStmt_list(self, ctx:BKITParser.Stmt_listContext):
        var_decls = self.visit(ctx.var_decl_stmt_list())
        stmts = self.visit(ctx.other_stmt_list())
        return var_decls, stmts

    # var_decl_stmt_list: var_decl_stmt var_decl_stmt_list | var_decl_stmt;
    def visitVar_decl_stmt_list(self, ctx:BKITParser.Var_decl_stmt_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.var_decl_stmt())]
        else:
            return [self.visit(ctx.var_decl_stmt())] + self.visit(ctx.var_decl_stmt_list())

    # other_stmt_list: other_stmt other_stmt_list | other_stmt;
    def visitOther_stmt_list(self, ctx:BKITParser.Other_stmt_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.other_stmt())]
        else:
            return [self.visit(ctx.other_stmt())] + [self.visit(ctx.other_stmt_list())]

    # other_stmt: assign_stmt | if_stmt | for_stmt | while_stmt | do_while_stmt | break_stmt | continue_stmt | call_stmt | return_stmt;
    def visitOther_stmt(self, ctx:BKITParser.Other_stmtContext):
        pass

    # var_decl_stmt: VAR COLON var_list SEMI;
    def visitVar_decl_stmt(self, ctx: BKITParser.Var_decl_stmtContext):
        pass

    # assign_stmt: (ID | index_exp) ASSIGN exp SEMI;
    def visitAssign_stmt(self, ctx: BKITParser.Assign_stmtContext):
        rhs = self.visit(ctx.exp())
        if ctx.ID():
            lhs = Id(ctx.ID().getText())
            return Assign(lhs, rhs)
        else:
            lhs = self.visit(ctx.index_exp())
            return Assign(lhs, rhs)

    # if_stmt: IF exp THEN stmt_list else_if_list? (ELSE stmt_list)? ENDIF DOT;
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        pass

    # else_if_list: else_if else_if_list | else_if;
    def visitElse_if_list(self, ctx:BKITParser.Else_if_listContext):
        pass

    # else_if: ELSEIF exp THEN stmt_list;
    def visitElse_if(self, ctx:BKITParser.Else_ifContext):
        pass

    # for_stmt: FOR LB ID ASSIGN exp COMMA exp COMMA exp RB DO stmt_list ENDFOR DOT;
    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        idx1 = Id(ctx.ID().getText())
        expr1 = self.visit(ctx.exp(0))
        expr2 = self.visit(ctx.exp(1))
        expr3 = self.visit(ctx.exp(2))
        var_decls, stmts = self.visit(ctx.stmt_list())
        loop = (var_decls, stmts)
        return For(idx1, expr1, expr2, expr3, loop)

    # while_stmt: WHILE exp DO stmt_list ENDWHILE DOT;
    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        exp = self.visit(ctx.exp())
        var_decls, stmts = self.visit(ctx.stmt_list())
        sl = (var_decls, stmts)
        return While(exp, sl)

    # do_while_stmt: DO stmt_list WHILE exp ENDDO DOT;
    def visitDo_while_stmt(self, ctx:BKITParser.Do_while_stmtContext):
        exp = self.visit(ctx.exp())
        var_decls, stmts = self.visit(ctx.stmt_list())
        sl = (var_decls, stmts)
        return Dowhile(sl, exp)

    # break_stmt: BREAK SEMI;
    def visitBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        return Break()

    # continue_stmt: CONTINUE SEMI;
    def visitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        return Continue()

    # call_stmt: ID LB exp_list? RB SEMI;
    def visitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        if ctx.getChildCount()==5:
            method = Id(ctx.ID().getText())
            param = self.visit(ctx.exp_list())
            return CallStmt(method, param)
        else:
            method = Id(ctx.ID().getText())
            param = []
            return CallStmt(method, param)


    # return_stmt: RETURN exp? SEMI;
    def visitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        if ctx.exp():
            expr = self.visit(ctx.exp)
            return Return(expr)
        return Return(None)

    # exp: exp1 (EQ_I | NEQ_I | LT_I | GT_I | LTE_I | GTE_I | NEQ_F | LT_F | GT_F | LTE_F | GTE_F) exp1 | exp1;
    def visitExp(self, ctx:BKITParser.ExpContext):
        pass

    # exp1: exp1 (AND | OR) exp2 | exp2;
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        pass

    # exp2: exp2 (ADD_I | ADD_F | SUB_I | SUB_F) exp3 | exp3;
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        pass

    # exp3: exp3 (MUL_I | MUL_F | DIV_I | DIV_F | MOD_I) exp4 | exp4;
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        pass

    # exp4: NOT exp4 | exp5;
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        pass

    # exp5: (SUB_I | SUB_F) exp5 | index_exp | func_call_exp;
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        pass

    # index_exp: (ID|func_call) index_operator;
    def visitIndex_exp(self, ctx:BKITParser.Index_expContext):
        pass

    # index_operator: LS exp RS | LS exp RS index_operator;
    def visitIndex_operator(self, ctx:BKITParser.Index_operatorContext):
        pass

    # func_call_exp: func_call | operand;
    def visitFunc_call_exp(self, ctx:BKITParser.Func_call_expContext):
        pass

    # operand: literal | ID | LB exp RB;
    def visitOperand(self, ctx:BKITParser.OperandContext):
        pass

    # func_call: ID LB exp_list? RB;
    def visitFunc_call(self, ctx:BKITParser.Func_callContext):
        pass

    # exp_list: exp COMMA exp_list | exp;
    def visitExp_list(self, ctx:BKITParser.Exp_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.exp())]
        else:
            return [self.visit(ctx.exp())] + self.visit(ctx.exp_list())

    # literal: DEC_INT_LIT | HEX_INT_LIT | OCT_INT_LIT | FLT_LIT | BOOL_LIT | STR_LIT | array_lit;
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        if ctx.DEC_INT_LIT():
            return IntLiteral(int(ctx.DEC_INT_LIT().getText(), base = 10))
        elif ctx.HEX_INT_LIT():
            return IntLiteral(int(ctx.HEX_INT_LIT().getText(), base = 16))
        elif ctx.OCT_INT_LIT():
            return IntLiteral(int(ctx.OCT_INT_LIT().getText(), base = 8))
        elif ctx.FLT_LIT():
            return FloatLiteral(float(ctx.FLT_LIT().getText()))
        elif ctx.BOOL_LIT():
            return BooleanLiteral(ctx.BOOL_LIT().getText() == "True")
        elif ctx.STR_LIT():
            return StringLiteral(ctx.STR_LIT().getText())
        else:
            return self.visit(ctx.array_lit())

    # dimensions: dimension dimensions | dimension;
    def visitDimensions(self, ctx:BKITParser.DimensionsContext):
        pass

    # dimension: LS (DEC_INT_LIT | HEX_INT_LIT | OCT_INT_LIT) RS;
    def visitDimension(self, ctx:BKITParser.DimensionContext):
        pass

    # array_lit: LC array_element_list RC;
    def visitArray_lit(self, ctx:BKITParser.Array_litContext):
        value = self.visit(ctx.array_element_list())
        return ArrayLiteral(value)

    # array_element_list: array_element COMMA array_element_list | array_element;
    def visitArray_element_list(self, ctx:BKITParser.Array_element_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.array_element())]
        else:
            return [self.visit(ctx.array_element())] + self.visit(ctx.array_element_list())

    # array_element: literal;
    def visitArray_element(self, ctx:BKITParser.Array_elementContext):
        return self.visit(ctx.literal())