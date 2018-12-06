.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static z [I

.method public static foo1([I)[I
.var 0 is a [I from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
.var 2 is i I from Label2 to Label4
Label2:
	iconst_3
	newarray int
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
	iaload
	iastore
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
	sipush 444
	iastore
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label5
Label7:
	aload_0
	goto Label1
Label1:
	areturn
.limit stack 5
.limit locals 3
.end method

.method public static foo2([F)[F
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
	sipush 555
	i2f
	fastore
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label5
Label7:
	aload_0
	goto Label1
Label1:
	areturn
.limit stack 5
.limit locals 3
.end method

.method public static foo3([Z)[Z
.var 0 is a [Z from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
.var 2 is i I from Label2 to Label4
Label2:
	iconst_3
	newarray boolean
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
	baload
	bastore
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
	iload_1
	iconst_2
	irem
	iconst_0
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	bastore
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label5
Label7:
	aload_0
	goto Label1
Label1:
	areturn
.limit stack 5
.limit locals 3
.end method

.method public static printArrayBoolean([Z)V
.var 0 is a [Z from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
.var 2 is i I from Label2 to Label4
Label2:
	iconst_3
	newarray boolean
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
	baload
	bastore
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
	baload
	invokestatic io/putBoolLn(Z)V
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label5
Label7:
Label1:
	return
.limit stack 5
.limit locals 3
.end method

.method public static printArrayInteger([I)V
.var 0 is a [I from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
.var 2 is i I from Label2 to Label4
Label2:
	iconst_3
	newarray int
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
	iaload
	iastore
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
	iaload
	invokestatic io/putIntLn(I)V
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label5
Label7:
Label1:
	return
.limit stack 5
.limit locals 3
.end method

.method public static printArrayFloat([F)V
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
Label1:
	return
.limit stack 5
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x [F from Label0 to Label1
	iconst_3
	newarray float
	astore_1
.var 2 is i I from Label0 to Label1
Label0:
.var 3 is x [Z from Label2 to Label3
	iconst_3
	newarray boolean
	astore_3
Label2:
	iconst_1
	istore_2
Label4:
	iload_2
	iconst_3
	if_icmpgt Label6
	aload_3
	iload_2
	iconst_1
	isub
	iconst_1
	bastore
Label5:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label6:
	aload_3
	invokestatic MPClass/printArrayBoolean([Z)V
	aload_3
	invokestatic MPClass/foo3([Z)[Z
	invokestatic MPClass/printArrayBoolean([Z)V
Label3:
	iconst_1
	istore_2
Label7:
	iload_2
	iconst_3
	if_icmpgt Label9
	aload_1
	iload_2
	iconst_1
	isub
	ldc 10.0
	fastore
	getstatic MPClass/z [I
	iload_2
	iconst_1
	isub
	bipush 20
	iastore
Label8:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label7
Label9:
	aload_1
	invokestatic MPClass/printArrayFloat([F)V
	aload_1
	invokestatic MPClass/foo2([F)[F
	invokestatic MPClass/printArrayFloat([F)V
	getstatic MPClass/z [I
	invokestatic MPClass/printArrayInteger([I)V
	getstatic MPClass/z [I
	invokestatic MPClass/foo1([I)[I
	invokestatic MPClass/printArrayInteger([I)V
Label1:
	return
.limit stack 3
.limit locals 4
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
	newarray int
	putstatic MPClass.z [I
	return
.limit stack 1
.limit locals 0
.end method
