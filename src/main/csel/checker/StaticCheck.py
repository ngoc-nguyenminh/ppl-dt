from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import *
from Visitor import *
from StaticError import *
from functools import *


class Type(ABC):
    __metaclass__ = ABCMeta
    pass


class Prim(Type):
    __metaclass__ = ABCMeta
    pass


class NumberType(Prim):
    pass


class StringType(Prim):
    pass


class BoolType(Prim):
    pass


class VoidType(Type):
    pass


class Unknown(Type):
    pass


@dataclass
class ArrayType(Type):
    dimen: List[int]
    eletype: Type


@dataclass
class MType:
    intype: List[Type]
    restype: Type


@dataclass
class Symbol:
    name: str
    mtype: Type

    def getType(self):
        return (
            self.mtype.restype if type(self.mtype) == MType
            else self.mtype.eletype if type(self.mtype) == ArrayType
            else self.mtype
        )

    def getClassType(self):
        return type(self.getType())

    def setType(self, typ):
        if type(self.mtype) == ArrayType:
            self.mtype.eletype = typ
        elif type(self.mtype) == MType:
            self.mtype.restype = typ
        else:
            self.mtype = typ

    def compare(self, other, ast, err):
        if [self.getClassType(), other.getClassType()] == [Unknown, Unknown]:
            raise TypeCannotBeInferred(ast)
        if [type(self.mtype), type(other.mtype)] == [ArrayType, ArrayType]:
            if self.mtype.dimen != other.mtype.dimen:
                raise err(ast)
        if self.getClassType() == Unknown:
            self.setType(other.getType())
        if other.getClassType() == Unknown:
            other.setType(self.getType())
        if ArrayType in [type(self.mtype), type(other.mtype)]:
            raise err(ast)
        if self.getClassType() != other.getClassType():
            raise err(ast)

    @staticmethod
    def getName(symbol):
        return str(symbol.name)

class ExpUtil:
    @staticmethod
    def checkMismatchExp(ast, lst, typ:Type, ret:Type):
        for item in lst:
            if item.getClassType() not in [type(typ), Unknown]:
                raise TypeMismatchInExpression(ast)
            item.setType(typ)
        return Symbol("", ret)


class StaticChecker(BaseVisitor):
    def __init__(self, ast):
        self.ast = ast
        self.global_envi = [
            Symbol("read", MType([], StringType())),
            Symbol("print", MType([StringType()], VoidType())),
            Symbol("printSLn", MType([StringType()], VoidType()))]

    def check(self):
        return self.visit(self.ast, self.global_envi)

    def visitProgram(self, ast, c):
        [self.visit(x, c) for x in ast.decl]

    def visitVarDecl(self, ast, param):
        return None

    def visitConstDecl(self, ast, param):
        return None

    def visitFuncDecl(self, ast, param):
        return None

    def visitBinaryOp(self, ast, param):
        return None

    def visitUnaryOp(self, ast, param):
        return None

    def visitCallExpr(self, ast, param):
        return None

    def visitId(self, ast, param):
        return None

    def visitArrayAccess(self, ast, param):
        return None

    def visitJSONAccess(self, ast, param):
        return None

    def visitAssign(self, ast, param):
        return None

    def visitIf(self, ast, param):
        return None

    def visitFor(self, ast, param):
        return None

    def visitContinue(self, ast, param):
        return None

    def visitBreak(self, ast, param):
        return None

    def visitReturn(self, ast, param):
        return None

    def visitDowhile(self, ast, param):
        return None

    def visitWhile(self, ast, param):
        return None

    def visitCallStmt(self, ast, param):
        return None

    def visitNumberLiteral(self, ast, param):
        return None

    def visitBooleanLiteral(self, ast, param):
        return None

    def visitStringLiteral(self, ast, param):
        return None

    def visitArrayLiteral(self, ast, param):
        return None

    def visitJSONLiteral(self, ast, param):
        return None
