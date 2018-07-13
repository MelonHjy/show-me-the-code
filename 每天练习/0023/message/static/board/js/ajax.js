$(document).ready(function(){
    document.getElementById("btn").onclick =
    function(){
        $.ajax({
            type:'post',
            url:"/submit/",
            dataType:"json",
            success:function(data, status){
                console.log(data)
            }
        })
    }
})


var myDate = new Date();
myDate.getFullYear();