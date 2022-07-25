import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test1(self):
        """Test variable declaration"""
        input = """Var: x;"""
        expect = str(Program([VarDecl(Id("x"),[],None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test2(self):
        """Test variable declaration"""
        input = """Var: x = 1;"""
        expect = str(Program([VarDecl(Id("x"),[],IntLiteral(1))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test3(self):
        """Test variable declaration"""
        input = """Var: arr[10];"""
        expect = str(Program([VarDecl(Id("arr"),[10],None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test4(self):
        """Test variable declaration"""
        input = """Var: arr[3] = {1, 2, 3};"""
        expect = str(Program([VarDecl(Id("arr"),[3],ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test5(self):
        """Test variable declaration"""
        input = """Var: arr[2][3] = {{1, 2, 3}, {4, 5, 6}};"""
        expect = str(Program([VarDecl(Id("arr"),[2, 3],ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2),
                    IntLiteral(3)]), ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test6(self):
        """Test variable declaration"""
        input = """Var: x, arr[10];"""
        expect = str(Program([VarDecl(Id("x"),[],None),VarDecl(Id("arr"),[10],None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test7(self):
        """Test variable declaration"""
        input = """Var: x, y = 1;"""
        expect = str(Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],IntLiteral(1))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test8(self):
        """Test variable declaration"""
        input = """Var: x = 1.0, y = 1, z = 1e-10;"""
        expect = str(Program([VarDecl(Id("x"),[],FloatLiteral(1.0)),VarDecl(Id("y"),[],IntLiteral(1)),VarDecl(Id("z"),[],FloatLiteral(1e-10))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test9(self):
        """Test variable declaration"""
        input = """Var: x = "hello", y = True, z = False;"""
        expect = str(Program([VarDecl(Id("x"),[],StringLiteral("hello")),VarDecl(Id("y"),[],BooleanLiteral(True)),VarDecl(Id("z"),[],BooleanLiteral(False))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test10(self):
        """Test variable declaration"""
        input = """Var: arr1[2] = {1, 2}, arr2[2][3] = {{1, 2, 3}, {4, 5, 6}};"""
        expect = str(Program([VarDecl(Id("arr1"),[2],ArrayLiteral([IntLiteral(1), IntLiteral(2)])),VarDecl(Id("arr2"),[2, 3],
                ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]), ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test11(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4, y;
                y = x + 6;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(4)),VarDecl(Id("y"),[],None)],
                [Assign(Id("y"),BinaryOp("+",Id("x"),IntLiteral(6)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test12(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4, y = 5, z = 6, t;
                t = x + y + z;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(4)),VarDecl(Id("y"),[],IntLiteral(5)),
                VarDecl(Id("z"),[],IntLiteral(6)), VarDecl(Id("t"),[],None)],
                [Assign(Id("t"),BinaryOp("+",BinaryOp("+",Id("x"),Id("y")),Id("z")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    # def test12(self):
    #     """Test function declaration"""
    #     input = """
    #     Function: main
    #         Body:
    #             Var: x;
    #             x = 10;
    #             print(x);
    #         EndBody.
    #     """
    #     expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],[Assign(Id("x"),IntLiteral(10)),CallStmt(Id("print"),[Id("x")])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,312))
    #
    # def test13(self):
    #     """Test function declaration"""
    #     input = """
    #     Function: add_one
    #         Parameter: n
    #         Body:
    #             Return n + 1;
    #         EndBody.
    #     Function: main
    #         Body:
    #             Var: x;
    #             x = 10;
    #             print(x);
    #         EndBody.
    #     """
    #     expect = str(Program([FuncDecl(Id("add_one"),[VarDecl(Id("n"),[],None)],([],[Return(BinaryOp("+",Id("n"),
    #             IntLiteral(1)))])),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],
    #             [Assign(Id("x"),IntLiteral(10)),CallStmt(Id("print"),[Id("x")])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,313))