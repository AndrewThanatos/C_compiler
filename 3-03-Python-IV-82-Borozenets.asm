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
	Caption1 db "Borozenets D.", 0
	buf dw ? 
	a_1 dword 0, 0 

.code 
otherfunc proc 
	mov eax, 122 
	push eax 
	pop dword ptr [a_1] 
	pop eax 
	push dword ptr [a_1] 
	jmp _main_end
 _main_end: 
	pop eax 
	fn MessageBox, 0, str$(eax), ADDR Caption1, MB_OK 
	ret 
otherfunc endp 


main:
	invoke otherfunc
	invoke ExitProcess, 0
end main
