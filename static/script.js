function cookiesAlert(){
    let dialog = window.confirm("Do you consent to cookies?")
    if(dialog == true){ 
        return true
    }else{
         window.location = 'http://google.com';
}}
cookiesAlert()

