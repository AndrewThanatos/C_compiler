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
	Caption1 db "Result", 0
	buf dw ? 
	func_count dword 0, 0 
	a_1 dword 0, 0 

.code 
mainfunc proc 
	jmp __main_start 
 __main_start: 
	mov eax, 25 
	push eax 
	pop dword ptr [a_1] 
	push dword ptr [a_1] 
	pop eax 
	mov ebx, -1 
	imul eax, ebx 
	mov ebx, 1
	sub eax, ebx 
	push eax
	mov eax, 2 
	push eax 
	pop ebx 
	pop eax 
	imul eax, ebx 
	push eax 
	mov eax, 3 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	jmp __main_end
 __main_end: 

	pop eax 
	jmp _output__ 

 _resume_: 
 _output__: 
	fn MessageBox, 0, str$(eax), ADDR Caption1, MB_OK 
	ret 
mainfunc endp 


main:
	invoke mainfunc
	invoke ExitProcess, 0
end main
