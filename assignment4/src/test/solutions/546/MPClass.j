.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static foo(IIF)V
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is c F from Label0 to Label1
.var 3 is i I from Label0 to Label1
.var 4 is i1 I from Label0 to Label1
.var 5 is f F from Label0 to Label1
.var 6 is f1 F from Label0 to Label1
.var 7 is b Z from Label0 to Label1
.var 8 is b1 Z from Label0 to Label1
Label0:
	iconst_1
	iconst_2
	if_icmpeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	istore 7
	iload 7
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 2
.limit locals 9
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	iconst_2
	ldc 4.3
	invokestatic MPClass/foo(IIF)V
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LMPClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
