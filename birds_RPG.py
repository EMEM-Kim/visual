# "새" RPG프로그램
# "새"의 종류는 앵무새, 참새, 비둘기, 닭, 러버덕(오리인형)이 존재함
# 각 새는 다른 종류의 울음소리를 가지고 있다.

birds = {
    "앵무새": {
        "cry": "까악",
        "fly": "날개를 힘차게",
        "distance": 2
    },
    "참새": {
        "cry": "짹짹",
        "fly": "날개를 빠르게",
        "distance": 8
    },
    "비둘기": {
        "cry": "구구",
        "fly": "날개를 부드럽게",
        "distance": 12
    },
    "닭": {
        "cry": "꼬끼오",
        "fly": "날개를 퍼덕이며",
        "distance": 1
    },
    "러버덕": {
        "cry": "삑삑삑",
        "fly": "날지 못함",
        "distance": 0
    }
}

birds_name = input()

if birds_name in birds:
    bird = birds[birds_name]
    print(f"{birds_name} 출발!!!")
    print(bird['cry'])

    if bird["distance"] == 0:
        print(f"{birds_name}은 날지 못합니다.")
    else:
        print(f"{bird['fly']} 날았습니다.")

        print(f"결과는 {bird['distance']}m 입니다.")
