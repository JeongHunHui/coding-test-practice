import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public int solution(int[] people, int limit) {
        Integer[] peopleArray = Arrays.stream(people).boxed().sorted(Comparator.reverseOrder()).toArray(Integer[]::new);
        int lightPeopleNum = people.length - 1;
        int count = 1;
        for (int i = 0; i < lightPeopleNum; i++) {
            if(peopleArray[i] + peopleArray[lightPeopleNum] <= limit) {
                count++;
                lightPeopleNum--;
                if(lightPeopleNum == i) count--;
            }
            else {
                count++;
            }
        }
        return count;
    }
}