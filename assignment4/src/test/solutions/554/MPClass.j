.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static mean(I)F
.var 0 is size I from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is s I from Label0 to Label1
.var 3 is x [I from Label0 to Label1
	iconst_3
	newarray int
	astore_3
Label0:
	aload_3
	iconst_3
	iconst_1
	isub
	iconst_1
	iastore
	aload_3
	iconst_1
	iconst_1
	isub
	iconst_3
	iastore
	aload_3
	iconst_2
	iconst_1
	isub
	iconst_5
	iastore
	iconst_0
	istore_2
	iconst_1
	istore_1
Label2:
	iload_1
	iload_0
	if_icmpgt Label4
	iload_2
	aload_3
	iload_1
	iconst_1
	isub
	iaload
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
	i2f
	fconst_0
	fadd
	iload_0
	i2f
	fdiv
	goto Label1
Label1:
	freturn
.limit stack 4
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	invokestatic MPClass/mean(I)F
	invokestatic io/putFloat(F)V
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
