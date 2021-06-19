# Generated from main/csel/parser/CSEL.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CSELParser import CSELParser
else:
    from CSELParser import CSELParser

# This class defines a complete generic visitor for a parse tree produced by CSELParser.

class CSELVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSELParser#program.
    def visitProgram(self, ctx:CSELParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#decls.
    def visitDecls(self, ctx:CSELParser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#funcdecl.
    def visitFuncdecl(self, ctx:CSELParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#paramlist.
    def visitParamlist(self, ctx:CSELParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#param.
    def visitParam(self, ctx:CSELParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#body.
    def visitBody(self, ctx:CSELParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#mytype.
    def visitMytype(self, ctx:CSELParser.MytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#typname.
    def visitTypname(self, ctx:CSELParser.TypnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#array.
    def visitArray(self, ctx:CSELParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#json.
    def visitJson(self, ctx:CSELParser.JsonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#keyval.
    def visitKeyval(self, ctx:CSELParser.KeyvalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#expression.
    def visitExpression(self, ctx:CSELParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp0.
    def visitExp0(self, ctx:CSELParser.Exp0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp1.
    def visitExp1(self, ctx:CSELParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp2.
    def visitExp2(self, ctx:CSELParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp3.
    def visitExp3(self, ctx:CSELParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp4.
    def visitExp4(self, ctx:CSELParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp5.
    def visitExp5(self, ctx:CSELParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp6.
    def visitExp6(self, ctx:CSELParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#operand.
    def visitOperand(self, ctx:CSELParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#index_exp.
    def visitIndex_exp(self, ctx:CSELParser.Index_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#json_exp.
    def visitJson_exp(self, ctx:CSELParser.Json_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#post_flix_array_exp.
    def visitPost_flix_array_exp(self, ctx:CSELParser.Post_flix_array_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#post_flix_json_exp.
    def visitPost_flix_json_exp(self, ctx:CSELParser.Post_flix_json_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#statement.
    def visitStatement(self, ctx:CSELParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#stm_list.
    def visitStm_list(self, ctx:CSELParser.Stm_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#constdecl.
    def visitConstdecl(self, ctx:CSELParser.ConstdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#constmodule.
    def visitConstmodule(self, ctx:CSELParser.ConstmoduleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#vardecl.
    def visitVardecl(self, ctx:CSELParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#varmodule.
    def visitVarmodule(self, ctx:CSELParser.VarmoduleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#dimension.
    def visitDimension(self, ctx:CSELParser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#assign.
    def visitAssign(self, ctx:CSELParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#lhs.
    def visitLhs(self, ctx:CSELParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#call.
    def visitCall(self, ctx:CSELParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#callstm.
    def visitCallstm(self, ctx:CSELParser.CallstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp_list.
    def visitExp_list(self, ctx:CSELParser.Exp_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#ret.
    def visitRet(self, ctx:CSELParser.RetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#ifstm.
    def visitIfstm(self, ctx:CSELParser.IfstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#if_module.
    def visitIf_module(self, ctx:CSELParser.If_moduleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#elif_module.
    def visitElif_module(self, ctx:CSELParser.Elif_moduleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#else_module.
    def visitElse_module(self, ctx:CSELParser.Else_moduleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#forinstm.
    def visitForinstm(self, ctx:CSELParser.ForinstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#foronstm.
    def visitForonstm(self, ctx:CSELParser.ForonstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#whilestm.
    def visitWhilestm(self, ctx:CSELParser.WhilestmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#brk.
    def visitBrk(self, ctx:CSELParser.BrkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#cont.
    def visitCont(self, ctx:CSELParser.ContContext):
        return self.visitChildren(ctx)



del CSELParser