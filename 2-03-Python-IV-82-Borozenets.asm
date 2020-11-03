.data
	Caption1 db "Borozenets", 0
	buf dw ? 

.code 
otherfunc proc 
	mov eax, 25 
	push eax 
	mov eax, 7 
	push eax 
	mov eax, 2 
	push eax 
	pop ebx 
	pop eax 
	sub eax, ebx 
	push eax 
	pop ebx 
	pop eax 
	cdq 
	idiv ebx 
	push eax 
	pop eax 
	fn MessageBox, 0, str$(eax), ADDR Caption1, MB_OK 
	ret 
otherfunc endp 
