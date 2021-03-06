# Script para salvar as posições iniciais dos personagens, inimigos e elementos do cenário de cada fase
# As informações são salvas no arquivo "dados.txt"

inimigo_esperto = [(95, 815)]
player = (65, 35)
end_phase = (810, 25)
inimigo_aleatorio = [(155, 245), (35, 455), (815, 515), (515, 785), (755, 35), (395, 65)]
bullets = [(300, 840), (330, 690), (60, 900), (300, 360), (300, 150), (60, 150), (300, 60), (810, 210), (720, 510), (780, 660), (480, 330)]
bullets2 = [(120, 250), (30, 360), (240, 510), (90, 660), (390, 815), (390, 460), (540, 150), (695, 31), (815, 360), (635, 665), (630, 330), (160, 35)]

Fase1 = {
    'phase': 1,
    'player': player,
    'end_phase': end_phase,
    'inimigo_esperto': inimigo_esperto,
    'inimigo_aleatorio': inimigo_aleatorio,
    'bullets': bullets,
    'bullets2': bullets2
}

inimigo_esperto = [(332, 196)]
player = (33, 80)
end_phase = (585, 490)
inimigo_aleatorio = [(95, 140), (500, 190), (770, 350), (1000, 160), (1000, 520), (100, 845), (515, 655)]
bullets = [(310, 380), (30, 845), (890, 585), (680, 265), (325, 205), (660, 815), (945, 30)]
bullets2 = [(30, 40), (90, 320), (35, 645), (240, 550), (240, 320), (300, 115), (530, 65), (795, 155), (500, 270),
            (350, 495), (532, 815), (790, 700), (1055, 815), (1145, 580), (1000, 250), (1145, 35), (1175, 385)]

Fase2 = {
    'phase': 2,
    'player': player,
    'end_phase': end_phase,
    'inimigo_esperto': inimigo_esperto,
    'inimigo_aleatorio': inimigo_aleatorio,
    'bullets': bullets,
    'bullets2': bullets2
}

inimigo_esperto = [(155, 365)]
player = (65, 65)
end_phase = (85, 1345)
inimigo_aleatorio = [(65, 665), (605, 455), (695, 95), (1115, 215), (1385, 515), (425, 665), (335, 995), (275, 1325), (785, 1385), (1085, 1055)]
bullets = [(750, 95), (1080, 215), (1380, 485), (480, 665), (150, 365), (60, 665), (270, 995), (270, 1175), (900, 1205), (930, 875), (1380,695), (660, 455)]
bullets2 = [(155, 175), (455, 95), (485, 270), (335, 555), (215, 755), (120, 1070), (690, 1175), (540, 900), (600, 665), (845, 445),
            (965, 325), (1345, 125), (1295, 665), (1055, 875), (1205, 1050), (1240, 1390), (60, 460), (460, 995), (930, 665), (1385, 1175)]

Fase3 = {
    'phase': 3,
    'player': player,
    'end_phase': end_phase,
    'inimigo_esperto': inimigo_esperto,
    'inimigo_aleatorio': inimigo_aleatorio,
    'bullets': bullets,
    'bullets2': bullets2
}

dados = [Fase1, Fase2, Fase3]
arquivo = open('dados.txt', 'w')
arquivo.write(str(dados))
arquivo.close()
