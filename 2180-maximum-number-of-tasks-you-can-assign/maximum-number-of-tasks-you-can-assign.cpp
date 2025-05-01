class Solution {
public:
    int maxTaskAssign(vector<int>& tasks, vector<int>& workers, int pills, int strength) {
        sort(tasks.begin(), tasks.end());
        sort(workers.begin(), workers.end());

        int left = 0, right = min((int)tasks.size(), (int)workers.size()), result = 0;

        while (left <= right) {
            int mid = (left + right) / 2;
            multiset<int> available;
            for (int i = workers.size() - mid; i < workers.size(); ++i) {
                available.insert(workers[i]);
            }

            bool possible = true;
            int remainingPills = pills;

            for (int i = mid - 1; i >= 0; --i) {
                int task = tasks[i];
                auto it = available.lower_bound(task);
                if (it != available.end()) {
                    available.erase(it);
                } else {
                    if (remainingPills == 0) {
                        possible = false;
                        break;
                    }
                    it = available.lower_bound(task - strength);
                    if (it == available.end()) {
                        possible = false;
                        break;
                    }
                    available.erase(it);
                    remainingPills--;
                }
            }

            if (possible) {
                result = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return result;
    }
};
