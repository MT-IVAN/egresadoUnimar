	//-------------------------------SELECT CASCADING-------------------------//
    var currentCities=[];
   
    var BATTUTA_KEY="e3dde5425198c63a574c90abfa81d5db";
    var auxCode ='';

    


        var urlCountry="https://api-world-egresados.herokuapp.com";
          $.getJSON(urlCountry,function(countries)
          {
             
           //loop de los paises que llegan de la peticion
            $.each(countries,function(key,country)
            {   
            
               
                let miOption=document.createElement("option");
                 
                // Añadimos las propiedades value y label
                miOption.setAttribute("data-value",country.id);
         
                miOption.append(country.name);
               
               
              //se agerega las opciones a el datalist
                document.getElementById('country').appendChild(miOption);
               
              
               
            });
          
    
          });
        
         
        $("#id_pais").on("change",function()
          { //OBtengo el nombre del pais que estoy buscando
              countryname=$("#id_pais").val();
              
              //borro los departamentos en caso de que haya cambiado de Pais
              $("#id_label_departamento").removeClass('active');
              $("#id_departamento ").val('').prop('disabled', true);
              $("#id_departamento").removeClass( "valid invalid" );
              $("#id_ciudad").removeClass( "valid invalid" );

              $("#id_ciudad ").val('').prop('disabled', true);
              $("#id_label_ciudad").removeClass('active');
               //quito las opciones anteriores
               document.getElementById('dpto').innerHTML = '';
               document.getElementById('city').innerHTML = '';
              
              if(countryname != ''){
                $("#id_label_departamento").html('Cargando...');


              var urlCode = "https://api-world-egresados.herokuapp.com/"+countryname;
                        $.getJSON(urlCode,function(regions)
                        {
                          
                          //cambio el label de cargando a deptamentos
                          $("#id_label_departamento").html('Departamento');
                          $("#id_departamento ").val('').prop('disabled', false);
                         

                          
                          $.each(regions,function(key,region)
                          {
                            let miOption=document.createElement("option");
                          
                            // Añadimos las propiedades value y label
                            miOption.setAttribute("data-value",region.id);
                            miOption.append(region.name);
                          
            
                            document.getElementById('dpto').appendChild(miOption);
                          });
                        
                          
                      }); 
                
              
              
           //si el pais es diferente de vacio >
           }
          });


          $("#id_departamento").on("change",function()
          {
            $("#id_label_ciudad").html('Cargando...');
            $("#id_label_ciudad").removeClass( "active" );
            $("#id_ciudad ").val('').prop('disabled', true);
            $("#id_ciudad").removeClass( "valid invalid" );
            //quito los anteriores elementos de la ciudad
            document.getElementById('city').innerHTML = '';
     
          
            region=$("#id_departamento").val();
            url="https://api-world-egresados.herokuapp.com/region/"+region;;
              
              $.getJSON(url,function(cities)
              {
                
                //loop through regions..
                $("#id_label_ciudad").html('Ciudad');
                $("#id_ciudad ").val('').prop('disabled', false);
                $.each(cities,function(key,city)
                {
                  let miOption=document.createElement("option");
                 
                  // Añadimos las propiedades value y label
                  miOption.setAttribute("data-value",city.id);
                  miOption.append(city.name);
                 
                //se agerega las opciones a el datalist
                  document.getElementById('city').appendChild(miOption);
                });
               
                
            }); 
            
          });	
          
       //-------------------------------END OF SELECT CASCADING-------------------------//


    //Fin de la peticion AJAX
