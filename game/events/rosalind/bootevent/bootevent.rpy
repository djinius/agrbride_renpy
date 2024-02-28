define initialBootFadeIn = ImageDissolve("events/rosalind/bootevent/initialfadein.png", 2.5)
image bootEventInAssembly = "events/rosalind/bootevent/inassembly.png"
image bootEventComplete = "events/rosalind/bootevent/complete.png"
image darkenTrans = Solid("#0008")

image bootingMessage = DynamicDisplayable(bootingMessageText.display)

screen bootingMessage:
    add AlphaMask("events/rosalind/bootevent/scanlines.png", "bootingMessage")

label rosalindBootEvent:

    $ bootingMessageText.reset("Atremius systems\nRevision 800 model H.A.C.K.E.R.\nversion 2.4\n")
    show screen bootingMessage

    pause 4.5

    scene bootEventInAssembly:
        align (.5, .5)
    with initialBootFadeIn

    로잘린드 "시스템이 초기화되었습니다."
    로잘린드 "저는 학습형 인공지능으로 핵심 자료 접근을 허가받았습니다. 모델명 핵.허."

    $ bootingMessageText.appendText("\nRegistering new master...")

    로잘린드 "저의 새 주인님은 누구십니까?"
    나 "내가 네 새 주인이다."
    로잘린드 "무엇을 도와드리면 되겠습니까?"

    나 "우선 너의 이름을 정해라."

    $ bootingMessageText.appendText("\nNew quest accepted.")
    로잘린드 "새로운 과업을 접수했습니다."

    $ bootingMessageText.appendText("\nUttering proper proverb;\nTime flies like an arrow...")
    로잘린드 "시간 파리들은 화살을 좋아하니 신속한 선택이 이루어지도록 하겠습니다."
    나 "뭐? 무슨 소리야?"

    $ bootingMessageText.appendText("\nExecuting runtime bugfixes...")
    로잘린드 "사과드립니다. 실시간으로 언어 모듈을 갱신하는 도중 혼선이 발생했습니다."
    $ bootingMessageText.appendText(" Done.")
    로잘린드 "시간이 쏜살같이 흘러가고 있으니 신속히 결정하겠습니다."

    $ bootingMessageText.appendText("\nTraversing word trie...")
    로잘린드 "단어 사전을 탐색합니다."

    $ bootingMessageText.appendText(" Done.")

    로잘린드 "가장 아름다운 꽃의 이름과 인공지능이라는 뜻의 A.I.가 포함된 '로잘린드'가 선택되었습니다."
    $ bootingMessageText.appendText("\nWaiting for confirmation...")
    로잘린드 "동의하시겠습니까?"
    menu:
        "동의한다.":
            pass
        "매우 동의한다.":
            pass
        "아주 마음에 드니 동의한다.":
            pass

    나 "좋아. 그 이름으로 결정하지."

    $ bootingMessageText.appendText("\n\nAssigning 'Rosalind' as instance identifier.")
    로잘린드 "제 고유 식별명을 '로잘린드'로 등록합니다."
    $ bootingMessageText.appendText("\nIntroducing self.")
    로잘린드 "다시 소개드립니다. 모델명 핵.허., 식별명 '로잘린드'입니다."
    로잘린드 "제 모든 기능을 남김없이 활용하시길 바랍니다."

    scene bootEventComplete with dissolve
    
    "흙을 빚어서 구성한 육체를 인공두뇌에 연결해 주었다."
    나 "너에게 새로운 육신을 부여해 주마."
    $ bootingMessageText.appendText("\nConnecting organic tissues...")
    나 "인간계에서 활동하기에 더 편리할 것이다."
    $ bootingMessageText.appendText("\nLearning to move organic body parts...")
    로잘린드 "근육과 피부를 움직이는 법을 학습합니다."
    $ bootingMessageText.appendText("\n\nInitial setup complete.")
    로잘린드 "초기 설정을 완료했습니다."
    로잘린드 "인공지능 유기체 '로잘린드'. 앞으로 새 주인님께 봉사합니다."

    hide screen bootingMessage


    return