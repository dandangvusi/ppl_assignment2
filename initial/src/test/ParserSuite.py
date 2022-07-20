import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program_1(self):
        """Simple program with built in functions"""
        input = """
        Function: main
            Body:
                printLn();
                print("Hello BKIT");
                printStrLn("Hello Dan");
                read();
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_simple_program_2(self):
        """Simple program with function call statement"""
        input = """
        Function: isGreaterThanZero
            Parameter: a
            Body:
                If a > 0 Then
                    Return True;
                Else
                    Return False;
                EndIf.
            EndBody.
        Function: main
            Body:
                Var: x = 1;
                print(isGreaterThanZero(x));
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_simple_program_3(self):
        """Simple program with If statement"""
        input = """
        Function: main
                Body:
                    Var: x = 5;
                    If x > 0 Then
                        print("x is greater than 0");
                    ElseIf x == 0 Then
                        print("x is equal to 0");
                    Else
                        print("x is less than 0");
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_simple_program_4(self):
        """Simple program with If statement"""
        input = """
        Function: main
                Body:
                    Var: x = 5;
                    If x > 0 Then
                        print("x is greater than 0");
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_simple_program_5(self):
        """Simple program with If statement"""
        input = """
        Function: main
                Body:
                    Var: x = 5;
                    If x > 0 Then
                        print("x is greater than 0");
                    ElseIf x == 0 Then
                        print("x is equal to 0");
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_simple_program_6(self):
        """Simple program with If statement"""
        input = """
        Function: main
                Body:
                    Var: x = 5;
                    If x > 0 Then
                        print("x is greater than 0");
                    Else
                        print("x is less than 0");
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_simple_program_7(self):
        """Simple program with If statement"""
        input = """
        Function: main
                Body:
                    Var: x = 5;
                    If x > 0 Then
                        print("x is greater than 0");
                    ElseIf x == 0 Then
                        print("x is equal to 0");
                    ElseIf x != 0 Then
                        print("x is not equal to 0");
                    Else
                        print("x is less than 0");
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_simple_program_8(self):
        """Simple program with Return statement"""
        input = """
        Function: add2int
            Parameter: a, b
            Body:
                Return a + b;
            EndBody.
        Function: main
            Body:
                Var: x = 1, y = 2, z;
                z = add2int(x, y);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_simple_program_9(self):
        """Simple program with Return statement"""
        input = """
        Function: foo
            Body:
                Return;
            EndBody.
        Function: main
            Body:
                foo();
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_simple_program_10(self):
        """Simple program with Return statement outside function"""
        input = """
        Var: a, b = 1;
        Return a;
        Function: main
            Body:
                a = b + 2;
                print(a);
            EndBody.
        """
        expect = "Error on line 3 col 8: Return"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_simple_program_11(self):
        """Simple program with variable declare statement"""
        input = """
        Var: x = 5, y = 2.0, z = "x*y = ";
        Function: main
            Body:
                Var: a;
                a = x * y;
                print(z);
                print(a);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_simple_program_12(self):
        """Simple program with variable declare statement"""
        input = """
        Var: x = 1.5e2, y = 3.6;
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                a[0] = 0;
                b = 5;
                print(b);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_simple_program_13(self):
        """Simple program with variable declare statement apear after other statements"""
        input = """
        Var: x = 1.5e2, y = 3.6;
        Function: main
            Body:
                a[0] = 0;
                b = 5;
                Var: a[5] = {1,2,3,4,5}, b = 2;
                print(b);
            EndBody.
        """
        expect = "Error on line 7 col 16: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_simple_program_14(self):
        """Simple program with assignment statement"""
        input = """
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                a[0] = getBigger(a[1], a[2]);
                b = 5 + 2*3;
                print(b);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_simple_program_15(self):
        """Simple program with illegal assignment statement"""
        input = """
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                5 = getBigger(a[1], a[2]);
                b = 5 + 2*3;
                print(b);
            EndBody.
        """
        expect = "Error on line 5 col 16: 5"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_simple_program_16(self):
        """Simple program with illegal assignment statement"""
        input = """
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                a[0] = getBigger(a[1], a[2]);
                True = 5 + 2*3;
                print(b);
            EndBody.
        """
        expect = "Error on line 6 col 16: True"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_simple_program_17(self):
        """Simple program with for statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < x, 1) Do
                    writeln(i);
                    If i % 2 == 0 Then
                        Continue;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_simple_program_18(self):
        """Simple program with for statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < x, 1 * 2) Do
                    If i % 2 == 0 Then
                        Continue;
                    EndIf.
                    writeln(i);
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_simple_program_19(self):
        """Simple program with for statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < x, getBigger(2, 3)) Do
                    writeln(i);
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_simple_program_20(self):
        """Simple program with for statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < x) Do
                    writeln(i);
                    If i % 2 == 0 Then
                        Continue;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = "Error on line 5 col 33: )"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_simple_program_21(self):
        """Simple program with for statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < x, 1)
                    writeln(i);
                    If i % 2 == 0 Then
                        Continue;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = "Error on line 6 col 20: writeln"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_simple_program_22(self):
        """Simple program with for statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < x, 1) Do
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_simple_program_23(self):
        """Simple program with while statement"""
        input = """
        Function: multipleArray
            Parameter: a[5], b
            Body:
                Var: i = 0;
                While i < 5 Do
                    a[i] = a[i]*b;
                    i = i + 1;
                EndWhile.
            EndBody.
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                multipleArray(a,b);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_simple_program_24(self):
        """Simple program with while statement"""
        input = """
        Function: multipleArray
            Parameter: a[5], b
            Body:
                Var: i = 0;
                While i < 5 + 1 Do
                    a[i] = a[i]*b;
                    i = i + 1;
                EndWhile.
            EndBody.
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                multipleArray(a,b);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_simple_program_25(self):
        """Simple program with while statement"""
        input = """
        Function: multipleArray
            Parameter: a[5], b
            Body:
                Var: i = 0;
                While i < 5 Do
                EndWhile.
            EndBody.
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                multipleArray(a,b);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_simple_program_26(self):
        """Simple program with while statement"""
        input = """
        Function: multipleArray
            Parameter: a[5], b
            Body:
                Var: i = 0;
                While i < 5 Do
            EndBody.
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                multipleArray(a,b);
            EndBody.
        """
        expect = "Error on line 7 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_simple_program_27(self):
        """Simple program with do-while statement"""
        input = """
        Function: multipleArray
            Parameter: a[5], b
            Body:
                Var: i = 0;
                Do
                    a[i] = a[i]*b;
                    i = i + 1;
                While i < 5
                EndDo.
            EndBody.
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                multipleArray(a,b);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_simple_program_28(self):
        """Simple program with do-while statement"""
        input = """
        Function: multipleArray
            Parameter: a[5], b
            Body:
                Var: i = 0;
                Do
                    a[i] = a[i]*b;
                    i = i + 1;
                While i < 5 + 1
                EndDo.
            EndBody.
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                multipleArray(a,b);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_simple_program_29(self):
        """Simple program with do-while statement"""
        input = """
        Function: multipleArray
            Parameter: a[5], b
            Body:
                Var: i = 0;
                Do
                While i < 5
                EndDo.
            EndBody.
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                multipleArray(a,b);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_simple_program_30(self):
        """Simple program with do-while statement"""
        input = """
        Function: multipleArray
            Parameter: a[5], b
            Body:
                Var: i = 0;
                Do
                While i < 5
            EndBody.
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                multipleArray(a,b);
            EndBody.
        """
        expect = "Error on line 8 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_simple_program_31(self):
        """Simple program with Break statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < x, 1) Do
                    print(i);
                    If i > 3 Then
                        Break;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_simple_program_32(self):
        """Simple program with continue statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < x, 1) Do
                    If i%2==0 Then
                        Continue;
                    EndIf.
                    print(i);
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_simple_program_33(self):
        """Simple program with call and return statement"""
        input = """
        Function: isGreaterZero
        Parameter: a
            Body:
                Return a > 0;
            EndBody.
        Function: main
            Body:
                Var: x = 5;
                print(isGreaterZero(x));
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_simple_program_34(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = !b && a;
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_simple_program_35(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = (c >. 1.0) || (c >. d);
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_simple_program_36(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = (c =/= d) && (d >. 0.0);
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_simple_program_37(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = arr1[1] + arr2[0] * arr2[1];
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_simple_program_38(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = abs(-2) % multi(2, 3) - 4;
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_simple_program_39(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = abs(arr1[1]) % multi(arr1[0], arr1[1]) - arr2[0];
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_simple_program_40(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = -e - -3;
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_simple_program_41(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = !!a && b || !b;
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_simple_program_42(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = e\\f\\2 - 2*3*1;
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_simple_program_43(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = e + 1 >= 3 * f;
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_simple_program_44(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: r = 10., v; 
                v = (4.\. 3.) *. 3.14 *. r *. r*. r;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_simple_program_45(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = arr1[0] * 4 - 1;
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_simple_program_46(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = !a && !b;
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_simple_program_47(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                a = d *. 3.2 >. c;
                print(a);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_simple_program_48(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                a = arr1[0] >= arr2[0];
                print(a);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_simple_program_49(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = arr1[0] != arr2[0];
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test_simple_program_50(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = arr1[1] * arr2[1] <= 100;
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_simple_program_51(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = 3.4 +. 5.3 -. c;
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_simple_program_52(self):
        """Simple program with If statement"""
        input = """
        Function: main
                Body:
                    Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};
                    If c >. d Then
                        print("If expression");
                    ElseIf c <. d Then
                        print("ElseIf expression");
                    Else
                        print("Else expression");
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_simple_program_53(self):
        """Simple program with If statement"""
        input = """
        Function: main
                Body:
                    Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};
                    If a Then
                        print("If expression");
                    ElseIf b Then
                        print("ElseIf expression");
                    Else
                        print("Else expression");
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_simple_program_54(self):
        """Simple program with If statement"""
        input = """
        Function: main
                Body:
                    Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};
                    If a != f Then
                        print("If expression");
                    ElseIf e - 1 >= 0 Then
                        print("ElseIf expression");
                    Else
                        print("Else expression");
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_simple_program_55(self):
        """Simple program with If statement"""
        input = """
        Function: main
                Body:
                    Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};
                    If len(g) > len(h) Then
                        print("If expression");
                    ElseIf len(g) < len(h) Then
                        print("ElseIf expression");
                    Else
                        print("Else expression");
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_simple_program_56(self):
        """Simple program with If statement"""
        input = """
        Function: main
                Body:
                    Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};
                    If len(g) > len(h) Then
                        d = d *. 2;
                    ElseIf len(g) < len(h) Then
                        d = len(g) *. 2;
                    Else
                        d = d +. 1;
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_simple_program_57(self):
        """Simple program with If statement"""
        input = """
        Function: main
                Body:
                    Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};
                    If len(g) > len(h) Then
                        a = a || b;
                    ElseIf len(g) < len(h) Then
                        b = b || a;
                    Else
                        c = a && b;
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_simple_program_58(self):
        """Simple program with If statement"""
        input = """
        Function: main
                Body:
                    Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};
                    If len(g) > len(h) Then
                        print(g);
                    ElseIf len(g) < len(h) Then
                        print(h);
                    Else
                        print("Else expression");
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_simple_program_59(self):
        """Simple program with while statement"""
        input = """
        Function: multipleArray
            Parameter: a[5], b
            Body:
                Var: i = 0, l = 5;
                While i < l Do
                    a[i] = a[i]*b;
                    i = i + 1;
                EndWhile.
            EndBody.
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                multipleArray(a,b);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_simple_program_60(self):
        """Simple program with while statement"""
        input = """
        Function: multipleArray
            Parameter: a[5], b
            Body:
                Var: i = 0;
                While i < 5 Do
                    a[i] = a[i]\\b;
                    i = i + 1;
                EndWhile.
            EndBody.
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                multipleArray(a,b);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_simple_program_61(self):
        """Simple program with while statement"""
        input = """
        Function: multipleArray
            Parameter: a[5], b
            Body:
                Var: i = 0;
                While True Do
                    a[i] = a[i]*b;
                    i = i + 1;
                EndWhile.
            EndBody.
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                multipleArray(a,b);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_simple_program_62(self):
        """Simple program with do-while statement"""
        input = """
        Function: multipleArray
            Parameter: a[5], b
            Body:
                Var: i = 0, l = 5;
                Do
                    a[i] = a[i]*b;
                    i = i + 1;
                While i < l
                EndDo.
            EndBody.
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                multipleArray(a,b);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_simple_program_63(self):
        """Simple program with do-while statement"""
        input = """
        Function: multipleArray
            Parameter: a[5], b
            Body:
                Var: i = 0;
                Do
                    a[i] = a[i]*b;
                    i = i + 1;
                While i < 1 + 2 * 2
                EndDo.
            EndBody.
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                multipleArray(a,b);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test_simple_program_64(self):
        """Simple program with do-while statement"""
        input = """
        Function: multipleArray
            Parameter: a[5], b
            Body:
                Var: i = 0;
                Do
                    a[i] = a[i]*b;
                    i = i + 1;
                While True
                EndDo.
            EndBody.
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                multipleArray(a,b);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_simple_program_65(self):
        """Simple program with for statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < 100 * 2 - 5, 1) Do
                    writeln(i);
                    If i % 2 == 0 Then
                        Continue;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test_simple_program_66(self):
        """Simple program with for statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 1 + 2 * 3, i < 1000, 1) Do
                    writeln(i);
                    If i % 2 == 0 Then
                        Continue;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_simple_program_67(self):
        """Simple program with for statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < 100, x) Do
                    writeln(i);
                    If i % 2 == 0 Then
                        Continue;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_simple_program_68(self):
        """Simple program with for statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < x, 1*2) Do
                    writeln(i);
                    If i % 2 == 0 Then
                        Continue;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_simple_program_69(self):
        """Simple program with for statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < x, 1) Do
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test_simple_program_70(self):
        """Simple program with for statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 10, i < x*100, 5*2) Do
                    writeln(i);
                    If i % 2 == 0 Then
                        Continue;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_simple_program_71(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                arr1[3 + foo(2)] = arr2[b[2][3]] + 4;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_simple_program_72(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                arr1[3*2 - e] = arr2[b[2 - 1]] + 4;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test_simple_program_73(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                arr1[2][3] = arr2[1] + 4*2 - 9;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test_simple_program_74(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = string2int(read());
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_simple_program_75(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = string2int(read());
                res = int2float(res) +. 2.0;
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_simple_program_76(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = string2int(read());
                res = int2float(res) +. 2.0 *. arr1[0];
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_simple_program_77(self):
        """Simple program with call statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                print(foo());
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test_simple_program_78(self):
        """Simple program with call statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                goo(x, y, z, "Hello");
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_simple_program_79(self):
        """Simple program with call statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                foo(arr1[0], arr1[1]);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_simple_program_80(self):
        """Simple program with call statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                foo(a, !b, e);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_simple_program_81(self):
        """Simple program"""
        input = """
        Var: x;
        Function: fact
            Parameter: n
            Body:
                If n==0 Then
                    Return 1;
                Else
                    Return n*fact(n-1);
                EndIf.
            EndBody.
        Function: main
            Body:
                x = 10;
                fact(x);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_simple_program_82(self):
        """Simple program no function declaration"""
        input = """
        Var: x;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_simple_program_83(self):
        """Simple program wrong parameter separate"""
        input = """
        Var: x;
        Function: fact
            Parameter: n,
            Body:
                If n==0 Then
                    Return 1;
                Else
                    Return n*fact(n-1);
                EndIf.
            EndBody.
        Function: main
            Body:
                x = 10;
                fact(x);
            EndBody.
        """
        expect = "Error on line 5 col 12: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_simple_program_84(self):
        """Simple program initialized parameter"""
        input = """
        Var: x;
        Function: fact
            Parameter: n = 2
            Body:
                If n==0 Then
                    Return 1;
                Else
                    Return n*fact(n-1);
                EndIf.
            EndBody.
        Function: main
            Body:
                x = 10;
                fact(x);
            EndBody.
        """
        expect = "Error on line 4 col 25: ="
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_simple_program_85(self):
        """Simple program with no statement main function"""
        input = """
        Var: x;
        Function: fact
            Parameter: n
            Body:
                If n==0 Then
                    Return 1;
                Else
                    Return n*fact(n-1);
                EndIf.
            EndBody.
        Function: main
            Body:
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test_simple_program_86(self):
        """Simple program missing EndBody"""
        input = """
        Var: x;
        Function: fact
            Parameter: n
            Body:
                If n==0 Then
                    Return 1;
                Else
                    Return n*fact(n-1);
                EndIf.
            EndBody.
        Function: main
            Body:
                x = 10;
                fact(x);
        """
        expect = "Error on line 16 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_simple_program_87(self):
        """Simple program with var declaration after function declare"""
        input = """
        Function: fact
            Parameter: n
            Body:
                If n==0 Then
                    Return 1;
                Else
                    Return n*fact(n-1);
                EndIf.
            EndBody.
        Function: main
            Body:
                x = 10;
                fact(x);
            EndBody.
        Var: x;
        """
        expect = "Error on line 16 col 8: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_simple_program_88(self):
        """Simple program with wrong var declaration"""
        input = """
        Var: ;
        Function: fact
            Parameter: n
            Body:
                If n==0 Then
                    Return 1;
                Else
                    Return n*fact(n-1);
                EndIf.
            EndBody.
        Function: main
            Body:
            EndBody.
        """
        expect = "Error on line 2 col 13: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_simple_program_89(self):
        """Simple program with wrong var declaration"""
        input = """
        Var: x, ;
        Function: fact
            Parameter: n
            Body:
                If n==0 Then
                    Return 1;
                Else
                    Return n*fact(n-1);
                EndIf.
            EndBody.
        Function: main
            Body:
            EndBody.
        """
        expect = "Error on line 2 col 16: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_simple_program_90(self):
        """Simple program"""
        input = """
        Function: double
            Parameter: n
            Body:
                Return n * 2;
            EndBody.
        Function: main
            Body:
                Var: x = 5;
                print(double(x));
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_simple_program_91(self):
        """Simple program"""
        input = """
        Function: double
            Parameter: n
            Body:
                Return n * 2;
            EndBody.
        Function: main
            Body:
                Var: x = 5;
                print(double(x + 4));
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_simple_program_92(self):
        """Simple program"""
        input = """
        Function: double
            Parameter: n
            Body:
                Return n * 2;
            EndBody.
        Function: main
            Body:
                Var: x = 5;
                print(double(4 * 4 - 3));
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_simple_program_93(self):
        """Simple program"""
        input = """
        Function: isGreaterZero
            Parameter: n
            Body:
                Return n > 0;
            EndBody.
        Function: main
            Body:
                Var: x = 5;
                print(isGreaterZero(4 * 4 - 3));
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_simple_program_94(self):
        """Simple program"""
        input = """
        Function: isGreaterZero
            Parameter: n
            Body:
                Return n > 0;
            EndBody.
        Function: main
            Body:
                Var: x = 5;
                print(isGreaterZero(-x));
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_simple_program_95(self):
        """Simple program"""
        input = """
        Function: isGreaterZero
            Parameter: n
            Body:
                Return n > 0;
            EndBody.
        Function: main
            Body:
                Var: x = 5;
                print(isGreaterZero(x));
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_simple_program_96(self):
        """Simple program"""
        input = """
        Function: abs
            Parameter: n
            Body:
                If n >= 0 Then
                    Return n;
                Else
                    Return -n;
                EndIf.
            EndBody.
        Function: main
            Body:
                Var: x = 5;
                print(abs(x));
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_simple_program_97(self):
        """Simple program"""
        input = """
        Function: abs
            Parameter: n
            Body:
                If n >= 0 Then
                    Return n;
                Else
                    Return -n;
                EndIf.
            EndBody.
        Function: main
            Body:
                Var: x = 5;
                print(abs(-x));
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_simple_program_98(self):
        """Simple program"""
        input = """
        Function: abs
            Parameter: n
            Body:
                If n >= 0 Then
                    Return n;
                Else
                    Return -n;
                EndIf.
            EndBody.
        Function: main
            Body:
                Var: x = 5;
                print(abs(-5 - 6));
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_simple_program_99(self):
        """Simple program"""
        input = """
        Function: abs
            Parameter: n
            Body:
                If n >= 0 Then
                    Return n;
                Else
                    Return -n;
                EndIf.
            EndBody.
        Function: main
            Body:
                Var: x = 5;
                print(abs(4*3\\2 - 1));
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_simple_program_100(self):
        """Simple program"""
        input = """
        Function: abs
            Parameter: n
            Body:
                If n >= 0 Then
                    Return n;
                Else
                    Return -n;
                EndIf.
            EndBody.
        Function: main
            Body:
                Var: x = 5;
                print(abs(True));
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))