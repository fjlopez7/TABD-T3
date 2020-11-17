
dictComunas = dict()
candidatos = []
regiones = dict()
with open("data/resultadosMesas.csv", "r", encoding="utf-8") as file:
    file.readline()
    for i,line in enumerate(file):
        comuna = line.strip().split(";")[4].replace("ni","ni")
        if comuna == "":
            continue
        region = line.strip().split(";")[0]  
        if region not in regiones:
            regiones[region] = set()
        regiones[region].add(comuna)
        candidato = line.strip().split(";")[12]
        if candidato not in candidatos:
            candidatos.append(candidato)
        votos = int(line.strip().split(";")[13])
        if comuna not in dictComunas:
            dictComunas[comuna] = dict()
        if candidato not in dictComunas[comuna]:
            dictComunas[comuna][candidato] = 0
        dictComunas[comuna][candidato] += votos
    
        
with open("data/resultadosComuna.csv", "w", encoding="utf-8") as file:
    file.write("comuna,"+",".join(candidatos)+ "\n")
    for comuna in dictComunas:
        file.write(comuna+","+",".join(str(dictComunas[comuna][candidato]) for candidato in candidatos)+ "\n")

a = 0
comu = [
            [1,'Arica',1],
            [2,'Camarones',1],
            [3,'General Lagos',1],
            [4,'Putre',1],
            [5,'Alto Hospicio',2],
            [6,'Iquique',2],
            [7,'Caminia',2],
            [8,'Colchane',2],
            [9,'Huara',2],
            [10,'Pica',2],
            [11,'Pozo Almonte',2],
            [12,'Antofagasta',3],
            [13,'Mejillones',3],
            [14,'Sierra Gorda',3],
            [15,'Taltal',3],
            [16,'Calama',3],
            [17,'Ollague',3],
            [18,'San Pedro de Atacama',3],
            [19,'Maria Elena',3],
            [20,'Tocopilla',3],
            [21,'Chaniaral',4],
            [22,'Diego de Almagro',4],
            [23,'Caldera',4],
            [24,'Copiapo',4],
            [25,'Tierra Amarilla',4],
            [26,'Alto del Carmen',4],
            [27,'Freirina',4],
            [28,'Huasco',4],
            [29,'Vallenar',4],
            [30,'Canela',5],
            [31,'Illapel',5],
            [32,'Los Vilos',5],
            [33,'Salamanca',5],
            [34,'Andacollo',5],
            [35,'Coquimbo',5],
            [36,'La Higuera',5],
            [37,'La Serena',5],
            [38,'Paihuaco',5],
            [39,'Vicunia',5],
            [40,'Combarbala',5],
            [41,'Monte Patria',5],
            [42,'Ovalle',5],
            [43,'Punitaqui',5],
            [44,'Rio Hurtado',5],
            [45,'Isla de Pascua',6],
            [46,'Calle Larga',6],
            [47,'Los Andes',6],
            [48,'Rinconada',6],
            [49,'San Esteban',6],
            [50,'La Ligua',6],
            [51,'Papudo',6],
            [52,'Petorca',6],
            [53,'Zapallar',6],
            [54,'Hijuelas',6],
            [55,'Calera',6],
            [56,'La Cruz',6],
            [57,'Limache',6],
            [58,'Nogales',6],
            [59,'Olmue',6],
            [60,'Quillota',6],
            [61,'Algarrobo',6],
            [62,'Cartagena',6],
            [63,'El Quisco',6],
            [64,'El Tabo',6],
            [65,'San Antonio',6],
            [66,'Santo Domingo',6],
            [67,'Catemu',6],
            [68,'Llaillay',6],
            [69,'Panquehue',6],
            [70,'Putaendo',6],
            [71,'San Felipe',6],
            [72,'Santa Maria',6],
            [73,'Casablanca',6],
            [74,'Concon',6],
            [75,'Juan Fernandez',6],
            [76,'Puchuncavi',6],
            [77,'Quilpue',6],
            [78,'Quintero',6],
            [79,'Valparaiso',6],
            [80,'Villa Alemana',6],
            [81,'Vinia del Mar',6],
            [82,'Colina',7],
            [83,'Lampa',7],
            [84,'Tiltil',7],
            [85,'Pirque',7],
            [86,'Puente Alto',7],
            [87,'San Jose de Maipo',7],
            [88,'Buin',7],
            [89,'Calera de Tango',7],
            [90,'Paine',7],
            [91,'San Bernardo',7],
            [92,'Alhue',7],
            [93,'Curacavi',7],
            [94,'Maria Pinto',7],
            [95,'Melipilla',7],
            [96,'San Pedro',7],
            [97,'Cerrillos',7],
            [98,'Cerro Navia',7],
            [99,'Conchali',7],
            [100,'El Bosque',7],
            [101,'Estacion Central',7],
            [102,'Huechuraba',7],
            [103,'Independencia',7],
            [104,'La Cisterna',7],
            [105,'La Granja',7],
            [106,'La Florida',7],
            [107,'La Pintana',7],
            [108,'La Reina',7],
            [109,'Las Condes',7],
            [110,'Lo Barnechea',7],
            [111,'Lo Espejo',7],
            [112,'Lo Prado',7],
            [113,'Macul',7],
            [114,'Maipu',7],
            [115,'Niunioa',7],
            [116,'Pedro Aguirre Cerda',7],
            [117,'Penialolen',7],
            [118,'Providencia',7],
            [119,'Pudahuel',7],
            [120,'Quilicura',7],
            [121,'Quinta Normal',7],
            [122,'Recoleta',7],
            [123,'Renca',7],
            [124,'San Miguel',7],
            [125,'San Joaquin',7],
            [126,'San Ramon',7],
            [127,'Santiago',7],
            [128,'Vitacura',7],
            [129,'El Monte',7],
            [130,'Isla de Maipo',7],
            [131,'Padre Hurtado',7],
            [132,'Peniaflor',7],
            [133,'Talagante',7],
            [134,'Codegua',8],
            [135,'Coinco',8],
            [136,'Coltauco',8],
            [137,'Doniihue',8],
            [138,'Graneros',8],
            [139,'Las Cabras',8],
            [140,'Machali',8],
            [141,'Malloa',8],
            [142,'Mostazal',8],
            [143,'Olivar',8],
            [144,'Peumo',8],
            [145,'Pichidegua',8],
            [146,'Quinta de Tilcoco',8],
            [147,'Rancagua',8],
            [148,'Rengo',8],
            [149,'Requinoa',8],
            [150,'San Vicente de Tagua Tagua',8],
            [151,'La Estrella',8],
            [152,'Litueche',8],
            [153,'Marchihue',8],
            [154,'Navidad',8],
            [155,'Peredones',8],
            [156,'Pichilemu',8],
            [157,'Chepica',8],
            [158,'Chimbarongo',8],
            [159,'Lolol',8],
            [160,'Nancagua',8],
            [161,'Palmilla',8],
            [162,'Peralillo',8],
            [163,'Placilla',8],
            [164,'Pumanque',8],
            [165,'San Fernando',8],
            [166,'Santa Cruz',8],
            [167,'Cauquenes',9],
            [168,'Chanco',9],
            [169,'Pelluhue',9],
            [170,'Curico',9],
            [171,'Hualanie',9],
            [172,'Licanten',9],
            [173,'Molina',9],
            [174,'Rauco',9],
            [175,'Romeral',9],
            [176,'Sagrada Familia',9],
            [177,'Teno',9],
            [178,'Vichuquen',9],
            [179,'Colbun',9],
            [180,'Linares',9],
            [181,'Longavi',9],
            [182,'Parral',9],
            [183,'Retiro',9],
            [184,'San Javier',9],
            [185,'Villa Alegre',9],
            [186,'Yerbas Buenas',9],
            [187,'Constitucion',9],
            [188,'Curepto',9],
            [189,'Empedrado',9],
            [190,'Maule',9],
            [191,'Pelarco',9],
            [192,'Pencahue',9],
            [193,'Rio Claro',9],
            [194,'San Clemente',9],
            [195,'San Rafael',9],
            [196,'Talca',9],
            [197,'Arauco',10],
            [198,'Caniete',10],
            [199,'Contulmo',10],
            [200,'Curanilahue',10],
            [201,'Lebu',10],
            [202,'Los alamos',10],
            [203,'Tirua',10],
            [204,'Alto Biobio',10],
            [205,'Antuco',10],
            [206,'Cabrero',10],
            [207,'Laja',10],
            [208,'Los angeles',10],
            [209,'Mulchen',10],
            [210,'Nacimiento',10],
            [211,'Negrete',10],
            [212,'Quilaco',10],
            [213,'Quilleco',10],
            [214,'San Rosendo',10],
            [215,'Santa Barbara',10],
            [216,'Tucapel',10],
            [217,'Yumbel',10],
            [218,'Chiguayante',10],
            [219,'Concepcion',10],
            [220,'Coronel',10],
            [221,'Florida',10],
            [222,'Hualpen',10],
            [223,'Hualqui',10],
            [224,'Lota',10],
            [225,'Penco',10],
            [226,'San Pedro de La Paz',10],
            [227,'Santa Juana',10],
            [228,'Talcahuano',10],
            [229,'Tome',10],
            [230,'Bulnes',10],
            [231,'Chillan',10],
            [232,'Chillan Viejo',10],
            [233,'Cobquecura',10],
            [234,'Coelemu',10],
            [235,'Coihueco',10],
            [236,'El Carmen',10],
            [237,'Ninhue',10],
            [238,'Niiquen',10],
            [239,'Pemuco',10],
            [240,'Pinto',10],
            [241,'Portezuelo',10],
            [242,'Quillon',10],
            [243,'Quirihue',10],
            [244,'Ranquil',10],
            [245,'San Carlos',10],
            [246,'San Fabian',10],
            [247,'San Ignacio',10],
            [248,'San Nicolas',10],
            [249,'Treguaco',10],
            [250,'Yungay',10],
            [251,'Carahue',11],
            [252,'Cholchol',11],
            [253,'Cunco',11],
            [254,'Curarrehue',11],
            [255,'Freire',11],
            [256,'Galvarino',11],
            [257,'Gorbea',11],
            [258,'Lautaro',11],
            [259,'Loncoche',11],
            [260,'Melipeuco',11],
            [261,'Nueva Imperial',11],
            [262,'Padre Las Casas',11],
            [263,'Perquenco',11],
            [264,'Pitrufquen',11],
            [265,'Pucon',11],
            [266,'Saavedra',11],
            [267,'Temuco',11],
            [268,'Teodoro Schmidt',11],
            [269,'Tolten',11],
            [270,'Vilcun',11],
            [271,'Villarrica',11],
            [272,'Angol',11],
            [273,'Collipulli',11],
            [274,'Curacautin',11],
            [275,'Ercilla',11],
            [276,'Lonquimay',11],
            [277,'Los Sauces',11],
            [278,'Lumaco',11],
            [279,'Puren',11],
            [280,'Renaico',11],
            [281,'Traiguen',11],
            [282,'Victoria',11],
            [283,'Corral',12],
            [284,'Lanco',12],
            [285,'Los Lagos',12],
            [286,'Mafil',12],
            [287,'Mariquina',12],
            [288,'Paillaco',12],
            [289,'Panguipulli',12],
            [290,'Valdivia',12],
            [291,'Futrono',12],
            [292,'La Union',12],
            [293,'Lago Ranco',12],
            [294,'Rio Bueno',12],
            [295,'Ancud',13],
            [296,'Castro',13],
            [297,'Chonchi',13],
            [298,'Curaco de Velez',13],
            [299,'Dalcahue',13],
            [300,'Puqueldon',13],
            [301,'Queilen',13],
            [302,'Quemchi',13],
            [303,'Quellon',13],
            [304,'Quinchao',13],
            [305,'Calbuco',13],
            [306,'Cochamo',13],
            [307,'Fresia',13],
            [308,'Frutillar',13],
            [309,'Llanquihue',13],
            [310,'Los Muermos',13],
            [311,'Maullin',13],
            [312,'Puerto Montt',13],
            [313,'Puerto Varas',13],
            [314,'Osorno',13],
            [315,'Puero Octay',13],
            [316,'Purranque',13],
            [317,'Puyehue',13],
            [318,'Rio Negro',13],
            [319,'San Juan de la Costa',13],
            [320,'San Pablo',13],
            [321,'Chaiten',13],
            [322,'Futaleufu',13],
            [323,'Hualaihue',13],
            [324,'Palena',13],
            [325,'Aysen',14],
            [326,'Cisnes',14],
            [327,'Guaitecas',14],
            [328,'Cochrane',14],
            [329,'O\'higgins',14],
            [330,'Tortel',14],
            [331,'Coihaique',14],
            [332,'Lago Verde',14],
            [333,'Chile Chico',14],
            [334,'Rio Ibaniez',14],
            [336,'Cabo de Hornos',15],
            [337,'Laguna Blanca',15],
            [338,'Punta Arenas',15],
            [339,'Rio Verde',15],
            [340,'San Gregorio',15],
            [341,'Porvenir',15],
            [342,'Primavera',15],
            [343,'Timaukel',15],
            [344,'Natales',15],
            [345,'Torres del Paine',15],
            [346,'Cabildo',6]
        ]
comu.sort(key= lambda x: x[1])
with open("data/comunas.csv", "w") as file:
    file.write("comuna\n")
    for i in comu:
        file.write(f"{i[1]}\n")
    