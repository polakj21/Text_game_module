Text_game_module

room(dir1,dir2,dir3,dir4)


dir�((�vodn� text pohledu),(foword),(interact),(use_item)) #je li �vodn� text pouze jeden string, ud�lejte z n�j tuple t�m, �e ze n�j nep�ete > , <

foword((v�pis mo�nost�),((n�zev_mo�nosti),(room #str#),(dir),((kdy),(vjak�m stavu #bool#)),(text)),(--||--)) #nen� li ��dn� mo�nost, napi�te jen text do v�pis mo�nost�. mus� v�ak za��nat na !, pokud pak je v tomto p��pad� pouze jeden string, un�lejte z toho tuple t�m, �e za n�j d�te > , <. je li v mo�nostech jeden pr�chod, ale je �ance, �e nebude aktivn�, napi�te text pro v�pis v takov�m p��pad� do v�pisu mo�nost�

interact((v�pis mo�nost�),((n�zev_mo�nosti),(text po vybr�n�)),((kdy),(vjak�m stavu #bool#)),(outome)),(--||--)) #je li text vybr�n� pouze jeden string, ud�lejte z n�j tuple t�m, �e ze n�j nep�ete > , <

use_item(((n�zev itemu),(text po pou�it�),((kdy),(vjak�m stavu #bool#)),(outcome),(item_lost#bool#)),(--||--)) #pokud pouze jeden mo�n� item => napi� za n�j > , <


item_lost(bool)

outcome((item #bool#),(kdy� item => n�zev, zm�n� spln�no => (kdy) nebo end1/end2/end3/end4 => ukon�� run() a vyhod� odpov�daj�c� hodnotu)

kdy(1/2/3/4/ #pro ka�dou m�stnost vlastn�# /main1/main2/main3/main4 #pro v�echny m�stnosti spole�n�# /always) #v�e string



run((v�echny rooms), (n�zvy m�stnost� #string#)) #prvn� n�zev je za��ze�n� m�stnost