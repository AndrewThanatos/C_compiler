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
	a_1 dword 0, 0 
	b_2 dword 0, 0 
	a_4 dword 0, 0 
	b_5 dword 0, 0 

.code 
otherfunc proc 
	mov eax, 1 
	push eax 
	pop dword ptr [a_4] 
	mov eax, 2 
	push eax 
	pop dword ptr [b_5] 
	pop dword ptr [a_1] 
	mov eax, 3 
	push eax 
	pop dword ptr [b_2] 
	push dword ptr [a_1] 
	push dword ptr [b_2] 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop eax 
	fn MessageBox, 0, str$(eax), ADDR Caption1, MB_OK 
	ret 
otherfunc endp 


main:
	invoke otherfunc
	invoke ExitProcess, 0
end main