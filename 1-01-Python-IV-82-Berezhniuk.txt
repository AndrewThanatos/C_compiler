.data
	Caption1 db "Andrew Berezhniuk", 0
	buf dw ? 
	a dword 0, 0 

.code 
otherfunc proc 
	push dword ptr [a] 
	pop eax 
	push dword ptr [a] 
	pop eax 
	fn MessageBox, 0, str$(eax), ADDR Caption1, MB_OK 
	ret 
otherfunc endp 
