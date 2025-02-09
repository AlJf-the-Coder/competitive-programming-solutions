bool isAnagram(char* s, char* t) {
   int freq[26] = {0};
   int s_len = 0;
   for (int i = 0; s[i] != '\0'; i++){
       freq[s[i] - 'a']++;
       s_len++;
   }
   int t_len = 0;
   for (int i = 0; t[i] != '\0'; i++){
       freq[t[i] - 'a']--;
       t_len++;
   }
   if (s_len != t_len){
       return 0;
   }
   for (int i = 0; i < 26; i++){
       if (freq[i] != 0){
           return 0;
       }
   }
   return 1;
}
