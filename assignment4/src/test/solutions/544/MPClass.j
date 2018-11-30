.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static n I

.method public static foo(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iconst_3
	putstatic MPClass/n I
	iload_0
	invokestatic io/putIntLn(I)V
	iload_1
	invokestatic io/putInt(I)V
	iload_0
	getstatic MPClass/n I
	imul
	iload_1
	iadd
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is n I from Label0 to Label1
Label0:
	iconst_1
	iconst_2
	invokestatic MPClass/foo(II)I
	istore_1
	iload_1
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 2
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
