
    function length() {  
        var name=f.first_name.value;
        var lname=f.second_name.value;
        var uname=f.Username.value; 
        var email=f.email.value;
        var password=f.pass.value;  
        if (name==null || name=="") {  
            alert("firstname can't be blank");  
             return false;
        }
        else if (lname==null || lname=="") {  
            alert("secondname can't be blank");  
             return false;
        }
        else if (uname==null || uname=="") {  
            alert("username can't be blank");  
             
        }
        else if (email==null || email=="") {  
            alert("email can't be blank");  
             
        }
        else if (password==null || password=="") {  
            alert("password can't be blank");  
             
        }
        else if(password.length<6 ) {  
            alert("Password must be at least 6 characters long."); 
        }    
        else if(password.length>26) {
            alert("Password must be atmost 26 characters long.");
        }
        else {
            passwordvalidation()
        }
           
    } 
    function passwordvalidation() {
        var p = f.pass.value;
        var cp = f.cpass.value;
        if (p == cp)
            alert("Password  match.");
        else
            alert("Password do not match.");
    }

     function validateForm() {
        length()  
        
                
    }

    function setPara(){
    chatpass=document.getElementById('chatpass').value;
    }
