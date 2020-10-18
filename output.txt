.data
	Caption1 db "Andrew Berezhniuk", 0
	buf dw ? 

.code 
otherfunc proc 
	mov eax, 10 
	push eax 
	pop eax 
	fn MessageBox, 0, str$(eax), ADDR Caption1, MB_OK 
	ret 
otherfunc endp 
