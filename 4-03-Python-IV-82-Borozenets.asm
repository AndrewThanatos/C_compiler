.data
	Caption1 db "Borozenets D.", 0
	buf dw ? 
	a_1 dword 0, 0 
	a_2 dword 0, 0 
	a_3 dword 0, 0 
	b_4 dword 0, 0 
	c_5 dword 0, 0 
	b_6 dword 0, 0 
	c_7 dword 0, 0 

.code 
otherfunc proc 
	mov eax, 4 
	push eax 
	pop dword ptr [a_1] 
	pop eax 
	push dword ptr [a_1] 
	mov eax, 4 
	push eax 
	pop eax 
	pop ebx 
	cmp ebx, eax 
	mov eax, 1 
	je _true_1 
	mov eax, 0 
 _true_1: 
	push eax 
	pop eax 
	cmp eax, 0 
	jz _else_2 
	mov eax, 10 
	push eax 
	jmp _else_end_2
 _else_2: 
	mov eax, 3 
	push eax 
 _else_end_2: 
	pop dword ptr [a_1] 
	pop eax 
	mov eax, 3 
	push eax 
	pop dword ptr [a_2] 
	pop eax 
	mov eax, 0 
	push eax 
	pop dword ptr [a_3] 
	pop eax 
	mov eax, 0 
	push eax 
	pop dword ptr [b_4] 
	pop eax 
	mov eax, 0 
	push eax 
	pop dword ptr [c_5] 
	pop eax 
	push dword ptr [a_1] 
	mov eax, 4 
	push eax 
	pop eax 
	pop ebx 
	cmp ebx, eax 
	mov eax, 1 
	je _true_3 
	mov eax, 0 
 _true_3: 
	push eax 
	pop eax 
	cmp eax, 0 
	jz _else_4 
	mov eax, 1 
	push eax 
	jmp _else_end_4
 _else_4: 
	mov eax, 100 
	push eax 
 _else_end_4: 
	pop dword ptr [b_6] 
	pop eax 
	push dword ptr [a_1] 
	push dword ptr [b_6] 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	mov eax, 50 
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
	jz _else_6 
	push dword ptr [a_1] 
	jmp _else_end_6
 _else_6: 
	push dword ptr [b_6] 
 _else_end_6: 
	pop dword ptr [c_7] 
	pop eax 
	push dword ptr [a_1] 
	push dword ptr [b_6] 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	push dword ptr [c_7] 
	pop eax 
	pop ebx 
	cmp ebx, eax 
	mov eax, 1 
	je _true_7 
	mov eax, 0 
 _true_7: 
	push eax 
	pop eax 
	cmp eax, 0 
	jz _else_8 
	push dword ptr [a_1] 
	push dword ptr [b_6] 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	push dword ptr [c_7] 
	mov eax, 2 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop ebx 
	pop eax 
	imul eax, ebx 
	push eax 
	jmp _else_end_8
 _else_8: 
	push dword ptr [a_1] 
	push dword ptr [b_6] 
	pop ebx 
	pop eax 
	imul eax, ebx 
	push eax 
	mov eax, 2 
	push eax 
	pop ebx 
	pop eax 
	cdq 
	idiv ebx 
	push eax 
 _else_end_8: 
	jmp _main_end
 _main_end: 
