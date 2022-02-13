Text_game_module

room(dir1,dir2,dir3,dir4)


dir¤((úvodní text pohledu),(foword),(interact),(use_item)) #je li úvodní text pouze jeden string, udìlejte z nìj tuple tím, že ze nìj nepíšete > , <

foword((výpis možností),((název_možnosti),(room #str#),(dir),((kdy),(vjakém stavu #bool#)),(text)),(--||--)) #není li žádná možnost, napište jen text do výpis možností. musí však zaèínat na !, pokud pak je v tomto pøípadì pouze jeden string, unìlejte z toho tuple tím, že za nìj dáte > , <. je li v možnostech jeden prùchod, ale je šance, že nebude aktivní, napište text pro výpis v takovém pøípadì do výpisu možností

interact((výpis možností),((název_možnosti),(text po vybrání)),((kdy),(vjakém stavu #bool#)),(outome)),(--||--)) #je li text vybrání pouze jeden string, udìlejte z nìj tuple tím, že ze nìj nepíšete > , <

use_item(((název itemu),(text po použití),((kdy),(vjakém stavu #bool#)),(outcome),(item_lost#bool#)),(--||--)) #pokud pouze jeden možný item => napiš za nìj > , <


item_lost(bool)

outcome((item #bool#),(když item => název, zmìní splnìno => (kdy) nebo end1/end2/end3/end4 => ukonèí run() a vyhodí odpovídající hodnotu)

kdy(1/2/3/4/ #pro každou místnost vlastní# /main1/main2/main3/main4 #pro všechny místnosti spoleèné# /always) #vše string



run((všechny rooms), (názvy místností #string#)) #první název je zaèázeèní místnost