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

    def test13(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4, y = 5, z = 6, t;
                t = x + y + z + 5;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(4)),VarDecl(Id("y"),[],IntLiteral(5)),
                VarDecl(Id("z"),[],IntLiteral(6)), VarDecl(Id("t"),[],None)],
                [Assign(Id("t"),BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("x"),Id("y")),Id("z")),IntLiteral(5)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test14(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4, y = 5, z = 6, t;
                t = x + y - z;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(4)),VarDecl(Id("y"),[],IntLiteral(5)),
                VarDecl(Id("z"),[],IntLiteral(6)), VarDecl(Id("t"),[],None)],
                [Assign(Id("t"),BinaryOp("-",BinaryOp("+",Id("x"),Id("y")),Id("z")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test15(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4, y = 5, z = 6, t;
                t = x - y + z - 5;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(4)),VarDecl(Id("y"),[],IntLiteral(5)),
                VarDecl(Id("z"),[],IntLiteral(6)), VarDecl(Id("t"),[],None)],
                [Assign(Id("t"),BinaryOp("-",BinaryOp("+",BinaryOp("-",Id("x"),Id("y")),Id("z")),IntLiteral(5)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test16(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4.5, y = 5.2e-1, z = 6.9, t;
                t = x -. y +. z -. 5e-10;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],FloatLiteral(4.5)),VarDecl(Id("y"),[],FloatLiteral(5.2e-1)),
                VarDecl(Id("z"),[],FloatLiteral(6.9)), VarDecl(Id("t"),[],None)],
                [Assign(Id("t"),BinaryOp("-.",BinaryOp("+.",BinaryOp("-.",Id("x"),Id("y")),Id("z")),FloatLiteral(5e-10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test17(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4.5, y = 5.2e-1, z = 6.9, t;
                t = x *. y +. z *. 5e-10;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],FloatLiteral(4.5)),VarDecl(Id("y"),[],FloatLiteral(5.2e-1)),
                VarDecl(Id("z"),[],FloatLiteral(6.9)), VarDecl(Id("t"),[],None)],
                [Assign(Id("t"),BinaryOp("+.",BinaryOp("*.",Id("x"),Id("y")),BinaryOp("*.",Id("z"),FloatLiteral(5e-10))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test18(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4, y = 5, z = 6, t;
                t = x * y - z \ 5;
            EndBody.
        """
        expect = str(Program(
            [FuncDecl(Id("main"), [], ([VarDecl(Id("x"), [], IntLiteral(4)), VarDecl(Id("y"), [], IntLiteral(5)),
                                        VarDecl(Id("z"), [], IntLiteral(6)), VarDecl(Id("t"), [], None)],
                                       [Assign(Id("t"),BinaryOp("-",BinaryOp("*",Id("x"),Id("y")),BinaryOp("\\",Id("z"),IntLiteral(5))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test19(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4, y = 5, z = 6, t;
                t = x \ y \ z * 5;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(4)),VarDecl(Id("y"),[],IntLiteral(5)),
                VarDecl(Id("z"),[],IntLiteral(6)), VarDecl(Id("t"),[],None)],
                [Assign(Id("t"),BinaryOp("*",BinaryOp("\\",BinaryOp("\\",Id("x"),Id("y")),Id("z")),IntLiteral(5)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test20(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4.5, y = 5.2e-1, z = 6.9, t;
                t = x \. y *. z \. 5e-10;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"), [], (
        [VarDecl(Id("x"), [], FloatLiteral(4.5)), VarDecl(Id("y"), [], FloatLiteral(5.2e-1)),
         VarDecl(Id("z"), [], FloatLiteral(6.9)), VarDecl(Id("t"), [], None)],
        [Assign(Id("t"),BinaryOp("\.", BinaryOp("*.", BinaryOp("\.", Id("x"), Id("y")), Id("z")), FloatLiteral(5e-10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test21(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4, y = 5, z = 6, t;
                t = -x * y - z \ -5;
            EndBody.
        """
        expect = str(Program(
            [FuncDecl(Id("main"), [], ([VarDecl(Id("x"), [], IntLiteral(4)), VarDecl(Id("y"), [], IntLiteral(5)),
                                        VarDecl(Id("z"), [], IntLiteral(6)), VarDecl(Id("t"), [], None)],
                                       [Assign(Id("t"),BinaryOp("-",BinaryOp("*",UnaryOp("-",Id("x")),Id("y")),BinaryOp("\\",Id("z"),UnaryOp("-",IntLiteral(5)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test22(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4.5, y = 5.2e-1, z = 6.9, t;
                t = x *. y +. -.z *. 5e-10;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],FloatLiteral(4.5)),VarDecl(Id("y"),[],FloatLiteral(5.2e-1)),
                VarDecl(Id("z"),[],FloatLiteral(6.9)), VarDecl(Id("t"),[],None)],
                [Assign(Id("t"),BinaryOp("+.",BinaryOp("*.",Id("x"),Id("y")),BinaryOp("*.",UnaryOp("-.",Id("z")),FloatLiteral(5e-10))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test23(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c;
                c = a && b;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],BooleanLiteral(True)),VarDecl(Id("b"),[],BooleanLiteral(False)),
                VarDecl(Id("c"),[],None)],
                [Assign(Id("c"),BinaryOp("&&",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test24(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c;
                c = a && b || False;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],BooleanLiteral(True)),VarDecl(Id("b"),[],BooleanLiteral(False)),
                VarDecl(Id("c"),[],None)],
                [Assign(Id("c"),BinaryOp("||",BinaryOp("&&",Id("a"),Id("b")),BooleanLiteral(False)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test25(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c;
                c = !a && b;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"), [], (
        [VarDecl(Id("a"), [], BooleanLiteral(True)), VarDecl(Id("b"), [], BooleanLiteral(False)),
         VarDecl(Id("c"), [], None)],
        [Assign(Id("c"), BinaryOp("&&", UnaryOp("!",Id("a")), Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test26(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c;
                c = !a || !b && True;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"), [], (
        [VarDecl(Id("a"), [], BooleanLiteral(True)), VarDecl(Id("b"), [], BooleanLiteral(False)),
         VarDecl(Id("c"), [], None)],
        [Assign(Id("c"),BinaryOp("&&",BinaryOp("||",UnaryOp("!",Id("a")),UnaryOp("!",Id("b"))),BooleanLiteral(True)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test27(self):
        """Test variable declaration"""
        input = """
        Function: main
            Body:
                Var: arr[3] = {1, 2, 3}, a = 1, b = 2, c;
                c = arr[3] + b;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("arr"),[3],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))
                                                       ,VarDecl(Id("a"),[],IntLiteral(1)),VarDecl(Id("b"),[],IntLiteral(2)),VarDecl(Id("c"),[],None)],
                                                      [Assign(Id("c"),BinaryOp("+",ArrayCell(Id("arr"),[IntLiteral(3)]),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test28(self):
        """Test variable declaration"""
        input = """
        Function: main
            Body:
                Var: arr[3] = {1, 2, 3}, a = 1, b = 2, c;
                c = arr[2] + b * arr[0];
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("arr"),[3],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))
                                                       ,VarDecl(Id("a"),[],IntLiteral(1)),VarDecl(Id("b"),[],IntLiteral(2)),VarDecl(Id("c"),[],None)],
                                                      [Assign(Id("c"),BinaryOp("+",ArrayCell(Id("arr"),[IntLiteral(2)]),BinaryOp("*",Id("b"),
                                                    ArrayCell(Id("arr"),[IntLiteral(0)]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test29(self):
        """Test variable declaration"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < 10, 1) Do
                    x = x + i;
                EndFor.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                                                      [For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(1),([],[Assign(Id("x"),BinaryOp("+",Id("x"),Id("i")))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test30(self):
        """Test variable declaration"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < 10, 1) Do
                    Var: y = 2;
                    x = y + i;
                EndFor.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(1),
                ([VarDecl(Id("y"),[],IntLiteral(2))],
                [Assign(Id("x"),BinaryOp("+",Id("y"),Id("i")))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test31(self):
        """Test variable declaration"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i =/= 10, 1*2) Do
                    Var: y = 2;
                    x = y + i;
                EndFor.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [For(Id("i"),IntLiteral(0),BinaryOp("=/=",Id("i"),IntLiteral(10)),BinaryOp("*",IntLiteral(1),IntLiteral(2)),
                ([VarDecl(Id("y"),[],IntLiteral(2))],
                [Assign(Id("x"),BinaryOp("+",Id("y"),Id("i")))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test32(self):
        """Test variable declaration"""
        input = """
        Function: main
            Body:
                For (i = 0, i =/= 10, 1*2) Do
                
                EndFor.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([],
                [For(Id("i"),IntLiteral(0),BinaryOp("=/=",Id("i"),IntLiteral(10)),BinaryOp("*",IntLiteral(1),IntLiteral(2)),
                ([],
                []))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    # def test29(self):
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
    #     self.assertTrue(TestAST.checkASTGen(input,expect,329))
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