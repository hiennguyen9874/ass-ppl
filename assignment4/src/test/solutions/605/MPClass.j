.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static x [Ljava/lang/String;

.method public static printAString([Ljava/lang/String;)I
.var 0 is x [Ljava/lang/String; from Label0 to Label1
.var 1 is I I from Label0 to Label1
Label0:
.var 2 is i I from Label2 to Label4
Label2:
	iconst_3
	anewarray java/lang/String
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
	aaload
	aastore
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
	aaload
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label5
Label7:
	iconst_1
	goto Label1
Label1:
	ireturn
.limit stack 5
.limit locals 3
.end method

.method public static printAInt([I)I
.var 0 is x [I from Label0 to Label1
.var 1 is I I from Label0 to Label1
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
	iconst_1
	goto Label1
Label1:
	ireturn
.limit stack 5
.limit locals 3
.end method

.method public static printAFloat([F)I
.var 0 is x [F from Label0 to Label1
.var 1 is I I from Label0 to Label1
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
	goto Label1
Label1:
	ireturn
.limit stack 5
.limit locals 3
.end method

.method public static printABoolean([Z)I
.var 0 is x [Z from Label0 to Label1
.var 1 is I I from Label0 to Label1
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
Label0:
.var 2 is x [Z from Label2 to Label3
	iconst_3
	newarray boolean
	astore_2
Label2:
.var 3 is x [I from Label4 to Label5
	iconst_3
	newarray int
	astore_3
Label4:
.var 4 is x [F from Label6 to Label7
	iconst_3
	newarray float
	astore 4
Label6:
	aload 4
	invokestatic MPClass/printAFloat([F)I
	istore_1
Label7:
	aload_3
	invokestatic MPClass/printAInt([I)I
	istore_1
Label5:
	aload_2
	invokestatic MPClass/printABoolean([Z)I
	istore_1
Label3:
	getstatic MPClass/x [Ljava/lang/String;
	invokestatic MPClass/printAString([Ljava/lang/String;)I
	istore_1
Label1:
	return
.limit stack 1
.limit locals 5
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
	anewarray java/lang/String
	putstatic MPClass.x [Ljava/lang/String;
	return
.limit stack 1
.limit locals 0
.end method
