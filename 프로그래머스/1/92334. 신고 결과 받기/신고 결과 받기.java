import java.util.ArrayList;
import java.util.List;

class User {
    private String id;
    private List<String> reportUsersId;
    private Integer reportedCount;
    private Boolean isReported;

    public User(String id) {
        this.id = id;
        this.reportUsersId = new ArrayList<>();
        this.reportedCount = 0;
        this.isReported = false;
    }

    public String getId() {
        return this.id;
    }

    public List<String> getReportUsersId() {
        return this.reportUsersId;
    }

    public boolean getIsReported() {
        return this.isReported;
    }

    public void report(String reportedUserId) {
        this.reportUsersId.add(reportedUserId);
    }

    public void reported(int k) {
        this.reportedCount++;
        if (this.reportedCount >= k) this.isReported = true;
    }

    public boolean isSameUserReport(String reportedUserId) {
        if (this.reportUsersId.contains(reportedUserId)) return true;
        return false;
    }
}

class Solution {
    List<User> users = new ArrayList<>();

    User getUser(String id) {
        for (User user : users) {
            if (user.getId().equals(id)) {
                return user;
            }
        }
        return null;
    }

    List<String> getFullReportedUsersId() {
        List<String> reportedUsers = new ArrayList<>();
        for (User user : users) {
            if (user.getIsReported()) {
                reportedUsers.add(user.getId());
            }
        }
        return reportedUsers;
    }

    public int getReportSuccessCount(User user) {
        List<String> reportedUsersId = getFullReportedUsersId();
        int count = 0;
        for (String userId : user.getReportUsersId()) {
            if (reportedUsersId.contains(userId)) count++;
        }
        return count;
    }

    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];

        for (String id : id_list) {
            users.add(new User(id));
        }

        for (String reportString : report) {
            String[] reportArray = reportString.split(" ");
            User reportUser = getUser(reportArray[0]);
            User reportedUser = getUser(reportArray[1]);
            if (!reportUser.isSameUserReport(reportedUser.getId())) {
                reportUser.report(reportedUser.getId());
                reportedUser.reported(k);
            }
        }

        for (int i = 0; i < id_list.length; i++) {
            answer[i] = getReportSuccessCount(getUser(id_list[i]));
        }

        return answer;
    }
}