# 이 파일에 게임 스크립트를 입력합니다.

image blank = Solid("#000")

# 여기에서부터 게임이 시작합니다.
label start:

    scene blank

    말리 "지금 이 리듬이 좋아. 뜨거운 태양 아래 너와 나."

    $ initializeCity()

label manageCity:
    scene blank
    call screen city
    jump manageCity

    return
