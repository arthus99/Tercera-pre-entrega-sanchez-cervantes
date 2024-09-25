function createNewProfile(){
    let x = document.getElementById("usn").value;
    if(x=="" || x==null)
    {
       alert("Please enter a username"); 
    }
    let y = document.getElementById("pwd").value;
    if(y =="" || y==null)
    {
       alert("Please enter a password"); 
    }
    let z = document.getElementById("dogNum").value;
    let zInt = parseInt(z);
    if(zInt < 1)
    {
       alert("Please enter the number of dogs"); 
    }
    if(zInt > 2)
    {
        alert("Sorry, we can register a most 2 dogs per custumer");
    }
    let a = document.getElementById("monthlyFee").value;
    if(a=="0")
    {
        alert("Please select a monthly fee package");
    }
}