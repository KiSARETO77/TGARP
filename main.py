from aminofix.lib.util.exceptions import IpTemporaryBan
from time import sleep as ZZ
from os import system as Z
import aminofix
import samino
#############################################
Z("clear")
C=samino.Client(proxies={"https":"http://dimatjasko10:KWJYs68q@185.112.13.43:2831"})
Ç=aminofix.Client(proxies={"https":"http://dimatjasko10:KWJYs68q@185.112.13.43:2831"})
Ç.login("pb-@digdig.org","GOKU12##")
C.login("pb-@digdig.org","GOKU12##")
S=samino.Local(comId=3434136,proxies={"https":"http://dimatjasko10:KWJYs68q@185.112.13.43:2831"})
Q=0
q=0
p=100
PI=[None,1,"1","None"]
while 1>0:
	M=S.get_online_users(start=q,size=p)
	q+=100
	p+=200
	NN,LL,UU=M.nickname,M.level,M.userId
	for (N,L,U) in zip(NN,LL,UU):
		P=Ç.get_user_info(U).privilegeOfChatInviteRequest
		if P in PI:
			try:
				Q+=1
				Ç.invite_to_chat(chatId="1cddf160-d5b9-4b42-b8f3-6701eb630e3a",userId=U)
				print(f"- {Q} Done invite {N} -{L}")
			except IpTemporaryBan:
				print(f"Wait For 60 Second")
				ZZ(60)
				pass
			except Exception as F:
				print(F)
				pass
