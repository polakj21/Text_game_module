Text_game_module

room(dir1,dir2,dir3,dir4)


dir�((�vodn� text pohledu),(foword),(interact),(use_item))

foword((v�pis mo�nost�),((n�zev_mo�nosti),(room),(dir),((kdy),(vjak�m stavu #bool#)),(text)),(--||--)) #pokud jen jedna mo�nost, nepsat v�pis mo�nost� - nen� li ��dn� mo�nost, napi�te jen text do v�pis mo�nost�. mus� v�ak za��nat na !

interact((v�pis mo�nost�),((n�zev_mo�nosti),(text po vybr�n�)),((kdy),(vjak�m stavu #bool#)),(outome)),(--||--)) #pokud jen jedna mo�nost, nepsat v�pis mo�nost�

use_item(((n�zev itemu),(text po pou�it�),((kdy),(vjak�m stavu #bool#)),(outcome),(item_lost)),(--||--))


item_lost(bool)

outcome((item #bool#),(kdy� item => n�zev, zm�n� spln�no => (kdy))

kdy(1/2/3/4/ #pro ka�dou m�stnost vlastn�# /main1/main2/main3/main4 #pro v�echny m�stnosti spole�n�# /always) #v�e string