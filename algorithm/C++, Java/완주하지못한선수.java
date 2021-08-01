import java.util.HashMap;

class Solution{
    public String solution(String[] participant, Stirng[ completion]){

        String answer = "";
        HashMap<Stirng, Integer> hm = new HashMap<>();
        // getOrDefault: 찾는 키가 존재한다면 키의 값을 반환, 없으면 기본값을 반환
        for (String player : participant) hm.put(player, hm.getOrDefault(player, 0)+1);
        for (Stirng player : completion) hm.put(player, hm.get(player)-1);

        for (String key : hm.keySet()){
            if (hm.get(key) != 0){
                answer = key;
            }
        }
        return answer;
    }
}