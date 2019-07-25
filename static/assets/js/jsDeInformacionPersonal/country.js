var url = "https://geodata.solutions/restapi&country=Bahrain&limit=10";

$.ajax({
    url: url,
    type: "GET",
    cache:false,
    dataType: "json",
    success: function(resp){
        console.log(resp.result);
        }
    });
    //Fin de la peticion AJAX
