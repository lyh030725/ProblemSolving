int strStr(char* haystack, char* needle) {
    int n_length = strlen(needle);
    int h_length = strlen(haystack);
    int result = -1;

    for(int i = 0; i <= h_length-n_length; i++){
        int flag = 1;
        for(int j = 0; j < n_length; j++){
            if(haystack[i+j] != needle[j]){
                flag = 0;
                break;
            }
        }
        if(flag){
            result = i;
            break;
        }
    }

    return result;
}