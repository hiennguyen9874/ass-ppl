.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static x [F

.method public static foo([F)Z
.var 0 is a [F from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
.var 2 is i I from Label2 to Label4
Label2:
	iconst_3
	newarray float
	iconst_0
	istore_2
Label3:
	iload_2
	iconst_3
	if_icmpge Label4
	dup
	iload_2
	aload_0
	iload_2
	faload
	fastore
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label3
Label4:
	astore_0
	iconst_1
	istore_1
Label5:
	iload_1
	iconst_3
	if_icmpgt Label7
	aload_0
	iload_1
	iconst_1
	isub
	faload
	invokestatic io/putFloatLn(F)V
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label5
Label7:
	iconst_1
	istore_1
Label8:
	iload_1
	iconst_3
	if_icmpgt Label10
	aload_0
	iload_1
	iconst_1
	isub
	sipush 444
	i2f
	fastore
Label9:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label8
Label10:
	iconst_1
	istore_1
Label11:
	iload_1
	iconst_3
	if_icmpgt Label13
	aload_0
	iload_1
	iconst_1
	isub
	faload
	invokestatic io/putFloatLn(F)V
Label12:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label11
Label13:
	iconst_1
	goto Label1
Label1:
	ireturn
.limit stack 5
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is z Z from Label0 to Label1
Label0:
	iconst_1
	istore_1
Label2:
	iload_1
	iconst_3
	if_icmpgt Label4
	getstatic MPClass/x [F
	iload_1
	iconst_1
	isub
	bipush 10
	i2f
	fastore
Label3:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label4:
	iconst_1
	istore_1
Label5:
	iload_1
	iconst_3
	if_icmpgt Label7
	getstatic MPClass/x [F
	iload_1
	iconst_1
	isub
	faload
	invokestatic io/putFloatLn(F)V
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label5
Label7:
	getstatic MPClass/x [F
	invokestatic MPClass/foo([F)Z
	istore_2
	iconst_1
	istore_1
Label8:
	iload_1
	iconst_3
	if_icmpgt Label10
	getstatic MPClass/x [F
	iload_1
	iconst_1
	isub
	faload
	invokestatic io/putFloatLn(F)V
Label9:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label8
Label10:
Label1:
	return
.limit stack 3
.limit locals 3
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

.method public static <clinit>()V
	iconst_3
	newarray float
	putstatic MPClass.x [F
	return
.limit stack 1
.limit locals 0
.end method
