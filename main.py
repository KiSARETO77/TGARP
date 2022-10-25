from aminofix.lib.util.exceptions import IpTemporaryBan
from aminofix import Client,SubClient
from colorama import Fore as K
from pyfiglet import Figlet as X
from time import sleep as ZZ
from os import system as Z
IB=K.BLUE
IG=K.GREEN
IY=K.YELLOW
IR=K.RED
IC=K.CYAN
IM=K.MAGENTA
IRW=K.RESET
IN=X(font='slant')
#############################################
Z("clear")
print(IC,IN.renderText("Invites"))
Ç=Client(proxies={"https":"http://dimatjasko10:KWJYs68q@185.112.13.43:2831"})
C,O=3434136,"1cddf160-d5b9-4b42-b8f3-6701eb630e3a"
q,p,Q=0,100,0
PI=[None,1,"1","None"]
while 1>0:
	Ç.login("pb-@digdig.org","GOKU12##")
	S=SubClient(comId=C,profile=Ç.profile)
	M=S.get_online_users(start=q,size=p).profile
	q+=100
	p+=200
	NN,LL,UU=M.nickname,M.level,M.userId
	#Ç.login("Z-@wwjmp.com","GOKU12")
	for (N,L,U) in zip(NN,LL,UU):
		P=Ç.get_user_info(U).privilegeOfChatInviteRequest
		if P in PI:
			try:
				Q+=1
				#if U not in open("Data/UserIds.txt").read(): open("Data/UserIds.txt","a+").write(f'"{U}"'+"\n"+",")
				Ç.invite_to_chat(chatId=O,userId=U)
				print(f"{IRW} - {IM}{Q} {IG}Done invite {IB}{N} {IRW}- {IY}{L}")
			except IpTemporaryBan:
				print(f"{IR} Wait For 60 Second")
				ZZ(60)
				pass
			except Exception as F:
				#R=F.args[0]["api:message"]
				print(IR,F)
				pass
