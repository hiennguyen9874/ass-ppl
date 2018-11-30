.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static foo(I)I
.var 0 is n I from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is sum I from Label0 to Label1
Label0:
	iconst_0
	istore_2
	iconst_0
	istore_1
Label2:
	iload_1
	iload_0
	if_icmpgt Label4
	iload_2
	iload_1
	iadd
	istore_2
Label3:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label4:
	iload_2
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 10
	invokestatic MPClass/foo(I)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
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
