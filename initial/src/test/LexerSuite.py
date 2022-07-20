import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_id_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 101))

    def test_id_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abC_3", "abC_3,<EOF>", 102))

    def test_id_3(self):
        """test illegal identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_abc", "Error Token _", 103))

    def test_id_4(self):
        """test illegal identifiers"""
        self.assertTrue(TestLexer.checkLexeme("Abc", "Error Token A", 104))

    def test_id_5(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("b3c", "b3c,<EOF>", 105))

    def test_id_6(self):
        """test illegal identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            "ab?svn", "ab,Error Token ?", 106))

    def test_key_words_1(self):
        """test key words"""
        self.assertTrue(TestLexer.checkLexeme(
            "Body Break Continue Do Else ElseIf EndBody EndIf EndFor EndWhile", "Body,Break,Continue,Do,Else,ElseIf,EndBody,EndIf,EndFor,EndWhile,<EOF>", 107))

    def test_key_words_2(self):
        """test key words"""
        self.assertTrue(TestLexer.checkLexeme(
            "For Function If Parameter Return Then Var While True False EndDo", "For,Function,If,Parameter,Return,Then,Var,While,True,False,EndDo,<EOF>", 108))

    def test_operators_1(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme(
            "+ +. - -. * *. \\ \\. % ! && ||", "+,+.,-,-.,*,*.,\\,\\.,%,!,&&,||,<EOF>", 109))

    def test_operators_2(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme(
            "== != < > <= >= =/= <. >. <=. >=.", "==,!=,<,>,<=,>=,=/=,<.,>.,<=.,>=.,<EOF>", 110))

    def test_separators(self):
        """test separators"""
        self.assertTrue(TestLexer.checkLexeme(
            "() [] {} : . , ;", "(,),[,],{,},:,.,,,;,<EOF>", 111))

    def test_int_lit_1(self):
        """test decimal intergers"""
        self.assertTrue(TestLexer.checkLexeme("12302", "12302,<EOF>", 112))

    def test_int_lit_2(self):
        """test decimal intergers"""
        self.assertTrue(TestLexer.checkLexeme("5", "5,<EOF>", 113))

    def test_int_lit_3(self):
        """test decimal intergers"""
        self.assertTrue(TestLexer.checkLexeme("0", "0,<EOF>", 114))

    def test_int_lit_4(self):
        """test illegal decimal intergers"""
        self.assertTrue(TestLexer.checkLexeme("012", "0,12,<EOF>", 115))

    def test_int_lit_5(self):
        """test illegal decimal intergers"""
        self.assertTrue(TestLexer.checkLexeme("002", "0,0,2,<EOF>", 116))

    def test_int_lit_6(self):
        """test hexadecimaloctal intergers"""
        self.assertTrue(TestLexer.checkLexeme("0xAF", "0xAF,<EOF>", 117))

    def test_int_lit_7(self):
        """test hexadecimal intergers"""
        self.assertTrue(TestLexer.checkLexeme("0X1A", "0X1A,<EOF>", 118))

    def test_int_lit_8(self):
        """test hexadecimal intergers"""
        self.assertTrue(TestLexer.checkLexeme("0X10", "0X10,<EOF>", 119))

    def test_int_lit_9(self):
        """test illegal hexadecimal intergers"""
        self.assertTrue(TestLexer.checkLexeme("0X0", "0,Error Token X", 120))

    def test_int_lit_10(self):
        """test illegal hexadecimal intergers"""
        self.assertTrue(TestLexer.checkLexeme(
            "0XAG", "0XA,Error Token G", 121))

    def test_int_lit_11(self):
        """test illegal hexadecimal intergers"""
        self.assertTrue(TestLexer.checkLexeme(
            "0X1b", "0X1,b,<EOF>", 122))

    def test_int_lit_12(self):
        """test illegal hexadecimal intergers"""
        self.assertTrue(TestLexer.checkLexeme(
            "0X1b", "0X1,b,<EOF>", 123))

    def test_int_lit_13(self):
        """test octal intergers"""
        self.assertTrue(TestLexer.checkLexeme(
            "0o567", "0o567,<EOF>", 124))

    def test_int_lit_14(self):
        """test octal intergers"""
        self.assertTrue(TestLexer.checkLexeme(
            "0O17", "0O17,<EOF>", 125))

    def test_int_lit_15(self):
        """test illegal octal intergers"""
        self.assertTrue(TestLexer.checkLexeme(
            "0O18", "0O1,8,<EOF>", 126))

    def test_int_lit_16(self):
        """test illegal octal intergers"""
        self.assertTrue(TestLexer.checkLexeme(
            "0O1A", "0O1,Error Token A", 127))

    def test_float_lit_1(self):
        """test floats"""
        self.assertTrue(TestLexer.checkLexeme(
            "12.0e3", "12.0e3,<EOF>", 128))

    def test_float_lit_2(self):
        """test floats"""
        self.assertTrue(TestLexer.checkLexeme(
            "12e3", "12e3,<EOF>", 129))

    def test_float_lit_3(self):
        """test floats"""
        self.assertTrue(TestLexer.checkLexeme(
            "12.e3", "12.e3,<EOF>", 130))

    def test_float_lit_4(self):
        """test floats"""
        self.assertTrue(TestLexer.checkLexeme(
            "12.0e-3", "12.0e-3,<EOF>", 131))

    def test_float_lit_5(self):
        """test floats"""
        self.assertTrue(TestLexer.checkLexeme(
            "12.", "12.,<EOF>", 132))

    def test_float_lit_6(self):
        """test floats"""
        self.assertTrue(TestLexer.checkLexeme(
            "12e-3", "12e-3,<EOF>", 133))

    def test_bool_lit_1(self):
        """test booleans"""
        self.assertTrue(TestLexer.checkLexeme(
            "True", "True,<EOF>", 134))

    def test_bool_lit_2(self):
        """test booleans"""
        self.assertTrue(TestLexer.checkLexeme(
            "False", "False,<EOF>", 135))

    def test_string_lit_1(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc\\h def"  """, """Illegal Escape In String: abc\\h""", 136))

    def test_string_lit_2(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc def  """, """Unclosed String: abc def  """, 137))

    def test_string_lit_3(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "ab'"c\\n def"  """, """ab'"c\\n def,<EOF>""", 138))

    def test_string_lit_4(self):
        """test normal string with tab"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "This is a string containing tab \t" """, "This is a string containing tab 	,<EOF>", 139))

    def test_string_lit_5(self):
        """test normal string with double quotes"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "He asked me: '"Where is John?'"" """, """He asked me: '"Where is John?'",<EOF>""", 140))

    def test_string_lit_6(self):
        """test normal string with double quotes"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "Hi, my name is Dan!" """, """Hi, my name is Dan!,<EOF>""", 141))

    def test_array_lit_1(self):
        """test array literal"""
        self.assertTrue(TestLexer.checkLexeme(
            "{1,2,3,4,5}", "{,1,,,2,,,3,,,4,,,5,},<EOF>", 142))

    def test_array_lit_2(self):
        """test array literal"""
        self.assertTrue(TestLexer.checkLexeme(
            """{"Dan", "Anh", "Trinh"}""", "{,Dan,,,Anh,,,Trinh,},<EOF>", 143))

    def test_array_lit_3(self):
        """test array literal"""
        self.assertTrue(TestLexer.checkLexeme(
            "{{1,2},{3,4},{5,6}}", "{,{,1,,,2,},,,{,3,,,4,},,,{,5,,,6,},},<EOF>", 144))

    def test_simple_program_1(self):
        """test simple program"""
        self.assertTrue(TestLexer.checkLexeme(
            "Var: a = 5;", "Var,:,a,=,5,;,<EOF>", 145))

    def test_simple_program_2(self):
        """test simple program"""
        self.assertTrue(TestLexer.checkLexeme(
            "Var: a[2][3] = {{2,3,4},{5,6,7}};", "Var,:,a,[,2,],[,3,],=,{,{,2,,,3,,,4,},,,{,5,,,6,,,7,},},;,<EOF>", 146))

    def test_simple_program_3(self):
        """test simple program"""
        self.assertTrue(TestLexer.checkLexeme(
            "Var: a, b = 5.8e-10, c, d;", "Var,:,a,,,b,=,5.8e-10,,,c,,,d,;,<EOF>", 147))

    def test_simple_program_4(self):
        """test simple program"""
        self.assertTrue(TestLexer.checkLexeme(
            "Var: m, n[10];", "Var,:,m,,,n,[,10,],;,<EOF>", 148))

    def test_simple_program_5(self):
        """test simple program"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Var: x;
            Function: fact
                Parameter: n
                Body:
                    If n == 0 Then
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
            """,
            """Var,:,x,;,Function,:,fact,Parameter,:,n,Body,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,EndBody,.,Function,:,main,Body,:,x,=,10,;,fact,(,x,),;,EndBody,.,<EOF>""", 149))

    def test_simple_program_6(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            **
            Global var declare
            **
            Var: x = 0;
            """, "Var,:,x,=,0,;,<EOF>", 150))

    def test_simple_program_7(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            ** Global var declare **
            Var: x = 0;
            """, "Var,:,x,=,0,;,<EOF>", 151))

    def test_general_1(self):
        """test simple program with expression"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Var: x = 0, y = 1;
            Function: main
                Body:
                    Var: z;
                    z = x + y;
                    print(z);
                EndBody.
            """,
            """Var,:,x,=,0,,,y,=,1,;,Function,:,main,Body,:,Var,:,z,;,z,=,x,+,y,;,print,(,z,),;,EndBody,.,<EOF>""", 152))

    def test_general_2(self):
        """test simple program with expression"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Var: x = 0, y = 1;
            Function: main
                Body:
                    Var: z;
                    z = x <= y;
                    print(z);
                EndBody.
            """,
            """Var,:,x,=,0,,,y,=,1,;,Function,:,main,Body,:,Var,:,z,;,z,=,x,<=,y,;,print,(,z,),;,EndBody,.,<EOF>""", 153))

    def test_general_3(self):
        """test simple program with expression"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Var: x = True, y = 1;
            Function: main
                Body:
                    Var: z;
                    z = !x;
                    print(z);
                EndBody.
            """,
            """Var,:,x,=,True,,,y,=,1,;,Function,:,main,Body,:,Var,:,z,;,z,=,!,x,;,print,(,z,),;,EndBody,.,<EOF>""", 154))

    def test_general_4(self):
        """test simple program with expression"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Var: x = 0, y = 1;
            Function: main
                Body:
                    Var: z;
                    z = x != y;
                    print(z);
                EndBody.
            """,
            """Var,:,x,=,0,,,y,=,1,;,Function,:,main,Body,:,Var,:,z,;,z,=,x,!=,y,;,print,(,z,),;,EndBody,.,<EOF>""", 155))

    def test_general_5(self):
        """test simple program with expression"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Var: x = 0.5, y = 1;
            Function: main
                Body:
                    Var: z;
                    z = x +. y;
                    print(z);
                EndBody.
            """,
            """Var,:,x,=,0.5,,,y,=,1,;,Function,:,main,Body,:,Var,:,z,;,z,=,x,+.,y,;,print,(,z,),;,EndBody,.,<EOF>""", 156))

    def test_general_6(self):
        """test simple program with expression"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Var: x = 1e-10, y = 1000.0;
            Function: main
                Body:
                    Var: z;
                    z = x *. y;
                    print(z);
                EndBody.
            """,
            """Var,:,x,=,1e-10,,,y,=,1000.0,;,Function,:,main,Body,:,Var,:,z,;,z,=,x,*.,y,;,print,(,z,),;,EndBody,.,<EOF>""", 157))

    def test_general_7(self):
        """test simple program with expression"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Var: x = 1.5e2, y = 3.6;
            Function: main
                Body:
                    Var: z;
                    z = x =/= y;
                    print(z);
                EndBody.
            """,
            """Var,:,x,=,1.5e2,,,y,=,3.6,;,Function,:,main,Body,:,Var,:,z,;,z,=,x,=/=,y,;,print,(,z,),;,EndBody,.,<EOF>""", 158))

    def test_general_8(self):
        """test simple program with expression"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Var: x = 1.5e2, y = 3.6;
            Function: main
                Body:
                    Var: z;
                    z = x >. y;
                    print(z);
                EndBody.
            """,
            """Var,:,x,=,1.5e2,,,y,=,3.6,;,Function,:,main,Body,:,Var,:,z,;,z,=,x,>.,y,;,print,(,z,),;,EndBody,.,<EOF>""", 159))

    def test_general_9(self):
        """test simple program with expression"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Var: x = 1.5e2, y = 3.6;
            Function: main
                Body:
                    Var: z;
                    z = x <=. y;
                    print(z);
                EndBody.
            """,
            """Var,:,x,=,1.5e2,,,y,=,3.6,;,Function,:,main,Body,:,Var,:,z,;,z,=,x,<=.,y,;,print,(,z,),;,EndBody,.,<EOF>""", 160))

    def test_general_10(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
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
                    multipleArray(a,b)
                EndBody.
            """,
            """Function,:,multipleArray,Parameter,:,a,[,5,],,,b,Body,:,Var,:,i,=,0,;,While,i,<,5,Do,a,[,i,],=,a,[,i,],*,b,;,i,=,i,+,1,;,EndWhile,.,EndBody,.,Function,:,main,Body,:,Var,:,a,[,5,],=,{,1,,,2,,,3,,,4,,,5,},,,b,=,2,;,multipleArray,(,a,,,b,),EndBody,.,<EOF>""", 161))

    def test_general_11(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Var: x = 1.5e2, y = 3.6;
            Function: main
                Body:
                    Var: a[5] = {1,2,3,4,5}, b = 2;
                    a[0] = 0;
                    b = 5;
                    print(b);
                EndBody.
            """,
            """Var,:,x,=,1.5e2,,,y,=,3.6,;,Function,:,main,Body,:,Var,:,a,[,5,],=,{,1,,,2,,,3,,,4,,,5,},,,b,=,2,;,a,[,0,],=,0,;,b,=,5,;,print,(,b,),;,EndBody,.,<EOF>""", 162))

    def test_general_12(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
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
            """,
            """Function,:,main,Body,:,Var,:,x,=,5,;,If,x,>,0,Then,print,(,x is greater than 0,),;,ElseIf,x,==,0,Then,print,(,x is equal to 0,),;,Else,print,(,x is less than 0,),;,EndIf,.,EndBody,.,<EOF>""", 163))

    def test_general_13(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Function: main
                Body:
                    Var: x = 5;
                    For (i = 0, i < x, 1) Do
                        writeln(i);
                    EndFor.
                EndBody.
            """,
            """Function,:,main,Body,:,Var,:,x,=,5,;,For,(,i,=,0,,,i,<,x,,,1,),Do,writeln,(,i,),;,EndFor,.,EndBody,.,<EOF>""", 164))

    def test_general_14(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Function: main
                Body:
                    Var: i = 0;
                    Do
                        writeln(i);
                        i = i + 1;
                    While i < 5
                    EndDo.
                EndBody.
            """,
            """Function,:,main,Body,:,Var,:,i,=,0,;,Do,writeln,(,i,),;,i,=,i,+,1,;,While,i,<,5,EndDo,.,EndBody,.,<EOF>""", 165))

    def test_general_15(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Function: main
                Body:
                    Var: x = 5;
                    For (i = 0, i < x, 1) Do
                        writeln(i);
                        If i > 2 Then
                            Break;
                        EndIf.
                    EndFor.
                EndBody.
            """,
            """Function,:,main,Body,:,Var,:,x,=,5,;,For,(,i,=,0,,,i,<,x,,,1,),Do,writeln,(,i,),;,If,i,>,2,Then,Break,;,EndIf,.,EndFor,.,EndBody,.,<EOF>""", 166))

    def test_general_16(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
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
            """,
            """Function,:,main,Body,:,Var,:,x,=,5,;,For,(,i,=,0,,,i,<,x,,,1,),Do,writeln,(,i,),;,If,i,%,2,==,0,Then,Continue,;,EndIf,.,EndFor,.,EndBody,.,<EOF>""", 167))

    def test_general_17(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
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
            """,
            """Function,:,main,Body,:,Var,:,x,=,5,;,If,x,>,0,Then,print,(,x is greater than 0,),;,ElseIf,x,==,0,Then,print,(,x is equal to 0,),;,Else,print,(,x is less than 0,),;,EndIf,.,EndBody,.,<EOF>""", 168))

    def test_general_18(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
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
            """,
            """Function,:,isGreaterThanZero,Parameter,:,a,Body,:,If,a,>,0,Then,Return,True,;,Else,Return,False,;,EndIf,.,EndBody,.,Function,:,main,Body,:,Var,:,x,=,1,;,print,(,isGreaterThanZero,(,x,),),;,EndBody,.,<EOF>""", 169))

    def test_built_in_function(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Function: main
                Body:
                    printLn();
                    print("Hello BKIT");
                    printStrLn("Hello Dan");
                    read();
                EndBody.
            """,
            """Function,:,main,Body,:,printLn,(,),;,print,(,Hello BKIT,),;,printStrLn,(,Hello Dan,),;,read,(,),;,EndBody,.,<EOF>""", 170))

    def test_simple_program_71(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                arr1[3 + foo(2)] = arr2[b[2][3]] + 4;
            EndBody.
            """,
            """Function,:,main,Body,:,Var,:,a,=,True,,,b,=,False,,,c,=,2.4e-1,,,d,=,1.0,,,e,=,5,,,f,=,3,,,g,=,Hello,,,h,=,Dan,,,arr1,[,2,],=,{,1,,,2,},,,arr2,[,2,],=,{,3,,,4,},;,arr1,[,3,+,foo,(,2,),],=,arr2,[,b,[,2,],[,3,],],+,4,;,EndBody,.,<EOF>""", 171))
    def test_simple_program_72(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                arr1[3*2 - e] = arr2[b[2 - 1]] + 4;
            EndBody.
            """,
            """Function,:,main,Body,:,Var,:,a,=,True,,,b,=,False,,,c,=,2.4e-1,,,d,=,1.0,,,e,=,5,,,f,=,3,,,g,=,Hello,,,h,=,Dan,,,arr1,[,2,],=,{,1,,,2,},,,arr2,[,2,],=,{,3,,,4,},;,arr1,[,3,*,2,-,e,],=,arr2,[,b,[,2,-,1,],],+,4,;,EndBody,.,<EOF>""", 172))
    def test_simple_program_73(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                arr1[2][3] = arr2[1] + 4*2 - 9;
            EndBody.
            """,
            """Function,:,main,Body,:,Var,:,a,=,True,,,b,=,False,,,c,=,2.4e-1,,,d,=,1.0,,,e,=,5,,,f,=,3,,,g,=,Hello,,,h,=,Dan,,,arr1,[,2,],=,{,1,,,2,},,,arr2,[,2,],=,{,3,,,4,},;,arr1,[,2,],[,3,],=,arr2,[,1,],+,4,*,2,-,9,;,EndBody,.,<EOF>""", 173))
    def test_simple_program_74(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = string2int(read());
                print(res);
            EndBody.
            """,
            """Function,:,main,Body,:,Var,:,a,=,True,,,b,=,False,,,c,=,2.4e-1,,,d,=,1.0,,,e,=,5,,,f,=,3,,,g,=,Hello,,,h,=,Dan,,,arr1,[,2,],=,{,1,,,2,},,,arr2,[,2,],=,{,3,,,4,},;,res,=,string2int,(,read,(,),),;,print,(,res,),;,EndBody,.,<EOF>""", 174))
    def test_simple_program_75(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = string2int(read());
                res = int2float(res) +. 2.0;
                print(res);
            EndBody.
            """,
            """Function,:,main,Body,:,Var,:,a,=,True,,,b,=,False,,,c,=,2.4e-1,,,d,=,1.0,,,e,=,5,,,f,=,3,,,g,=,Hello,,,h,=,Dan,,,arr1,[,2,],=,{,1,,,2,},,,arr2,[,2,],=,{,3,,,4,},;,res,=,string2int,(,read,(,),),;,res,=,int2float,(,res,),+.,2.0,;,print,(,res,),;,EndBody,.,<EOF>""", 175))

    def test_simple_program_76(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = string2int(read());
                res = int2float(res) +. 2.0 *. arr1[0];
                print(res);
            EndBody.
            """,
            """Function,:,main,Body,:,Var,:,a,=,True,,,b,=,False,,,c,=,2.4e-1,,,d,=,1.0,,,e,=,5,,,f,=,3,,,g,=,Hello,,,h,=,Dan,,,arr1,[,2,],=,{,1,,,2,},,,arr2,[,2,],=,{,3,,,4,},;,res,=,string2int,(,read,(,),),;,res,=,int2float,(,res,),+.,2.0,*.,arr1,[,0,],;,print,(,res,),;,EndBody,.,<EOF>""", 176))
    def test_simple_program_77(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                print(foo());
            EndBody.
            """,
            """Function,:,main,Body,:,Var,:,a,=,True,,,b,=,False,,,c,=,2.4e-1,,,d,=,1.0,,,e,=,5,,,f,=,3,,,g,=,Hello,,,h,=,Dan,,,arr1,[,2,],=,{,1,,,2,},,,arr2,[,2,],=,{,3,,,4,},;,print,(,foo,(,),),;,EndBody,.,<EOF>""", 177))
    def test_simple_program_78(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                goo(x, y, z, "Hello");
            EndBody.
            """,
            """Function,:,main,Body,:,Var,:,a,=,True,,,b,=,False,,,c,=,2.4e-1,,,d,=,1.0,,,e,=,5,,,f,=,3,,,g,=,Hello,,,h,=,Dan,,,arr1,[,2,],=,{,1,,,2,},,,arr2,[,2,],=,{,3,,,4,},;,goo,(,x,,,y,,,z,,,Hello,),;,EndBody,.,<EOF>""", 178))
    def test_simple_program_79(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                foo(arr1[0], arr1[1]);
            EndBody.
            """,
            """Function,:,main,Body,:,Var,:,a,=,True,,,b,=,False,,,c,=,2.4e-1,,,d,=,1.0,,,e,=,5,,,f,=,3,,,g,=,Hello,,,h,=,Dan,,,arr1,[,2,],=,{,1,,,2,},,,arr2,[,2,],=,{,3,,,4,},;,foo,(,arr1,[,0,],,,arr1,[,1,],),;,EndBody,.,<EOF>""", 179))
    def test_simple_program_80(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                foo(a, !b, e);
            EndBody.
            """,
            """Function,:,main,Body,:,Var,:,a,=,True,,,b,=,False,,,c,=,2.4e-1,,,d,=,1.0,,,e,=,5,,,f,=,3,,,g,=,Hello,,,h,=,Dan,,,arr1,[,2,],=,{,1,,,2,},,,arr2,[,2,],=,{,3,,,4,},;,foo,(,a,,,!,b,,,e,),;,EndBody,.,<EOF>""", 180))

    def test_simple_program_81(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
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
            """,
            """Var,:,x,;,Function,:,fact,Parameter,:,n,Body,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,EndBody,.,Function,:,main,Body,:,x,=,10,;,fact,(,x,),;,EndBody,.,<EOF>""", 181))
    def test_simple_program_82(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            Var: x;
            """,
            """Var,:,x,;,<EOF>""", 182))
    def test_simple_program_83(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
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
            """,
            """Var,:,x,;,Function,:,fact,Parameter,:,n,,,Body,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,EndBody,.,Function,:,main,Body,:,x,=,10,;,fact,(,x,),;,EndBody,.,<EOF>""", 183))
    def test_simple_program_84(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
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
            """,
            """Var,:,x,;,Function,:,fact,Parameter,:,n,=,2,Body,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,EndBody,.,Function,:,main,Body,:,x,=,10,;,fact,(,x,),;,EndBody,.,<EOF>""", 184))
    def test_simple_program_85(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
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
            """,
            """Var,:,x,;,Function,:,fact,Parameter,:,n,Body,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,EndBody,.,Function,:,main,Body,:,EndBody,.,<EOF>""", 185))

    def test_simple_program_86(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
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
            """,
            """Var,:,x,;,Function,:,fact,Parameter,:,n,Body,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,EndBody,.,Function,:,main,Body,:,x,=,10,;,fact,(,x,),;,<EOF>""", 186))
    def test_simple_program_87(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
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
            """,
            """Function,:,fact,Parameter,:,n,Body,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,EndBody,.,Function,:,main,Body,:,x,=,10,;,fact,(,x,),;,EndBody,.,Var,:,x,;,<EOF>""", 187))
    def test_simple_program_88(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
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
            """,
            """Var,:,;,Function,:,fact,Parameter,:,n,Body,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,EndBody,.,Function,:,main,Body,:,EndBody,.,<EOF>""", 188))
    def test_simple_program_89(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
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
            """,
            """Var,:,x,,,;,Function,:,fact,Parameter,:,n,Body,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,EndBody,.,Function,:,main,Body,:,EndBody,.,<EOF>""", 189))
    def test_simple_program_90(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
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
            """,
            """Function,:,double,Parameter,:,n,Body,:,Return,n,*,2,;,EndBody,.,Function,:,main,Body,:,Var,:,x,=,5,;,print,(,double,(,x,),),;,EndBody,.,<EOF>""", 190))

    def test_simple_program_91(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
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
            """,
            """Function,:,double,Parameter,:,n,Body,:,Return,n,*,2,;,EndBody,.,Function,:,main,Body,:,Var,:,x,=,5,;,print,(,double,(,x,+,4,),),;,EndBody,.,<EOF>""", 191))
    def test_simple_program_92(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
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
            """,
            """Function,:,double,Parameter,:,n,Body,:,Return,n,*,2,;,EndBody,.,Function,:,main,Body,:,Var,:,x,=,5,;,print,(,double,(,4,*,4,-,3,),),;,EndBody,.,<EOF>""", 192))
    def test_simple_program_93(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
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
            """,
            """Function,:,isGreaterZero,Parameter,:,n,Body,:,Return,n,>,0,;,EndBody,.,Function,:,main,Body,:,Var,:,x,=,5,;,print,(,isGreaterZero,(,4,*,4,-,3,),),;,EndBody,.,<EOF>""", 193))
    def test_simple_program_94(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
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
            """,
            """Function,:,isGreaterZero,Parameter,:,n,Body,:,Return,n,>,0,;,EndBody,.,Function,:,main,Body,:,Var,:,x,=,5,;,print,(,isGreaterZero,(,-,x,),),;,EndBody,.,<EOF>""", 194))
    def test_simple_program_95(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
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
            """,
            """Function,:,isGreaterZero,Parameter,:,n,Body,:,Return,n,>,0,;,EndBody,.,Function,:,main,Body,:,Var,:,x,=,5,;,print,(,isGreaterZero,(,x,),),;,EndBody,.,<EOF>""", 195))

    def test_simple_program_96(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
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
            """,
            """Function,:,abs,Parameter,:,n,Body,:,If,n,>=,0,Then,Return,n,;,Else,Return,-,n,;,EndIf,.,EndBody,.,Function,:,main,Body,:,Var,:,x,=,5,;,print,(,abs,(,x,),),;,EndBody,.,<EOF>""", 196))
    def test_simple_program_97(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
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
            """,
            """Function,:,abs,Parameter,:,n,Body,:,If,n,>=,0,Then,Return,n,;,Else,Return,-,n,;,EndIf,.,EndBody,.,Function,:,main,Body,:,Var,:,x,=,5,;,print,(,abs,(,-,x,),),;,EndBody,.,<EOF>""", 197))
    def test_simple_program_98(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
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
            """,
            """Function,:,abs,Parameter,:,n,Body,:,If,n,>=,0,Then,Return,n,;,Else,Return,-,n,;,EndIf,.,EndBody,.,Function,:,main,Body,:,Var,:,x,=,5,;,print,(,abs,(,-,5,-,6,),),;,EndBody,.,<EOF>""", 198))
    def test_simple_program_99(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
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
            """,
            """Function,:,abs,Parameter,:,n,Body,:,If,n,>=,0,Then,Return,n,;,Else,Return,-,n,;,EndIf,.,EndBody,.,Function,:,main,Body,:,Var,:,x,=,5,;,print,(,abs,(,4,*,3,\,2,-,1,),),;,EndBody,.,<EOF>""", 199))
    def test_simple_program_100(self):
        """test simple program with statements"""
        self.assertTrue(TestLexer.checkLexeme(
            """
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
            """,
            """Function,:,abs,Parameter,:,n,Body,:,If,n,>=,0,Then,Return,n,;,Else,Return,-,n,;,EndIf,.,EndBody,.,Function,:,main,Body,:,Var,:,x,=,5,;,print,(,abs,(,True,),),;,EndBody,.,<EOF>""", 200))