# export API_KEY=AIzaSyCQaj2moJdMJO6y14ZqrLqI86JeDWdUka8
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

code = """
class Solution {
public:
    string makeFancyString(string s) {
        int pointer = 0;
        int n= s.size();
        string ans = "";
        int match =0;
        ans+=s[0];
        for(int i=1;i<n;i++){
            if(s[i-1]==s[i]){
                match++;
                cout<<"match : "<<match<<endl;
            }
            if(match>=2){
                if(s[i]==s[i+1] and i<n-2){
                    i+=2;
                }
                else if(i<n-1){
                    i++;
                }
                else{
                    break;
                }
                match = 0;
                cout<<"i :"<<i<<endl;
            }
            ans+=s[i];
            cout<<"ans : "<<ans<<endl;
        }
        
        return ans;
    }
};

correct the code to give me the output of "aabaa".
"""
response = model.generate_content(code)
print(response.text)
