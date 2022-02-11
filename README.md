Text_game_module

room(dir1,dir2,dir3,dir4)


dir¤((úvodní text pohledu),(foword),(interact),(use_item))

foword((výpis možností),((název_možnosti),(room),(dir),((kdy),(vjakém stavu #bool#)),(text)),(--||--)) #pokud jen jedna možnost, nepsat výpis možností - není li žádná možnost, napište jen text do výpis možností. musí však zaèínat na !

interact((výpis možností),((název_možnosti),(text po vybrání)),((kdy),(vjakém stavu #bool#)),(outome)),(--||--)) #pokud jen jedna možnost, nepsat výpis možností

use_item(((název itemu),(text po použití),((kdy),(vjakém stavu #bool#)),(outcome),(item_lost)),(--||--))


item_lost(bool)

outcome((item #bool#),(když item => název, zmìní splnìno => (kdy))

kdy(1/2/3/4/ #pro každou místnost vlastní# /main1/main2/main3/main4 #pro všechny místnosti spoleèné# /always) #vše string