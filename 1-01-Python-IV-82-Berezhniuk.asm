.data
	Caption1 db "Andrew Berezhniuk", 0
	buf dw ? 

.code 
otherfunc proc 
	mov eax, 2 
	push eax 
	mov eax, 3 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop eax 
	fn MessageBox, 0, str$(eax), ADDR Caption1, MB_OK 
	ret 
otherfunc endp 
