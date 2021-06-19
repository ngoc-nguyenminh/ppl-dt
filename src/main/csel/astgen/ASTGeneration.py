from CSELVisitor import CSELVisitor
from CSELParser import CSELParser
from AST import *

# from target.CSELVisitor import CSELVisitor
# from target.CSELParser import CSELParser
# from src.main.csel.utils.AST import *
from functools import *

def flatten(lst):
    return reduce(lambda lit, ele: lit + [ele], lst, [])

class ASTGeneration(CSELVisitor):
    # Visit a parse tree produced by CSELParser#program.
    def visitProgram(self, ctx: CSELParser.ProgramContext):
        Decls = []
        for i in ctx.decls():
            decl = self.visitDecls(i)
            if isinstance(decl, list):
                Decls.extend(decl if decl else [])
            else:
                Decls.append(decl)
        return Program(Decls)

    # Visit a parse tree produced by CSELParser#decls.
    def visitDecls(self, ctx: CSELParser.DeclsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CSELParser#funcdecl.
    def visitFuncdecl(self, ctx: CSELParser.FuncdeclContext):
        name = ctx.ID().getText()
        paramList = self.visitParamlist(ctx.paramlist()) if ctx.paramlist() else []
        body = self.visitBody(ctx.body())
        return FuncDecl(Id(name), paramList, body)

    # Visit a parse tree produced by CSELParser#paramlist.
    def visitParamlist(self, ctx: CSELParser.ParamlistContext):
        return [self.visitParam(x) for x in ctx.param()]

    # Visit a parse tree produced by CSELParser#param.
    def visitParam(self, ctx: CSELParser.ParamContext):
        if ctx.dimension():
            return VarDecl(Id(ctx.ID().getText()), self.visitDimension(ctx.dimension()), NoneType(),None)
        return VarDecl(Id(ctx.ID().getText()), [], NoneType(), None)

    # Visit a parse tree produced by CSELParser#body.
    def visitBody(self, ctx: CSELParser.BodyContext):
        return self.visitStm_list(ctx.stm_list())

    # Visit a parse tree produced by CSELParser#mytype.
    def visitMytype(self, ctx: CSELParser.MytypeContext):
        if ctx.INTLIT():
            return NumberLiteral(float(ctx.INTLIT().getText()))
        if ctx.FLOATLIT():
            return NumberLiteral(float(ctx.FLOATLIT().getText()))
        if ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT())
        if ctx.STRINGLIT():
            # print(ctx.STRINGLIT().getText())
            return StringLiteral(ctx.STRINGLIT().getText())
        if ctx.array():
            return self.visitArray(ctx.array())
        if ctx.json():
            return self.visitJson(ctx.array())

    # Visit a parse tree produced by CSELParser#typname.
    def visitTypname(self, ctx: CSELParser.TypnameContext):
        if ctx.NUMBER():
            return NumberType()
        if ctx.BOOLEAN():
            return BooleanType()
        if ctx.STRING():
            return StringType()
        if ctx.ARRAY():
            return ArrayType()
        if ctx.JSON():
            return JSONType()

    # Visit a parse tree produced by CSELParser#array.
    def visitArray(self, ctx: CSELParser.ArrayContext):
        ret = []
        for i in ctx.mytype():
            val = self.visitMytype(i)
            if isinstance(val, list):
                ret.extend(val if val else [])
            else:
                ret.append(val)
        return ArrayLiteral(ret)

    # Visit a parse tree produced by CSELParser#json.
    def visitJson(self, ctx: CSELParser.JsonContext):
        ret = []
        for i in ctx.keyval():
            val = self.visitKeyval(i)
            if isinstance(val, list):
                ret.extend(val if val else [])
            else:
                ret.append(val)
        return JSONLiteral(ret)

    # Visit a parse tree produced by CSELParser#keyval.
    def visitKeyval(self, ctx: CSELParser.KeyvalContext):
        val = self.visitMytype(ctx.mytype())
        return Id(ctx.ID().getText()), val

    # Visit a parse tree produced by CSELParser#expression.
    def visitExpression(self, ctx: CSELParser.ExpressionContext):
        if ctx.getChildCount() > 1:
            left = self.visitExp1(ctx.exp0(0))
            op = ctx.getChild(1).getText()
            right = self.visitExp0(ctx.exp0(1))
            return BinaryOp(op, left, right)
        return self.visitExp0(ctx.exp0(0))

    # Visit a parse tree produced by CSELParser#exp0.
    def visitExp0(self, ctx: CSELParser.Exp0Context):
        if ctx.getChildCount() > 1:
            left = self.visitExp1(ctx.exp1(0))
            op = ctx.getChild(1).getText()
            right = self.visitExp1(ctx.exp1(1))
            return BinaryOp(op, left, right)
        return self.visitExp1(ctx.exp1(0))

    # Visit a parse tree produced by CSELParser#exp1.
    def visitExp1(self, ctx: CSELParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visitExp2(ctx.exp2())
        left = self.visitExp1(ctx.exp1())
        op = ctx.getChild(1).getText()
        right = self.visitExp2(ctx.exp2())
        return BinaryOp(op, left, right)

    # Visit a parse tree produced by CSELParser#exp2.
    def visitExp2(self, ctx: CSELParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visitExp3(ctx.exp3())
        left = self.visitExp2(ctx.exp2())
        op = ctx.getChild(1).getText()
        right = self.visitExp3(ctx.exp3())
        return BinaryOp(op, left, right)

    # Visit a parse tree produced by CSELParser#exp3.
    def visitExp3(self, ctx: CSELParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visitExp4(ctx.exp4())
        left = self.visitExp3(ctx.exp3())
        op = ctx.getChild(1).getText()
        right = self.visitExp4(ctx.exp4())
        return BinaryOp(op, left, right)

    # Visit a parse tree produced by CSELParser#exp4.
    def visitExp4(self, ctx: CSELParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visitExp5(ctx.exp5())
        op = ctx.getChild(0).getText()
        body = self.visitExp4(ctx.exp4())
        return UnaryOp(op, body)

    # Visit a parse tree produced by CSELParser#exp5.
    def visitExp5(self, ctx: CSELParser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visitExp6(ctx.exp6())
        op = ctx.getChild(0).getText()
        body = self.visitExp5(ctx.exp5())
        return UnaryOp(op, body)

    # Visit a parse tree produced by CSELParser#exp6.
    def visitExp6(self, ctx: CSELParser.Exp6Context):
        if ctx.getChildCount() == 1:
            return self.visitOperand(ctx.operand())
        arr = self.visitExp6(ctx.exp6())
        if ctx.post_flix_array_exp():
            if isinstance(arr, ArrayAccess):
                arr.idx.append(*self.visitPost_flix_array_exp(ctx.post_flix_array_exp()))
                return arr
            return ArrayAccess(arr, self.visitPost_flix_array_exp(ctx.post_flix_array_exp()))
        if isinstance(arr, JSONAccess):
            arr.idx.append(*self.visitPost_flix_json_exp(ctx.post_flix_json_exp()))
            return arr
        return JSONAccess(arr, self.visitPost_flix_json_exp(ctx.post_flix_json_exp()))

    # Visit a parse tree produced by CSELParser#operand.
    def visitOperand(self, ctx: CSELParser.OperandContext):
        if ctx.getChildCount() == 1:
            if ctx.ID():
                return Id(ctx.ID().getText())
            if ctx.CONSTID():
                return Id(ctx.CONSTID().getText())
            if ctx.mytype():
                return self.visitMytype(ctx.mytype())
            return self.visitCall(ctx.call())
        return self.visitExpression(ctx.expression())

    # Visit a parse tree produced by CSELParser#index_exp.
    def visitIndex_exp(self, ctx: CSELParser.Index_expContext):
        return self.visitExpression(ctx.expression())
        # exp = self.visitExpression(ctx.expression())
        # if isinstance(exp, ArrayAccess):
        #     exp.idx.append(*self.visitPost_flix_array_exp(ctx.post_flix_array_exp()))
        #     return exp
        # return ArrayAccess(exp, self.visitPost_flix_array_exp(ctx.post_flix_array_exp()))

    # Visit a parse tree produced by CSELParser#json_exp.
    def visitJson_exp(self, ctx: CSELParser.Json_expContext):
        return self.visitExpression(ctx.expression())

    # Visit a parse tree produced by CSELParser#post_flix_array_exp.
    def visitPost_flix_array_exp(self, ctx: CSELParser.Post_flix_array_expContext):
        Exp = []
        for i in ctx.expression():
            exp = self.visitExpression(i)
            if isinstance(exp, list):
                Exp.extend(exp if exp else [])
            else:
                Exp.append(exp)
        return Exp

    # Visit a parse tree produced by CSELParser#post_flix_json_exp.
    def visitPost_flix_json_exp(self, ctx: CSELParser.Post_flix_json_expContext):
        Key = []
        if ctx.STRINGLIT():
            Key.append(StringLiteral(ctx.STRINGLIT().getText()))
        return Key
    # Visit a parse tree produced by CSELParser#statement.
    def visitStatement(self, ctx: CSELParser.StatementContext):
        if ctx.brk():
            return Break()
        elif ctx.cont():
            return Continue()
        else:
            return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by CSELParser#stm_list.
    def visitStm_list(self, ctx: CSELParser.Stm_listContext):
        ret = []
        for i in range(0, ctx.getChildCount()):
            ins = self.visit(ctx.getChild(i))
            if isinstance(ins, list):
                ret.append(ins if ins else [])
            else:
                ret.append(ins)
        return flatten(ret)

    # Visit a parse tree produced by CSELParser#constdecl.
    def visitConstdecl(self, ctx: CSELParser.ConstdeclContext):
        Decl = []
        for i in ctx.constmodule():
            decl = self.visitConstmodule(i)
            if isinstance(decl, list):
                Decl.extend(decl if decl else [])
            else:
                Decl.append(decl)
        return Decl

    # Visit a parse tree produced by CSELParser#constmodule.
    def visitConstmodule(self, ctx: CSELParser.ConstmoduleContext):
        id = Id(ctx.CONSTID().getText())
        Dim = self.visitDimension(ctx.dimension()) if ctx.dimension() else []
        typ = self.visitTypname(ctx.typname()) if ctx.typname() else NoneType()
        initVal = self.visitExpression(ctx.expression())
        return ConstDecl(id, Dim, typ, initVal)

    # Visit a parse tree produced by CSELParser#vardecl.
    def visitVardecl(self, ctx: CSELParser.VardeclContext):
        Decl = []
        for i in ctx.varmodule():
            decl = self.visitVarmodule(i)
            if isinstance(decl, list):
                Decl.extend(decl if decl else [])
            else:
                Decl.append(decl)
        return Decl

    # Visit a parse tree produced by CSELParser#varmodule.
    def visitVarmodule(self, ctx: CSELParser.VarmoduleContext):
        id = Id(ctx.ID().getText())
        Dim = self.visitDimension(ctx.dimension()) if ctx.dimension() else []
        typ = self.visitTypname(ctx.typname()) if ctx.typname() else NoneType()
        initVal = self.visitExpression(ctx.expression()) if ctx.expression() else None
        return VarDecl(id, Dim, typ, initVal)

    # Visit a parse tree produced by CSELParser#dimension.
    def visitDimension(self, ctx: CSELParser.DimensionContext):
        ret = []
        for i in ctx.INTLIT():
            ret.append(NumberLiteral(float(i.getText())))
        return ret

    # Visit a parse tree produced by CSELParser#assign.
    def visitAssign(self, ctx: CSELParser.AssignContext):
        return Assign(self.visitLhs(ctx.lhs()), self.visitExpression(ctx.expression()))

    # Visit a parse tree produced by CSELParser#lhs.
    def visitLhs(self, ctx: CSELParser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.index_exp():
            return self.visitIndex_exp(ctx.index_exp())
        if ctx.json_exp():
            return self.visitJson_exp(ctx.json_exp())

    # Visit a parse tree produced by CSELParser#call.
    def visitCall(self, ctx: CSELParser.CallContext):
        id = ctx.ID().getText()
        expList = []
        if ctx.exp_list():
            expList = self.visitExp_list(ctx.exp_list())
        return CallExpr(Id(id), expList)

    # Visit a parse tree produced by CSELParser#callstm.
    def visitCallstm(self, ctx: CSELParser.CallstmContext):
        id = ctx.ID().getText()
        expList = []
        if ctx.exp_list():
            expList = self.visitExp_list(ctx.exp_list())
        return CallStmt(Id(id), expList)

    # Visit a parse tree produced by CSELParser#exp_list.
    def visitExp_list(self, ctx: CSELParser.Exp_listContext):
        expList = []
        for i in ctx.expression():
            exp = self.visitExpression(i)
            if isinstance(exp, list):
                expList.extend(exp if exp else [])
            else:
                expList.append(exp)
        return expList

    # Visit a parse tree produced by CSELParser#ret.
    def visitRet(self, ctx: CSELParser.RetContext):
        return Return(self.visitExpression(ctx.expression())) if ctx.expression() else Return(None)

    # Visit a parse tree produced by CSELParser#ifstm.
    def visitIfstm(self, ctx: CSELParser.IfstmContext):
        ifThenStm = []
        ifThenStm.append(self.visitIf_module(ctx.if_module()))

        if ctx.elif_module():
            for i in ctx.elif_module():
                ifstm = self.visitElif_module(i)
                if isinstance(ifstm, list):
                    ifThenStm.extend(ifstm if ifstm else [])
                else:
                    ifThenStm.append(ifstm)

        elseStm = self.visitElse_module(ctx.else_module()) if ctx.else_module() else ([], [])

        return If(ifThenStm, elseStm)

    # Visit a parse tree produced by CSELParser#if_module.
    def visitIf_module(self, ctx: CSELParser.If_moduleContext):
        exp = self.visitExpression(ctx.expression())
        stm = self.visitStm_list(ctx.stm_list())
        return exp, stm[0], stm[1]

    # Visit a parse tree produced by CSELParser#elif_module.
    def visitElif_module(self, ctx: CSELParser.Elif_moduleContext):
        exp = self.visitExpression(ctx.expression())
        stm = self.visitStm_list(ctx.stm_list())
        return exp, stm[0], stm[1]

    # Visit a parse tree produced by CSELParser#else_module.
    def visitElse_module(self, ctx: CSELParser.Else_moduleContext):
        return self.visitStm_list(ctx.stm_list())

    # Visit a parse tree produced by CSELParser#forinstm.
    def visitForinstm(self, ctx: CSELParser.ForinstmContext):
        id = Id(ctx.ID().getText())
        exp = self.visitExpression(ctx.expression())
        stm = self.visitStm_list(ctx.stm_list())
        return ForIn(id, exp, stm)

    # Visit a parse tree produced by CSELParser#foronstm.
    def visitForonstm(self, ctx: CSELParser.ForonstmContext):
        id = Id(ctx.ID().getText())
        exp = self.visitExpression(ctx.expression())
        stm = self.visitStm_list(ctx.stm_list())
        return ForIn(id, exp, stm)

    # Visit a parse tree produced by CSELParser#whilestm.
    def visitWhilestm(self, ctx: CSELParser.WhilestmContext):
        exp = self.visitExpression(ctx.expression())
        stm = self.visitStm_list(ctx.stm_list())
        return While(exp, stm)

    # Visit a parse tree produced by CSELParser#brk.
    def visitBrk(self, ctx: CSELParser.BrkContext):
        return Break()

    # Visit a parse tree produced by CSELParser#cont.
    def visitCont(self, ctx: CSELParser.ContContext):
        return Continue()
