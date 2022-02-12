import TeGaMo

R1 = TeGaMo.room((("pohled1","pohled1"),
                  ("!nikam nejdeš",),
                  ((),((),("interagoval jsi v pohledu 1",),("always", True),((False),((),("always"))))),
                  ((("párek"),("použil jsi párek",":?:"),(("always"),True),((False),((),("always"))),(False)))
                  ),
                 
                 (("pohled2"),
                  ("!nikam nejdeš",),
                  ((),((),("interagoval jsi v pohledu 2",),("always", True),((False),((),("always"))))),
                  ()
                  ),
                 
                 (("pohled3"),
                  ((("mtext?"),("R2"),(3),("always",True),("rozléhá se před tebou majestátní room2"))),
                  ((),((),("interagoval jsi v pohledu 3",),("always", True),((False),((),("always"))))),
                  ()
                  ),
                 
                 (("pohled4","?"),
                  ("!nikam nejdeš",),
                  (("vyber si"),(("1"),("interagoval jsi v pohledu 1",),("always", True),((False),((),("always")))),(("párek"),("našel jsi párek!§",),("1", False),((True),(("párek"),("1"))))),
                  ()
                  )
                 )

R2 = TeGaMo.room((("vidíš ?"),
                  (((),("R1"),(2),("main1",True),("vešel jsi do majestátní R1...","nějak"))),
                  ((),((),("jsi špatný",),("always",True),(False,((),("main1"))))),
                  ()
                  ),
                 
                 (("vidíš  ?"),
                  ("!nikam nejdeš",),
                  ((),(("text"),("text po vybrání",),("always", True),(True,("kvetoucí katkus","always")))),
                  ()
                  ),
                 
                 (("vidíš   ?"),
                  ("!nikam nejdeš",),
                  ((),((),("pohled 3?",),("always",True),(False,((),"always")))),
                  ()
                  ),
                 
                 (("vidíš    ?"),
                  ("!nikam nejdeš",),
                  ((),((),("pohled 4?",),("always",True),(False,((),"always")))),
                  ()
                  )
                 )

TeGaMo.run((R1,R2),("R1","R2"))
