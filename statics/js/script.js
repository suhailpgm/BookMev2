
    function length() {  
        var name=f.first_name.value;
        var lname=f.second_name.value;
        var uname=f.Username.value; 
        var email=f.email.value;
        var password=f.pass.value;
        var cpassword=f.cpass.value;
        var errorflag=0;
        if (name==null || name=="") {
            document.getElementById('errormsg1').innerHTML="firstname can't be blank";
            errorflag=1;


        }
        if (lname==null || lname=="") {
            errorflag=1;
            document.getElementById('errormsg2').innerHTML="secondname can't be blank";


        }
        if (uname==null || uname=="") {
            errorflag=1;
            document.getElementById('errormsg3').innerHTML="username can't be blank";


        }
        if (email==null || email=="") {
            errorflag=1;
            document.getElementById('errormsg4').innerHTML="email can't be blank";


        }
        if (password==null || password=="") {
            errorflag=1;
            document.getElementById('errormsg5').innerHTML="password can't be blank";


        }
        if(password.length<6 ) {
            errorflag=1;
            document.getElementById('errormsg5').innerHTML="Password must be at least 6 characters long.";

        }    
        if(password.length>26) {
            errorflag=1;
            document.getElementById('errormsg5').innerHTML="Password must be atmost 26 characters long.";

        }

        if(errorflag==0) {
            passwordvalidation()
        }
        else{

            return false;
        }
           
    } 
    function passwordvalidation() {
        var p = f.pass.value;
        var cp = f.cpass.value;
        if (cp==null || cp=="") {

            document.getElementById('errormsg6').innerHTML="confirm you password";
            length();
            return false;

        }
        if (p != cp)

            alert("Password do not match.")
            return false;
    }

     function validateForm() {
       return length()
        
                
    }

    function setPara(){
    chatpass=document.getElementById('chatpass').value;
    }
