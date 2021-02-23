> 실용주의 프로그래머

# 저자가 말하는 실용주의란?
특정 기술에 얽매이지 않고, 
상황마다 좋은 해결방안을 고를 수 있는 배경지식과 경험을 가지는 것이다.

# 1. 실용주의 철학
Tip 1. 자신의 기술craft에 관심과 애정을 가져라
Tip 2. 자신의 일에 대해 생각하면서 일하라
Tip 3. 어설픈 변명을 만들지 말고 대안을 제시하라
Tip 4. 깨진 창문을 내버려두지 말라
Tip 5. 변화의 촉매가 되라
Tip 6. 큰 그림을 기억하라
Tip 7. 품질을 요구사항으로 만들어라
Tip 8. 지식 포트폴리오에 주기적으로 투자하라
Tip 9. 읽고 듣는 것을 비판적으로 분석하라
Tip 10. 무엇을 말하는가와 어떻게 말하는가 모두 중요하다

# 2. 실용주의 접근법
Tip 11. DRY - 반복하지 마라 Don't Repeat Yourself
```
class Line {
    public:
        Point start;
        Point end;
        double length;
};

class Line {
    private:
        bool changed;
        double length;
        Point start;
        Point end;
    public:
        void setStart(Point P) {start = p; chnaged=true;}
        void setEnd(Point P) {end = p; chnaged=true;}
        Point getStart(void) {return start;}
        Point getEnt(void) {return end;}
        double getLength() {
            if (changed) {
                length = start.distanceTo(end);
                changed = false;
            }
            return length;
        }
};
```
Tip 12. 재사용하기 쉽게 만들라
Tip 13. 관련 없는 것들 간에 서로 영향이 없도록 하라
Tip 14. 최종 결정이란 없다
Tip 15. 목표물을 찾기 위해 예광탄을 써라
Tip 16. 프로토타입을 통해 학습하라
Tip 17. 문제 도메인에 가깝게 프로그래밍하라
Tip 18. 추정을 통해 놀람을 피하라
Tip 19. 코드와 함께 일정도 반복하며 조정하라