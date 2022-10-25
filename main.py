from aminofix.lib.util.exceptions import IpTemporaryBan
from aminofix import Client,SubClient
from samino import Client,Local
from time import sleep as ZZ
from os import system as Z
#############################################
Z("clear")
Ç=Client(proxies={"https":"http://dimatjasko10:KWJYs68q@185.112.13.43:2831"})
C,O=3434136,"1cddf160-d5b9-4b42-b8f3-6701eb630e3a"
q,p,Q=0,100,0
PI=[None,1,"1","None"]
while 1>0:
	Ç.login("pb-@digdig.org","GOKU12##")
	S=Local(comId=C,proxies={"https":"http://dimatjasko10:KWJYs68q@185.112.13.43:2831"})
	M=S.get_online_users(start=q,size=p)
	q+=100
	p+=200
	NN,LL,UU=M.nickname,M.level,M.userId
	for (N,L,U) in zip(NN,LL,UU):
		P=Ç.get_user_info(U).privilegeOfChatInviteRequest
		if P in PI:
			try:
				Q+=1
				S=Local(comId=0,proxies={"https":"http://dimatjasko10:KWJYs68q@185.112.13.43:2831"})
				S.invite_to_chat(chatId=O,userId=U)
				print(f"- {Q} Done invite {N} -{L}")
			except IpTemporaryBan:
				print(f"Wait For 60 Second")
				ZZ(60)
				pass
			except Exception as F:
				print(F)
				pass
