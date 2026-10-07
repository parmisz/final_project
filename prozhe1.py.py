





import random

fal_hafez=["be jahan khoram az aanam ke jahan khorram az oost","yousef gom gashte baz ayaad be kanaan gham makhor", "resid mozhde ke ayyam gham nakhahad maand"]
fal_eshgh=["be zoodi yek etefagh asheghane dar entezar ast","kasi be to fekr mikonad ","yek khabar khoob khahi shenid"]
fal_shans=["yek forsat khoob be zoodi sare rahet gharar migirad","ba talash bbe chizi ke mikhahi miresi","in roozha shans ba to yar ast"]
while True:
    print("faal tasadofi")
    print("1.faal hafez")
    print("2.faal eshgh")
    print("3.faal shans")
    print("4.exit")
    entekhab = input("moozo faal ra entekhab konid:")
    match entekhab:
        case "1":
            print("faale shoma:")
            print(random.choice(fal_hafez))
        case "2":
            print("faale shoma:")
            print(random.choice(fal_eshgh))
        case "3":
            print("faale shoma:")
            print(random.choice(fal_shans))
        case "4":
            print("barname tamoom shod")
            break
        case _:
            print("entekhab na motabar ast")
