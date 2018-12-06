.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static x [I
.field static j I
.field static i I

.method public static foo(ILjava/lang/String;FZ)V
.var 0 is x I from Label0 to Label1
.var 1 is y Ljava/lang/String; from Label0 to Label1
.var 2 is z F from Label0 to Label1
.var 3 is t Z from Label0 to Label1
Label0:
	iload_3
	ifle Label2
	aload_1
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iload_0
	invokestatic io/putIntLn(I)V
	fload_2
	invokestatic io/putFloatLn(F)V
Label2:
	getstatic MPClass/i I
	iconst_1
	iadd
	putstatic MPClass/i I
	getstatic MPClass/i I
	bipush 110
	if_icmpne Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label5
	goto Label1
	goto Label6
Label5:
	iload_0
	iconst_1
	iadd
	ldc "PPL"
	fload_2
	ldc 1.5
	fadd
	iload_3
	ifgt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	invokestatic MPClass/foo(ILjava/lang/String;FZ)V
Label6:
Label1:
	return
.limit stack 5
.limit locals 4
.end method

.method public static foo1([F[I)V
.var 0 is x [F from Label0 to Label1
.var 1 is y [I from Label0 to Label1
.var 2 is i I from Label0 to Label1
.var 3 is res [F from Label0 to Label1
	bipush 10
	newarray float
	astore_3
Label0:
.var 4 is i I from Label2 to Label4
Label2:
	bipush 10
	newarray float
	iconst_0
	istore 4
Label3:
	iload 4
	bipush 10
	if_icmpge Label4
	dup
	iload 4
	aload_0
	iload 4
	faload
	fastore
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label3
Label4:
	astore_0
.var 5 is i I from Label5 to Label7
Label5:
	bipush 10
	newarray int
	iconst_0
	istore 5
Label6:
	iload 5
	bipush 10
	if_icmpge Label7
	dup
	iload 5
	aload_1
	iload 5
	iaload
	iastore
	iload 5
	iconst_1
	iadd
	istore 5
	goto Label6
Label7:
	astore_1
	iconst_1
	istore_2
Label8:
	iload_2
	bipush 10
	if_icmpgt Label10
	aload_3
	iload_2
	iconst_1
	isub
	aload_0
	iload_2
	iconst_1
	isub
	faload
	aload_1
	iload_2
	iconst_1
	isub
	iaload
	i2f
	fadd
	fastore
Label9:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label8
Label10:
	bipush 10
	istore_2
Label11:
	iload_2
	iconst_1
	if_icmplt Label13
	aload_3
	iload_2
	iconst_1
	isub
	faload
	invokestatic io/putFloatLn(F)V
Label12:
	iload_2
	iconst_1
	isub
	istore_2
	goto Label11
Label13:
Label1:
	return
.limit stack 6
.limit locals 6
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 100
	putstatic MPClass/i I
	bipush 10
	ldc "ppl"
	ldc 1.23
	iconst_1
	invokestatic MPClass/foo(ILjava/lang/String;FZ)V
.var 1 is y [F from Label2 to Label3
	bipush 10
	newarray float
	astore_1
Label2:
	bipush 10
	putstatic MPClass/j I
Label4:
	getstatic MPClass/j I
	iconst_1
	if_icmplt Label6
	getstatic MPClass/x [I
	getstatic MPClass/j I
	iconst_1
	isub
	getstatic MPClass/j I
	getstatic MPClass/j I
	imul
	iastore
	aload_1
	getstatic MPClass/j I
	iconst_1
	isub
	getstatic MPClass/j I
	i2f
	fastore
Label5:
	getstatic MPClass/j I
	iconst_1
	isub
	putstatic MPClass/j I
	goto Label4
Label6:
	aload_1
	getstatic MPClass/x [I
	invokestatic MPClass/foo1([F[I)V
Label3:
Label1:
	return
.limit stack 4
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

.method public static <clinit>()V
	bipush 10
	newarray int
	putstatic MPClass.x [I
	return
.limit stack 1
.limit locals 0
.end method
