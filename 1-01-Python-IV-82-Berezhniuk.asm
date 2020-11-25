.586
.model flat, stdcall

option casemap: none

include \masm32\include\kernel32.inc
include \masm32\include\user32.inc
include \masm32\include\windows.inc
include \masm32\include\masm32rt.inc

includelib \masm32\lib\kernel32.lib
includelib \masm32\lib\user32.lib


.data
	Caption1 db "Andrew Berezhniuk", 0
	buf dw ? 
	func_count dword 0, 0 
	a_1 dword 0, 0 
	b_2 dword 0, 0 
	a_4 dword 0, 0 
	b_5 dword 0, 0 
	a_7 dword 0, 0 
	b_8 dword 0, 0 
	c_9 dword 0, 0 
	i_10 dword 0, 0 
	j_11 dword 0, 0 
	a_13 dword 0, 0 
	a_15 dword 0, 0 
	b_16 dword 0, 0 
	a_18 dword 0, 0 
	b_19 dword 0, 0 
	a_21 dword 0, 0 
	b_22 dword 0, 0 
	a_24 dword 0, 0 
	b_25 dword 0, 0 
	a_27 dword 0, 0 
	b_28 dword 0, 0 
	c_29 dword 0, 0 
	d_30 dword 0, 0 
	i_31 dword 0, 0 

.code 
otherfunc proc 
	jmp __main_start 
 __max_start: 
	push dword ptr [a_1] 
	push dword ptr [b_2] 
	pop eax 
	pop ebx 
	cmp ebx, eax 
	mov eax, 1 
	jg _true_1 
	mov eax, 0 
 _true_1: 
	push eax 
	pop eax 
	cmp eax, 0 
	jz _else_1 
	push dword ptr [a_1] 
	jmp __max_end
	jmp _else_end_1
 _else_1: 
	push dword ptr [b_2] 
	jmp __max_end
 _else_end_1: 
 __max_end: 
	jmp _resume_

 __min_start: 
	push dword ptr [a_4] 
	push dword ptr [b_5] 
	pop eax 
	pop ebx 
	cmp ebx, eax 
	mov eax, 1 
	jl _true_2 
	mov eax, 0 
 _true_2: 
	push eax 
	pop eax 
	cmp eax, 0 
	jz _else_2 
	push dword ptr [a_4] 
	jmp __min_end
	jmp _else_end_2
 _else_2: 
	push dword ptr [b_5] 
	jmp __min_end
 _else_end_2: 
 __min_end: 
	jmp _resume_

 __func_start: 
	mov eax, 0 
	push eax 
	pop dword ptr [i_10] 
 _loop_condition_3: 
	push dword ptr [i_10] 
	mov eax, 5 
	push eax 
	pop eax 
	pop ebx 
	cmp ebx, eax 
	mov eax, 1 
	jl _true_3 
	mov eax, 0 
 _true_3: 
	push eax 
	pop eax 
	cmp eax, 0 
	jz _loop_end_3 
	mov eax, 5 
	push eax 
	pop dword ptr [j_11] 
 _loop_condition_4: 
	push dword ptr [j_11] 
	mov eax, 0 
	push eax 
	pop eax 
	pop ebx 
	cmp ebx, eax 
	mov eax, 1 
	jg _true_4 
	mov eax, 0 
 _true_4: 
	push eax 
	pop eax 
	cmp eax, 0 
	jz _loop_end_4 
	push dword ptr [a_7] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [a_7] 
	push dword ptr [j_11] 
	mov eax, 2 
	push eax 
	pop ebx 
	pop eax 
	sub eax, ebx 
	push eax 
	pop dword ptr [j_11] 
	jmp _loop_condition_4
 _loop_end_4: 
	push dword ptr [i_10] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [i_10] 
	jmp _loop_condition_3
 _loop_end_3: 
	push dword ptr [a_7] 
	push dword ptr [b_8] 
	push dword ptr [c_9] 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	jmp __func_end
 __func_end: 
	jmp _resume_

 __sqr_start: 
	push dword ptr [a_13] 
	push dword ptr [a_13] 
	pop ebx 
	pop eax 
	imul eax, ebx 
	push eax 
	jmp __sqr_end
 __sqr_end: 
	jmp _resume_

 __sum_start: 
	push dword ptr [a_15] 
	push dword ptr [b_16] 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	jmp __sum_end
 __sum_end: 
	jmp _resume_

 __mul_start: 
	push dword ptr [a_18] 
	push dword ptr [b_19] 
	pop ebx 
	pop eax 
	imul eax, ebx 
	push eax 
	jmp __mul_end
 __mul_end: 
	jmp _resume_

 __divv_start: 
	push dword ptr [a_21] 
	push dword ptr [b_22] 
	pop ebx 
	pop eax 
	cdq 
	idiv ebx 
	push eax 
	jmp __divv_end
 __divv_end: 
	jmp _resume_

 __sub_start: 
	push dword ptr [a_24] 
	push dword ptr [b_25] 
	pop ebx 
	pop eax 
	sub eax, ebx 
	push eax 
	jmp __sub_end
 __sub_end: 
	jmp _resume_

 __main_start: 
	mov eax, 25 
	push eax 
	pop dword ptr [a_27] 
	push dword ptr [a_27] 
	pop dword ptr [a_15] 
	mov eax, 5 
	push eax 
	pop dword ptr [b_16] 
	jmp __sum_start
 _resume_0: 
	push dword ptr [func_count] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [func_count] 
	pop dword ptr [b_28] 
	push dword ptr [a_27] 
	pop dword ptr [a_1] 
	push dword ptr [b_28] 
	pop dword ptr [b_2] 
	jmp __max_start
 _resume_1: 
	push dword ptr [func_count] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [func_count] 
	pop dword ptr [a_18] 
	mov eax, 2 
	push eax 
	pop dword ptr [b_19] 
	jmp __mul_start
 _resume_2: 
	push dword ptr [func_count] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [func_count] 
	pop dword ptr [c_29] 
	push dword ptr [a_27] 
	pop dword ptr [a_24] 
	push dword ptr [c_29] 
	pop dword ptr [b_25] 
	jmp __sub_start
 _resume_3: 
	push dword ptr [func_count] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [func_count] 
	pop dword ptr [a_21] 
	mov eax, 5 
	push eax 
	pop dword ptr [b_22] 
	jmp __divv_start
 _resume_4: 
	push dword ptr [func_count] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [func_count] 
	pop dword ptr [d_30] 
	push dword ptr [a_27] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [a_27] 
	push dword ptr [b_28] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	sub eax, ebx 
	push eax 
	pop dword ptr [b_28] 
	push dword ptr [c_29] 
	mov eax, 2 
	push eax 
	pop ebx 
	pop eax 
	imul eax, ebx 
	push eax 
	pop dword ptr [c_29] 
	push dword ptr [d_30] 
	mov eax, 2 
	push eax 
	pop ebx 
	pop eax 
	cdq 
	idiv ebx 
	push eax 
	pop dword ptr [d_30] 
	push dword ptr [a_27] 
	push dword ptr [a_27] 
	mov eax, 3 
	push eax 
	pop ebx 
	pop eax 
	imul eax, ebx 
	push eax 
	pop dword ptr [a_4] 
	push dword ptr [d_30] 
	pop dword ptr [b_5] 
	jmp __min_start
 _resume_5: 
	push dword ptr [func_count] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [func_count] 
	pop ebx 
	pop eax 
	imul eax, ebx 
	push eax 
	pop dword ptr [a_27] 
 _loop_condition_5: 
	push dword ptr [a_27] 
	mov eax, 100 
	push eax 
	pop eax 
	pop ebx 
	cmp ebx, eax 
	mov eax, 1 
	jl _true_5 
	mov eax, 0 
 _true_5: 
	push eax 
	pop eax 
	cmp eax, 0 
	jz _loop_end_5 
	push dword ptr [a_27] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [a_27] 
	push dword ptr [b_28] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	sub eax, ebx 
	push eax 
	pop dword ptr [b_28] 
	jmp _loop_condition_5
 _loop_end_5: 
	mov eax, 0 
	push eax 
	pop dword ptr [i_31] 
 _loop_condition_6: 
	push dword ptr [i_31] 
	mov eax, 10 
	push eax 
	pop eax 
	pop ebx 
	cmp ebx, eax 
	mov eax, 1 
	jl _true_6 
	mov eax, 0 
 _true_6: 
	push eax 
	pop eax 
	cmp eax, 0 
	jz _loop_end_6 
	push dword ptr [a_27] 
	mov eax, 2 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [a_27] 
	push dword ptr [i_31] 
	mov eax, 2 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [i_31] 
	jmp _loop_condition_6
 _loop_end_6: 
	push dword ptr [a_27] 
	pop dword ptr [a_7] 
	push dword ptr [b_28] 
	pop dword ptr [b_8] 
	push dword ptr [c_29] 
	push dword ptr [b_28] 
	pop ebx 
	pop eax 
	cdq 
	idiv ebx 
	push eax 
	pop dword ptr [a_13] 
	jmp __sqr_start
 _resume_6: 
	push dword ptr [func_count] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [func_count] 
	pop dword ptr [c_9] 
	jmp __func_start
 _resume_7: 
	push dword ptr [func_count] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [func_count] 
	jmp __main_end
 __main_end: 

	pop eax 
	jmp _output__ 

 _resume_: 
	push dword ptr [func_count]
	pop eax 
	cmp eax, 0 
	jz _resume_0 
	push dword ptr [func_count]
	pop eax 
	cmp eax, 1 
	jz _resume_1 
	push dword ptr [func_count]
	pop eax 
	cmp eax, 2 
	jz _resume_2 
	push dword ptr [func_count]
	pop eax 
	cmp eax, 3 
	jz _resume_3 
	push dword ptr [func_count]
	pop eax 
	cmp eax, 4 
	jz _resume_4 
	push dword ptr [func_count]
	pop eax 
	cmp eax, 5 
	jz _resume_5 
	push dword ptr [func_count]
	pop eax 
	cmp eax, 6 
	jz _resume_6 
	push dword ptr [func_count]
	pop eax 
	cmp eax, 7 
	jz _resume_7 
 _output__: 
	fn MessageBox, 0, str$(eax), ADDR Caption1, MB_OK 
	ret 
otherfunc endp 


main:
	invoke otherfunc
	invoke ExitProcess, 0
end main
