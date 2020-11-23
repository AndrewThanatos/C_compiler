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
	a_3 dword 0, 0 
	a_5 dword 0, 0 
	b_7 dword 0, 0 
	a_8 dword 0, 0 

.code 
otherfunc proc 
	jmp __main_start 
 __func_start: 
	push dword ptr [a_1] 
	mov eax, 1 
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
	jz _else_1 
	push dword ptr [a_1] 
	mov eax, 1 
	push eax 
	pop eax 
	pop ebx 
	cmp ebx, eax 
	mov eax, 1 
	je _true_2 
	mov eax, 0 
 _true_2: 
	push eax 
	pop eax 
	cmp eax, 0 
	jz _else_2 
	mov eax, 100 
	push eax 
	pop dword ptr [a_1] 
	pop eax 
	jmp _else_end_2
 _else_2: 
	mov eax, 1 
	push eax 
	pop eax 
	mov ebx, -1 
	imul eax, ebx 
	push eax 
	jmp __func_end
 _else_end_2: 
	jmp _else_end_1
 _else_1: 
	mov eax, 1 
	push eax 
	pop eax 
	mov ebx, -1 
	imul eax, ebx 
	push eax 
	jmp __func_end
 _else_end_1: 
	push dword ptr [a_1] 
	jmp __func_end
 __func_end: 
	jmp _resume_

 __two_start: 
	push dword ptr [a_3] 
	mov eax, 53 
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
	jz _else_3 
	push dword ptr [a_3] 
	mov eax, 1 
	push eax 
	pop eax 
	pop ebx 
	cmp ebx, eax 
	mov eax, 1 
	je _true_4 
	mov eax, 0 
 _true_4: 
	push eax 
	pop eax 
	cmp eax, 0 
	jz _else_4 
	mov eax, 100 
	push eax 
	pop dword ptr [a_3] 
	pop eax 
	jmp _else_end_4
 _else_4: 
	mov eax, 1 
	push eax 
	pop eax 
	mov ebx, -1 
	imul eax, ebx 
	push eax 
	jmp __two_end
 _else_end_4: 
	jmp _else_end_3
 _else_3: 
	push dword ptr [a_3] 
	mov eax, 2 
	push eax 
	pop ebx 
	pop eax 
	imul eax, ebx 
	push eax 
	pop dword ptr [a_3] 
	pop eax 
	push dword ptr [a_3] 
	mov eax, 1 
	push eax 
	pop eax 
	pop ebx 
	cmp ebx, eax 
	mov eax, 1 
	je _true_5 
	mov eax, 0 
 _true_5: 
	push eax 
	pop eax 
	cmp eax, 0 
	jz _else_5 
	mov eax, 1000 
	push eax 
	pop dword ptr [a_3] 
	pop eax 
	jmp _else_end_5
 _else_5: 
	push dword ptr [a_3] 
	mov eax, 200 
	push eax 
	pop eax 
	pop ebx 
	cmp ebx, eax 
	mov eax, 1 
	je _true_6 
	mov eax, 0 
 _true_6: 
	push eax 
	pop eax 
	cmp eax, 0 
	jz _else_6 
	push dword ptr [a_3] 
	mov eax, 2 
	push eax 
	pop ebx 
	pop eax 
	imul eax, ebx 
	push eax 
	jmp __two_end
	mov eax, 1 
	push eax 
	pop eax 
	mov ebx, -1 
	imul eax, ebx 
	push eax 
	jmp __two_end
 _else_6: 
 _else_end_5: 
 _else_end_3: 
	mov eax, 1 
	push eax 
	pop eax 
	mov ebx, -1 
	imul eax, ebx 
	push eax 
	jmp __two_end
 __two_end: 
	jmp _resume_

 __sqr_start: 
	push dword ptr [a_5] 
	push dword ptr [a_5] 
	pop ebx 
	pop eax 
	imul eax, ebx 
	push eax 
	jmp __sqr_end
 __sqr_end: 
	jmp _resume_

 __main_start: 
	mov eax, 3 
	push eax 
	pop dword ptr [b_7] 
	pop eax 
	mov eax, 1 
	push eax 
	pop dword ptr [a_1] 
	jmp __func_start
 _resume_0: 
	push dword ptr [func_count] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [func_count] 
	pop dword ptr [a_8] 
	pop eax 
	push dword ptr [a_8] 
	pop dword ptr [a_3] 
	jmp __two_start
 _resume_1: 
	push dword ptr [func_count] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [func_count] 
	push dword ptr [b_7] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [a_5] 
	jmp __sqr_start
 _resume_2: 
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
	add eax, ebx 
	push eax 
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
 _output__: 
	fn MessageBox, 0, str$(eax), ADDR Caption1, MB_OK 
	ret 
otherfunc endp 


main:
	invoke otherfunc
	invoke ExitProcess, 0
end main
