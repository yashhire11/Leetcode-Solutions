class TimeMap {
    unordered_map<string, vector<pair<int, string>>> _map;
public:
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        _map[key].push_back({timestamp, value});
    }
    
    string get(string key, int timestamp) {
        int n = _map[key].size();
        int l = 0, r = n-1;
        while(l <= r){
            int mid = l + (r-l)/2;
            if(_map[key][mid].first < timestamp){
                if(mid == r || _map[key][mid+1].first > timestamp)
                    return _map[key][mid].second;
                l = mid + 1;
            } else if(_map[key][mid].first > timestamp)
                r = mid-1;
            else 
                return _map[key][mid].second;
        }
        return "";
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */
